# Simulated EEG Authentication Study

## Overview

This is an academic research prototype designed to study user perception, trust, and acceptance of EEG-based authentication within Zero-Trust continuous authentication contexts.

**⚠️ IMPORTANT: This is NOT a real biometric system.**

## Purpose

This application is a **simulation only** used to:
- Study user perceptions of authentication technologies
- Gather feedback on EEG-based authentication concepts
- Research acceptance of continuous authentication in Zero-Trust environments
- Collect anonymous survey data for academic research

## What This Application Does NOT Do

- Process or collect real EEG data
- Use machine learning or AI classification
- Perform actual biometric verification
- Make security or performance claims
- Store personal or identifiable information

## What This Application DOES Do

- Simulates an EEG authentication experience
- Uses randomized outcomes (85% success rate)
- Collects anonymous survey responses
- Stores data locally in CSV format
- Provides educational comparison of authentication methods

## Technical Stack

- **Python 3.x** (tested with Python 3.12.3)
- **Streamlit** (web framework)
- **Standard library only**: `random`, `time`, `csv`, `datetime`, `os`

## Installation

1. Ensure Python 3.x is installed:
   ```bash
   python3 --version
   ```

2. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Application Flow

The application follows a 6-step process:

1. **Introduction** - Study overview and disclaimer
2. **Simulation** - Mock EEG authentication process (3-second animation)
3. **Result** - Randomized authentication outcome (granted/denied)
4. **Comparison** - Table comparing authentication methods
5. **Survey** - 4 Likert-scale questions + optional comments
6. **Completion** - Thank you message and data confirmation

## Data Collection

Survey responses are saved to `survey_responses.csv` with the following fields:

- `timestamp` - ISO format timestamp
- `authentication_result` - "granted" or "denied"
- `ease_of_use` - Likert scale 1-5
- `trust` - Likert scale 1-5
- `comfort_comparison` - Likert scale 1-5
- `zta_comfort` - Likert scale 1-5
- `comments` - Optional free text

**All data is anonymous and stored locally.**

## Ethical Considerations

This simulation explicitly:
- Labels all processes as "simulated" or "mock"
- Provides clear disclaimers about data collection
- Uses randomized outcomes (not real analysis)
- Maintains academic and research-focused language
- Avoids misleading claims about accuracy or security

## File Structure

```
eeg-auth/
├── app.py                           # Main entry point (redirects to pages)
├── utils.py                         # Shared utilities and UI components
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── pages/                           # Multi-page application structure
│   ├── 1_Intro_UseCase.py          # Welcome/Introduction page
│   ├── 2_Preparation.py            # Authentication login page
│   ├── 3_Verification.py           # Processing/verification page
│   ├── 4_Result.py                 # Authentication result page
│   ├── 5_Feedback_Survey.py        # Survey questions page
│   └── 6_ZeroTrust_Diagram.py      # Completion/thank you page
└── survey_responses.csv             # Generated after first survey submission
```

## Code Structure

The application uses Streamlit's multi-page architecture with:

- **app.py**: Entry point that initializes session state and redirects to first page
- **utils.py**: Shared components including:
  - Custom CSS styling with gradient themes
  - Progress stepper navigation
  - SVG icon renderers (brain, user, waveform)
  - CSV data storage functions
- **pages/**: Individual page files for each step of the study
  - Modern UI with cards, gradients, and animations
  - Progress tracking with visual stepper
  - Consistent styling across all pages

## Research Context

This prototype is designed for academic research in:
- Cybersecurity authentication systems
- User experience and human-computer interaction
- Zero-Trust Architecture (ZTA) acceptance
- Biometric authentication perception studies

## References

The comparison table cites:
- Verdoliva (2020) - Deepfake detection
- Jain et al. (2016) - Biometric systems
- Wang et al. (2022) - Authentication technologies

## License

This is an academic research prototype. Use only for educational and research purposes.

## Support

For questions about this research study, please contact the research team.

---

**Last Updated**: December 2024
