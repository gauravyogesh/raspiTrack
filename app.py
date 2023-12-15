import streamlit as st 
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/gauravyogesh/Track/main/saved.csv')

filled_space =  df['Status'].values.sum()
empty_space = len(df) -  filled_space

st.header("Occupency Table")
st.dataframe(df)

st.text(f"Occuped space {filled_space}.")
st.text(f"Available space {empty_space}.")
