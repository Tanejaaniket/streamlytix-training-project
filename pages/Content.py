import streamlit as st
from component.sidebar import sidebar

#Private route protection
if "name" not in st.session_state or "email" not in st.session_state:
  st.switch_page("pages/Login.py")

#Loads sidebar  
sidebar()

#Page content
st.header(f"👋🏻 Hi there {st.session_state.name} Team Streamlytix welcomes you...")  
st.markdown("""
  > Welcome to the world of movies and tv shows. Here are some quick instructions to help you get started to get insights, based on  your watch history :
  > - Starting with the app
  >   - Navigate to the required content (either shows or movies).
  >   - Mark the content as watched.
  >   - Make sure to mark enough content to get usefull insights.
  >   - Enjoy your valuable insights and recommendations on what to watch next.
  > ---          
  > _Note: You can always search for your favourite movies and tv shows from the search option in the sidebar._
  >          
""",unsafe_allow_html=True)

