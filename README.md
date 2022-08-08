# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
-There were 369,711 votes cast in election.
-The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 votes
    - Diana DeGette received 73.8% of the votes and 272,892 votes
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes
-The winner of the election was:
    - Diana DeGette, who received 73.8% and 272,892 votes

## Challenge Overview
The Election Audit
- The election audit that I created was to read the election data. Code was created to organize and seperate the information into a readable format. This created two sections, candidates and counties. The election audit read the votes per category, the percentage out of all the votes, and the winners of both categories.

![The election analysis(election results) txt file](https://user-images.githubusercontent.com/106329824/183518517-012314f3-9c19-495c-83d2-2f50352fd2a6.png)


The Election Audit Results
- There were 369,711 votes cast in this congressional election.

- County results were: 
    - Jefferson recieved 38,855 votes. This is a total of 10.5% of all votes for county.
    - Denver recieved 306,055 votes. This is a total of 82.8% of all votes for county.
    - Arapahoe recieved 24,801 votes. This is a total of 6.7% of all votes for county.
        - Denver has the largest number of votes.

- Candidate results were:
    - Candidate Charles Casper Stockham recieved 85,213 votes. This is a total of 23% of all votes for candidates.
    - Candidate Diana DeGette recieved 272,892 votes. This is a total of 73.8% of all votes for candidates.
    - Candidate Raymon Anthony Doane recieved 11,606 votes. This is a total of 3.1% of all votes for candidates.
        - Candidate Diana DeGette has the largest number of votes.

![The results](https://user-images.githubusercontent.com/106329824/183518317-c3a726f3-ede0-4783-85a7-8720f692832e.png)

## Challenge Summary
- I propose this script to be used for all upcoming elections. I believe the code that is already set up can be easily modified for the use of all election data as it is designed to loop through and calculate the highest numbers/ the most votes. It can be used as an easy summary of how an election went for safe keeping or even for analysis to be used in upcoming elections. The code is set up using a specific location, so it would be really simple to use it for any type of election.
- Modification example 1
    - Changing the data files.
        It would be simple to replace the old data files with the new ones. This would be a simple modification since the only editing is to replace the files using the same name so the data doesn't change.
- Modification example 2
    - Change the data path.
        Changing the path to the data involves more code but it might allow for more storage of information. It would involve changing the actual code but would be beneficial if it is important to keep records of previous elections.
