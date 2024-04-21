import csv
import os

# Define file paths
tsv_file_paths = ['name.basics.tsv', 'title.basics.tsv']

# Function to create output directories if they don't exist
def create_output_directories():
    for tsv_file_path in tsv_file_paths:
        directory_name = os.path.splitext(os.path.basename(tsv_file_path))[0]
        output_directory = os.path.join('split_files', directory_name)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

# Create output directories
create_output_directories()

# Function to split each TSV file into smaller files and save them into separate directories
def split_files_and_save():
    for tsv_file_path in tsv_file_paths:
        output_directory = os.path.join('split_files', os.path.splitext(os.path.basename(tsv_file_path))[0])
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

# Split each TSV file and save them into separate directories
split_files_and_save()
