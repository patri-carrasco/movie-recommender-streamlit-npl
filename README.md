# Movie recommender streamlit npl
<div align="center">
  <a href="default.asp">
    <img src="https://portugalinews.eu/wp-content/uploads/2018/09/film.jpg" alt="Recommender" style="width:400px;height:400px;", aling = "center">
  </a>
</div>

En este proyecto vamos hacer una recomendador de películas con streamlit y procesamiento de lenguaje natural

# **Estructura del repo**
Hemos estructurado el proyecto en varios archivos y carpetas para que sea más fácil su entendimiento.

**images:**  carpeta de las imágenes.

**data:**  carpeta donde va los archivos datos.
  
  
**src:** carpeta que guarda todos los archivos de funciones que usamos en este proyecto:
    
**user_input_features** : Archivo que contiene una función para detectar el título que ha introducido el ususario.

- **recommender.py**: Este es el archivo principal de la aplicación web.

- **npl.py**: Archivo que contiene el NPL para producir las recomendaciones por la descripción

# Tecnologías usadas


* Tratamiento de datos

    - pandas

    
* Aplicación

    - Streamlit

* Recommender

    - sklearn.feature_extraction.text:  TfidfVectorizer

    - sklearn.metrics.pairwise:  linear_kernel