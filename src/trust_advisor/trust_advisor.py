import streamlit as st

import os 
import pathlib
import pickle
from   sklearn.ensemble import RandomForestRegressor


DATA_DIR = pathlib.Path(__file__).parent.parent.parent


def trust_advisor():
    st.title("Trust Advisor")
    st.write("This section is under development. Please check back later for updates.")

    AGE = st.sidebar.slider('Age', 20, 100)
    EDU = st.sidebar.slider('Education Level', 1, 5)
    INC = st.sidebar.slider('Income Level', 1, 10)
    MAD = st.sidebar.selectbox('Marital Status', ['Not Married', 'Married'])
    KID = st.sidebar.slider('Number of Kids', 0, 8)
    OCU = st.sidebar.selectbox('Occupation', ['Unemployed', 'Employed', 'Self-Employed', 'Retired'])
    NET = st.sidebar.slider('Net Worth', 0, 1000000, step=1000)
    RIK = st.sidebar.slider('Risk Tolerance', 1, 4)

    MAD = 1 if MAD == 'Married' else 0
    OCU = ['Unemployed', 'Employed', 'Self-Employed', 'Retired'].index(OCU)
    X = [[AGE, EDU, MAD, KID, OCU, INC, RIK, NET]]

    st.write(f'{model(X)}')

def model(X):
    with open(DATA_DIR / 'models' / 'trust_advisor' / 'model_random_forest.pkl', 'rb') as f:
        model = pickle.load(f)
        pred = model.predict(X)
    return pred
