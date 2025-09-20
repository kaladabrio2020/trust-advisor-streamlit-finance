import streamlit as st 
import pathlib 
import pickle
import os

BASE_ID = pathlib.Path(__file__).parent.parent


def save_data(input_id_fred):
    with open(BASE_ID / 'data' / 'id_fred.pkl', 'wb') as f:
        pickle.dump(input_id_fred, f)


def open_data():
    with open(BASE_ID / 'data' / 'id_fred.pkl', 'rb') as f:
        input_id_fred = pickle.load(f)
    return input_id_fred


def config():
    st.set_page_config(layout="wide", page_title="Your Portfolio", page_icon=':moneybag:')


    # Exist id
    if not os.path.exists(BASE_ID / 'data' / 'id_fred.pkl'):
        pass

    # ID Fred
    input_id_fred = st.text_input('ID FRED', 'A0B2C0D0E0F0G0H0I0J0K0L0M0N0O0P0Q0R0S0T0U0V0W0X0Y0Z0', disabled=True, placeholder='ID FRED', help='ID FRED')

    # Save

    button = st.button('Save')

    if button:
        save_data(input_id_fred)
