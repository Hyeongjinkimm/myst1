import streamlit as st

x = st.slider("select a value")
st.write(x, 'squared is', x*x)

st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender",["Male","Female"])
import pandas as pd
import numpy as np
df = pd.DataFrame(
  np.random.randn(10,2),
  columns=['x','y'])
st.line_chart(df)


df = pd.DataFrame(np.random.randn(500,2) / [50,50] + [37.76, -122.4],
columns=['lat','lon']
st.map(df)
