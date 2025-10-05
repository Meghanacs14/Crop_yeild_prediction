# 🌾 India Crop Yield Prediction using XGBoost

Predict the crop yield (tons/hectare) in India based on historical data using an **XGBoost regression model**. The project includes a **Streamlit web app** for interactive predictions.

---

## 📋 Features

* Predict crop yield using features:

  * State Name
  * District Name
  * Crop Year
  * Season (Kharif, Rabi, Summer)
  * Crop Name
* Preprocessing with **OrdinalEncoder** to handle categorical variables and unseen categories.
* Simple and fast **XGBoost regression model**.
* **Streamlit interface** for interactive predictions.
* Display model **performance metrics**:

  * RMSE
  * MAE
  * R² Score
* **Dropdown inputs** in Streamlit to prevent invalid entries.
* Optional visualizations (Actual vs Predicted Yield plot, feature importance plot).

---

## 📁 Dataset

The dataset should have the following columns:

```
State_Name, District_Name, Crop_Year, Season, Crop, Area, Production
```

* `Yield` is calculated as `Production / Area`.
* Example dataset: [India Crop Production Dataset](https://www.kaggle.com/datasets/abhinand05/crop-production-in-india)

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/india-crop-yield.git
cd india-crop-yield
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

> **requirements.txt** should include:

```
pandas
numpy
scikit-learn
xgboost
streamlit
matplotlib
```

---

## 🚀 Usage

### 1. Train the model

```bash
python train_model.py
```

* Trains XGBoost on the dataset.
* Saves the model (`xgb_crop_yield_model.pkl`) and encoder (`encoder.pkl`) for deployment.

### 2. Run Streamlit App

```bash
streamlit run app.py
```

* Opens a web app for interactive yield predictions.
* Select the **State, District, Season, Crop**, and enter the **Year**.
* Click **Predict Yield** to get the predicted crop yield.

---

## 📊 Model Performance

* Example metrics from testing:

| Metric | Value  |
| ------ | ------ |
| RMSE   | 262.29 |
| MAE    | 15.49  |
| R²     | 0.8728 |

---

## 📈 Visualizations

* **Actual vs Predicted Yield**: Scatter plot to compare predictions with real data.
* Optional **Feature Importance Plot**: Shows which features affect yield the most.

---

## ⚡ Notes

* OrdinalEncoder handles **unseen categories** by mapping them to -1.
* Using dropdowns in Streamlit prevents invalid category errors.
* The app can be easily extended for other crops, states, or regions.

