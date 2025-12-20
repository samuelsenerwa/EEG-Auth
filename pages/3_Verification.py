import streamlit as st
import time
import random
import sys
sys.path.append('..')
from utils import init_session_state, apply_custom_css, render_header, render_stepper, render_brain_icon, render_waveform

st.set_page_config(
    page_title="Verification - EEG Auth Study",
    page_icon="🧠",
    layout="centered"
)

init_session_state()
apply_custom_css()

render_header(
    "Verification in Progress",
    "Reading brainwave patterns..."
)

render_stepper(2)

# st.markdown('<div class="info-card" style="text-align: center; padding: 3rem 2rem;">', unsafe_allow_html=True)

# render_brain_icon(100, animated=True)

st.markdown("""
<h2 style="color: #333; font-size: 1.5rem; margin: 2rem 0 1rem 0;">Verification in Progress</h2>
<p style="color: #666; font-size: 0.95rem;">Reading brainwave patterns...</p>
""", unsafe_allow_html=True)

render_waveform(400, 100)

status_placeholder = st.empty()
progress_bar = st.progress(0)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<p style="text-align: center; color: #999; font-size: 0.85rem; font-style: italic; margin-top: 2rem;">
Do not remove headset during verification
</p>
""", unsafe_allow_html=True)

steps = [
    ("Initializing mock verification system...", 0.33),
    ("Simulating brainwave pattern analysis...", 0.66),
    ("Processing simulated neural signature...", 1.0)
]

for step_text, progress_value in steps:
    status_placeholder.markdown(f"""
    <div style="text-align: center; margin: 1rem 0;">
        <p style="color: #667eea; font-weight: 600; font-size: 1rem;">{step_text}</p>
    </div>
    """, unsafe_allow_html=True)
    progress_bar.progress(progress_value)
    time.sleep(1.2)

success_rate = random.random()
if success_rate <= 0.85:
    st.session_state.auth_result = "granted"
else:
    st.session_state.auth_result = "denied"

st.session_state.completed_steps.add(2)
time.sleep(0.5)
st.switch_page("pages/4_Result.py")