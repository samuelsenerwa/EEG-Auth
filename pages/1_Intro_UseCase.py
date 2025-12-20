import streamlit as st
import sys
sys.path.append('..')
from utils import init_session_state, apply_custom_css, render_header, render_stepper, render_brain_icon

st.set_page_config(
    page_title="Welcome - EEG Auth Study",
    page_icon="🧠",
    layout="centered"
)

init_session_state()
apply_custom_css()

render_header(
    "EEG Authentication Research Study",
    "Exploring user acceptance of brainwave-based authentication for secure access"
)

render_stepper(0)

st.markdown('<div class="info-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 3rem; color: #667eea;">🧠</div>
        <h3 style="font-size: 1.1rem; margin: 0.5rem 0;">Experience EEG Auth</h3>
        <p style="font-size: 0.85rem; color: #666;">Simulate an EEG-based authentication process through our interactive demo</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 3rem; color: #667eea;">🛡️</div>
        <h3 style="font-size: 1.1rem; margin: 0.5rem 0;">Compare Methods</h3>
        <p style="font-size: 0.85rem; color: #666;">Review how EEG compares to fingerprint, Face ID, and Voice ID</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 3rem; color: #667eea;">👥</div>
        <h3 style="font-size: 1.1rem; margin: 0.5rem 0;">Share Feedback</h3>
        <p style="font-size: 0.85rem; color: #666;">Help shape the future of authentication with your insights</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""<div class="info-card" style="margin-top: 2rem;">
<h2 style="color: #333; font-size: 1.4rem; margin-bottom: 1rem;">📋 About This Study</h2>
<p style="line-height: 1.8; color: #555;">
This research explores user acceptance of <strong>EEG (electroencephalogram)</strong> authentication as an alternative to traditional biometric methods. 
EEG authentication uses brainwave patterns to verify identity, offering unique advantages in security and deepfake resistance.
</p>
<p style="line-height: 1.8; color: #555; margin-top: 1rem;">
Through this prototype, you'll experience a <strong>mock EEG authentication process</strong>, compare it with other biometric methods, 
and provide valuable feedback.
</p>
<div style="background: #f0f4ff; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
<p style="margin: 0; color: #667eea; font-weight: 600;">⏱ Estimated time: 10-15 minutes</p>
</div>
</div>""", unsafe_allow_html=True)

st.markdown("""<div class="disclaimer-box">
<p style="margin: 0; font-weight: 600; color: #856404;">⚠️ Important Disclaimer</p>
<p style="margin: 0.5rem 0 0 0; color: #856404; font-size: 0.9rem;">
This simulation does not record any personal or EEG data. All responses are anonymous and used solely for academic research purposes.
</p>
</div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Begin Study", type="primary", use_container_width=True):
    st.session_state.completed_steps.add(0)
    st.switch_page("pages/2_Preparation.py")

st.markdown("""<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: white; border-radius: 10px;">
<p style="color: #999; font-size: 0.85rem; margin: 0;">
<span class="research-badge">Research Prototype</span>
</p>
<p style="color: #999; font-size: 0.75rem; margin: 0.5rem 0 0 0;">
Biometric Authentication Research • Zero-Trust Security Framework
</p>
</div>""", unsafe_allow_html=True)