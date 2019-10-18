import os
import csv

#import election_data.csv
pypoll_csv = os.path.join ("election_data.csv")

#declare arrays and set variables to zero
total_votes = 0
candidates = []
total_votes_0=0
total_votes_1=0
total_votes_2=0
total_votes_3=0

#extract data and calculate
with open(pypoll_csv, newline = "") as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter=",")
    next(pypoll_reader)

    for row in pypoll_reader:
        total_votes = total_votes + 1
        if row[2] not in candidates:
            candidates.append(row[2])
        elif row[2] == candidates[0]:
            total_votes_0 = total_votes_0 + 1
        elif row[2] == candidates[1]:
            total_votes_1 = total_votes_1 + 1
        elif row[2] == candidates[2]:
            total_votes_2 = total_votes_2 + 1
        elif row[2] == candidates[3]:
            total_votes_3 = total_votes_3 + 1

#make percentages
candidate_0_percentage = (total_votes_0 / total_votes) * 100
candidate_1_percentage = (total_votes_1 / total_votes) * 100
candidate_2_percentage = (total_votes_2 / total_votes) * 100
candidate_3_percentage = (total_votes_3 / total_votes) * 100

candidatelist = [candidate_0_percentage, candidate_1_percentage, candidate_2_percentage, candidate_3_percentage]
winner = max(candidatelist)
if winner == candidate_0_percentage:
    overallwinner = candidates[0]
elif winner == candidate_1_percentage:
    overallwinner = candidates[1]
elif winner == candidate_1_percentage:
    overallwinner = candidates[2]
else:
    overallwinner = candidates[3]

#print to terminal
print ("Election Results")
print ("-------------------------")
print (f"Total Votes: {total_votes}")
print ("-------------------------")
print (f"{candidates[0]}: {candidate_0_percentage:.3f}% ({total_votes_0})")
print (f"{candidates[1]}: {candidate_1_percentage:.3f}% ({total_votes_1})")
print (f"{candidates[2]}: {candidate_2_percentage:.3f}% ({total_votes_2})")
print (f"{candidates[3]}: {candidate_3_percentage:.3f}% ({total_votes_3})")
print ("-------------------------")
print (f"Winner: {overallwinner}")
print ("-------------------------")

#print to text file
print ("Election Results",file=open("PyPoll.txt", "a"))
print ("-------------------------", file=open("PyPoll.txt", "a"))
print (f"Total Votes: {total_votes}", file=open("PyPoll.txt", "a"))
print ("-------------------------", file=open("PyPoll.txt", "a"))
print (f"{candidates[0]}: {candidate_0_percentage:.3f}% ({total_votes_0})", file=open("PyPoll.txt", "a"))
print (f"{candidates[1]}: {candidate_1_percentage:.3f}% ({total_votes_1})", file=open("PyPoll.txt", "a"))
print (f"{candidates[2]}: {candidate_2_percentage:.3f}% ({total_votes_2})", file=open("PyPoll.txt", "a"))
print (f"{candidates[3]}: {candidate_3_percentage:.3f}% ({total_votes_3})", file=open("PyPoll.txt", "a"))
print ("-------------------------", file=open("PyPoll.txt", "a"))
print (f"Winner: {overallwinner}", file=open("PyPoll.txt", "a"))
print ("-------------------------", file=open("PyPoll.txt", "a"))