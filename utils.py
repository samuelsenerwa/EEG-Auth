import streamlit as st
import csv
import os
from datetime import datetime

CSV_FILE = "survey_responses.csv"

def init_session_state():
    """Initialize session state variables"""
    if 'auth_result' not in st.session_state:
        st.session_state.auth_result = None
    if 'survey_data' not in st.session_state:
        st.session_state.survey_data = {}
    if 'completed_steps' not in st.session_state:
        st.session_state.completed_steps = set()

def save_survey_to_csv(data):
    """Save survey response to CSV file"""
    file_exists = os.path.isfile(CSV_FILE)
    
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['timestamp', 'authentication_result', 'ease_of_use', 
                     'trust', 'comfort_comparison', 'zta_comfort', 'comments']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)

def apply_custom_css():
    """Apply custom CSS styling for modern UI"""
    st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background: radial-gradient(circle at top, #f2f5ff 0%, #ffffff 45%, #f8f9fc 100%);
        color: #142044;
    }
    
    .stApp {
        background: #eef2ff;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .header-title {
        color: white;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0;
        text-align: center;
    }
    
    .header-subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 0.95rem;
        margin: 0.5rem 0 0 0;
        text-align: center;
    }
    
    /* Progress stepper styling */
    .stepper-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 2rem 0;
        padding: 0 1rem;
    }
    
    .step-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        flex: 1;
        position: relative;
    }
    
    .step-circle {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 0.9rem;
        z-index: 2;
        background: white;
        border: 3px solid #e0e0e0;
        color: #999;
    }
    
    .step-circle.completed {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-color: #667eea;
        color: white;
    }
    
    .step-circle.active {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-color: #667eea;
        color: white;
        box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.2);
    }
    
    .step-label {
        margin-top: 0.5rem;
        font-size: 0.75rem;
        color: #666;
        text-align: center;
    }
    
    .step-label.active {
        color: #667eea;
        font-weight: 600;
    }
    
    .step-line {
        position: absolute;
        top: 20px;
        left: -50%;
        width: 100%;
        height: 3px;
        background: #e0e0e0;
        z-index: 1;
    }
    
    .step-line.completed {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    .step-item:first-child .step-line {
        display: none;
    }
    
    /* Card styling */
    .info-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        margin: 1.5rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Ensure radio option text stays readable */
    .stRadio div[role="radiogroup"] label, 
    .stRadio div[role="radiogroup"] label p {
        color: #0f172a !important;
        font-weight: 500;
    }

    /* Brain icon animation */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    .brain-icon {
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Waveform animation */
    @keyframes wave {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .wave-line {
        animation: wave 1.5s ease-in-out infinite;
    }
    
    /* Research badge */
    .research-badge {
        display: inline-block;
        background: rgba(102, 126, 234, 0.1);
        color: #667eea;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-left: 0.5rem;
    }
    
    /* Disclaimer box */
    .disclaimer-box {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Table styling */
    .stTable {
        border-radius: 8px;
        overflow: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

def render_header(title, subtitle=None):
    """Render modern header with gradient background"""
    subtitle_html = f'<p class="header-subtitle">{subtitle}</p>' if subtitle else ''
    st.markdown(f"""
    <div class="header-container">
        <h1 class="header-title">{title}</h1>
        {subtitle_html}
    </div>
    """, unsafe_allow_html=True)

def render_stepper(current_step):
    """Render progress stepper navigation"""
    steps = [
        ("Welcome", "1"),
        ("Authentication", "2"),
        ("Results", "3"),
        ("Comparison", "4"),
        ("Survey", "5"),
        ("Complete", "6")
    ]
    
    stepper_html = '<div class="stepper-container">'
    
    for idx, (label, num) in enumerate(steps):
        is_completed = idx < current_step
        is_active = idx == current_step
        
        circle_class = "step-circle"
        if is_completed:
            circle_class += " completed"
            icon = "✓"
        elif is_active:
            circle_class += " active"
            icon = num
        else:
            icon = num
        
        label_class = "step-label active" if is_active else "step-label"
        
        line_html = ""
        if idx > 0:
            line_class = "step-line completed" if is_completed else "step-line"
            line_html = f'<div class="{line_class}"></div>'
        
        stepper_html += f'<div class="step-item">{line_html}<div class="{circle_class}">{icon}</div><div class="{label_class}">{label}</div></div>'
    
    stepper_html += '</div>'
    st.markdown(stepper_html, unsafe_allow_html=True)

def render_brain_icon(size=100, animated=True):
    """Render brain icon SVG"""
    animation_class = "brain-icon" if animated else ""
    st.markdown(f"""
    <div style="text-align: center; margin: 2rem 0;">
        <svg class="{animation_class}" width="{size}" height="{size}" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="#e8eaf6" opacity="0.5"/>
            <path d="M30 40 Q 35 25, 50 30 T 70 40" stroke="#667eea" stroke-width="3" fill="none"/>
            <path d="M30 50 Q 35 35, 50 40 T 70 50" stroke="#667eea" stroke-width="3" fill="none"/>
            <path d="M30 60 Q 35 45, 50 50 T 70 60" stroke="#667eea" stroke-width="3" fill="none"/>
            <circle cx="50" cy="45" r="25" stroke="#764ba2" stroke-width="3" fill="none" opacity="0.6"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)

def render_user_icon(size=80):
    """Render user icon SVG"""
    st.markdown(f"""
    <div style="text-align: center; margin: 2rem 0;">
        <svg width="{size}" height="{size}" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="45" fill="#e3f2fd" opacity="0.5"/>
            <circle cx="50" cy="35" r="12" stroke="#667eea" stroke-width="3" fill="none"/>
            <path d="M 30 70 Q 50 55, 70 70" stroke="#667eea" stroke-width="3" fill="none"/>
            <path d="M 35 65 L 35 75" stroke="#00bcd4" stroke-width="2"/>
            <path d="M 65 65 L 65 75" stroke="#00bcd4" stroke-width="2"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)

def render_waveform(width=400, height=100):
    """Render animated waveform"""
    st.markdown(f"""
    <div style="text-align: center; margin: 2rem 0;">
        <svg width="{width}" height="{height}" viewBox="0 0 400 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path class="wave-line" d="M 0 50 Q 50 20, 100 50 T 200 50 T 300 50 T 400 50" 
                  stroke="#667eea" stroke-width="3" fill="none" opacity="0.8"/>
            <path class="wave-line" d="M 0 50 Q 50 70, 100 50 T 200 50 T 300 50 T 400 50" 
                  stroke="#764ba2" stroke-width="3" fill="none" opacity="0.6" 
                  style="animation-delay: 0.3s;"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)
