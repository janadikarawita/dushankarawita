import streamlit as st
import joblib
import numpy as np
from PIL import Image
import time

# Load models
easi_model = joblib.load("easi_prediction_model.pkl")
flare_model = joblib.load("flare_prediction_model.pkl")

# Set page config
st.set_page_config(page_title="EASI Score & Flare-Up Prediction Tool", layout="wide")

# Background gradient and moving auroras with CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #dfc2fc, #5f5ed4, #4993de);
        animation: gradientMove 10s ease infinite;
    }
    @keyframes gradientMove {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .title-text {
        font-family: 'Montserrat', sans-serif;
        font-size: 3rem;
        font-weight: bold;
        color: white;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.4);
        text-align: center;
    }
    .small-text {
        color: black;
        font-size: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load and display logos
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    logo1 = Image.open("logo.png.png").resize((50, 50))
    st.image(logo1)
with col3:
    logo2 = Image.open("tsmu_logo.png.png").resize((50, 50))
    st.image(logo2)

# Title
st.markdown('<div class="title-text">EASI Score & Flare-Up Prediction Tool</div>', unsafe_allow_html=True)

# Input fields
st.markdown("### Eosinophil Relative Count (ERC, Raw %):", unsafe_allow_html=True)
erc = st.number_input("", min_value=0.0, max_value=100.0, step=0.01, key="erc")
st.markdown("### Eosinophil-to-Lymphocyte Ratio (ELR, Raw):", unsafe_allow_html=True)
elr = st.number_input("", min_value=0.0, max_value=10.0, step=0.01, key="elr")

# Predict button with animations
if st.button("Predict"):
    with st.spinner("Processing..."):
        time.sleep(2)  # Simulating processing time
        easi_score = easi_model.predict(np.array([[erc, elr]]))[0]
        flare_risk = flare_model.predict(np.array([[erc, elr]]))[0]
    
    # Show confetti animation if flare-up risk is high
    if flare_risk:
        st.balloons()
        st.markdown("<h3 style='color:red; text-align:center;'>Future Flare-Up Risk: Yes</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:green; text-align:center;'>Future Flare-Up Risk: No</h3>", unsafe_allow_html=True)
    
    st.markdown(f"<h2 style='color:white; text-align:center;'>Predicted Future EASI Score: {easi_score:.2f}</h2>", unsafe_allow_html=True)


