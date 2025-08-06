import streamlit as st
import pandas as pd

def init_user():
  if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.name = None
    st.session_state.email = None
    st.session_state.user_watched_series = pd.DataFrame(columns=['id', 'name', 'number_of_seasons', 'number_of_episodes','original_language', 'vote_count', 'vote_average', 'overview', 'adult','backdrop_path', 'first_air_date', 'last_air_date', 'homepage','in_production', 'original_name', 'popularity', 'poster_path', 'type','status', 'tagline', 'genres',   'created_by', 'languages', 'networks','origin_country', 'spoken_languages', 'production_companies','production_countries', 'episode_run_time'])
    st.session_state.user_watched_movies = pd.DataFrame(columns=['id', 'title', 'vote_average', 'vote_count', 'status', 'release_date','revenue', 'runtime', 'adult', 'backdrop_path', 'budget', 'homepage','imdb_id', 'original_language', 'original_title', 'overview','popularity', 'poster_path', 'tagline', 'genres','production_companies', 'production_countries', 'spoken_languages','keywords'])
    print("Initialization done")

def init_watched_content():
  try:
    st.session_state.user_watched_series = pd.read_csv(f"user/content/series/{st.session_state.email}.csv")
  except FileNotFoundError as e:
    st.session_state.user_watched_series.to_csv(f"user/content/series/{st.session_state.email}.csv")
  try:
    st.session_state.user_watched_movies = pd.read_csv(f"user/content/movies/{st.session_state.email}.csv")
  except FileNotFoundError as e:
    st.session_state.user_watched_movies.to_csv(f"user/content/movies/{st.session_state.email}.csv")

