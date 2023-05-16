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


import matplotlib.pyplot as plt
import numpy as np

rand = np.random.normal(1,2,size=20)
fig, ax = plt.subplots()
ax.hist(rand,bins=15) #,color="yellow"
st.pyplot(fig)
