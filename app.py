import streamlit as st
import numpy as np
from WaLSAtools import WaLSAtools
import json

st.set_page_config(page_title="WaLSAtools Web App", layout="centered")
st.title("📊 WaLSAtools Analysis")
st.markdown("Upload your **signal** and **time** arrays (in `.npy` format) and choose your analysis method.")

# File upload
signal_file = st.file_uploader("Upload signal array (.npy)", type=["npy"])
time_file = st.file_uploader("Upload time array (.npy)", type=["npy"])

# Method selector
method = st.selectbox("Analysis method", ["fft", "lomb_scargle"])

# Output format
as_api = st.checkbox("Return result as raw JSON (for external integration)?", value=True)

# Run analysis
if signal_file and time_file and st.button("Run Analysis"):
    try:
        # Load arrays
        signal = np.load(signal_file)
        time = np.load(time_file)

        # Run WaLSAtools
        st.info("Running WaLSAtools...")
        power, freqs, sig = WaLSAtools(signal=signal, time=time, method=method)

        if as_api:
            st.success("Done! Returning JSON result.")
            st.json({
                "frequencies": freqs.tolist(),
                "power": power.tolist(),
                "significance": sig.tolist()
            })
        else:
            st.success("Done! Showing plot of power spectrum.")
            st.line_chart(power)

    except Exception as e:
        st.error(f"Error during analysis: {e}")
