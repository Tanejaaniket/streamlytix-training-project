import pandas as pd
import streamlit as st
import ast

def fetch_recommeded_content(df:pd.DataFrame,content_type:str)->pd.DataFrame: 
  recommended_content_df = pd.DataFrame()
  recommended_content_details = None
  watched_series_id = df["id"].to_list()

  if content_type.lower() == "series":
      series_recommendations = pd.read_csv("datasets/recommended_series.csv")
      for i in watched_series_id:
        recommended_content_df = pd.concat([recommended_content_df,series_recommendations[(series_recommendations["series_id"]==i)]])
        recommended_content_details = recommended_content_df["recommended_series"].to_list()
  else:
      movie_recommendations = pd.read_csv("datasets/recommended_movies.csv")
      for i in watched_series_id:
        recommended_content_df = pd.concat([recommended_content_df,movie_recommendations[(movie_recommendations["movie_id"]==i)]])
        recommended_content_details = recommended_content_df["recommended_movies"].to_list()

  temp = []
  recommended_content_details = [ast.literal_eval(i) for i in recommended_content_details]

  for i in recommended_content_details:
    temp.append(i[0])
    temp.append(i[1])
    temp.append(i[2])
    temp.append(i[3])
    temp.append(i[4])

  return pd.DataFrame(temp).drop_duplicates()


def init_user()->None:
  if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.name = None
    st.session_state.email = None
    st.session_state.user_watched_series = pd.DataFrame(columns=['id', 'name', 'number_of_seasons', 'number_of_episodes','original_language', 'vote_count', 'vote_average', 'overview', 'adult','backdrop_path', 'first_air_date', 'last_air_date', 'homepage','in_production', 'original_name', 'popularity', 'poster_path', 'type','status', 'tagline', 'genres',   'created_by', 'languages', 'networks','origin_country', 'spoken_languages', 'production_companies','production_countries', 'episode_run_time'])
    st.session_state.user_watched_movies = pd.DataFrame(columns=['id', 'title', 'vote_average', 'vote_count', 'status', 'release_date','revenue', 'runtime', 'adult', 'backdrop_path', 'budget', 'homepage','imdb_id', 'original_language', 'original_title', 'overview','popularity', 'poster_path', 'tagline', 'genres','production_companies', 'production_countries', 'spoken_languages','keywords'])
    print("Initialization done")


def init_watched_content()->None:
  try:
    st.session_state.user_watched_series = pd.read_csv(f"user/content/series/{st.session_state.email}.csv")
  except FileNotFoundError as e:
    st.session_state.user_watched_series.to_csv(f"user/content/series/{st.session_state.email}.csv")
  try:
    st.session_state.user_watched_movies = pd.read_csv(f"user/content/movies/{st.session_state.email}.csv")
  except FileNotFoundError as e:
    st.session_state.user_watched_movies.to_csv(f"user/content/movies/{st.session_state.email}.csv")


def get_movie_chunks()->list:
    chunks = []
    for chunk in pd.read_csv("datasets/TMDB_movie_dataset_v11.csv",nrows=10000,chunksize=50):
        chunks.append(chunk)
    return chunks


def get_show_chunks()->list:
    chunks = []
    for chunk in pd.read_csv("datasets/TMDB_tv_dataset_v3.csv",nrows=10000,chunksize=50):
        chunks.append(chunk)
    return chunks
