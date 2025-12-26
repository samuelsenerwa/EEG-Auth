import streamlit as st
import sys
from pathlib import Path
sys.path.append('..')
from utils import init_session_state, apply_custom_css, render_header, render_stepper, render_user_icon

st.set_page_config(
    page_title="Authentication - EEG Auth Study",
    page_icon="🧠",
    layout="centered"
)

init_session_state()
apply_custom_css()

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
HEADSET_IMAGE = ASSETS_DIR / "headset.png"

render_header(
    "EEG Authentication Login",
    "Please put on your EEG headset to begin"
)

render_stepper(1)

st.markdown('<div class="info-card" style="text-align: center; padding: 3rem 2rem;">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if HEADSET_IMAGE.exists():
        st.image(HEADSET_IMAGE, use_container_width=True)
    else:
        st.warning("Headset image missing from assets directory.")

st.markdown("""
<p style="font-size: 0.95rem; color: #666; margin: 1.5rem 0; line-height: 1.6;">
Please imagine wearing an EEG headset while the system verifies your identity.
</p>
<p style="font-size: 0.85rem; color: #999; font-style: italic;">
In a real scenario, the headset would capture brainwave patterns for authentication purposes.
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""<div class="disclaimer-box" style="margin: 2rem 0;">
<p style="margin: 0; font-weight: 600; color: #856404;">Research Note</p>
<p style="margin: 0.5rem 0 0 0; color: #856404; font-size: 0.9rem;">
This is a simulation only. No actual EEG data is processed or recorded.
</p>
</div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("Start Authentication", type="primary", use_container_width=True):
        st.session_state.completed_steps.add(1)
        st.switch_page("pages/3_Verification.py")

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin-top: 2rem;">
<h4 style="color: #667eea; font-size: 1rem; margin: 0 0 1rem 0;">💡 What is EEG Authentication?</h4>
<p style="font-size: 0.85rem; color: #666; line-height: 1.6; margin: 0;">
EEG authentication uses brain signals to verify identity. Each person's brainwave patterns are unique, 
making them difficult to replicate or steal. This technology offers potential advantages in security, 
especially against deepfakes and spoofing attacks.
</p>
</div>
""", unsafe_allow_html=True)