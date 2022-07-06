# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
path = "C:\\Users\\jacqu\\OneDrive\\Desktop\\Data Analytics Bootcamp\\Module 3\\Election_Analysis"
file_to_load = os.path.join(path, "Resources\election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join(path, "Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and Votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes = total_votes + 1
    
    # Print the candidate name from each row
    candidate_name = row[2]
    
    if candidate_name not in candidate_options:
    
        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

        # Begin tracking that candidate's vote count.
        candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count.
    candidate_votes[candidate_name] += 1

with open (file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end ="")
    
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #print(candidate_results)

    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
# To do:  Print each candidates name, vote count, and percentage of votes to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
#print(winning_candidate_summary)

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:


    txt_file.write(winning_candidate_summary)

