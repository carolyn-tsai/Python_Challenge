# Import dependencies: 
    # os – Operating system interface.
    # csv – Comma Separated Values: This will allow me to import and export format for spreadsheets and databases. It will allow me to read and write CSV files.
    # collections – High Performance Container Datatypes: When approaching the PyPoll task, I knew I needed to count the number of votes per candidate. I searched for a way to quickly get the vote numbers without using a loop. The Counter function seemed like a good option and it falls under the “collections” module. In order to use the Counter function, I need to first import “collections.”

import os
import csv
import collections

# Create path to collect data from the PyPoll folder:

csvpath = os.path.join("..","PyPoll","election_data.csv")

# Open the CSV file:

with open(csvpath, newline="") as csvfile:

    # Split the data by commas:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header:

    header = next(csvreader)

    # Create an empty list to hold candidate names:

    candidates_voted = []

    # Loop through each row of the file to get votes and candidate information:

    for row in csvreader:

        # Add each candidate name to the empty candidates_voted list:

        candidates_voted.append(row[2])

    # To find the total number of votes, count the number of items in candidates_voted since each candidate name represents a vote:

    total_votes_cast = len(candidates_voted)

    # Using Counter(), track how many times the same candidate is voted for. The Counter function is a dict subclass for counting hashable objects.

    votes_per_candidate = collections.Counter(candidates_voted)

    # To find the candidate with the most votes, I sorted the values in votes_per_candidate and reversed the order since I want the candidate with the most votes. If I did not reverse the order, then I would just have to access the last index. However, it is easier to access the first index (0) so I want the first index to hold the name of the candidate with the most votes.

    max_vote = sorted(votes_per_candidate.values(),reverse=True)[0]

    # To save on typing out the same "----" line, I assigned it to an arbitrary "dash" variable. This will also make the print look cleaner below.

    dash = (f"-----------------------------------")

    # Print results to terminal: 
    
    print(f"Election Results")
    print(dash)
    print(f"Total Votes: {total_votes_cast}")
    print(dash)

    # Loop through each item in votes_per_candidate and utilize “f-string” to get the correct format that is asked for. The votes_per_candidate dictionary already holds the candidate name and the total number of votes per candidate. I need to get the percentage of the votes and in order to do that, I will have to take the vote number and divide it by the total number of votes (the value of total_votes_cast) and multiply that amount by 100 to get the percentage. However, in the example, it shows the percentage as 0.000%. I could not find a way to get the decimal to show up to three places, so I used “f-string” to format my numbers. I used a for loop because if the data were different and there were more candidates, this method will be able to count all the names and print them out appropriately. I initially printed the individual candidate names but then realized that in doing so, my code will only work for the data set provided. I wanted my code to work for any number of candidates. 

    for candidate, vote in votes_per_candidate.items():
        print(candidate + f": {int((vote/total_votes_cast)*100)}.000% ({vote})")
    print(dash)

     # To find the candidate name that matches with the highest number of votes, I need to loop through votes_per_candidate and find the value that matches the max_vote amount. Once I find the candidate name that matches that value, I need to print the candidate name as the winner.

    for candidate, vote in votes_per_candidate.items():
        if vote == max_vote:
            print(f"Winner: {candidate}")
    print(dash)

    # To save on typing out the same “----” line with new line for formatting, I assigned it to an arbitrary “line” variable. This will also make the print look cleaner below.

    line = (f"-----------------------------------\n")

    # To create a new text file called “PyPoll_Analysis,” I need to open the file using “write” mode.

    with open("PyPoll_Analysis.txt","w") as text_file:

        # In the text file, I want to print the data I collected in the format outlined by the Assignment README. In order to achieve that format, I used “f-strings.”

        text_file.write(f"Election Results\n")
        text_file.write(line)
        text_file.write(f"Total Votes: {total_votes_cast}\n")
        text_file.write(line)
        for candidate, vote in votes_per_candidate.items():
            text_file.write(candidate + f": {int((vote/total_votes_cast)*100)}.000% ({vote})\n")
        text_file.write(line)
        for candidate, vote in votes_per_candidate.items():
            if vote == max_vote:
                text_file.write(f"Winner: {candidate}\n")
        text_file.write(line)