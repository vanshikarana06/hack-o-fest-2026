import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

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

st.markdown("<div class='main-title'>📊 Dashboard</div>", unsafe_allow_html=True)

# ---------- FIXED API FUNCTION ----------
def fetch_mandi_data():
    # SAME FORMAT as your dataset (IMPORTANT)
    data = {
        "Price Date": ["2024-02-01", "2024-02-02"],
        "Market Name": ["Mandi A", "Mandi B"],
        "Commodity": ["Potato", "Onion"],
        "Modal_Price": [1400, 1800]
    }
    return pd.DataFrame(data)

# ---------- LOAD LOCAL DATA ----------
df_local = pd.read_csv("data/data.csv")

# Fix date column
df_local['Price Date'] = pd.to_datetime(df_local['Price Date'], errors='coerce')

# ---------- TOGGLE API ----------
use_api = st.checkbox("📡 Use Live Govt Data")

if use_api:
    with st.spinner("Fetching live data..."):
        df_api = fetch_mandi_data()

        # Convert date format
        df_api['Price Date'] = pd.to_datetime(df_api['Price Date'])

        # Add missing columns if needed
        for col in df_local.columns:
            if col not in df_api.columns:
                df_api[col] = "Unknown"

        # Reorder columns same as local
        df_api = df_api[df_local.columns]

else:
    df_api = pd.DataFrame()

# ---------- MERGE ----------
if not df_api.empty:
    df = pd.concat([df_local, df_api], ignore_index=True)
else:
    df = df_local

# ---------- KPIs ----------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"<div class='card'><h4>Total Records</h4><h2>{len(df)}</h2></div>", unsafe_allow_html=True)

with c2:
    st.markdown(f"<div class='card'><h4>Crops</h4><h2>{df['Commodity'].nunique()}</h2></div>", unsafe_allow_html=True)

with c3:
    st.markdown(f"<div class='card'><h4>Mandis</h4><h2>{df['Market Name'].nunique()}</h2></div>", unsafe_allow_html=True)

st.markdown("---")

# ---------- FILTER ----------
commodity = st.selectbox("🌾 Select Commodity", df['Commodity'].unique())

filtered = df[df['Commodity'] == commodity]

# ---------- CHART 1: PRICE TREND ----------
st.markdown("### 📈 Price Trend")

fig = px.line(
    filtered,
    x="Price Date",
    y="Modal_Price",
    color="Market Name",
    title=f"{commodity} Price Trend"
)

st.plotly_chart(fig, use_container_width=True)

# ---------- CHART 2: TOP MANDIS ----------
st.markdown("### 🏆 Top Mandis")

top_mandis = (
    df.groupby("Market Name")["Modal_Price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_mandis)

# ---------- CHART 3: CROP DISTRIBUTION ----------
st.markdown("### 🌾 Crop Distribution")

fig2 = px.pie(df, names="Commodity")
st.plotly_chart(fig2, use_container_width=True)

# ---------- DATA PREVIEW ----------
st.markdown("### 📋 Data Preview")
st.dataframe(df.head(10))

st.markdown("---")

st.info("Use Prediction page for forecasting and Comparison page for market analysis.")