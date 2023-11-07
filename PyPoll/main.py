#reference CSV file
import csv
filein = "/Users/elizabethdworkin/Desktop/Data Analytics/Challenge III/python-challenge/PyPoll/Resources/election_data.csv"
fileout = "/Users/elizabethdworkin/Desktop/Data Analytics/Challenge III/python-challenge/PyPoll/Analysis/Analysis PyPoll.txt"

# read data
with open(filein) as f:
    reader = csv.reader(f)
    data = list(reader)

# clean data    
data = data[1:] # starts from index 1 - all the way to end 

total_votes = len(data)

votes_per_candidate = {}

for ballot_id, county, candidate in data:
  if candidate not in votes_per_candidate:
    votes_per_candidate[candidate] = 0
  votes_per_candidate[candidate] += 1


# Print the analysis to the terminal and export a text file with the results

output = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

winner_count = 0
winner = ""
for candidate, vote_count in votes_per_candidate.items():
    if vote_count > winner_count:
        winner_count = vote_count
        winner = candidate
    output += f"{candidate}: {round(vote_count / total_votes *100, 3)}% ({vote_count})\n"
    
output += f"""-------------------------
Winner: {winner}
-------------------------"""

print(output)

with open(fileout, "w") as f:
    f.write(output)





