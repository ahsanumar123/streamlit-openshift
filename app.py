import streamlit as st
selection = st.selectbox(label = "Select One", options =["papu", "chapu"], index=0)
st.write(selection)