import streamlit as st

st.set_page_config(page_title="About", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: 800;
    color: #1b5e20;
    margin-bottom: 10px;
}

.sub-title {
    font-size: 22px;
    font-weight: 600;
    color: #2e7d32;
    margin-top: 20px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.highlight {
    color: #1b5e20;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<div class='main-title'>ℹ️ About This Application</div>", unsafe_allow_html=True)

# ---------- INTRO ----------
st.markdown("""
<div class='card'>
This application is an <span class='highlight'>AI-powered mandi price prediction system</span> 
designed to help farmers and traders make smarter selling decisions using data.
</div>
""", unsafe_allow_html=True)

# ---------- FEATURES ----------
st.markdown("<div class='sub-title'>🚀 Key Features</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<ul>
<li>📊 Historical price analysis</li>
<li>🔮 7-day ML-based forecasting</li>
<li>🏪 Multi-mandi comparison</li>
<li>💡 Smart advisory system (Sell / Wait)</li>
<li>📈 Interactive dashboards</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------- MODEL ----------
st.markdown("<div class='sub-title'>🤖 Machine Learning Model</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
This system uses a <span class='highlight'>Random Forest Regressor</span>, 
a powerful ensemble machine learning algorithm.

<br><br>

It learns patterns from:
<ul>
<li>📍 Location (State, District, Market)</li>
<li>🌾 Crop details (Commodity, Variety, Grade)</li>
<li>📅 Date features (Year, Month, Day)</li>
</ul>

and predicts future mandi prices based on these factors.
</div>
""", unsafe_allow_html=True)

# ---------- HOW IT WORKS ----------
st.markdown("<div class='sub-title'>⚙️ How It Works</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
1. Historical mandi data is collected 📊<br>
2. Data is cleaned and preprocessed 🔧<br>
3. Machine Learning model is trained 🤖<br>
4. User selects inputs (crop, mandi, date) 🧑‍🌾<br>
5. System predicts price & future trend 🔮<br>
</div>
""", unsafe_allow_html=True)

# ---------- PURPOSE ----------
st.markdown("<div class='sub-title'>🎯 Purpose</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<ul>
<li>Help farmers maximize profit 💰</li>
<li>Reduce uncertainty in pricing 📉</li>
<li>Enable data-driven agriculture decisions 🌱</li>
<li>Bridge gap between technology & farming 🚜</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("✅ Built with Streamlit | 🤖 Machine Learning Project | 🌱 AgriTech Hackathon Solution")