# Nicholas Wisnefske
# CS 125
# 2/27/2023

def computegrade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'


userscore=float(input('What is your score? '))
grade=computegrade(userscore)
print(grade)