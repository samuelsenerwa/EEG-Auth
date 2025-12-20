import streamlit as st
from datetime import datetime
import sys
sys.path.append('..')
from utils import init_session_state, apply_custom_css, render_header, render_stepper, save_survey_to_csv

st.set_page_config(
    page_title="Survey - EEG Auth Study",
    page_icon="🧠",
    layout="centered"
)

init_session_state()
apply_custom_css()

render_header(
    "Your Feedback",
    "Share your thoughts on EEG authentication"
)

render_stepper(4)

st.markdown("""<div class="info-card">
<p style="color: #666; font-size: 0.95rem; line-height: 1.6; margin-bottom: 2rem;">
Please share your perceptions about the simulated EEG authentication experience. 
Your responses will contribute to academic research in cybersecurity and authentication systems.
</p>
</div>""", unsafe_allow_html=True)

st.markdown('<div class="info-card" style="margin-top: 1.5rem;">', unsafe_allow_html=True)

with st.form("survey_form"):
    st.markdown("<h3 style='color: #667eea; font-size: 1.2rem; margin-bottom: 1.5rem;'>📊 Survey Questions</h3>", unsafe_allow_html=True)
    st.caption("Rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""<div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
    <p style="margin: 0; color: #333; font-weight: 500;">1. The EEG authentication process was easy to understand and use.*</p>
    </div>""", unsafe_allow_html=True)
    
    ease_of_use = st.radio(
        "Question 1",
        options=[1, 2, 3, 4, 5],
        horizontal=True,
        format_func=lambda x: {1: "1 - Strongly Disagree", 2: "2 - Disagree", 
                               3: "3 - Neutral", 4: "4 - Agree", 
                               5: "5 - Strongly Agree"}[x],
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""<div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
    <p style="margin: 0; color: #333; font-weight: 500;">2. I would trust EEG authentication for secure work login.*</p>
    </div>""", unsafe_allow_html=True)
    
    trust = st.radio(
        "Question 2",
        options=[1, 2, 3, 4, 5],
        horizontal=True,
        format_func=lambda x: {1: "1 - Strongly Disagree", 2: "2 - Disagree", 
                               3: "3 - Neutral", 4: "4 - Agree", 
                               5: "5 - Strongly Agree"}[x],
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""<div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
    <p style="margin: 0; color: #333; font-weight: 500;">3. I would feel more comfortable using EEG authentication compared to fingerprint recognition.*</p>
    </div>""", unsafe_allow_html=True)
    
    comfort_comparison = st.radio(
        "Question 3",
        options=[1, 2, 3, 4, 5],
        horizontal=True,
        format_func=lambda x: {1: "1 - Strongly Disagree", 2: "2 - Disagree", 
                               3: "3 - Neutral", 4: "4 - Agree", 
                               5: "5 - Strongly Agree"}[x],
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""<div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
    <p style="margin: 0; color: #333; font-weight: 500;">4. I would be comfortable using EEG authentication in a Zero-Trust continuous verification environment.*</p>
    </div>""", unsafe_allow_html=True)
    
    zta_comfort = st.radio(
        "Question 4",
        options=[1, 2, 3, 4, 5],
        horizontal=True,
        format_func=lambda x: {1: "1 - Strongly Disagree", 2: "2 - Disagree", 
                               3: "3 - Neutral", 4: "4 - Agree", 
                               5: "5 - Strongly Agree"}[x],
        label_visibility="collapsed"
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='color: #667eea; font-size: 1rem; margin-bottom: 1rem;'>💬 Additional Comments (Optional)</h4>", unsafe_allow_html=True)
    comments = st.text_area(
        "Please share any additional thoughts or concerns about EEG-based authentication:",
        placeholder="Your comments here (optional)...",
        height=120,
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    submitted = st.form_submit_button("✅ Submit Survey", type="primary", use_container_width=True)
    
    if submitted:
        survey_data = {
            'timestamp': datetime.now().isoformat(),
            'authentication_result': st.session_state.auth_result,
            'ease_of_use': ease_of_use,
            'trust': trust,
            'comfort_comparison': comfort_comparison,
            'zta_comfort': zta_comfort,
            'comments': comments.strip()
        }
        
        save_survey_to_csv(survey_data)
        st.session_state.survey_data = survey_data
        st.session_state.completed_steps.add(4)
        st.switch_page("pages/6_ZeroTrust_Diagram.py")

st.markdown('</div>', unsafe_allow_html=True)