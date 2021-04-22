import streamlit as st
import pandas as pd
from PIL import Image


st.write("""
# Movier recommender using NPL

""")


image = Image.open('./images/film.jpg')
st.image(image, caption='Movie recommender')


st.sidebar.header('Title')

title = st.sidebar.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)