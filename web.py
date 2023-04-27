import streamlit as st
import pickle
import pandas as pd
import requests as r

def fetch_Poster(movie_id):
    responce = r.get('https://api.themoviedb.org/3/movie/{}?api_key=8c86b08b6e2eceefdebe6bafc3ecea99&language=en-US'.format(movie_id))
    data = responce.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def Recommend(movie):
    movie_indx = movies[movies['Title'] == movie].index[0]
    distance = similarity[movie_indx]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    M_List = []
    M_List_Poster = []
    for i in movie_list:
        movie_Id = movies.iloc[i[0]].Movie_Id
        M_List.append(movies.iloc[i[0]].Title)
        M_List_Poster.append(fetch_Poster(movie_Id))
    return M_List,M_List_Poster

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("MRC System")

selected_movie = st.selectbox("This is Sumit's Movie Recommendation system. Select a Movie and Go for Similarity",movies['Title'].values)


if st.button("Search"):
    names,posters = Recommend(selected_movie)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[1])

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