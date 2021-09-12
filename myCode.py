# Trey Miller
# CSCI 236
# Sep 11, 2021
# Program 01 - Steps
# approximate number of hours you invested
# Grade Version (so if you did the A version say: A version)
# description of any major problems you ran into
# status of the program - does it compile, does it run perfectly, does it have bugs, any limitations, etc

# Named constants - create one for each month to store number of days in that month; assume this is NOT a leap year
import sys
def main():
    month_name = ( 'January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # Open the steps file using the first command line argument to get the input file name. For example: python steps.py steps.txt would open the file steps.txt to read the steps 
    #steps_file = open(sys.argv[1], 'r')
    steps_file = open(sys.argv[1], 'r')
    length = len(sys.argv[1])
    def isLeapYear():
        if length == 366:
            days[2]=29
    # Display the average steps for each month using a function to calculate and display
    #def avg_steps():
     #   month = 0
      #  isLeapYear()
       # for num in days:
        #    total = 0
         #   count = 0
          #  average = 0
           # for count in range (1, days[month]+1):
            #    steps = int(steps_file.readline())
             #   total += steps
            #average = total / days[month]
            #print ("The average steps taken in ", month_name[month], " was ", average)
                
            #month = month + 1
    # Close the file.

    def average_steps():
        month = 0
        isLeapYear()
        for num in days:
            total = 0
            count = 0
            average = 0
            for count in range (1, days[month]+1):
                steps = int(steps_file.readline())
                total += steps
            average = total / days[month]
            print ("The average steps taken in ", month_name[month], " was ", average)
                
            month = month + 1
    # compute the average number of steps for the given month
    # output the results
main()
