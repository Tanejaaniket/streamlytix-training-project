import streamlit as st
import pandas as pd
from component.sidebar import sidebar
from component.content_cards import series_card_with_buttons,series_card_without_button,movie_card_with_buttons,movie_card_without_buttons
from utils.helper import fetch_recommeded_content

#Check is user is logged in or not
if "name" not in st.session_state or "email" not in st.session_state:
  st.switch_page("pages/Login.py")  

#Loads sidebar
sidebar()

#Select box
option = st.selectbox(label="Select type of content",options=["Movies","Shows"])

#Load watched content and watch next recommendations according to selected options
if option == "Shows":
  df = pd.read_csv(f"user/content/series/{st.session_state.email}.csv") 
 
  if df.empty:
    st.error("You haven't watched anything yet. Marked as watched to get started")
  else:
    st.header("Already watched TV shows")
    series_card_with_buttons(df=df)
    st.header(" ")
    st.header("Watch next")
    recommended_series_details = fetch_recommeded_content(df=df,content_type="series")
    series_card_without_button(df=recommended_series_details)
elif option == "Movies":
  df = pd.read_csv(f"user/content/movies/{st.session_state.email}.csv") 
  
  if df.empty:
    st.error("You haven't watched anything yet. Marked as watched to get started")
  else:
    recommended_movies_details = fetch_recommeded_content(df=df,content_type="movie")
    st.header("Already watched movies")
    movie_card_with_buttons(df=df)
    st.header(" ")
    st.header("Watch next")
    movie_card_without_buttons(df=recommended_movies_details)    
else:
  st.write("Choose correct option")