#PyPoll script
import os
import csv

#we'll need the two filepaths- one for the input csv and one for the output txt
csvpath=os.path.join("Resources","election_data.csv")
outputpath=os.path.join("analysis","pypoll.txt")

#initiate our variables- I decided to put everything into a dictionary to test
# out what we learned in class. I probably could have gotten away with making
# each name the only keys in my dictionary and used some magic with the count()
# methods for the total, but wanted to challenge myself further
winnerVotes=0
winner=""
votes={}
votes['total']=0
votes['name']={}

#we'll need to open up the file we want to read and skip the header line
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvfile)

    #for each row in the csv file, grab the name of the person who received the vote
    # and check to see if we already have that name in our dictionary
    for row in csvreader:
        voteName=row[2]
        votes['total'] = votes['total'] + 1 #update the total

        #if this person has already received a vote, we'll update the value to include one more
        if voteName in votes['name']:
            votes['name'][voteName] = votes['name'][voteName]+1
        #otherwise, this is the first vote they have received, so populate it as appropriate
        else:
            votes['name'][voteName] = 1

#print out our data to the terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {votes['total']}")
print("------------------------")
for key in list(votes['name'].keys()):
    print(f"{key}: {(votes['name'][key]/votes['total'] * 100):.3f}% ({votes['name'][key]})")
    if votes['name'][key] > winnerVotes:
        winner=key
        winnerVotes=votes['name'][key]
print("------------------------")
print(f"Winner: {winner}")    

#print this data to our txt file
with open(outputpath, "w") as outputfile:
    outputfile.write("Election Results\n------------------------")
    outputfile.write(f"\nTotal Votes: {votes['total']}\n------------------------")
    for key in list(votes['name'].keys()):
        outputfile.write(f"\n{key}: {(votes['name'][key]/votes['total'] * 100):.3f}% ({votes['name'][key]})")
    outputfile.write(f"\n------------------------\nWinner: {winner}\n------------------------\n")
