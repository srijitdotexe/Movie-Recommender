import streamlit as st
from joblib import load
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0bddaa685894fa474da82a410453e3cd&language=en-US")
    data = response.json()

    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/original/" + poster_path

    return full_path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = load('movies_dict.joblib')
movies = pd.DataFrame(movies_dict)


similarity = load('similarity.joblib')



st.title("Movie Recommender")

selected_movie = st.selectbox(
   "What was the last good film you watched?",
   (movies['title'].values),
   index=None,
   placeholder="Select a movie...",
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie)


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])