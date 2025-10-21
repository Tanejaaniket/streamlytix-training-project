import streamlit as st

#Public route protection
if "name" in st.session_state and "email" in st.session_state:
  st.switch_page("pages/Content.py")

#Page content
st.title("Welcome to Streamlytix")
st.markdown("""
  <p>This is a data analaysis, machine learning project built with the help of Python and its various libraries and frameworks mainly Pandas, Numpy, Matplotlib, Seaborn, Plotly-express, Schikit-Learn. The project's ui is built with the help of Streamlit.</p>
  <p>Main focus of this project is to provide insights to user about his/her content consumption and recommendations. The goal is to provide user with the details about his/her watch patterns in the simplest way possible and providing user with recommendations of what to watch next.</p>
  <p>Our platform consists of a vast collection of movies and tv shows (10K+) to provide better user experience for everyone. </p>
""",unsafe_allow_html=True)
btn = st.button("Get started",type="primary")
st.image("assets/img.jpg")
if btn:
  st.switch_page("pages/Login.py") 