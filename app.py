import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['Series_Title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].Series_Title)
        recommended_posters.append(movies_metadata.iloc[i[0]].Poster_Link)

    return recommended_movies,recommended_posters

movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))

movies_metadata = pickle.load(open("movies_metadata.pkl", "rb"))

st.title("Movie Recommender System")


selected_movie_name=st.selectbox(
    'Select a movie to get recommendations:',
    movies['Series_Title'].values)

if st.button('Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            # st.text(recommended_movie_names[i])
            st.markdown(
                f"<h4 style='text-align:center; font-size:20px; font-weight:bold;'>{recommended_movie_names[i]}</h4>",
                unsafe_allow_html=True
            )
            st.image(recommended_movie_posters[i],  use_container_width=True)