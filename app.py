import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="🏥"
)

model = joblib.load("best_model.joblib")
feature_columns = joblib.load("feature_columns.joblib")
scaler = joblib.load("scaler.joblib")

st.title("Insurance Cost Predictor")
st.write("Estimate your annual insurance charges.")

age = st.slider("Age", 18, 64, 30)
sex = st.selectbox("Sex", ["Female", "Male"])
bmi = st.number_input(
    "BMI", min_value=10.0, max_value=60.0, value=25.0
)
smoker = st.selectbox("Smoker?", ["No", "Yes"])
children = st.slider("Number of children", 0, 5, 0)

region = st.selectbox(
    "Region",
    ["Northeast", "Northwest", "Southeast", "Southwest"]
)

if st.button("Predict Insurance Cost"):
    # Apply the same fitted scaler as training
    scaled = scaler.transform([[age, bmi, children]])

    inputs = {
        "age": scaled[0][0],
        "is_female": int(sex == "Female"),
        "is_smoker": int(smoker == "Yes"),
        "bmi": scaled[0][1],
        "children": scaled[0][2],
        "region_southwest": int(region == "Southwest"),
        "bmi_category_Obese": int(bmi >= 30)
    }

    input_df = pd.DataFrame(
        [[inputs[col] for col in feature_columns]],
        columns=feature_columns
    )

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated annual charges: ₹{prediction:,.2f} per year")
    st.caption(
        "This is a machine-learning estimate, not an insurance quote."
    )