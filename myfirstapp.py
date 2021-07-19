import streamlit as st

import numpy as np
import pandas as pd
import time



st.header("My first Streamlit App")

button = st.button("Covid_19 Data")
st.write("Please click on the button above for general info")

st.text_input('First name:')
show = st.text_input


if show:
    st.text_input('Last name:')

else:
    st.text_input('Please type your Last name:')



st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')
if show:
        st.write(pd.DataFrame({
        'Region': ['Americas', 'Asia', 'Europe', 'Africa', 'Oceania'],
        'Covid_19 Cases (as of 18/05/2021)': [50000, 20000, 30000, 40000, 10000]
        }))
else:
    'Thank you, please proceed'

data = pd.read_csv("covid19_data.csv")

# st.sidebar.checkbox("Show Analysis by State", True, key=1)
# select = st.sidebar.selectbox('Select a Country',data['country'])

option = st.sidebar.selectbox(
    'Select a Region',
     ['Americas','Asia','Europe','Africa','Oceania'])
