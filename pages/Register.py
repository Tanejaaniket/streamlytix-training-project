import streamlit as st

st.markdown("""
    <style>
              
    </style>
  """,unsafe_allow_html=True)

with st.form("form2"):
  st.markdown("""
    <h2 style="text-align: center">Welcome back to Streamlytix</h2>
  """,unsafe_allow_html=True)
  name = st.text_input("Enter your Name: ",placeholder="Name *")
  email = st.text_input("Enter your Email: ",placeholder="Email *")
  password = st.text_input("Enter your Password: ",type="password",placeholder="Password* ")
  submit_btn = st.form_submit_button("Submit",use_container_width=True,type="primary")
  st.page_link("pages/Login.py",label="Already had a Streamlytix account? Click here to login")

  