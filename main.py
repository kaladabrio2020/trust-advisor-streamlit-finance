import streamlit as st

## Import components
from src.your_portfolium.your_portfolium import your_portfolium




def about():
    ## Style
    st.set_page_config(layout="wide", page_title="About")
    
    st.title("Trust Advisor Streamlit Finance")
    st.markdown('''
### About
''')

OPTIONS = {
    'about'         : 'About',
    'your_portfolio': 'Your Portfolio'
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