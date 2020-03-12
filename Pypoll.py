# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
txt__file = os.path.join("analysis", "election_analysis.txt")

#Initializing variables
total_votes=0
candidateoptions=[]
candidatevotes={}
winning_votes=0
winning_cand=""
winning_percent=0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Find number of votes per candidate
    for row in file_reader:
        candidatename=row[2]
        if candidatename not in candidateoptions:
            
            candidateoptions.append(candidatename)
            candidatevotes[candidatename]=0
        candidatevotes[candidatename]+=1
        total_votes+=1
        
#Find the winner
for name in candidateoptions:
    if candidatevotes[name] > winning_votes:
        winning_cand=name
        winning_votes=candidatevotes[name]
        winning_percent=100*candidatevotes[name]/total_votes
        
#    print(f'{name} got {candidatevotes[name]} ({winning_percent:,.2f}%) votes.')
#print(
#    f"-------------------------\n"
#    f"Winner: {winning_cand}\n"
#    f"Winning Vote Count: {winning_votes:,}\n"
#    f"Winning Percentage: {winning_percent:.1f}%\n"
#    f"-------------------------\n")

 
    
    
    
    
    
with open(txt__file,'w') as txt_file:
    election_results = (f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
   
    for name in candidatevotes:
        # Retrieve vote count and percentage.
        votes = candidatevotes[name]
        vote_percentage = votes / total_votes * 100
        candidate_results = (
            f"{name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)
        
    winning_candidate_summary = (f"-------------------------\n"
        f"Winner: {winning_cand}\n"
        f"Winning Vote Count: {winning_votes:,}\n"
        f"Winning Percentage: {winning_percent:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)



#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#{"county":"Denver", "registered_voters": 463353},
#{"county":"Jefferson", "registered_voters": 432438}]
##
#for i in voting_data:
#    
#    message=(f"{i['county']} county has {i['registered_voters']} registered voters.")
#    print(message)
    
    
    
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")
    






#election_data.close()