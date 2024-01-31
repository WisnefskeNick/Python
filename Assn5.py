# Nicholas Wisnefske
# CS 125
# 2/28/23

Total = 0
Count = 0

UserInput = input('Enter a number: ')

while UserInput != 'done':
    try:
        Total = Total + float(UserInput)
        Count = Count + 1
    except:
        print('Invalid')
    UserInput = input('Enter another number: ')

Avg = Total/Count
print('Total: ' + str(Total) + '\n')
print('Count: ' + str(Count) + '\n')
print('Average: ' + str(Avg) + '\n')