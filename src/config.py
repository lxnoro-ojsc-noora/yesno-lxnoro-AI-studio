import os
from dotenv import load_dotenv

load_dotenv()

MOCK_MODE = os.getenv("MOCK_MODE", "True").lower() == "true"
NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY", "")

try:
    import streamlit as st
    if hasattr(st, "secrets") and "NEBIUS_API_KEY" in st.secrets:
        NEBIUS_API_KEY = st.secrets["NEBIUS_API_KEY"]
except Exception:
    pass

if not MOCK_MODE and not NEBIUS_API_KEY:
    raise RuntimeError("NEBIUS_API_KEY is required when MOCK_MODE=False")
