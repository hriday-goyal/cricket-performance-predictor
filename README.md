[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cricket-performance-predictor-mc4a2kbjp6a5xvjrml3tuc.streamlit.app/)
# 🏏 Cricket Performance Predictor

This is a machine learning project that predicts how many runs a cricketer might score based on their recent performance, batting average, and strike rate.

## 💡 How It Works

The model was trained using a Random Forest Regressor on IPL-style data. It takes in:
- Runs scored in the last 3 matches
- Batting average
- Strike rate

It then outputs a predicted run value using learned patterns.

## 🚀 Tech Stack

- Python
- Streamlit (for the web app)
- Scikit-learn (Random Forest)
- Pandas, NumPy, Joblib
- Matplotlib (for evaluation graphs)

## 📦 Files Included

- `app.py`: The Streamlit frontend code
- `cricket_run_predictor_model.pkl`: The trained model file
- `README.md`: Project overview

## 🌐 Live Demo

Try the app here:  
👉 https://cricket-performance-predictor-mc4a2kbjp6a5xvjrml3tuc.streamlit.app/
