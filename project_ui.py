import streamlit as st
import os

#TODO: Add about us,private routes security, movie/series recommendations from yt, mailer (see chat gpt for more) 


pg = st.navigation(
  ["pages/Home.py",
  "pages/About.py",
  "pages/Login.py",
  "pages/Register.py",
  "pages/Content.py",
  "pages/Movies.py",
  "pages/Series.py",
  "pages/Search.py",
  "pages/Analytics.py",
  "pages/Account_Settings.py",
  "pages/Watchlist.py",
  "pages/Already_Watched.py",
  ],position="hidden"
)

pg.run()