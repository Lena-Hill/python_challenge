import csv

# Specify the file path
file_path = r'C:\Users\lenar\OneDrive\Documents\Data Bootcamp\python_challenge\Starter_Code\PyBank\Resources\budget_data.csv'

# Open the CSV file and read it
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # skip the headers
    next(csvreader)

    # initialize counters and variables
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    total_change = 0 # accumulator for change
    greatest_increase = {"date": None, "amount": float("-inf")}
    greatest_decrease = {"date": None, "amount": float("inf")}

    #iterate over each row
    for row in csvreader:
        # increment counter for each row
        total_months += 1

        # extract profit/loss value
        profit_loss = int(row[1])

        # increment the net total with the profit/loss value
        net_total += profit_loss

        # calculate the change in profit/loss and store it in a list
        change = profit_loss - previous_profit_loss
        total_change += change

        # update the change in profit/loss and store it in the changes list
        previous_profit_loss = profit_loss

        # Check for the greatest increase in profits
        if change > greatest_increase["amount"]:
            greatest_increase["date"] = row[0]
            greatest_increase["amount"] = change

         # Check for the greatest decrease in profits
        if change < greatest_decrease["amount"]:
            greatest_decrease["date"] = row[0]
            greatest_decrease["amount"] = change   
        
# calculate the average change directly
average_change = total_change/(total_months - 1)

# print results
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]:.2f})')
print(f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]:.2f})')

# Export the results to a text file
output_file_path = r'C:\Users\lenar\OneDrive\Documents\Data Bootcamp\python_challenge\Starter_Code\PyBank\analysis_results.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(f'Total Months: {total_months}\n')
    output_file.write(f'Total: ${net_total}\n')
    output_file.write(f'Average Change: ${average_change:.2f}\n')
    output_file.write(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]:.2f})\n')
    output_file.write(f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]:.2f})\n')

print(f'Results exported to: {output_file_path}')