import streamlit as st

st.title("Welcome to Streamlytix")
st.markdown("""
  <p>This is a data analaysis project built with the help of Python and its various libraries and frameworks mainly Pandas, Numpy, Matplotlib, Seaborn, Plotly-express. The project's ui is built with the help of Streamlit.</p>
  <p>Main focus of this project is to provide isights to user about his/her content consumption insights. The goal is to provide user with the details about his/her watch patterns in the simplest way possible.</p>
  <p>Our platform consists of a vast collection of movies (1M+) and tv shows (150K+) to provide better user experience for everyone. </p>
    
""",unsafe_allow_html=True)
btn = st.button("Get started",type="primary")
st.image("img.jpg")

if btn:
  st.switch_page("About.py") 