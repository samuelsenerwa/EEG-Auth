import streamlit as st
import sys
sys.path.append('..')
from utils import init_session_state, apply_custom_css, render_header, render_stepper

st.set_page_config(
    page_title="Results - EEG Auth Study",
    page_icon="🧠",
    layout="centered"
)

init_session_state()
apply_custom_css()

if st.session_state.auth_result == "granted":
    render_header(
        "Authentication Successful",
        "Your simulated neural identity has been verified"
    )
else:
    render_header(
        "Authentication Failed",
        "Simulated brainwave mismatch detected"
    )

render_stepper(3)

st.markdown('<div class="info-card" style="text-align: center; padding: 3rem 2rem;">', unsafe_allow_html=True)

if st.session_state.auth_result == "granted":
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("assets/success.png", width=100)
    
    st.markdown("""
    <h2 style="color: #4caf50; font-size: 1.8rem; margin: 1.5rem 0;">Access Granted</h2>
    
    <p style="color: #555; font-size: 1rem; line-height: 1.8; margin: 1.5rem 0;">
        Your simulated neural identity has been matched successfully.
    </p>
    
    <div style="background: #e8f5e9; padding: 1.5rem; border-radius: 10px; margin: 2rem 0;">
        <p style="color: #2e7d32; font-size: 0.9rem; line-height: 1.6; margin: 0;">
            <strong>In a real system:</strong> Continuous authentication would now be active, 
            periodically verifying your identity in the background without requiring repeated logins.
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image("assets/failure.png", width=100)
    
    st.markdown("""
    <h2 style="color: #f44336; font-size: 1.8rem; margin: 1.5rem 0;">Access Denied</h2>
    
    <p style="color: #555; font-size: 1rem; line-height: 1.8; margin: 1.5rem 0;">
        Simulated brainwave mismatch detected — re-authentication would be required.
    </p>
    
    <div style="background: #ffebee; padding: 1.5rem; border-radius: 10px; margin: 2rem 0;">
        <p style="color: #c62828; font-size: 0.9rem; line-height: 1.6; margin: 0;">
            <strong>In a real system:</strong> You would be prompted to authenticate again using 
            the EEG headset or a fallback authentication method.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""<div class="disclaimer-box" style="margin: 2rem 0;">
<p style="margin: 0; font-weight: 600; color: #856404;">📝 Note</p>
<p style="margin: 0.5rem 0 0 0; color: #856404; font-size: 0.9rem;">
This outcome was randomly generated for research purposes. Please continue with the study.
</p>
</div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("➡️ Continue to Comparison", type="primary", use_container_width=True):
    st.session_state.completed_steps.add(3)
    st.switch_page("pages/5_Feedback_Survey.py")