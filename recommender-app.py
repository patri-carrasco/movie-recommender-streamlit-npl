import streamlit as st
import pandas as pd
from PIL import Image

from src.user_input_features import user_input_features
from src.npl import get_recommendations

st.set_page_config(page_title='Movier recommender',
    layout='wide')

#Título de la aplicación web
st.write("""
# Movier recommender using NPL

""")
# cargamos los datos y la imagen
#df = pd.read_csv("./data/data_best_ratings.csv")
df = pd.read_csv("./data/prueba.csv")

image = Image.open('./images/film.jpg')
st.image(image, caption='Movie recommender')

#título del la barra lateral y obtención del título introducido por el usuario
st.sidebar.header('Title')
title = st.sidebar.text_input('Movie title', 'Life of Brian')

#Título de los datos indtroducidos por el usuario
st.write('The current movie title is', title)
film =user_input_features(title,df)

if len(film)!=0:
    st.write(film)


    # Título del recomendador
    st.write('Recommendations offered by the description of the chosen film the npl')

    recommender = pd.DataFrame(get_recommendations(title,df))

    st.write(recommender)
else:
    st.write("""
        # The title was not found in the database, please try again
        """)