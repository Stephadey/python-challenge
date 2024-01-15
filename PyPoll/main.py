#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv

# Set CSV file path
csvpath = "../Resources/election_data.csv"

# Set output folder
output_folder = "../analysis/"

# Initialise variables to store election data
total_votes = 0
candidates = []
candidate_votes = {}

# Read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Extract the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not in the candidates list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Count the votes for each candidate
        candidate_votes[candidate_name] += 1

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print analysis results
analysis_results = [
    'Election Results',
    '-------------------------',
    f'Total Votes: {total_votes}',
    '-------------------------'
]

for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    analysis_results.append(f'{candidate}: {percentage:.3f}% ({votes})')

analysis_results.extend([
    '-------------------------',
    f'Winner: {winner}',
    '-------------------------'
])

for result in analysis_results:
    print(result)

# Specify the full path for the output file, including the folder
output_file = os.path.join(output_folder, "election_results.txt")

# Write the analysis results to a text file
with open(output_file, "w") as txtfile:
    txtfile.write('\n'.join(analysis_results))
    


# In[ ]:




