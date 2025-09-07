import pandas as pd
def get_movie_recommendations():
    return pd.read_csv("datasets/recommended_movies.csv")


movie_recommendations = get_movie_recommendations()
def get_show_recommendation():
    return pd.read_csv("datasets/recommended_series.csv")


series_recommendations = get_show_recommendation()