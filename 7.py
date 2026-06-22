import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\13\heart_failure.csv')

tab1, tab2 = st.tabs(['표', '차트'])

with tab1:
    st.dataframe(df)
    
with tab2 :
    fig, ax = plt.subplots()
    ax.hist(df['age'])