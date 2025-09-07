import streamlit as st
from utils.helper import get_movie_chunks,get_show_chunks
from component.sidebar import sidebar
from component.content_cards import movie_card_with_buttons,series_card_with_buttons

#Private route protection
if "name" not in st.session_state or "email" not in st.session_state:
  st.switch_page("pages/Login.py")

#Initializing pagination index  
if "search_chunk_index" not in st.session_state:
    st.session_state.search_chunk_index = 0

movies = get_movie_chunks()
shows = get_show_chunks()

sidebar()
st.header("Search for any Show/Movie")

#Search box
col1,col2 = st.columns([4,2])
query = ""
option = None
df = None
result = []
with col1:
  query = st.text_input("Enter content name/title",on_change=lambda:st.session_state.update(search_chunk_index = 0)).lower()
with col2:
  option = st.radio("Select content type",["Movie","Series"],horizontal=True)

#Searching based on content types
if ((query != "") and (option == "Movie")):
  result = []
  df = movies
  for chunk in df:
    chunk["lowered_title"] = chunk["title"].str.lower()
    matched = chunk[(chunk["lowered_title"].str.contains(query))]
    result.append(matched)

  movie_data = result[st.session_state.search_chunk_index]
  movie_card_with_buttons(df=movie_data)

  total_chunks = len(movie_data)
  col1, col2, col3 = st.columns([1, 2, 1])
  with col1:
    st.button("⬅️ Previous", 
    on_click=lambda: st.session_state.update(search_chunk_index=st.session_state.search_chunk_index - 1),
    disabled=st.session_state.search_chunk_index == 0)
  with col3:
    st.button("Next ➡️", 
    on_click=lambda: st.session_state.update(search_chunk_index=st.session_state.search_chunk_index + 1),
    disabled=st.session_state.search_chunk_index >= total_chunks - 1)
  with col2:
    st.markdown(f"<div style='text-align:center;'>Page {st.session_state.search_chunk_index + 1} of {total_chunks}</div>", unsafe_allow_html=True)
elif ((query!= "") and (option == "Series")):
  result = []
  df = shows
  for chunk in df:
    chunk["lowered_name"] = chunk["name"].str.lower()
    matched = chunk[(chunk["lowered_name"].str.contains(query))] 
    result.append(matched)

  series_data = result[st.session_state.search_chunk_index]
  series_card_with_buttons(df=series_data)

  total_chunks = len(series_data)
  col1, col2, col3 = st.columns([1, 2, 1])
  with col1:
    st.button("⬅️ Previous", 
    on_click=lambda: st.session_state.update(search_chunk_index=st.session_state.search_chunk_index - 1),
    disabled=st.session_state.search_chunk_index == 0)
  with col3:
    st.button("Next ➡️", 
    on_click=lambda: st.session_state.update(search_chunk_index=st.session_state.search_chunk_index + 1),
    disabled=st.session_state.search_chunk_index >= total_chunks - 1)
  with col2:
    st.markdown(f"<div style='text-align:center;'>Page {st.session_state.search_chunk_index + 1} of {total_chunks}</div>", unsafe_allow_html=True)
else:
  st.info("Start writing movie/series name and select type to search")