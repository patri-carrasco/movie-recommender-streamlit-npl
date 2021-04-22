# Movie recommender streamlit npl
<div align="center">
  <a href="default.asp">
    <img src="https://portugalinews.eu/wp-content/uploads/2018/09/film.jpg" alt="Recommender" style="width:400px;height:400px;", aling = "center">
  </a>
</div>

# Objetivo

En este proyecto vamos hacer una recomendador de películas con streamlit y procesamiento de lenguaje natural

# Estructura del repo
Hemos estructurado el proyecto en varios archivos y carpetas para que sea más fácil su entendimiento.

**images:**  carpeta de las imágenes.

**data:**  carpeta donde va los archivos datos.
  
  
**src:** carpeta que guarda todos los archivos de funciones que usamos en este proyecto:
    
- **user_input_features** : Archivo que contiene una función para detectar el título que ha introducido el ususario.

- **recommender.py**: Este es el archivo principal de la aplicación web.

- **npl.py**: Archivo que contiene el NPL para producir las recomendaciones por la descripción.

## **Funcionamiento del recomendador por machine learning**

### Procesamiento del lenguaje natural. 
Para calcular las similitudes de y/o disimilitud hay que calcular los vectores de cada palabra de cada descripción. 
 

### Los vectores de palabras

Los vectores de palabras son representaciones vectorizadas de palabras en un documento. 
Los vectores llevan consigo un significado semántico. Por ejemplo, el hombre y el rey tendrán representaciones vectoriales cercanas entre sí, mientras que el hombre y la mujer tendrán representaciones alejadas entre sí.

Calcularemos los vectores de frecuencia de término-frecuencia de documento inverso (TF-IDF) para cada documento. Esto nos dará una matriz donde cada columna representa una palabra en el vocabulario general (todas las palabras que aparecen en al menos un documento), y cada columna representa una película.

Scikit-learn tiene una clase TfIdfVectorizer incorporada que produce la matriz TF-IDF.

### Matriz TF-IDF.
Eliminamos las palabras vacías como 'el', 'una', etc. ya que no brindan ninguna información útil sobre el tema;
Reemplazamos los valores que no sean un número con una cadena en blanco;
Finalmente, construimos la matriz TF-IDF sobre los datos.

### Similarity 
Dado que hemos utilizado el vectorizador TF-IDF, calcular el producto escalar entre cada vector nos dará directamente la puntuación de similitud del coseno. Por lo tanto, usaremos linear_kernel () de sklearn en lugar de cosine_similarities () ya que es más rápido.

### Construir un mapa inverso de índices y títulos de películas
Vamos a definir una función que toma el título de una película como entrada y genera una lista de las 10 películas más similares. 
En primer lugar, para esto, necesitamos un mapeo inverso de títulos de películas e índices de DataFrame. En otras palabras, necesitamos un mecanismo para identificar el índice de una película en su DataFrame de metadatos, dado su título.


# Enlaces usados

Sistema de recomendador: https://www.datacamp.com/community/tutorials/recommender-systems-python



# Tecnologías usadas


* Tratamiento de datos

    - pandas

    
* Aplicación

    - Streamlit

* Recommender

    - sklearn.feature_extraction.text:  TfidfVectorizer

    - sklearn.metrics.pairwise:  linear_kernel