import pandas as pd

def get_movie_chunks():
    chunks = []
    for chunk in pd.read_csv("datasets/TMDB_movie_dataset_v11.csv",nrows=10000,chunksize=50):
        chunks.append(chunk)
    return chunks

movies = get_movie_chunks()

def get_show_chunks():
    chunks = []
    for chunk in pd.read_csv("datasets/TMDB_tv_dataset_v3.csv",nrows=10000,chunksize=50):
        chunks.append(chunk)
    return chunks


shows = get_show_chunks()