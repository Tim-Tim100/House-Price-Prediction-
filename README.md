# House-Price-Prediction-
End‑to‑end ML project predicting house prices with XGBoost and Streamlit
# 🏡 House Price Prediction (King County Dataset)


## 📌 Overview
This project predicts house prices in King County, WA using machine learning.  
It started as a raw dataset and evolved into a full pipeline — from cleaning and feature engineering to modeling and deployment.  
The final tuned XGBoost model achieved **R² ≈ 0.892**, offering strong predictive performance and interpretability.

---

## 🧠 My Process

### 1. Data Exploration & Cleaning
- Loaded the original `kc_house_data.csv` dataset.
- Dropped irrelevant columns like `id`, `date`, and `zipcode`.
- Checked for missing values and ensured data consistency.
- Visualized distributions, correlations, and outliers using Seaborn and Matplotlib.

### 2. Feature Engineering
To improve model performance, I created new features:
- **House Age**: `2025 - yr_built`
- **Renovated (Yes=1)**: Flag for homes with `yr_renovated > 0`
- **Living-to-Lot Ratio**: `sqft_living / sqft_lot`
- **Has Basement (Yes=1)**: Flag for `sqft_basement > 0`

I also renamed columns for clarity, e.g.:
- `sqft_living` → `Living Area (sqft)`
- `grade` → `Construction Grade`
- `view` → `View Rating`

### 3. Model Building
I compared several models:
- **Linear Regression**: Simple baseline
- **Random Forest**: Better performance, less interpretability
- **XGBoost**: Best performance after tuning



### 4. Deployment
Built a **Streamlit app** for interactive predictions:
- Users can input house features via sliders and dropdowns
- The app loads the trained model and returns a predicted price

---

## 🚀 Results
- **Top Features**: Living Area, Construction Grade, Latitude, View, Waterfront  
- **Best Model**: Tuned XGBoost  
- **Performance**: R² ≈ 0.892, RMSE ≈ $127k  

---

## 📊 Demo
- Interactive app built with Streamlit  
- Try it locally with the instructions below  

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn, XGBoost  
- Seaborn, Matplotlib  
- Streamlit  

---

---

## ⚡ How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/Tim-Tim100/House-Price-Prediction.git
   cd house-price-prediction

2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
 
---

3.   Run the Streamlit App

   ```bash
  streamlit run app/app.py

---








  







