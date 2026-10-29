# YESNO LXNORO AI Studio

AI-powered cinematic anime trailer generation system by LXNORO OJSC.

## Overview

YESNO LXNORO AI Studio is an advanced cinematic trailer generation platform combining:
- Ghibli-inspired visual aesthetic and deterministic affine motion transforms (zoom, pan, rotation via NumPy/OpenCV master keyframes at 12fps/30fps).
- Exact -12 dB ambient audio ducking during dialogue via NumPy FFT voice-band activity detection (100 Hz – 3400 Hz) and Pydub.
- Professional dark/light mode Streamlit UI (`app.py`).

---

## Streamlit Community Cloud Deployment

This repository is fully configured for deployment on [Streamlit Community Cloud](https://share.streamlit.io/).

### Prerequisites & Configuration Files
1. **Python Dependencies (`requirements.txt`):** Includes `opencv-python-headless` for headless Linux container compatibility.
2. **System Dependencies (`packages.txt`):** Automatically provisions system `ffmpeg` required by `moviepy` and `pydub`.
3. **Environment & Secrets:**
   - Default mode: `MOCK_MODE=True` (no API key required to run and test locally or on Streamlit Cloud).
   - Cloud production mode (`MOCK_MODE=False`): Configure `NEBIUS_API_KEY` in Streamlit Community Cloud **Secrets** (under App Settings -> Secrets):
     ```toml
     NEBIUS_API_KEY = "your-nebius-api-key-here"
     ```

### Deployment Steps on Streamlit Community Cloud
1. Push your repository to GitHub (branch `main`).
2. Go to [share.streamlit.io](https://share.streamlit.io/).
3. Click **New app**.
4. Select your GitHub repository, branch (`main`), and set the main file path to `app.py`.
5. Click **Deploy!**

---

## Local Development & Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure Environment:**
   Copy `.env.example` to `.env` and set your variables:
   ```env
   MOCK_MODE=True
   NEBIUS_API_KEY=your_key_here
   ```
3. **Run Application:**
   ```bash
   streamlit run app.py
   ```
