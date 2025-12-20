import streamlit as st
from utils import init_session_state, apply_custom_css

st.set_page_config(
    page_title="EEG Authentication Study",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

init_session_state()
apply_custom_css()

st.switch_page("pages/1_Intro_UseCase.py")
