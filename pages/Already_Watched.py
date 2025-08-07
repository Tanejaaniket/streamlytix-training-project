import streamlit as st
import pandas as pd

option = st.selectbox(label="Select type of content",options=["Movies","Shows"])


with st.sidebar:
  st.page_link("pages/Content.py",label="How to get started")
  st.page_link("pages/Series.py",label="Shows",icon="🎬")
  st.page_link("pages/Movies.py",label="Movies",icon="🎥")
  st.page_link("pages/Search.py",label="Search",icon="🔎")
  st.page_link("pages/Analytics.py",label="Insights / Analytics",icon="📊")
  st.page_link("pages/Analytics.py",label="View Already Watched",icon="💾")
  st.page_link("pages/Account_Settings.py",label="Account Settings",icon="🔐")

if option == "Shows":   
  df = pd.read_csv(f"user/content/series/{st.session_state.email}.csv") 
  if df.empty:
    st.write("You haven't watched anything yet. Marked as watched to get started")
  else:
    st.header("Already watched TV shows")
    cols = st.columns(3)
    i = 0

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

elif option == "Movies":
  df = pd.read_csv(f"user/content/movies/{st.session_state.email}.csv") 
  if df.empty:
    st.write("You haven't watched anything yet. Marked as watched to get started")
  else:
    st.header("Already watched movies")
    cols = st.columns(3)
    i = 0

    for key,image,name,rating,date in zip(df["id"],df["poster_path"],df["title"],df["vote_average"],df["release_date"]):
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
        row = df[df["id"] == key]
        st.session_state.user_watched_movies = pd.concat([st.session_state.user_watched_movies,row],ignore_index=True)
        st.session_state.user_watched_movies.to_csv(f"user/content/movies/{st.session_state.email}.csv")
      if btn_unwatch:
        st.session_state.user_watched_movies = st.session_state.user_watched_movies[~(st.session_state.user_watched_movies["id"] == key)]
        st.session_state.user_watched_movies.to_csv(f"user/content/movies/{st.session_state.email}.csv")
      i += 1

else:
  st.write("Choose correct option")