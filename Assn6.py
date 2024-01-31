# Nicholas Wisnefske
# CS 125
# 3/9/2023

def count(word,char): # creates count class
    cnt = 0 #sets count to 0
    for letter in word: # creates a loop to find how many letter +1 there are in a word
        if letter == char:
            cnt = cnt + 1
    print(cnt) #prints the amount of letters

UserWord = input('Enter Word: ') # collects User Word
UserChar = input('Enter Letter: ') # collects User Letter
count(UserWord,UserChar) # calls upon the count function