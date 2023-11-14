import csv

# Specify the file path
file_path = ('C:\\Users\\lenar\OneDrive\\Documents\\Data Bootcamp\\python_challenge\data_budget.csv')

# Open the CSV file and read its contents
with open(file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each 'row' variable represents a row in the CSV file
        print(row)
