# House Price Prediction

## Overview

This project focuses on predicting residential house prices using Machine Learning techniques on the Ames Housing Dataset from Kaggle. The objective is to build a regression model that can estimate a property's selling price based on various house characteristics such as location, size, quality, condition, garage details, basement information, and more.

## Dataset

Dataset: House Prices – Advanced Regression Techniques (Kaggle)

The dataset contains 79 explanatory variables describing different aspects of residential homes.

### Target Variable

* SalePrice

### Features Include

* Neighborhood
* Overall Quality
* House Style
* Garage Features
* Basement Features
* Lot Size
* Exterior Quality
* Heating Quality
* Kitchen Quality
* Year Built
* And many more

---

## Project Workflow

### 1. Data Exploration

* Loaded and inspected the dataset
* Performed exploratory data analysis
* Analyzed feature distributions
* Identified missing values

### 2. Data Cleaning

Handled missing values using:

* Mean imputation for numerical features
* Mode imputation for categorical features
* Removal of columns with excessive missing values

Dropped columns such as:

* Alley
* PoolQC
* Fence
* MiscFeature
* GarageYrBlt

### 3. Feature Engineering

* Removed unnecessary identifiers
* Processed categorical variables
* Converted categorical features into numerical representations using One-Hot Encoding

### 4. Data Preprocessing

* Missing value treatment
* Categorical encoding
* Feature selection
* Dataset preparation for model training

---

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

## Skills Demonstrated

* Data Cleaning
* Missing Value Handling
* Exploratory Data Analysis (EDA)
* Feature Engineering
* One-Hot Encoding
* Regression Problem Solving
* Machine Learning Data Preparation

---

## Project Structure

```text
House-prices/
│
├── house-price.ipynb
├── data_descriptions.text
├── output.csv
├── sample_submission.csv
├── test.csv
└── train.csv

```

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Real-world dataset preprocessing
* Handling large numbers of missing values
* Feature transformation techniques
* Preparing data for machine learning models
* Building a complete machine learning workflow

---



## Author

Kunal Singh

Aspiring AI/ML Engineer | Python Developer | Machine Learning Enthusiast
