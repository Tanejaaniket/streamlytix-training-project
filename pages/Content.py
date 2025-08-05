import streamlit as st

if "name" not in st.session_state:
  st.switch_page("pages/Login.py")

st.header(f"👋🏻 Hi there {st.session_state.name} Team Streamlytix welcomes you...")  
st.markdown("""
  > Welcome to the world of movies and tv shows. Here are some quick instructions to help you get started to get insights about your watch history :
  > - Starting with the app
  >   - Navigate to the required content (either shows or movies).
  >   - Mark the content as watched.
  >   - Make sure to mark enough content to get usefull insights.
  >   - Enjoy your valuable insights.
  > ---          
  > _Note: You can always search for your favourite movies and tv shows from the search option in the sidebar._
  >

            
""",unsafe_allow_html=True)

with st.sidebar:
  st.page_link("pages/Content.py",label="How to get started")
  st.page_link("pages/Series.py",label="Shows",icon="🎬")
  st.page_link("pages/Movies.py",label="Movies",icon="🎥")
  st.page_link("pages/Search.py",label="Search",icon="🔎")
  st.page_link("pages/Analytics.py",label="Insights / Analytics",icon="📊")
  st.page_link("pages/Analytics.py",label="View Already Watched",icon="💾")
  st.page_link("pages/Account_Settings.py",label="Account Settings",icon="🔐")
