import streamlit as st
import pandas as pd
from PIL import Image

from src.user_input_features import user_input_features



st.write("""
# Movier recommender using NPL

""")
df = pd.read_csv("./data/data_best_ratings.csv")


image = Image.open('./images/film.jpg')
st.image(image, caption='Movie recommender')


st.sidebar.header('Title')

title = st.sidebar.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

film =user_input_features(title,df)
st.write(film)

