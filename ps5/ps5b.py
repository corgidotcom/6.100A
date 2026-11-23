# 6.100A Spring 2026
# Problem Set 5B
# Name: <insert name>
# Collaborators: <insert collaborators>

import csv
from ps5a import User, Movie, UserToUserRecommender, ItemToItemRecommender # Importing your work from Part A

## BEGIN HELPER CODE ##
RATINGS_FILENAME = 'ratings.csv'
MOVIES_FILENAME = 'movies.csv'
GENRES = ['Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

def load_recommender(recommender, movies_file=MOVIES_FILENAME, ratings_file=RATINGS_FILENAME):
    """
    Loads the recommender with data from the movies_file and ratings_file.

    recommender (UserToUserRecommender or ItemToItemRecommender): the recommender to be loaded
    movies_file (string): the filename of a csv file containing information about movies, RATINGS_FILENAME by default
    ratings_file (string): the filename of a csv file containing user ratings of movies, MOVIES_FILENAME by default

    Returns: None
    """
    users = {}
    movies = {}
    processed_users = set()

    with open(movies_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movie_id = int(row['movieId'])
            name = row['title']
            genres = row['genres'].split('|') if row['genres'] != '(no genres listed)' else []
            movie = Movie(movie_id, name, genres)
            movies[movie_id] = movie

    with open(ratings_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            user_id = int(row['userId'])
            name = row['firstName']

            if user_id not in processed_users:
                users[user_id] = User(user_id, name)
                processed_users.add(user_id)

            movie_id = int(row['movieId'])
            rating = float(row['rating'])

            movie = movies[movie_id]
            if movie:
                recommender.add_rating(users[user_id], movie, rating)
### END HELPER CODE ###

def interactive_recommender(recommender_type, user_ids=list(range(1, 285)), genres=GENRES):
    """
    Initializes and loads the specified recommender type.
    Interacts with a user by asking for their ID,
                             genre of movie they would like recommendations for, and
                             number of recommendations to provide.
    Prints recommendations for the user based on their input.

    recommender_type (str): the type of recommender to use, either 'user' or 'item'
    user_ids (list[int]): the list of existing user IDs
    genres (list[str]): the list of available movie genres

    Returns: None
    """
    raise NotImplementedError  # TODO: delete this line and replace with your code here

if __name__ == '__main__':
    # # Uncomment these lines to try running interactive_recommender()
    # interactive_recommender('user')
    # interactive_recommender('item')
    pass
