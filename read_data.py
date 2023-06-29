import csv

def extract_column_data(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        column2_data = []
        for row in reader:
            if len(row) >= 2:  # Check if the row has at least two columns
                column2_data.append(row[1].strip())  # Append data from column 2 to the list
    return column2_data