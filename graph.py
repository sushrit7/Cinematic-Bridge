import csv
import os
import pickle
from collections import defaultdict


# Define file paths
input_directory = 'split_files'
output_graph_file = 'graph.pickle'

# Create a defaultdict to store the graph
graph = defaultdict(list)

# Function to build the graph from split files
def build_graph():
    for filename in os.listdir(input_directory):
        if filename.endswith('.tsv'):
            with open(os.path.join(input_directory, filename), 'r', encoding='utf-8') as tsvfile:
                reader = csv.reader(tsvfile, delimiter='\t')
                next(reader)  # Skip header
                for row in reader:
                    primary_profession = row[4]
                    # Check if primaryProfession contains "actor" or "actress"
                    if "actor" in primary_profession.lower() or "actress" in primary_profession.lower():
                        actor_id = row[1]
                        known_for = row[5].split(',') if row[5] != '\\N' else []  # Split knownForTitles if not NULL
                        for movie in known_for:
                            graph[actor_id].append(movie)
                            graph[movie].append(actor_id)


# Build the graph
build_graph()

# Function to save the graph to a file
def save_graph():
    with open(output_graph_file, 'wb') as f:
        pickle.dump(graph, f)

# Save the graph
save_graph()
