import streamlit as st
from db import register_user
from user import user_info

if user_info.user_info["name"] != None:
  st.switch_page("pages/Content.py")

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

if submit_btn:
  if (not name):
    st.error("Name is required")
  elif ((not email) or (email.count("@") == 0)):
    st.error("Valid email id is required")
  elif ((not password) or (len(password) < 8)):
    st.error("Password must atleast include 8 characters")
  else:  
    user = register_user((name,email,password))
    if user["status"]:
      user_info.set_user_info((0,name,email,password))
      st.success("User registered sucessfull")
      st.switch_page("pages/Content.py")
    else:
      st.error("Unable to register please try again.")