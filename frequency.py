# Python3 code that finds the occurence of a character in a string length n 
# I wasn't sure if string of length 'n' meant any length I chose or if it was a variable length so I made it user input.
# The purpose of this program is take any string of characters and tell the user how many occurences the character of their choice appears. 

print("Enter 'x' for exit."); #this is the exit key in the progam. If you did not want to continue the user could press 'x' and exit the program
string = input("Enter any string to count character: "); #this is the user input 
if string == 'x': #this if statement is the initiation of the exit
    exit();
else:
    char = input("Enter a character to count to count from above string: ");
    val = string.count(char); #the 'value' is the number of times  the character appears. 'Char' is the user input of their selected character. 
    print("Total = ",val); #here is the total of times the character appeared. 