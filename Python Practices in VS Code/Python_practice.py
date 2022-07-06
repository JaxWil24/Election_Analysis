print("Hello World")


counties = ["Arapahoe","Denver","Jefferson"]

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


counties_dict = {"Arapahoe": 422829, "Denver":463353,"Jefferson":432438}

for county, voters in counties_dict.items():

    print(f"{county} county has {voters:,} registered voters.")

voting_data = [f'{"county": "Arapahoe", "registered_voters": 422829,},{"county":"Denver","registered_voters":463353,},{"county":"Jefferson","registered_voters":432438,}']

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
percentage_votes=()*100
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes. ")

print(message_to_candidate)

