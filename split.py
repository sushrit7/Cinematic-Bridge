import csv
import os

# Define file paths
tsv_file_path = 'name.basics.tsv','title.basics.tsv'
output_directory = 'split_files'

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to split the TSV file into smaller files
def split_file():
    with open(tsv_file_path, 'r', encoding='utf-8') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        header = next(reader)  # Get header
        current_file_index = 1
        current_output_file = None
        current_output_writer = None
        row_count = 0

        for row in reader:
            if row_count % 1000000 == 0:
                # Close the current output file if it exists
                if current_output_file:
                    current_output_file.close()
                
                # Open a new output file
                output_file_path = os.path.join(output_directory, f'part_{current_file_index}.tsv')
                current_output_file = open(output_file_path, 'w', encoding='utf-8', newline='')
                current_output_writer = csv.writer(current_output_file, delimiter='\t')
                current_output_writer.writerow(header)  # Write header to new file
                current_file_index += 1
            
            # Write row to current output file
            current_output_writer.writerow(row)
            row_count += 1
        
        # Close the last output file
        if current_output_file:
            current_output_file.close()

# Split the file
split_file()
