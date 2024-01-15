#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv

# Set CSV file path
csvpath = "../Resources/budget_data.csv"

# Set output folder
output_folder = "../analysis/"

# Initialise variables to store financial data
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
months = []

# Read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Count total months
        total_months += 1

        # Extract the date and profit/loss from the row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the net total amount of profit/loss
        net_total += profit_loss

        # Calculate the change in profit/loss from the previous month
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            months.append(date)

        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
max_increase = max(changes)
max_decrease = min(changes)
max_increase_month = months[changes.index(max_increase)]
max_decrease_month = months[changes.index(max_decrease)]

# Print analysis results
analysis_results = [
    'Financial Analysis',
    '-------------------------',
    f'Total Months: {total_months}',
    f'Total: ${net_total}',
    f'Average Change: ${average_change:.2f}',
    f'Greatest Increase in Profits: {max_increase_month} (${max_increase})',
    f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})',
    '-------------------------'
]

for result in analysis_results:
    print(result)

# Specify the full path for the output file, including the folder
output_file = os.path.join(output_folder, "financial_analysis.txt")

# Write the analysis results to a text file
with open(output_file, "w") as txtfile:
    txtfile.write('\n'.join(analysis_results))


