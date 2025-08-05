import streamlit as st
import pandas as pd

def init_user():
  if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.name = None
    st.session_state.email = None
    st.session_state.user_watched_content = pd.DataFrame(columns=['id', 'name', 'number_of_seasons', 'number_of_episodes','original_language', 'vote_count', 'vote_average', 'overview', 'adult','backdrop_path', 'first_air_date', 'last_air_date', 'homepage','in_production', 'original_name', 'popularity', 'poster_path', 'type','status', 'tagline', 'genres',   'created_by', 'languages', 'networks','origin_country', 'spoken_languages', 'production_companies','production_countries', 'episode_run_time'])
    print("Initialization done")

def init_watched_content():
  try:
    st.session_state.user_watched_content = pd.read_csv(f"user/content/{st.session_state.email}.csv")
  except FileNotFoundError as e:
    st.session_state.user_watched_content.to_csv(f"user/content/{st.session_state.email}.csv")
