import streamlit as st
import numpy as np
from WaLSAtools import WaLSAtools
import json
import tempfile

st.title("WaLSAtools API")

uploaded_file = st.file_uploader("Upload a .npy file", type=["npy"])
cadence = st.number_input("Cadence (s)", value=0.01)
method = st.selectbox("Method", ["fft", "lomb_scargle"])
as_api = st.checkbox("Return as raw JSON (for external fetch)?", value=True)

if uploaded_file and st.button("Run"):
    signal = np.load(uploaded_file)
    power, freqs, sig, _ = WaLSAtools(signal=signal, time=time, method='fft')

    if as_api:
        # Return result as JSON
        st.json({
            "frequencies": freqs.tolist(),
            "power": power.tolist(),
            "significance": sig.tolist()
        })
    else:
        st.line_chart(power)
