
import csv

file_path = r'C:\Users\lenar\OneDrive\Documents\Data Bootcamp\python_challenge\Starter_Code_PythonChallenge\Starter_Code\PyBank\Resources\budget_data.csv'


withopen(file_path, 'r') as file: 

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header= next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        print(f"Date:(row[0])")
        print(f"Profti/Loss:{row[1]}")
