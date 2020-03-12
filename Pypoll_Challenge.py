# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = "Resources/election_results.csv"
# Assign a variable to save the file to a path.
txt__file = os.path.join("analysis", "election_analysis.txt")

#Initializing variables
total_votes=0
candidateoptions=[]
candidatevotes={}
winning_votes=0
winning_cand=""
winning_percent=0

countyoptions=[]
countyvotes={}
largest_turnout=0
turnout_value=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    
    # Read the header row.
    headers = next(file_reader)
    print(headers)


    for row in file_reader:
        total_votes+=1
        
        #Identify and find votes per candidate
        candidatename=row[2]
        if candidatename not in candidateoptions:
            candidateoptions.append(candidatename)
            candidatevotes[candidatename]=0
        candidatevotes[candidatename]+=1
       
        
        #Identify and find votes per county
        countyname=row[1]
        if countyname not in countyoptions:
            countyoptions.append(countyname)
            countyvotes[countyname]=0
        countyvotes[countyname]+=1
            
        
        
#Find the winner
for name in candidateoptions:
    if candidatevotes[name] > winning_votes:
        winning_cand=name
        winning_votes=candidatevotes[name]
        winning_percent=100*candidatevotes[name]/total_votes
 

#Find largest turnout
for county in countyoptions:
    if countyvotes[county]>turnout_value:
        largest_turnout=county
        turnout_value=countyvotes[county]

    
    
    
    
with open(txt__file,'w') as txt_file:
    
    
    #Save/print total votes
    election_results = (f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    txt_file.write(election_results)
   
    
    #Save/print county votes
    txt_file.write(f"County Votes:\n")
    for county in countyoptions:
        votes=countyvotes[county]
        vote_percent= 100*votes/total_votes
        county_results=(f"{county}: {vote_percent:,.1f}% ({votes:,})\n")
        txt_file.write(county_results)
        print(county_results)
        
        
    #Largest Turnout Summary   
    lts=(f"-------------------------\n"
         f"Largest County Turnout: {largest_turnout}\n"
         f"-------------------------\n")
    
    txt_file.write(lts)
    print(lts)
    
    
    #Save/print candidate votes
    for name in candidatevotes:
        
        votes = candidatevotes[name]
        vote_percentage = votes / total_votes * 100
        candidate_results = (
            f"{name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results, end="")
        txt_file.write(candidate_results)
      
        
    #Winner stats
    winning_candidate_summary = (f"-------------------------\n"
        f"Winner: {winning_cand}\n"
        f"Winning Vote Count: {winning_votes:,}\n"
        f"Winning Percentage: {winning_percent:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
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