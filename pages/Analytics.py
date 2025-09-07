import streamlit as st
from component.sidebar import sidebar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

if "name" not in st.session_state:
  st.switch_page("pages/Login.py")
  
if "email" not in st.session_state:
  st.switch_page("pages/Login.py")

st.header("Your Binge Wrapped")

sidebar()
option = st.selectbox("Choose type of content",options=["Movie","TV Shows"])

if option == "Movie":
  movies = pd.read_csv(f"user/content/movies/{st.session_state.email}.csv")
  if movies.empty:
    st.error("Please watch atleast one movie to continue.")
  else:
    movies = movies.dropna(axis=1)
    col1,col2 = st.columns(2,gap="large",border=True)
    with col1:
      # st.subheader("Total watch time")
      # st.subheader(f"{movies["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4>Total Watch Time(min)</h4>
          <h5 style="font-weight:normal;">{movies["runtime"].sum()}</h5>
        </div>
      """,unsafe_allow_html=True)
    with col2:
      # st.subheader("Total watch time")
      # st.subheader(f"{movies["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4>Average Rating(/10)</h4>
          <h5 style="font-weight:normal;">{round(movies["vote_average"].mean(),2)}</h5>
        </div>
      """,unsafe_allow_html=True)
    
    temp = []
    for i in movies["genres"].str.split(","):
      temp.extend(i)
    genre_occ = pd.Series(temp)
    
    col1,col2 = st.columns(2,gap="large",border=True)
    with col1:
      # st.subheader("Total watch time")
      # st.subheader(f"{movies["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4>Most Watched genre</h4>
          <h5 style="font-weight:normal;">{str.join(",",genre_occ.mode())}</h5>
        </div>
      """,unsafe_allow_html=True)
    
    with col2:
      # st.subheader("Total watch time")
      # st.subheader(f"{movies["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4>Most Watched Language</h4>
          <h5 style="font-weight:normal;">{str.join(",",movies["original_language"].mode())}</h5>
        </div>
      """,unsafe_allow_html=True)
    
    temp = []
    for i in movies["production_companies"].str.split(","):
      temp.extend(i)
    prod_companies = pd.Series(temp)

    temp = []
    for i in movies["production_countries"].str.split(","):
      temp.extend(i)
    prod_countries = pd.Series(temp)

    temp = []
    for i in movies["keywords"].str.split(","):
      temp.extend(i)
    keywords = pd.Series(temp)

    col1 = st.columns(1,border=True)
    with col1[0]:
      # st.subheader("Total watch time")
      # st.subheader(f"{movies["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4 style="font-weight:normal;"><span style="font-weight:bold;">{str.join(",",prod_companies.mode())}</span> is producing most of the movies you watch in <span style="font-weight:bold;">{prod_countries.mode()[0]}</span></h4>
        </div>
      """,unsafe_allow_html=True)
  
    # col1 = st.columns(1,border=True)
    col1,col2 = st.columns(2,border=True)
    with col1:
      # st.subheader("Total watch time")
      # st.subheader(f"{movies["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4 style="font-weight:normal;">Top rated movie in your watchlist is <span style="font-weight:bold;">{movies["title"][movies["vote_average"].idxmax()]}</span></h4>
        </div>
      """,unsafe_allow_html=True)
    
    with col2:
      # st.subheader("Total watch time")
      # st.subheader(f"{movies["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4 style="font-weight:normal;">Your most liked keywords are <span style="font-weight:bold;">'{str.join(",",keywords.mode())}'</span></h4>
        </div>
      """,unsafe_allow_html=True)
    
    # st.header(,width="content")
    # graph = plt.(movies,x="title",y="vote_average")
    graph = px.bar(movies,x="title",y="vote_average",labels={"title":"Title","vote_average":"Rating"},title="Movie Ratings")
    st.plotly_chart(graph)
    
    graph = px.bar(movies,x="title",y="revenue",labels={"title":"Title","revenue":"Revenue","vote_average":"Rating"},title="Revenue earned by movies",color="vote_average")
    st.plotly_chart(graph)
    
    graph = px.bar(movies,x="title",y="budget",labels={"title":"Title","budget":"Budget","vote_average":"Rating"},title="Budget of the movies",color="vote_average")
    st.plotly_chart(graph)
    
    movies["release_date"] = pd.to_datetime(movies["release_date"])
    movies["release_year"] = movies["release_date"].dt.year

    fig = px.scatter(
        movies,
        y="release_date",
        x="title",
        title="Movies and their release year",
        labels={"title":"Title","release_date":"Release Date"}
    )
    st.plotly_chart(fig)

elif option == "TV Shows":
  series = pd.read_csv(f"user/content/series/{st.session_state.email}.csv")
  if series.empty:
    st.error("Please watch atleast one tv show to continue.")
  else:
    series = series.dropna(axis=1)
    # st.dataframe(series)
    col1,col2 = st.columns(2,gap="large",border=True)
    with col1:
      # st.subheader("Total watch time")
      # st.subheader(f"{series["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4>Total Episodes Watched</h4>
          <h5 style="font-weight:normal;">{int(series["number_of_episodes"].sum())}</h5>
        </div>
      """,unsafe_allow_html=True)
    with col2:
      # st.subheader("Total watch time")
      # st.subheader(f"{series["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4>Average Rating(/10)</h4>
          <h5 style="font-weight:normal;">{round(series["vote_average"].mean(),2)}</h5>
        </div>
      """,unsafe_allow_html=True)
    
    temp = []
    for i in series["genres"].str.split(","):
      temp.extend(i)
    genre_occ = pd.Series(temp)
    
    col1,col2 = st.columns(2,gap="large",border=True)
    with col1:
      # st.subheader("Total watch time")
      # st.subheader(f"{series["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4>Most Watched genre</h4>
          <h5 style="font-weight:normal;">{str.join(",",genre_occ.mode())}</h5>
        </div>
      """,unsafe_allow_html=True)
    
    with col2:
      # st.subheader("Total watch time")
      # st.subheader(f"{series["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4>Most Watched Language</h4>
          <h5 style="font-weight:normal;">{str.join(",",series["original_language"].mode())}</h5>
        </div>
      """,unsafe_allow_html=True)
    
    temp = []
    for i in series["production_companies"].str.split(","):
      temp.extend(i)
    prod_companies = pd.Series(temp)

    temp = []
    for i in series["production_countries"].str.split(","):
      temp.extend(i)
    prod_countries = pd.Series(temp)

    col1 = st.columns(1,border=True)
    with col1[0]:
      # st.subheader("Total watch time")
      # st.subheader(f"{series["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4 style="font-weight:normal;"><span style="font-weight:bold;">{str.join(",",prod_companies.mode())}</span> is producing most of the series you watch in <span style="font-weight:bold;">{prod_countries.mode()[0]}</span></h4>
        </div>
      """,unsafe_allow_html=True)
  
    # col1 = st.columns(1,border=True)
    col1 = st.columns(1,border=True)
    with col1[0]:
      # st.subheader("Total watch time")
      # st.subheader(f"{series["runtime"].sum()} m")
      st.markdown(f"""
        <div style="text-align:center;">
          <h4 style="font-weight:normal;">Top rated movie in your watchlist is <span style="font-weight:bold;">{series["name"][series["vote_average"].idxmax()]}</span></h4>
        </div>
      """,unsafe_allow_html=True)
    
    # st.header(,width="content")
    # graph = plt.(series,x="title",y="vote_average")
    graph = px.bar(series,x="name",y="vote_average",labels={"name":"Title","vote_average":"Rating"},title="Series Ratings",color="status")
    st.plotly_chart(graph)
    
    graph = px.bar(series,x="name",y="number_of_episodes",labels={"name":"Title","revenue":"Revenue","vote_average":"Rating"},title="Episodes per tv show",color="status")
    st.plotly_chart(graph)
    
    graph = px.bar(series,x="name",y="number_of_seasons",labels={"name":"Title","budget":"Budget","vote_average":"Rating"},title="Seasons in a tv show",color="status")
    st.plotly_chart(graph)
    
    series["first_air_date"] = pd.to_datetime(series["first_air_date"])
    series["last_air_date"] = pd.to_datetime(series["last_air_date"])
    # series["release_year"] = series["release_date"].dt.year

    fig = px.timeline(
        series,
        y="name",
        x_start="first_air_date",
        x_end="last_air_date",
        color="status",
        title="TV shows and their release date their release year",
        labels={"name":"Title","first_air_date":"Release Date","last_air_date":"End Date"}
    )
    st.plotly_chart(fig)


else:
  st.write("Invalid option. Please choose any one option from above.")
