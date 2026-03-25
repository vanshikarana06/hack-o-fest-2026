# 🌾 Mandi Price Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://techies.streamlit.app/)

An intelligent, data-driven dashboard built to empower farmers with actionable market insights. This tool helps users predict commodity prices, compare different Mandis (markets), and make informed selling decisions to maximize profits.

🔗 **Live Demo:** [techies.streamlit.app](https://techies.streamlit.app/)

---

## 🚀 Features

- **Price Prediction:** Uses Machine Learning (Random Forest) to forecast prices for the next 7 days.
- **Interactive Dashboard:** Visualize price trends across various commodities and markets using Plotly.
- **Live Data Integration:** Toggle between local historical datasets and live Agmarknet API data.
- **Market Comparison:** Compare multiple Mandis side-by-side to find the best selling price.
- **User-Friendly UI:** Clean, responsive interface built with Streamlit and custom CSS.

## 🛠 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Data Handling:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualization:** [Plotly Express](https://plotly.com/python/)
- **Machine Learning:** [Scikit-Learn](https://scikit-learn.org/) (Random Forest Regressor)
- **Model Deployment:** [Joblib](https://joblib.readthedocs.io/)
- **Version Control:** GitHub

## 📂 Project Structure

```text
├── Home.py                # Landing page of the app
├── requirements.txt      # List of dependencies
├── artifacts/            # Saved ML models (.pkl files)
├── data/                 # Historical Mandi datasets (.csv)
├── utils/                # Helper functions
└── pages/                # Multi-page application structure
    ├── 1_Dashboard.py
    ├── 2_Prediction.py
    └── 3_Comparison.py
```


⚙️ Installation & Local Setup
To run this project locally, follow these steps:

Clone the repository:

Bash
git clone [https://github.com/vanshikarana06/hack-o-fest-2026.git](https://github.com/vanshikarana06/hack-o-fest-2026.git)
cd hack-o-fest-2026
Install dependencies:

Bash
pip install -r requirements.txt
Run the app:

Bash
streamlit run Home.py
# 💡 Future Scope
Integration with more real-time Government APIs (Agmarknet).

Weather data incorporation to improve prediction accuracy.

Support for regional Indian languages to increase accessibility for farmers.


---


