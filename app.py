import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ==========================================
# 1. LOAD MODEL + PREPROCESSING INFORMATION
# ==========================================

model = joblib.load("house_price_model.pkl")
model_features = joblib.load("model_features.pkl")
numeric_defaults = joblib.load("numeric_defaults.pkl")
bool_defaults = joblib.load("bool_defaults.pkl")


# ==========================================
# 2. PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)


# ==========================================
# 3. TITLE
# ==========================================

st.title("🏠 House Price Predictor")

st.write(
    "Enter the details of a house to estimate its selling price."
)

st.divider()


# ==========================================
# 4. INPUT SECTION
# ==========================================

st.subheader("🏡 House Details")


col1, col2, col3 = st.columns(3)


with col1:

    overall_qual = st.slider(
        "Overall Quality",
        min_value=1,
        max_value=10,
        value=5
    )

    overall_cond = st.slider(
        "Overall Condition",
        min_value=1,
        max_value=10,
        value=5
    )

    year_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2026,
        value=2000
    )

    year_remod_add = st.number_input(
        "Year Remodeled",
        min_value=1800,
        max_value=2026,
        value=2000
    )


with col2:

    lot_area = st.number_input(
        "Lot Area (sq ft)",
        min_value=100,
        max_value=200000,
        value=8000
    )

    gr_liv_area = st.number_input(
        "Living Area (sq ft)",
        min_value=100,
        max_value=10000,
        value=1500
    )

    total_bsmt_sf = st.number_input(
        "Basement Area (sq ft)",
        min_value=0,
        max_value=5000,
        value=1000
    )

    first_flr_sf = st.number_input(
        "1st Floor Area (sq ft)",
        min_value=100,
        max_value=5000,
        value=1000
    )


with col3:

    second_flr_sf = st.number_input(
        "2nd Floor Area (sq ft)",
        min_value=0,
        max_value=5000,
        value=500
    )

    full_bath = st.number_input(
        "Full Bathrooms",
        min_value=0,
        max_value=5,
        value=2
    )

    half_bath = st.number_input(
        "Half Bathrooms",
        min_value=0,
        max_value=3,
        value=1
    )

    bedroom_abv_gr = st.number_input(
        "Bedrooms",
        min_value=0,
        max_value=10,
        value=3
    )


st.divider()


# ==========================================
# 5. ADDITIONAL DETAILS
# ==========================================

st.subheader("🔧 Additional Details")


col1, col2, col3 = st.columns(3)


with col1:

    tot_rms_abv_grd = st.number_input(
        "Total Rooms",
        min_value=1,
        max_value=20,
        value=6
    )

    fireplaces = st.number_input(
        "Fireplaces",
        min_value=0,
        max_value=5,
        value=1
    )

    garage_cars = st.number_input(
        "Garage Capacity (Cars)",
        min_value=0,
        max_value=5,
        value=2
    )


with col2:

    garage_area = st.number_input(
        "Garage Area (sq ft)",
        min_value=0,
        max_value=2000,
        value=500
    )

    garage_yr_blt = st.number_input(
        "Garage Year Built",
        min_value=1800,
        max_value=2026,
        value=2000
    )

    central_air = st.selectbox(
        "Central Air",
        ["Y", "N"]
    )


with col3:

    neighborhood = st.selectbox(
        "Neighborhood",
        [
            "CollgCr",
            "Veenker",
            "Crawford",
            "NoRidge",
            "Mitchel",
            "OldTown",
            "BrkSide",
            "Somerst",
            "NridgHt",
            "NAmes"
        ]
    )

    ms_zoning = st.selectbox(
        "MS Zoning",
        [
            "RL",
            "RM",
            "FV",
            "RH",
            "C (all)"
        ]
    )

    kitchen_qual = st.selectbox(
        "Kitchen Quality",
        [
            "Ex",
            "Gd",
            "TA",
            "Fa"
        ]
    )


st.divider()


# ==========================================
# 6. CREATE MODEL INPUT
# ==========================================

def create_user_input():

    # Start with realistic training-data defaults
    user_input = pd.DataFrame(
        [numeric_defaults],
        columns=model_features
    )

    # Set boolean defaults
    for feature, value in bool_defaults.items():

        if feature in user_input.columns:
            user_input[feature] = value

    # ======================================
    # USER NUMERIC INPUTS
    # ======================================

    user_input["OverallQual"] = overall_qual
    user_input["OverallCond"] = overall_cond

    user_input["YearBuilt"] = year_built
    user_input["YearRemodAdd"] = year_remod_add

    user_input["LotArea"] = lot_area
    user_input["GrLivArea"] = gr_liv_area

    user_input["TotalBsmtSF"] = total_bsmt_sf
    user_input["1stFlrSF"] = first_flr_sf
    user_input["2ndFlrSF"] = second_flr_sf

    user_input["FullBath"] = full_bath
    user_input["HalfBath"] = half_bath

    user_input["BedroomAbvGr"] = bedroom_abv_gr
    user_input["TotRmsAbvGrd"] = tot_rms_abv_grd

    user_input["Fireplaces"] = fireplaces

    user_input["GarageCars"] = garage_cars
    user_input["GarageArea"] = garage_area
    user_input["GarageYrBlt"] = garage_yr_blt

    # ======================================
    # CATEGORICAL INPUTS
    # ======================================

    categorical_inputs = {

        "Neighborhood": neighborhood,

        "MSZoning": ms_zoning,

        "KitchenQual": kitchen_qual,

        "CentralAir": central_air
    }


    for feature, value in categorical_inputs.items():

        column_name = f"{feature}_{value}"

        if column_name in user_input.columns:

            user_input[column_name] = True


    # Make absolutely sure column order is identical
    user_input = user_input[model_features]

    return user_input


# ==========================================
# 7. PREDICTION
# ==========================================

if st.button(
    "💰 Predict House Price",
    type="primary",
    use_container_width=True
):

    user_input = create_user_input()

    # Check feature count
    if user_input.shape[1] != len(model_features):

        st.error(
            f"Feature mismatch: "
            f"{user_input.shape[1]} vs {len(model_features)}"
        )

    else:

        prediction_log = model.predict(user_input)

        # Convert log prediction back to original price
        prediction = np.expm1(prediction_log)[0]


        # ==================================
        # RESULT
        # ==================================

        st.success("Prediction completed successfully!")

        st.metric(
            "🏠 Estimated House Price",
            f"${prediction:,.0f}"
        )

        