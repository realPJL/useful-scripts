import json
import csv

def json_to_csv(input_file, output_file):
    # Read JSON data from input file
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)
    
    # Extract headers from JSON keys
    headers = list(data[0].keys())
    
    # Write CSV data
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

# Example usage:
input_file = 'sample.json'  # Path to input JSON file
output_file = 'sample_output.csv'  # Path to output CSV file

json_to_csv(input_file, output_file)
