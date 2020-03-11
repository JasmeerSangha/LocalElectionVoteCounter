
import csv
import os
electfile = os.path.join('Resources','election_results.csv')
outerfile=os.path.join('analysis','election_analysis.txt')

with open(electfile) as election_data:
    
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)
    
    
    
     
    
    
with open(outerfile,'w') as txtfile:
    
    txtfile.write("Counties in Election\n----------------------\na\nb\nc")
#outfile.close()

    









#election_data.close()