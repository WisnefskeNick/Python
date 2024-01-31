# Nicholas Wisnefske
# CS 125
# 3/9/2023

NameScores = dict() # creates dictonary
while True: #starts loop
    Name = input('Enter Name: ') #asks for names
    if Name == 'done': #when done is typed break loop
        break
    Score = input('Enter Score: ') # asks for scores
    NameScores[Name] = Score # adds scores to dict

t=list(NameScores.items()) #lists all items in dict
t.sort() # sorts all of the items

for key,val in t: #prints ouput as key first followed by value
    print (key,val)

StudentName = input('Display Score for: ') #asks for a name
for key,val in t: #finds and prints students score based on key
    if key == StudentName:
        print (val)