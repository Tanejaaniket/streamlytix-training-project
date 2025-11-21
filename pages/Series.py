import streamlit as st
from utils.helper import get_show_chunks
from component.sidebar import sidebar
from component.content_cards import series_card_with_buttons

#Private route protection
if "name" not in st.session_state or "email" not in st.session_state:
  st.switch_page("pages/Login.py")
  
#Pagination initialization
if "series_chunk_index" not in st.session_state:
    st.session_state.series_chunk_index = 0

#Loads sidebar
sidebar()

#Loads shows as 50-50 chunks from dataframe
chunks = get_show_chunks()
st.header("TV shows")
df = chunks[st.session_state.series_chunk_index]

#Load series
series_card_with_buttons(df=df)

#Pagination controls
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

