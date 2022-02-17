import csv
import os

#Assign variable to load a file from a path
file_to_load = os.path.join('Resources/election_results.csv')
                            
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    # file_reader = csv.reader(election_data)
    # count=0
    # for row in file_reader:
    #     count = count + 1 
    #     print(row)
    #     if count == 10:
    #         break
    #     # Read and print the header row.
    #     headers = next(file_reader)
    #     print(headers)
    
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #for row in file_reader:
        #print(row[0])
    headers = next(file_reader)
    print(headers)
        


# 1. The total number of votes cast
# 3. A complete list of candidates who received votes
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.