import streamlit as st
selection = st.selectbox(label = "Select One", options =["papu", "chapu","tapu"], index=0)
st.write(selection)