import streamlit as st

pg = st.navigation(
  ["pages/Home.py",
  "pages/About.py",
  "pages/Login.py",
  "pages/Register.py",
  "pages/Content.py",
  ],position="hidden"
)

pg.run()