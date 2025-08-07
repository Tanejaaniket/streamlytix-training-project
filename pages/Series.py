import streamlit as st
import pandas as pd
from load_data import shows as chunks

if "series_chunk_index" not in st.session_state:
    st.session_state.series_chunk_index = 0

st.header("TV shows")
with st.sidebar:
  st.page_link("pages/Content.py",label="How to get started")
  st.page_link("pages/Series.py",label="Shows",icon="🎬")
  st.page_link("pages/Movies.py",label="Movies",icon="🎥")
  st.page_link("pages/Search.py",label="Search",icon="🔎")
  st.page_link("pages/Analytics.py",label="Insights / Analytics",icon="📊")
  st.page_link("pages/Already_Watched.py",label="View Already Watched",icon="💾")
  st.page_link("pages/Account_Settings.py",label="Account Settings",icon="🔐")

cols = st.columns(3)
i = 0
df = chunks[st.session_state.series_chunk_index]

for key,image,name,rating,date in zip(df["id"],df["poster_path"],df["name"],df["vote_average"],df["first_air_date"]):
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
    row = df[df["id"] == key]
    st.session_state.user_watched_series = pd.concat([st.session_state.user_watched_series,row],ignore_index=True)
    st.session_state.user_watched_series.to_csv(f"user/content/series/{st.session_state.email}.csv")
  if btn_unwatch:
    st.session_state.user_watched_series = st.session_state.user_watched_series[~(st.session_state.user_watched_series["id"] == key)]
    st.session_state.user_watched_series.to_csv(f"user/content/series/{st.session_state.email}.csv")
  i += 1

total_chunks = len(chunks)
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
  st.button("⬅️ Previous", 
  on_click=lambda: st.session_state.update(series_chunk_index=st.session_state.series_chunk_index - 1),
  disabled=st.session_state.series_chunk_index == 0)

with col3:
  st.button("Next ➡️", 
  on_click=lambda: st.session_state.update(series_chunk_index=st.session_state.series_chunk_index + 1),
  disabled=st.session_state.series_chunk_index >= total_chunks - 1)

with col2:
  st.markdown(f"<div style='text-align:center;'>Page {st.session_state.series_chunk_index + 1} of {total_chunks}</div>", unsafe_allow_html=True)

