# Add our dependencies
import csv
import os
path = "C:/Users/jacqu/Election_Analysis"
# Assign a variable for the file to load and the path.
file_to_load = os.path.join(path, "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join(path, "analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
    # Print the candidate name from each row
    candidate_name = row[2]
    
    if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

        # Begin tracking that candidate's vote count.
        candidate_votes[candidate_name] = 0

# Print the candidate list.
print(candidate_votes)

    # Using the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file
    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")
