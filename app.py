import streamlit as streamlit

x = st.slider("select a value")
st.write(x, 'squared is', x*x)
