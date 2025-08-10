import streamlit as st

def sidebar():
  with st.sidebar:
    st.page_link("pages/Content.py",label="How to get started")
    st.page_link("pages/Series.py",label="Shows",icon="🎬")
    st.page_link("pages/Movies.py",label="Movies",icon="🎥")
    st.page_link("pages/Search.py",label="Search",icon="🔎")
    st.page_link("pages/Analytics.py",label="Insights / Analytics",icon="📊")
    st.page_link("pages/Analytics.py",label="View Already Watched",icon="💾")
    st.page_link("pages/Account_Settings.py",label="Account Settings",icon="🔐")
    btn = st.button("Logout",type="primary",use_container_width=True)
    if btn:
      st.session_state.clear()
      st.switch_page("pages/Home.py")