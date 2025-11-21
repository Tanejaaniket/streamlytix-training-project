import streamlit as st
from utils.db import login_user
from utils.helper import init_user,init_watched_content

#Public route protection
if "name" in st.session_state and st.session_state.name != None:
  st.switch_page("pages/Content.py")
  st.stop()

#Initalize users session states
init_user()

#Login form
with st.form("form1"):
  st.markdown("""
    <h2 style="text-align: center">Welcome back to Streamlytix</h2>
  """,unsafe_allow_html=True)
  email = st.text_input("Enter your Email: ",placeholder="Email *")
  password = st.text_input("Enter your Password: ",type="password",placeholder="Password* ")
  submit_btn = st.form_submit_button("Submit",use_container_width=True,type="primary")
  st.page_link("pages/Register.py",label="New to Streamlytix? Click here to register")

#Form validation checks
if submit_btn:
  if ((not email) or (email.count("@") == 0)):
    st.error("Valid email id is required")
  elif ((not password) or (len(password) < 8)):
    st.error("Password must atleast include 8 characters")
  else:  
    user = login_user((email,password))
    if user["status"]:
      st.session_state.logged_in = True
      st.session_state.name = user["data"][1]
      st.session_state.email = user["data"][2]
      init_watched_content()
      st.success("User login sucessfull")
      st.switch_page("pages/Content.py")
    else:
      st.error("Unable to log in please recheck your email and password")