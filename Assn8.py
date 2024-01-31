# Nicholas Wisnefske
# CS 125
# 3/9/2023

NumList = [] #sets array to numlist

while True: # creates a loop
    UserInput = input('Enter a number: ') #collects number from user
    if UserInput == 'done': #when user types done loop end
        break #splits up the if and else statements

    elif UserInput != int:
        print('enter an integer')

    else:
        NumList.append(UserInput) #prints out the userInput until done is typed

print('Max: ', max(NumList)) #prints the max number
print('Min: ', min(NumList)) #prints the min number