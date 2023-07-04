# Suggested_movies
# A system that uses algorithms and data to recommend movies to users based on their interests.
import streamlit as st
import pickle
import pandas as pd
import requests

url = "https://api.themoviedb.org/3/movie/64?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "53ab276f9633eaf1df9479db4ee42068"
}

response = requests.get(url, headers=headers)

print(response.text)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        #fetch postor for api
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('movies_similarity_vector.pkl','rb'))

st.title("Suggested movies by Sidhanta")
selected_movie_name = st.selectbox('Search you movies',movies['title'].values)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)

