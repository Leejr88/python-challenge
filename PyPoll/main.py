# import our file 
import os
import csv
csvpath = "resources/election_data.csv"

# create lists to store column data
ballot_id = []
county = []
candidate_vote = []

# open csv file

with open(csvpath, encoding= 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header row
    csv_header = next(csvreader)


    # iterate through the sheet
    for row in csvreader:
        # append our values to our lists from columns
        ballot_id.append(row[0])
        county.append(row[1])
        candidate_vote.append(row[2])

votes_cast = len(ballot_id)
candidates = set(candidate_vote)

# count votes for each candidate and find out the total, the %, and who won
doane_votes = candidate_vote.count("Raymon Anthony Doane")
degette_votes = candidate_vote.count("Diana DeGette")
stockham_votes = candidate_vote.count("Charles Casper Stockham")

percent_doane = round((doane_votes / votes_cast)*100, 2)
percent_degette = round((degette_votes / votes_cast)*100, 2)
percent_stockham = round((stockham_votes / votes_cast)*100, 2)

# spit out winner of election

if percent_doane > percent_degette and percent_stockham:
    election_winner = "Raymon Anthony Doane"
elif  percent_stockham > percent_degette and percent_doane:
    election_winner = "Charles Casper Stockham"
else:
    election_winner = "Diane DeGette"

# print our analysis
print("Election Results")
print("-------------------------------------")
print(f"Total Votes: {votes_cast}")
print("-------------------------------------")
print(f"Charles Casper Stockham: {percent_stockham}% ({stockham_votes})")
print(f"Diana DeGette: {percent_degette}% ({degette_votes})")
print(f"Raymon Anthony Doane: {percent_doane}% ({doane_votes})")
print("-------------------------------------")
print(f"Winner: {election_winner}")
print("-------------------------------------")

# output
output_file = "output.txt"

with open(output_file, "w") as output:
    output.write("Election Results\n")
    output.write("-------------------------------------\n")
    output.write("Total Votes: {votes_cast}\n")
    output.write("-------------------------------------\n")
    output.write(f"Charles Casper Stockham: {percent_stockham}% ({stockham_votes})\n")
    output.write(f"Diana DeGette: {percent_degette}% ({degette_votes})\n")
    output.write(f"Raymon Anthony Doane: {percent_doane}% ({doane_votes})\n")
    output.write("-------------------------------------\n")
    output.write(f"Winner: {election_winner}\n")
    output.write("-------------------------------------\n")

print(f"Election Results has been saved to {output_file}")