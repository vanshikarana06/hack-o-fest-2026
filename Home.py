import streamlit as st
st.set_page_config(
    page_title="Mandi Price Predictor",
    page_icon="🌾",
    layout="wide"
)
#st.set_page_config(page_title="Home", page_icon="🏠")
# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
/* 1. Global Text Visibility Fix - Forces all text to be dark charcoal */
.stApp, .stMarkdown, p, li, span, label, .subtitle {
    color: #1e293b !important;
}

/* 2. Background */
.stApp {
    background-color: #f8fafc !important;
}

/* 3. Main Title - Your green color */
.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #1b5e20 !important;
    margin-bottom: 10px;
}

/* 4. Subtitle */
.subtitle {
    font-size: 20px;
    margin-bottom: 20px;
    display: block; /* Ensures it behaves like a block element */
}

/* 5. Card Style */
.card {
    padding: 25px;
    border-radius: 18px;
    background: white !important;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    transition: transform 0.2s ease-in-out;
}

.card:hover {
    transform: translateY(-5px);
}

/* 6. Button Style */
.stButton>button {
    background: linear-gradient(90deg, #2e7d32, #66bb6a) !important;
    color: white !important;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #1b5e20, #43a047) !important;
}

/* 7. Section Title */
.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 30px;
    color: #1b5e20 !important;
}

/* 8. Footer */
.footer {
    text-align: center;
    color: #64748b !important; /* Slightly darker than gray for visibility */
    margin-top: 40px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='main-title'>🌾 Mandi Price Predictor</div>", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
An intelligent tool to help farmers predict mandi prices, compare markets, and make better selling decisions.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- HERO SECTION ----------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🚀 Smarter Farming Starts Here

    ✔ Predict prices for next 7 days  
    ✔ Compare different mandis  
    ✔ Simple and easy to use  
    ✔ Data-driven insights for better decisions  
    """)

    st.success("💡 Built to support farmers with actionable insights, not complex theory.")

    if st.button("Explore Prediction →"):
        st.switch_page("pages/2_Prediction.py")

with col2:
    st.image(
        "https://images.unsplash.com/photo-1501004318641-b39e6451bec6",
        use_container_width=True
    )

st.markdown("---")

# ---------- FEATURES ----------
st.markdown("<div class='section-title'>⭐ Key Features</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
    <h4>📊 Data Driven</h4>
    <p>Uses historical mandi data to generate insights.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h4>🤖 ML Powered</h4>
    <p>Linear regression model for short-term forecasting.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
    <h4>🏪 Market Comparison</h4>
    <p>Compare prices across multiple mandis easily.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------- TRUST SECTION ----------
st.markdown("<div class='section-title'>🌱 Why This Matters</div>", unsafe_allow_html=True)

st.info("""
Farmers often sell without knowing future price trends.  
This tool reduces uncertainty by providing **simple, explainable forecasts**.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
    <h4>📉 Reduce Risk</h4>
    Avoid selling at lower prices by timing the market.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h4>📈 Increase Profit</h4>
    Make informed decisions based on predicted trends.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------- HOW TO USE ----------
st.markdown("<div class='section-title'>🧭 How to Use</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
1. Open the sidebar menu\n
2. Go to <b>Prediction Page</b>\n
3. Select crop and mandi\n
4. View forecast and advisory\n
5. Use <b>Compare Page</b> for market comparison  
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- FOOTER ----------
st.markdown("""
<div class='footer'>
🚜 Built for Hackathon | Powered by Streamlit & Machine Learning
</div>
""", unsafe_allow_html=True)
