import pickle

# Load the data from the pickle file
def load_data_from_pickle(file_path):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data

# # Load the data from the pickle file
data = load_data_from_pickle('graph.pickle')

# # Print the type of data
# print("Type of data:", type(data))

# # Print the data for Jim Carrey
# print("\nData for Jim Carrey:")
# print(data.get('Jim Carrey', "Actor not found"))

# # Print the data for Jeff Daniels
# print("\nData for Jeff Daniels:")
# print(data.get('Jeff Daniels', "Actor not found"))


def have_common_movie(actor1_movies, actor2_movies):
    # Convert both lists to sets for faster lookup
    actor1_movies_set = set(actor1_movies)
    actor2_movies_set = set(actor2_movies)
    
    # Check if there are any common movies
    common_movies = actor1_movies_set.intersection(actor2_movies_set)
    
    return common_movies

# Example usage
jim_carrey_movies = data.get('Jim Carrey', [])
jeff_daniels_movies = data.get('Jeff Daniels', [])

common_movies = have_common_movie(jim_carrey_movies, jeff_daniels_movies)

if common_movies:
    print("Jim Carrey and Jeff Daniels have the following movie(s) together:")
    for movie_id in common_movies:
        print(movie_id)
else:
    print("Jim Carrey and Jeff Daniels do not have any movie together.")
