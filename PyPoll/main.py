#this is the PyPoll project

import os
import csv

#set up a list for the potential "winners"
Winner = ["Khan", "Correy","Li","O'Tooley"]

votes = 0
total = 0
#import the csv file

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
#print the initial rows of the output
print ("Election Results")
print("--------------------------")

#start the with loop through the csv file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#set the variables

    count =0
    diff1=0
    KhanTally = 0
    CorreyTally = 0
    LiTally= 0
    OTally=0
    KPerc = 0
    CPerc = 0
    LPerc = 0
    OPerc = 0

#skip the first row
#     
    next(csvreader)
    for x in csvreader:
        total = total + 1
        #create if loop to add votes to each individual tally
        if x[2] == "Khan":
            KhanTally +=1
        if x[2] == "Correy":
            CorreyTally +=1
        if x[2] == "Li":
            LiTally +=1
        if x[2] == "O'Tooley":
            OTally +=1  
        #second set of loops to find Winner
        #once the tally becomes greater than the total
        #and the other candidates
        #it becomes the Winner
        # by setting the variable list to a specific value

        if KhanTally > total-1:
            Winner = Winner[0]       
        if CorreyTally > total-1:
            Winner = Winner[1]
        if LiTally > total-1:
            Winner = Winner[2]
        if OTally > total-1:
            Winner = Winner[3]

        
   
                  
    #calculate the percentage of votes for each candidate

    KPerc = KhanTally / total * 100
    CPerc = CorreyTally / total * 100
    LPerc = LiTally / total * 100
    OPerc = OTally / total * 100
   
#print the results

    print (f"Total Votes: {total}")
    print("--------------------------")
    print (f"Khan: {KPerc}% ({KhanTally})")
    print (f"Correy: {CPerc}% ({CorreyTally})")
    print (f"Li: {LPerc}% ({LiTally})")
    print (f"O'Tooley: {OPerc}% ({OTally})")
    print("--------------------------")
    print("--------------------------")
    print (f"Winner : {Winner}")
    print("--------------------------")


#output to a text file

file = open("polloutput.txt","w")
file.write("Election Results\n")
file.write("--------------------------\n")
file.write (f"Total Votes: {total}\n")
file.write("--------------------------\n")
file.write (f"Correy: ({CorreyTally})\n")
file.write(f"Khan: {KPerc}% ({KhanTally})\n")
file.write(f"Correy: {CPerc}% ({CorreyTally}\n")
file.write(f"Li: {LPerc}% ({LiTally})\n")
file.write(f"O'Tooley: {OPerc}% ({OTally})\n")
file.write("--------------------------\n")
file.write("--------------------------\n")
file.write(f"Winner : {Winner}\n")
file.write("--------------------------\n")


