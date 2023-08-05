import csv

def extract_data(file_path):
    """
    Extracts data from a CSV file and returns a list of dictionaries representing each row.
    """
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def transform_data(data):
    """
    Transforms the data by converting all names to uppercase.
    """
    transformed_data = []
    for row in data:
        transformed_row = {k: v.upper() for k, v in row.items()}
        transformed_data.append(transformed_row)
    return transformed_data

def load_data(file_path, data):
    """
    Loads the transformed data into a new CSV file.
    """
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    # File paths
    input_file_path = "input_data.csv"
    output_file_path = "output_data.csv"

    # Step 1: Extract data from the input CSV file
    data = extract_data(input_file_path)

    # Step 2: Transform the data (convert names to uppercase)
    transformed_data = transform_data(data)

    # Step 3: Load the transformed data into a new CSV file
    load_data(output_file_path, transformed_data)

    print("ETL task completed successfully.")

