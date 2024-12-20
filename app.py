import streamlit as st
import numpy as np
import joblib

# Load the trained models
easi_model = joblib.load('easi_prediction_model.pkl')  # Model for predicting future EASI scores
flare_model = joblib.load('flare_prediction_model.pkl')  # Model for predicting flare-up risk

# App title
st.title("EASI Score and Flare-Up Prediction Tool")
st.write("Predict future EASI scores and flare-ups based on previous blood marker values.")

# Input fields for all required features
age = st.number_input("Age (normalized between 0 and 1):", min_value=0.0, max_value=1.0, step=0.01)
erc = st.number_input("Eosinophil Relative Count (ERC, normalized):", min_value=0.0, max_value=1.0, step=0.01)
nlr = st.number_input("Neutrophil-to-Lymphocyte Ratio (NLR, normalized):", min_value=0.0, max_value=1.0, step=0.01)
blr = st.number_input("Basophil-to-Lymphocyte Ratio (BLR, normalized):", min_value=0.0, max_value=1.0, step=0.01)
elr = st.number_input("Eosinophil-to-Lymphocyte Ratio (ELR, normalized):", min_value=0.0, max_value=1.0, step=0.01)

# Predict button
if st.button("Predict"):
    # Prepare input for prediction
    input_data = np.array([[age, erc, nlr, blr, elr]])

    try:
        # Predict future EASI score
        predicted_easi = easi_model.predict(input_data)

        # Predict flare-up
        flare_prediction = flare_model.predict(input_data)
        flare_risk = "Yes" if flare_prediction[0] == 1 else "No"

        # Display results
        st.write(f"Predicted Future EASI Score: {predicted_easi[0]:.2f}")
        st.write(f"Future Flare-Up Risk: {flare_risk}")
    except ValueError as e:
        st.error(f"An error occurred during prediction: {e}")
import pandas as pd

# Prepare input for prediction with valid feature names
input_data = pd.DataFrame([[age, erc, nlr, blr, elr]], columns=['Age', 'ERC', 'NLR', 'BLR', 'ELR'])

# Predict future EASI score
predicted_easi = easi_model.predict(input_data)

# Predict flare-up
flare_prediction = flare_model.predict(input_data)
flare_risk = "Yes" if flare_prediction[0] == 1 else "No"

# Load models in the app
easi_model = joblib.load('easi_prediction_model.pkl')
flare_model = joblib.load('flare_prediction_model.pkl')

# Input example
import numpy as np
sample_input = np.array([[0.25, 0.0875, 0.478778, 0.076923, 1.0]])  # Example normalized input

# Predict
predicted_easi = easi_model.predict(sample_input)
predicted_flare = flare_model.predict(sample_input)

print("Predicted EASI Score:", predicted_easi[0])
print("Predicted Flare-Up:", "Yes" if predicted_flare[0] == 1 else "No")
