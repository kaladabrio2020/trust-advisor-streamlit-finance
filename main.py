import streamlit as st

## Import components
from src.your_portfolium.your_portfolium       import your_portfolium
from src.series_information.series_information import series_information
from src.trust_advisor.trust_advisor           import trust_advisor
from src.about.about import about
# theme

OPTIONS = {
    'about'         : 'About',
    'your_portfolio': 'Your Portfolio',
    'series_information': 'Series Information',
    'trust_advisor' : 'Trust Advisor'
}


# Sidebar
choice = st.sidebar.selectbox(
    label   = 'Select a page', 
    options = list(OPTIONS.values()), 
    index   = 0, # Default about, but can be changed
    
)

# Options selection
match choice:
    case 'Your Portfolio':
        your_portfolium()
    case 'About':
        about()
    case 'Series Information':
        series_information()
    case 'Trust Advisor':
        trust_advisor()
