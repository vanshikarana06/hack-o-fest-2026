import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Comparison", layout="wide")

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
    padding: 15px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<div class='main-title'>🏪 Mandi Comparison</div>", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
df = pd.read_csv("data/data.csv")

# ---------- CLEAN DATA ----------
df["Market Name"] = df["Market Name"].astype(str).str.strip().str.title()
df["Commodity"] = df["Commodity"].astype(str).str.strip().str.title()

# Convert Date
df["Price Date"] = pd.to_datetime(df["Price Date"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["Price Date", "Modal_Price"])

# ---------- FILTERS ----------
col1, col2 = st.columns([1,2])

with col1:
    crop = st.selectbox("🌾 Select Crop", sorted(df["Commodity"].unique()))

with col2:
    compare_all = st.checkbox("🔍 Compare All Mandis", value=True)

# ---------- MANDI SELECTION ----------
if not compare_all:
    mandis = st.multiselect(
        "🏪 Select Mandis",
        sorted(df["Market Name"].unique())
    )
else:
    mandis = df["Market Name"].unique()

st.markdown("---")

# ---------- VALIDATION ----------
if not compare_all:
    if len(mandis) == 0:
        st.warning("Please select at least one mandi.")
        st.stop()
    
    if len(mandis) == 1:
        st.error("❌ Please select at least 2 mandis for comparison.")
        st.stop()

# ---------- FILTER DATA ----------
filtered_df = df[df["Commodity"] == crop]

if not compare_all:
    if len(mandis) == 0:
        st.warning("Please select at least one mandi.")
        st.stop()
    filtered_df = filtered_df[filtered_df["Market Name"].isin(mandis)]

# ---------- SORT ----------
filtered_df = filtered_df.sort_values(by="Price Date")

# ---------- TITLE ----------
if compare_all:
    title_text = f"{crop} - All Mandis Comparison"
else:
    title_text = f"{crop} - Selected Mandis Comparison"

# ---------- CHART ----------
st.markdown("### 📊 Price Comparison")

fig = px.line(
    filtered_df,
    x="Price Date",
    y="Modal_Price",
    color="Market Name",
    markers=True,
    title=title_text
)

st.plotly_chart(fig, use_container_width=True)

# ---------- SUMMARY ----------
st.markdown("### 📈 Summary")

summary = (
    filtered_df
    .groupby("Market Name")["Modal_Price"]
    .agg(["mean", "min", "max"])
    .reset_index()
)

st.dataframe(summary)

# ---------- BEST MANDI (🔥 BONUS FEATURE) ----------
st.markdown("### 🏆 Best Mandi (Highest Avg Price)")

best = summary.sort_values(by="mean", ascending=False).iloc[0]

st.success(f"Best Mandi: {best['Market Name']} (Avg Price: ₹{int(best['mean'])})")

# ---------- DATA ----------
st.markdown("### 📋 Data Table")
st.dataframe(filtered_df)