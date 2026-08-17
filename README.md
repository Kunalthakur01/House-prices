# 🏠 House Price Prediction

A Machine Learning project that predicts house prices using the **Ames Housing Dataset**.

The project uses a **Gradient Boosting Regressor** trained on housing features such as overall quality, living area, basement area, garage details, neighborhood, and other property characteristics.

A **Streamlit web application** is included so users can enter house details and get an estimated selling price.

---

## 🚀 Live Demo

🔗 **Streamlit App:**  
[House Price Prediction](YOUR_STREAMLIT_APP_URL)

---
📊 Dataset
[Dataset Link]((https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data))
This project uses the Ames Housing Dataset provided through the Kaggle House Prices competition.

The dataset contains information about residential properties and their corresponding sale prices.

The model learns relationships between property characteristics and the final sale price.
## 📌 Project Overview

The goal of this project is to build a regression model capable of predicting house sale prices based on various property features.

The project includes:

- Data preprocessing
- Missing-value handling
- Categorical feature encoding
- Feature engineering/preparation
- Log transformation of the target variable
- Model comparison
- Cross-validation
- Gradient Boosting model tuning
- House price prediction
- Streamlit frontend
- Model deployment

---

## 🧠 Machine Learning Approach

### Target Variable

The target variable is:

```
text
SalePrice
```
Because house prices are highly skewed, the target was transformed using:
```
y = np.log1p(SalePrice)
```
After prediction, the transformation is reversed using:
```
prediction = np.expm1(prediction_log)
```

🔧 Data Preprocessing

The following preprocessing steps were performed:

1. Train and Test Data

The Kaggle training and testing datasets were loaded and combined for consistent feature preparation.

2. Missing Values

Categorical columns with a very high number of missing values were removed.

Selected numerical missing values were handled using:

Mode imputation
Mean imputation
3. Categorical Encoding

Categorical variables were converted into numerical features using:
```
pd.get_dummies()
```
This resulted in a feature matrix containing 283 input features.

4. Feature Defaults

For the Streamlit application, training-data defaults are used for features that are not directly entered by the user.

This prevents unspecified features from simply being assigned zero values.
.

🤖 Models Tested

Several regression models were evaluated.
```
| Model                       | Approach           |
| --------------------------- | ------------------ |
| Linear Regression           | Raw and log target |
| Random Forest Regressor     | Raw and log target |
| Gradient Boosting Regressor | Raw and log target |
| XGBoost Regressor           | Raw and log target |
```
The log-transformed target generally produced better results for this dataset.

🏆 Final Model

The final model is a Gradient Boosting Regressor.

Configuration:
```
GradientBoostingRegressor(
    n_estimators=1000,
    learning_rate=0.03,
    max_depth=3,
    min_samples_leaf=3,
    min_samples_split=10,
    loss="huber",
    random_state=42
)
```
Cross-Validation Result

Using 5-fold cross-validation:
```
Mean CV Score: 0.1287
Standard Deviation: 0.0211
```
The model was then trained on the complete training dataset before generating predictions for the test dataset.

🖥️ Streamlit Application

The project includes an interactive Streamlit frontend.

Users can enter important house characteristics such as:

Overall Quality
Overall Condition
Year Built
Year Remodeled
Lot Area
Living Area
Basement Area
First Floor Area
Second Floor Area
Full Bathrooms
Half Bathrooms
Bedrooms
Total Rooms
Fireplaces
Garage Capacity
Garage Area
Garage Year Built
Neighborhood
MS Zoning
Kitchen Quality
Central Air

The application then generates an estimated house price.
📂 Project Structure
```
House-prices/
│
├── app.py
├── house_price_model.pkl
├── model_features.pkl
├── numeric_defaults.pkl
├── bool_defaults.pkl
├── requirements.txt
└── README.md
```
🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
Matplotlib
Seaborn
XGBoost
⚙️ Installation
1. Clone the repository
```
git clone https://github.com/Kunalthakur01/House-prices.git
```
2. Navigate to the project
```
git clone https://github.com/Kunalthakur01/House-prices.git
```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit application
   ```
   streamlit run app.py
   ```
   The application will open in your browser.
