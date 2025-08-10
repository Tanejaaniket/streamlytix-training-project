import streamlit as st
from load_data import shows,movies
import pandas as pd
from component.sidebar import sidebar
st.header("Search for any Show/Movie")
if "search_chunk_index" not in st.session_state:
    st.session_state.search_chunk_index = 0

sidebar()
col1,col2 = st.columns([4,2])
query = ""
option = None
df = None
result = []
with col1:
  query = st.text_input("Enter content name/title").lower()
with col2:
  option = st.radio("Select content type",["Movie","Series"],horizontal=True)

if ((query != "") and (option == "Movie")):
  result = []
  df = movies
  for chunk in df:
    chunk["lowered_title"] = chunk["title"].str.lower()
    matched = chunk[(chunk["lowered_title"].str.contains(query))]
    result.append(matched)

  cols = st.columns(3)
  i = 0 
  movie_data = result[st.session_state.search_chunk_index]
  for key,image,name,rating,date in zip(movie_data["id"],movie_data["poster_path"],movie_data["title"],movie_data["vote_average"],movie_data["release_date"]):
    i = i % 3
    
    with cols[i]:
      st.image(f"https://image.tmdb.org/t/p/w500/{image}",width=300)
      st.markdown(f"""<h5 style='height: 80px; padding-left: 2px;'>{name}</h5><div style='display:flex; justify-content: space-between; padding-left:2px;'><p>Rating: {round(float(rating),1)}</p><p>{date}</p></div>""",unsafe_allow_html=True)
      row = st.session_state.user_watched_movies[st.session_state.user_watched_movies["id"] == key]
      btn_watch = None
      btn_unwatch = None
      if row.empty:
        btn_watch = st.button("Already Watched?",key=key,use_container_width=True,type="primary")
      else:
        btn_unwatch = st.button("Unwatch",key=key,use_container_width=True)

    if btn_watch:
      row = movie_data[movie_data["id"] == key]
      st.session_state.user_watched_movies = pd.concat([st.session_state.user_watched_movies,row],ignore_index=True)
      st.session_state.user_watched_movies.to_csv(f"user/content/movies/{st.session_state.email}.csv")
    if btn_unwatch:
      st.session_state.user_watched_movies = st.session_state.user_watched_movies[~(st.session_state.user_watched_movies["id"] == key)]
      st.session_state.user_watched_movies.to_csv(f"user/content/movies/{st.session_state.email}.csv")
    i += 1

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

if ((query!= "") and (option == "Series")):
  result = []
  df = shows
  for chunk in df:
    chunk["lowered_name"] = chunk["name"].str.lower()
    matched = chunk[(chunk["lowered_name"].str.contains(query))] 
    result.append(matched)
  cols = st.columns(3)
  i = 0
  series_data = result[st.session_state.search_chunk_index]
  for key,image,name,rating,date in zip(series_data["id"],series_data["poster_path"],series_data["name"],series_data["vote_average"],series_data["first_air_date"]):
    i = i % 3
      
    with cols[i]:
      st.image(f"https://image.tmdb.org/t/p/w500/{image}",width=300)
      st.markdown(f"""<h5 style='height: 80px; padding-left: 2px;'>{name}</h5><div style='display:flex; justify-content: space-between; padding-left:2px;'><p>Rating: {round(float(rating),1)}</p><p>{date}</p></div>""",unsafe_allow_html=True)
      row = st.session_state.user_watched_series[st.session_state.user_watched_series["id"] == key]
      btn_watch = None
      btn_unwatch = None
      if row.empty:
        btn_watch = st.button("Already Watched?",key=key,use_container_width=True,type="primary")
      else:
        btn_unwatch = st.button("Unwatch",key=key,use_container_width=True)

    if btn_watch:
      row = series_data[series_data["id"] == key]
      st.session_state.user_watched_series = pd.concat([st.session_state.user_watched_series,row],ignore_index=True)
      st.session_state.user_watched_series.to_csv(f"user/content/series/{st.session_state.email}.csv")
    if btn_unwatch:
      st.session_state.user_watched_series = st.session_state.user_watched_series[~(st.session_state.user_watched_series["id"] == key)]
      st.session_state.user_watched_series.to_csv(f"user/content/series/{st.session_state.email}.csv")
    i += 1

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

