# Nicholas Wisnefske
# CS 125
# 3/9/2023

NameScores = dict() #sets the dictonary to namescores
while True: #creates loop
    Name = input('Enter Name: ') #asks user for a name
    if Name == 'done': #when done is enter break the loop
        break
    Score = input('Enter Score: ') #asks for score
    NameScores[Name] = Score #adds score to dictonary

print(len(NameScores)) #prints the number of entries
print(NameScores) #prints all of the entries