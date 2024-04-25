import csv
import os
import pickle
from collections import defaultdict


# Define file paths
input_directory = 'split_files/name.basics'
output_graph_file = 'graph.pickle'

# Create a defaultdict to store the graph
graph_to_save = defaultdict(list)

# Function to load the graph from a pickle file
def title_to_pickle(input_directory):
    title_data = {}
    for filename in os.listdir(input_directory):
            if filename.endswith('.tsv'):
                with open(os.path.join(input_directory, filename), 'r', encoding='utf-8') as tsvfile:
                    reader = csv.reader(tsvfile, delimiter='\t')
                    next(reader)  # Skiping header
                    for row in reader:
                        # Extracting title ID and name from the 0th and 2nd elements
                        title_id = row[0]
                        title_type = row[2]
                        title_data[title_id] = title_type
    output_pickle_file = 'title.pickle'
    with open(output_pickle_file, 'wb') as f:
        pickle.dump(title_data, f)
    print("Title data saved to title.pickle.")

# Function to load the title data from a pickle file
def load_title_from_pickle():
    with open("title.pickle", 'rb') as f:
        title = pickle.load(f)
    return title
    
# Function to build the graph from split files
def build_graph():
    input_directory_title = 'split_files/title.basics'
    title_to_pickle(input_directory_title)
    #Loading the title data from the pickle file
    title_data = load_title_from_pickle()
    #Iterating through the name.basics files
    for filename in os.listdir("split_files/name.basics"):
        if filename.endswith('.tsv'):
            with open(os.path.join("split_files/name.basics", filename), 'r', encoding='utf-8') as tsvfile:
                reader = csv.reader(tsvfile, delimiter='\t')
                next(reader)  # Skiping header
                for row in reader:
                    primary_profession = row[4]
                    # Checking if primaryProfession contains "actor" or "actress"
                    if "actor" in primary_profession.lower() or "actress" in primary_profession.lower():
                        actor = row[1]
                        known_for = row[5].split(',') if row[5] != '\\N' else []  # Split knownForTitles if not NULL
                        for movie in known_for:
                            movie_name = title_data.get(movie, None)
                            graph_to_save[actor].append(movie_name)
                            graph_to_save[movie_name].append(actor)



# Build the graph
build_graph()

# Function to save the graph to a file
def save_graph():
    with open(output_graph_file, 'wb') as f:
        pickle.dump(graph_to_save, f)

# Save the graph
save_graph()
