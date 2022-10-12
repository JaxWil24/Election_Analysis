# Election_Analysis

## Project Overview
A Colorado Board of Elections requested an audit for the local congressional election. The election audit read the election data to organize and seperate information into a readable format. This created two sections, candidates and counties. The election audit read the votes per category, the percentage out of all the votes, and the winners of both categories.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
* There were 369,711 votes cast in election.
![The votes](https://user-images.githubusercontent.com/106329824/195368758-87ecae8a-3bc4-49a0-ae8d-69f6961031c2.png)

The candidate results were:
    * Charles Casper Stockham received 23.0% of the votes and 85,213 votes
    * Diana DeGette received 73.8% of the votes and 272,892 votes
    * Raymon Anthony Doane received 3.1% of the votes and 11,606 votes
![The candidates](https://user-images.githubusercontent.com/106329824/195368667-18881e28-d7ac-4bbc-9b93-8b3eed3d43e1.png)
    
* The winner of the election was:
    *  Diana DeGette, who received 73.8% and 272,892 votes
![The winner](https://user-images.githubusercontent.com/106329824/195369106-970e20c6-c2ac-42af-9ac9-0f6e22cd5c8f.png)

The County results were: 
    * Jefferson recieved 38,855 votes. This is a total of 10.5% of all votes for county.
    * Denver recieved 306,055 votes. This is a total of 82.8% of all votes for county.
    * Arapahoe recieved 24,801 votes. This is a total of 6.7% of all votes for county.
        * Denver has the largest number of votes.
![Countyj](https://user-images.githubusercontent.com/106329824/195370916-e7ad44f5-73dc-45e7-943b-059644e3f2ba.png)

Creating a text file with the processed information.
![The election analysis(election results) txt file](https://user-images.githubusercontent.com/106329824/183518517-012314f3-9c19-495c-83d2-2f50352fd2a6.png)

The output from the VS-Code terminal.
![The results](https://user-images.githubusercontent.com/106329824/183518317-c3a726f3-ede0-4783-85a7-8720f692832e.png)

## Challenge Summary
- I propose this script to be used for all upcoming elections. I believe the code that is already set up can be easily modified for the use of all election data as it is designed to loop through and calculate the highest numbers/ the most votes. It can be used as an easy summary of how an election went for safe keeping or even for analysis to be used in upcoming elections. The code is set up using a specific location, so it would be really simple to use it for any type of election.
- Modification example 1
    - Changing the data files.
        It would be simple to replace the old data files with the new ones. This would be a simple modification since the only editing is to replace the files using the same name so the data doesn't change.
- Modification example 2
    - Change the data path.
        Changing the path to the data involves more code but it might allow for more storage of information. It would involve changing the actual code but would be beneficial if it is important to keep records of previous elections.
