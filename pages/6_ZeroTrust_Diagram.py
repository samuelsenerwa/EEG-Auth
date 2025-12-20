import streamlit as st
import sys
sys.path.append('..')
from utils import init_session_state, apply_custom_css, render_header, render_stepper

st.set_page_config(
    page_title="Complete - EEG Auth Study",
    page_icon="🧠",
    layout="centered"
)

init_session_state()
apply_custom_css()

render_header(
    "Thank You!",
    "Your feedback contributes to cutting-edge cybersecurity research"
)

render_stepper(5)

st.markdown('<div class="info-card" style="text-align: center; padding: 2rem;">', unsafe_allow_html=True)

st.markdown("""
<div style="margin: 2rem 0;">
    <div style="width: 100px; height: 100px; margin: 0 auto; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 50%; display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 3rem;">✓</span>
    </div>
</div>

<h2 style="color: #333; font-size: 1.8rem; margin: 1.5rem 0;">Survey Completed Successfully</h2>

<p style="color: #666; font-size: 1rem; line-height: 1.8;">
Your feedback contributes to academic research in cybersecurity and authentication systems.
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""<div class="info-card" style="margin-top: 2rem;">
<h3 style="color: #667eea; font-size: 1.3rem; margin-bottom: 1.5rem;">🎓 Research Impact</h3>
<p style="color: #555; line-height: 1.8; margin-bottom: 1rem;">
Your responses will be analyzed alongside other participants to understand:
</p>
<ul style="color: #555; line-height: 2; margin-left: 1.5rem;">
    <li>User comfort with different authentication methods</li>
    <li>Trust factors in biometric systems</li>
    <li>Acceptance of continuous authentication in Zero-Trust environments</li>
</ul>
<p style="color: #555; line-height: 1.8; margin-top: 1rem;">
The findings will contribute to research on biometric authentication methods and their role in Zero-Trust security frameworks.
</p>
</div>""", unsafe_allow_html=True)

st.markdown("""<div class="info-card" style="margin-top: 2rem;">
<h3 style="color: #667eea; font-size: 1.3rem; margin-bottom: 1.5rem;">Authentication Methods Comparison</h3>
<p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">
The table below compares different biometric authentication modalities based on academic literature and industry research.
</p>
</div>""", unsafe_allow_html=True)

comparison_data = {
    "Method": ["Fingerprint", "Face ID", "Voice ID", "EEG (simulated)"],
    "Resistance to Deepfakes": ["Moderate", "Low-Moderate", "Low", "High"],
    "Convenience": ["High", "High", "High", "Moderate"],
    "Privacy Risk": ["Moderate", "High", "Moderate", "Low"],
    "Cost": ["Low", "Low", "Low", "High"]
}

st.table(comparison_data)

st.caption("""
**Figure:** Comparison of biometric modalities based on literature 
(Verdoliva, 2020; Jain et al., 2016; Wang et al., 2022).
""")

st.markdown("""<div class="info-card" style="margin-top: 2rem; background: #f0f4ff;">
<h3 style="color: #667eea; font-size: 1.1rem; margin-bottom: 1rem;">🔒 Key Reminders</h3>
<ul style="color: #555; line-height: 2; margin: 0;">
    <li>All responses are completely anonymous</li>
    <li>No personal or biometric data was collected</li>
    <li>The authentication process was entirely simulated</li>
    <li>Your data is stored locally and used only for research purposes</li>
</ul>
</div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.balloons()

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("Return to Start", type="secondary", use_container_width=True):
        st.session_state.auth_result = None
        st.session_state.survey_data = {}
        st.session_state.completed_steps = set()
        st.switch_page("pages/1_Intro_UseCase.py")

st.markdown("""<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: white; border-radius: 10px;">
<p style="color: #999; font-size: 0.85rem; margin: 0;">
<span class="research-badge">Research Prototype</span>
</p>
<p style="color: #999; font-size: 0.75rem; margin: 0.5rem 0 0 0;">
Biometric Authentication Research • Zero-Trust Security Framework
</p>
<p style="color: #999; font-size: 0.75rem; margin: 0.5rem 0 0 0;">
Thank you for participating in this research study!
</p>
</div>""", unsafe_allow_html=True)