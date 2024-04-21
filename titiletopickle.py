import csv
import os
import pickle

# Define input and output directories
input_directory = 'split_files/title.basics'
output_pickle_file = 'title.pickle'

# Define a dictionary to store title data
title_data = {}

# Function to read and process TSV files
def process_tsv_files():
    for filename in os.listdir(input_directory):
        if filename.endswith('.tsv'):
            with open(os.path.join(input_directory, filename), 'r', encoding='utf-8') as tsvfile:
                reader = csv.reader(tsvfile, delimiter='\t')
                next(reader)  # Skip header
                for row in reader:
                    # Extract title ID and title type from the 0th and 2nd elements
                    title_id = row[0]
                    title_type = row[2]
                    # Store title data in the dictionary
                    title_data[title_id] = title_type

# Process TSV files
process_tsv_files()

# Save the title data to a pickle file
with open(output_pickle_file, 'wb') as f:
    pickle.dump(title_data, f)

print("Conversion completed. Title data saved to title.pickle.")
