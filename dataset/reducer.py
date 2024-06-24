import csv
import random
import gzip
import shutil

def process_csv(input_path, output_path):

    # Load the CSV file into a list of rows
    with open(input_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Keep the header
        rows = list(reader)
    
    # Randomly delete 50% of the rows
    reduced_rows = random.sample(rows, len(rows) // 2)
    
    # Save the reduced rows to a new CSV file
    reduced_csv_path = 'reduced_file.csv'
    with open(reduced_csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Write the header
        writer.writerows(reduced_rows)
    
    # Compress the new CSV file using gzip
    with open(reduced_csv_path, 'rb') as f_in:
        with gzip.open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    # Clean up the temporary reduced CSV file
    import os
    os.remove(reduced_csv_path)

# Define your input and output file paths
input_path = 'dataset.csv'
output_path = 'dataset_half.csv.gz'

# Call the function to process the CSV file
process_csv(input_path, output_path)

