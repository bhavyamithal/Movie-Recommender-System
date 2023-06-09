# Movie Recommender System using Jupyter Notebook and Streamlit
- This repository contains code for a movie recommender system implemented in two parts: a Jupyter Notebook for data preprocessing and model building, and a Streamlit web application for displaying recommendations based on user input.

# Jupyter Notebook
- The Jupyter Notebook file (movie_recommender.ipynb) contains the code for data preprocessing, model building, and saving the necessary files for the web application. Here are the main sections of the notebook:

- Importing Libraries: This section imports the required libraries for data analysis and visualization.

- Data Loading: The dataset files (tmdb_5000_movies.csv and tmdb_5000_credits.csv) are loaded into Pandas DataFrames.

- Data Cleaning and Feature Selection: This section performs data cleaning and selects the relevant columns for building the recommendation system.

- Data Preprocessing: The text data in the selected columns is processed by converting them into appropriate formats and cleaning them.

- Building the Recommender System: The bag-of-words model is created using CountVectorizer, and cosine similarity is calculated between movies. A function for recommending similar movies is defined.

- Saving Data: The preprocessed data and similarity matrix are saved as pickle files (movies_dict.pkl and similarity.pkl, respectively) for later use in the web application.

# Streamlit Web Application
- The Streamlit web application file (app.py) uses the saved pickle files from the Jupyter Notebook to display movie recommendations. Here is an overview of the code:

- Function to Fetch Movie Poster: This function fetches the poster of a movie given its ID using the TMDb API.

- Function to Recommend Movies: This function recommends similar movies based on a given movie using the precomputed similarity matrix.

- Streamlit App: The Streamlit web application is created with the following sections:

- Header: Displays the title of the app.
- Data Loading: Loads the preprocessed data and similarity matrix from the pickle files.
- Movie Selection: Provides a dropdown to select a movie from the available options.
- Recommendation Button: When clicked, triggers the recommendation function and displays the top 5 recommended movies along with their posters.
- Please make sure to place the pickle files (movies_dict.pkl and similarity.pkl) in the same directory as the app.py file before running the web application.