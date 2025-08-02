import streamlit as st
from db import login_user
from user import user_info
st.markdown("""
    <style>
              
    </style>
  """,unsafe_allow_html=True)
with st.form("form1"):
  st.markdown("""
    <h2 style="text-align: center">Welcome back to Streamlytix</h2>
  """,unsafe_allow_html=True)
  email = st.text_input("Enter your Email: ",placeholder="Email *")
  password = st.text_input("Enter your Password: ",type="password",placeholder="Password* ")
  submit_btn = st.form_submit_button("Submit",use_container_width=True,type="primary")
  st.page_link("pages/Register.py",label="New to Streamlytix? Click here to register")

if submit_btn:
  user = login_user((email,password))
  if user["status"]:
    user_info.set_user_info(user["data"])
    st.success("User login sucessfull")
    st.switch_page("pages/Content.py")
  else:
    st.error("Unable to log in please recheck your email and password")