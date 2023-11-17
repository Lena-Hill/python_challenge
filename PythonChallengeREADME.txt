# python_challenge

PyBank Challenge

In this challenge we were tasked with creating a Python script to analyze financial records. We were given a dataset in a csv file coposed of two columns: "Date" and "Profit/Losses". We were asked to create a Python script that analyzes each record to calculate the following values:
  The total number of months included in the dataset
  The net total amount of "Profit/Losses" over the entire period
  The changes in "Profit/Losses" over the entire period, and the average of those changes
  The greatest increase in profits (date and amount) over the entire period
  The greatest decrease in profits (date and amount) over the entire period

Description:
Using week=three Python course materials and notes I created a Python script to analyse financial data. This week we learned how to use Python, so I started by importing the CSV module and specifiying the path to the CSV file we want to analyze. The 'r' before the string is a raw string literal, which I used to get around an error. After brining my CSV file in to read and initializing variables and counters, I started a for loop that iterates over each row in the CSV file. For each row, increment the 'total_months' counter. Next I extracted the profit/loss value from the second column and converted it into an integer. I then addd the current profit/loss value to the 'net_total' accumulator. I calculated the change in profit/loss by subtracting the previous profit/loss from the current one. This change is added to the 'total_change' accumulator. Lines 39-47 check whether the current change is greater than the current greatest increase or less thatn the current greatest decrease. if so, it updates the vlaues in the 'greatest_increase' and 'greatest_decrease' dictionaries. I calculated the average change directly average_change = total_change/(total_months). I then printed the results to the terminal using formatted formatted strings and exported the results to a text file. 

Resources:
For this week's challenge I exclusively used the week-three course materials/solutions, and ChatGPT to help check my code as answer questions. I used these resoources for both parts of the challenge. I also used Slack to ask the class for help, like how to get around that file_not_found error. 

PyPoll Challenge

For this challenge we were asked to help a rural town streamline their vote counting. We were given a data set composed of three columns: "Voter ID", "County", and "Candidate". I created a Python scrip that analyzes the votes and calculates each of the following values:
  The total number of votes cast
  A complete list of candidates who recieved votes
  The percentage of votes each candidate won
  The winner of the election based on popular vote

Description:
I started this challenge exactly the same way I started the PyBank challenge: By importing CSV module, specifying my file path (raw again), opening and reading the CSV file, skipping the header, initializing variables/counters, asnd iterating over each row in the CSV file. I used a for loop to iterate over each row and extract the relevant data. On line 25 I updated the vote count for the current candidate in the candidate_votes dictionary. If the candidate was already in the dictionary, I increment their vote count; otherwise, add them to the dictionary with a count of 1. Finally, we determine the winner based on popular vote, print the results to the terminal, then export a text file with the analysis results. Again, I exclusively used week-three course material/solutions, ChatGPT, and ask the class.  



