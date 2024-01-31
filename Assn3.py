# Nicholas Wisnefske
# CS125
# 2/21/23

hrs = input('Enter Hours ')
h = float(hrs)
ot = 0

rate = input('Enter Hourly Rate ')
r = float(rate)

if h > 40:
    ot = h - 40
    h = 40

tot = (h * r) + (ot * r * 1.5)
print(tot)