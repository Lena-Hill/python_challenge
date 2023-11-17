import csv

# Specify the file path
file_path = r'C:\Users\lenar\OneDrive\Documents\Data Bootcamp\python_challenge\Starter_Code\PyPoll\Resources\election_data.csv'

# Open the CSV file and read it
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

    # Initialize variables
    total_votes = 0
    candidate_votes = {}  # Dictionary to store candidate votes

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment total votes
        total_votes += 1

        # Extract candidate name
        candidate = row[2]

        # Update candidate votes count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes for each candidate
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print results to the terminal
print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f'{candidate}: {percentage_votes[candidate]:.3f}% ({votes})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

# Export the results to a text file
output_file_path = r'C:\Users\lenar\OneDrive\Documents\Data Bootcamp\python_challenge\PyPoll\analysis\election_analysis.txt'

with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f'Total Votes: {total_votes}\n')
    output_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        output_file.write(f'{candidate}: {percentage_votes[candidate]:.3f}% ({votes})\n')
    output_file.write("-------------------------\n")
    output_file.write(f'Winner: {winner}\n')
    output_file.write("-------------------------\n")

print(f'Results exported to: {output_file_path}')