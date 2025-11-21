import streamlit as st

pg = st.navigation(
  ["pages/Home.py",
  "pages/Login.py",
  "pages/Register.py",
  "pages/Content.py",
  "pages/Movies.py",
  "pages/Series.py",
  "pages/Search.py",
  "pages/Analytics.py",
  "pages/Account_Settings.py",
  "pages/Already_Watched.py",
  ],position="hidden"
)

pg.run()