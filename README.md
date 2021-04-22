# Movie recommender streamlit npl


En este proyecto vamos hacer una recomendador de películas con streamlit y procesamiento de lenguaje natural

 **Estructura del repo**
  Hemos estructurado el proyecto en varios archivos y carpetas para que sea más fácil su entendimiento.

  

  **data:**  carpeta donde va los archivos datos.
  
  
  **src:** carpeta que guarda todos los archivos de funciones que usamos en este proyecto:
    
    * user_input_features : Archivo que contiene una función para detectar el título que ha introducido el ususario



*recommenda.py:** Este es el archivo principal de la API.

**index.html:** Archivo html de las visualizaciones

**index.md:** Archivo de la documentación de la API

**Movie recommender.pdf** : Presentación del proyecto


# Tecnologías usadas

* Configuración interna

    - sys

    - json

    - load_dotenv

    - os

* Tratamiento de datos

    - pandas

    - selenium

    - sqlalchemy

    - Mysql

* Api

    - flask, Flask, request

    - flask_cors, CORS

    - markdown extensions fenced_code

* Recommender

    - sklearn.feature_extraction.text:  TfidfVectorizer

    - sklearn.metrics.pairwise:  linear_kernel