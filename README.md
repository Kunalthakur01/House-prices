Here is the README in plain text:

🏠 House Price Prediction
A machine learning project to predict residential house prices using the Kaggle House Prices: Advanced Regression Techniques dataset. The project covers full data preprocessing, feature encoding, model training with multiple algorithms, and final submission generation.

📁 Project Structure

├── House_price_predictions.ipynb  # Full ML Pipeline notebook (main)
├── train.csv                      # Training dataset
├── test.csv                       # Test dataset
├── output.csv                     # Final predictions (Kaggle submission)
└── README.md

📌 Problem Statement
Predict the final sale price of homes in Ames, Iowa based on 79 explanatory variables describing almost every aspect of residential homes.

🔄 Workflow

 House_price_predictions.ipynb (Full ML Pipeline)

Setup — Import pandas, numpy, matplotlib, seaborn
Load & Merge Data — Combine train.csv and test.csv into one DataFrame for consistent preprocessing
EDA & Missing Value Analysis — Heatmaps and null summaries
Drop Sparse Columns — Automatically drop categorical columns with more than 1100 missing values
One-Hot Encode Categorical Features — Fill remaining nulls with string 'null', apply pd.get_dummies(), drop dummy columns containing 'null'
Merge Encoded Columns — Concatenate dummies back; drop original text columns
Fill Numeric Nulls — Mode for GarageCars, GarageYrBlt, BsmtFullBath, BsmtHalfBath; Mean for LotFrontage, MasVnrArea, BsmtFinSF1, BsmtFinSF2, BsmtUnfSF, TotalBsmtSF, GarageArea
Split Back — Separate combined DataFrame back into training and testing sets
Train/Test Split — 80/20 split using train_test_split
Train 3 Models — Linear Regression (default), XGBoost (n_estimators=1000, learning_rate=0.1), Random Forest (n_estimators=1000)
Evaluate — Compare models using Mean Squared Error (MSE)
Visualize — Line plot of Original vs Predicted prices
Generate Submission — Predict with XGBoost on test data, save as output.csv


🧰 Technologies Used
Python 3, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost, Kaggle/KaggleHub

📊 Models & Evaluation
All models are evaluated using Mean Squared Error (MSE) on a held-out 20% test set. Linear Regression is used as the baseline. XGBoost is the best performer and is used for the final submission. Random Forest is a strong ensemble model but computationally heavier.

🚀 How to Run

Clone the repository and place train.csv and test.csv in the root directory
Install dependencies: pip install pandas numpy matplotlib seaborn scikit-learn xgboost
Run house-price.ipynb for EDA and preprocessing insights
Run House_price_predictions.ipynb for the full pipeline and to generate output.csv


📤 Output
The final file output.csv contains two columns — Id and SalePrice — and is ready for direct submission to the Kaggle competition.

📚 Dataset
Source: Kaggle — House Prices: Advanced Regression Techniques. Train size: 1460 rows × 81 columns. Test size: 1459 rows × 80 columns. Target variable: SalePrice.
