import streamlit as st
import requests

st.set_page_config(page_title="Debt CRM", layout="wide")
st.title("📊 Debt Collection CRM")

backend_url = "http://127.0.0.1:8000"  # Your FastAPI backend URL

st.header("Check Backend Health")

if st.button("Ping Backend"):
    try:
        response = requests.get(f"{backend_url}/health")
        if response.status_code == 200:
            st.success(f"Backend is up! ✅ Message: {response.json()['status']}")
        else:
            st.error("Backend responded but not OK.")
    except Exception as e:
        st.error(f"Could not connect to backend: {e}")
