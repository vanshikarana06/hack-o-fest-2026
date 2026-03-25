import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import timedelta
from utils.load_model import load_model, load_mapping

st.set_page_config(page_title="Prediction", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.stApp { background-color: #f8fafc; }

.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #1b5e20;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>📈 Prediction</div>", unsafe_allow_html=True)

# ---------- LOAD MODEL ----------
model = load_model()
mapping = load_mapping()

# ---------- INPUT ----------
col1, col2 = st.columns(2)

with col1:
    commodity = st.selectbox("🌾 Select Commodity", list(mapping['Commodity'].keys()))

with col2:
    market = st.selectbox("🏪 Select Market", list(mapping['Market Name'].keys()))

# Optional (advanced inputs)
state = st.selectbox("State", list(mapping['STATE'].keys()))
district = st.selectbox("District", list(mapping['District Name'].keys()))
variety = st.selectbox("Variety", list(mapping['Variety'].keys()))
grade = st.selectbox("Grade", list(mapping['Grade'].keys()))

date = st.date_input("📅 Select Date")

# ---------- ENCODING ----------
def encode(col, value):
    return mapping[col].get(value, 0)

# ---------- PREDICTION ----------
if st.button("Predict Price 💰"):

    input_data = pd.DataFrame([{
        'STATE': encode('STATE', state),
        'District Name': encode('District Name', district),
        'Market Name': encode('Market Name', market),
        'Commodity': encode('Commodity', commodity),
        'Variety': encode('Variety', variety),
        'Grade': encode('Grade', grade),
        'Year': date.year,
        'Month': date.month,
        'Day': date.day
    }])

    # Single prediction
    prediction = model.predict(input_data)[0]

    st.success(f"💰 Predicted Price: ₹{int(prediction)}")

    # ---------- 7 DAY FORECAST ----------
    st.markdown("### 📊 7-Day Forecast")

    future_prices = []
    future_dates = []

    for i in range(7):
        future_date = date + timedelta(days=i)

        temp = input_data.copy()
        temp['Year'] = future_date.year
        temp['Month'] = future_date.month
        temp['Day'] = future_date.day

        pred = model.predict(temp)[0]

        future_prices.append(pred)
        future_dates.append(future_date)

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Predicted Price": future_prices
    })

    # ---------- CHART ----------
    fig = px.line(
        forecast_df,
        x="Date",
        y="Predicted Price",
        markers=True,
        title=f"{commodity} Price Forecast for {market}"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------- TABLE ----------
    st.markdown("### 📋 Forecast Data")
    st.dataframe(forecast_df)

    # ---------- ADVISORY ----------
    future_avg = forecast_df["Predicted Price"].mean()

    st.markdown("### 💡 Advisory")

    if future_avg > prediction * 1.02:
        st.success("📈 Prices likely to rise. Consider waiting.")
    elif future_avg < prediction * 0.98:
        st.error("📉 Prices likely to fall. Consider selling.")
    else:
        st.warning("⚖️ Prices are stable.")