import streamlit as st

st.set_page_config(page_title="Lab 12", page_icon="🏠", layout="centered")

pages = [
    st.Page("app_pages/predictor.py", title="Housing Predictor", icon="🏠", default=True),
    st.Page("app_pages/roulette.py", title="Roulette", icon="🎰"),
]

st.navigation(pages, position="top").run()
