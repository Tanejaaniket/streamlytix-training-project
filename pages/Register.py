import streamlit as st
from utils.db import register_user
from utils.helper import init_user,init_watched_content

#Public route protection
if ("name" in st.session_state and st.session_state.name != None) and "email" in st.session_state:
  st.switch_page("pages/Content.py")

#Initialize users session states  
init_user()

#Registration Form
with st.form("register_form"):
  st.markdown("""
    <h2 style="text-align: center">Welcome back to Streamlytix</h2>
  """,unsafe_allow_html=True)
  name = st.text_input("Enter your Name: ",placeholder="Name *")
  email = st.text_input("Enter your Email: ",placeholder="Email *")
  password = st.text_input("Enter your Password: ",type="password",placeholder="Password* ")
  submit_btn = st.form_submit_button("Submit",use_container_width=True,type="primary")
  st.page_link("pages/Login.py",label="Already had a Streamlytix account? Click here to login")

#Form validation checks
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
      st.session_state.logged_in = True
      st.session_state.name = name
      st.session_state.email = email
      init_watched_content()
      st.success("User registered sucessfull")
      st.switch_page("pages/Content.py")
    else:
      st.error("Unable to register please try again.")