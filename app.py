import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommender System')

option = st.selectbox(
    'Suggesting the best movies', movies['title'].values
)

if st.button('Suggest'):
    final_result = recommend(option)
    for i in final_result:
        st.write(i)
