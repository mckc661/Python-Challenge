#this is the PyBank project

import os
import csv
#set our initial variables

total=0
dollars = 0
highchange = 0
lowchange = 0
prev = 0
current = 0
max1 = 0
diff=0 
#import the csv file 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
print ("Financial Analysis")
print("--------------------------")
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    count =0
    diff1=0
    next(csvreader)
    for x in csvreader:
        #total gets the total number of months
        total = total + 1
        #dollars gets us the total dollars 
        dollars += int(x[1])
        #current gives us the current value
        current = x[1]
        #difference becomes the difference between the current and the previous value

        diff= float(current) - float(prev)
        #Skipping the first value, we set up Diff1 as the running total for the difference
        if total > 1:
            diff1 += diff
#reset the previous value to be the current value
        prev=current
        #set up a highchange value that is set and stays when you find the high difference
        if diff>highchange:
            highchange = diff
            highmonth= x[0]
        #set up a lowchange value that is set and stays when you find the lowest difference
        if diff<lowchange:
            lowchange = diff
            lowmonth= x[0]    
    #average value is the sum of the changes divided by the number of changes    
    average=diff1/(total-1)
         
   #print the results
    print (f"Total Months: {total}")
    print (f"Total: ${dollars}")
    print (f"Average Change: ${average}")
    print (f"Greatest Increase in Profits: {highmonth} (${highchange})")
    print (f"Greatest Decrease in Profits: {lowmonth} (${lowchange})")
 
    

#write to a text file
#tell it what file to write to
file = open("bankoutput.txt","w")

#tell the program what to write into the file
file.write("Financial Analysis\n")
file.write("--------------------------\n")
file.write(f"Total Months: {total}\n")
file.write(f"Total: ${dollars}\n")
file.write(f"Average Change: ${average}\n")
file.write(f"Greatest Increase in Profits: {highmonth} (${highchange})\n")
file.write(f"Greatest Decrease in Profits: {lowmonth} (${lowchange})\n")
