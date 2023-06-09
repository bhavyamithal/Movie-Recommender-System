import pickle
import streamlit as st
import requests

# Function to fetch the poster of a movie given its ID
def fetch_poster(movie_id):
    # API request to get movie data
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend similar movies based on a given movie
def recommend(movie):
    # Find the index of the selected movie in the movies dataframe
    index = movies[movies['title'] == movie].index[0]
    # Sort the similarity scores in descending order and get the indices
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    # Fetch details of the top 5 similar movies
    for i in distances[1:6]:
        # Fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Streamlit app header
st.header('Movie Recommender System')

# Load preprocessed data from pickle files
movies = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Get the list of movie titles
movie_list = movies['title'].values

# Display a dropdown to select a movie
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to trigger recommendation
if st.button('Show Recommendation'):
    # Get recommended movie names and posters
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
