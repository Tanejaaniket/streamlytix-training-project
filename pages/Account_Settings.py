import streamlit as st
from db import update_user_account,verify_user

user_details = None
if "verified" not in st.session_state:
  st.session_state.verified = False
else: 
  st.session_state.verified = False  
if not st.session_state.verified:
  password = st.text_input("Enter your password",type="password")
  btn = st.button("Submit")
  if btn:
    res = verify_user((st.session_state.email,password))
    user_details = res["data"]
    if res["status"]:
      st.session_state.update(verified = True)
      st.success("Verification successfull")
    else:
      st.session_state.update(verified = False)
      st.success("Unable to verify! please recheck your password")

if ((st.session_state.verified) and (user_details != None)):

  st.markdown("""
    <h2 style="text-align: center">Update your account details</h2>
  """,unsafe_allow_html=True)
  new_name = st.text_input("Enter your Name: ",placeholder="Name *",value=user_details[1])
  new_email = st.text_input("Enter your Email: ",placeholder="Email *",value=user_details[2])
  new_password = st.text_input("Enter your Password: ",type="password",placeholder="Password* ",value=user_details[3])
  submit_btn = st.button("Submit",use_container_width=True,type="primary")

  if submit_btn:
    # if (not new_name):
    #   st.error("Name is required")
    # elif ((not new_email) or (new_email.count("@") == 0)):
    #   st.error("Valid email id is required")
    # elif ((not new_password) or (len(new_password) < 8)):
    #   st.error("Password must atleast include 8 characters")
    # else:
    #   print((new_email,new_name))
    user = update_user_account((new_name,new_email,new_password,user_details[2],user_details[3]))
    if user["status"]:
      st.session_state.update(name = new_email)
      st.session_state.update(email = new_email)
      st.success("Account updated sucessfull")
      # st.switch_page("pages/Content.py")
    else:
      st.error("Unable to register please try again.")

with st.sidebar:
  st.page_link("pages/Content.py",label="How to get started")
  st.page_link("pages/Series.py",label="Shows",icon="🎬")
  st.page_link("pages/Movies.py",label="Movies",icon="🎥")
  st.page_link("pages/Search.py",label="Search",icon="🔎")
  st.page_link("pages/Analytics.py",label="Insights / Analytics",icon="📊")
  st.page_link("pages/Already_Watched.py",label="View Already Watched",icon="💾")
  st.page_link("pages/Account_Settings.py",label="Account Settings",icon="🔐")