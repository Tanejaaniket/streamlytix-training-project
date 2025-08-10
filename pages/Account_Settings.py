import streamlit as st
from db import update_user_account,verify_user
import os
import time
from component.sidebar import sidebar

sidebar()

if "verified" not in st.session_state:
  st.session_state.verified = False

if "user_details" not in st.session_state:
  st.session_state.user_details = None

password = None

st.header("Update account details")
if not st.session_state.verified:
  with st.form("verification"):
    password = st.text_input("Enter your password to update account details",type="password")
    btn = st.form_submit_button("Submit",type="primary",use_container_width=True)
  if btn:
    res = verify_user((st.session_state.email,password))
    st.session_state.update(user_details = res["data"])
    if res["status"]:
      st.session_state.update(verified = True)
      st.success("Verification successfull")
    else:
      st.session_state.update(verified = False)
      st.success("Unable to verify! please recheck your password")

if ((st.session_state.verified) and (st.session_state.user_details != None)):
  with st.form("update_form"):
    st.markdown("""
      <h2 style="text-align: center">Update your account details</h2>
    """,unsafe_allow_html=True)
    new_name = st.text_input("Enter your Name: ",placeholder="Name *",value=st.session_state.user_details[1])
    new_email = st.text_input("Enter your Email: ",placeholder="Email *",value=st.session_state.user_details[2])
    new_password = st.text_input("Enter your Password: ",type="password",placeholder="Password* ",value=st.session_state.user_details[3])
    submit_btn = st.form_submit_button("Submit",use_container_width=True,type="primary")
  if submit_btn:
    if (not new_name):
      st.error("Name is required")
    elif ((not new_email) or (new_email.count("@") == 0)):
      st.error("Valid email id is required")
    elif ((not new_password) or (len(new_password) < 8)):
      st.error("Password must atleast include 8 characters")
    else:
      user = update_user_account((new_name,new_email,new_password,st.session_state.user_details[2],st.session_state.user_details[3]))
      if user["status"]:
        st.session_state.update(name = new_name)
        st.session_state.update(email = new_email)
        st.session_state.update(verified = False)
        password = None
        os.rename(f"user/content/movies/{st.session_state.user_details[2]}.csv",f"user/content/movies/{new_email}.csv")
        os.rename(f"user/content/series/{st.session_state.user_details[2]}.csv",f"user/content/series/{new_email}.csv")
        st.session_state.pop("user_details")
        st.toast("Account updated sucessfull")
        time.sleep(5.0)
        st.switch_page("pages/Content.py")
      else:
        st.error("Unable to update please try again.")
