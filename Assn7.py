# Nicholas Wisnefske
# CS 125
# 3/9/2023

def count(word,char): # creates count class
    cnt = 0 #sets count to 0
    for letter in word: # creates a loop to find how many letter +1 there are in a word
        if letter == char:
            cnt = cnt + 1
    return(cnt) #prints the amount of letters

File = open(input('Enter File Name: ')) # Collects and opens a file by name
UserLetter = input('Enter Letter: ') # collects a user letter
Total = 0 #Sets starting total to 0

for Line in File: #creates loop to find lines in the user file
    Total = Total + count(Line,UserLetter) #counts the lines in the file and sets it to total

print(str(Total) + ' ' + UserLetter + ' found in file') #prints the total(as a string) and UserLetter