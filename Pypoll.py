# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes=0
candidateoptions=[]
candidatevotes={}
winning_votes=0
winning_cand=""
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        candidatename=row[2]
        if candidatename not in candidateoptions:
            
            candidateoptions.append(candidatename)
            candidatevotes[candidatename]=0
        candidatevotes[candidatename]+=1
        total_votes+=1

for name in candidateoptions:
    if candidatevotes[name] > winning_votes:
        winning_cand=name
        winning_votes=candidatevotes[name]
        
    print(f'{name} got {candidatevotes[name]} ({100*candidatevotes[name]/total_votes:,.2f}%) votes.')
print(
    f"-------------------------\n"
    f"Winner: {winning_cand}\n"
    f"Winning Vote Count: {winning_votes:,}\n"
    f"Winning Percentage: {100*winning_votes/total_votes:.1f}%\n"
    f"-------------------------\n")

 
    
    
    
    
    
with open(file_to_save,'w') as txtfile:
    
    txtfile.write("Counties in Election\n----------------------\na\nb\nc")



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