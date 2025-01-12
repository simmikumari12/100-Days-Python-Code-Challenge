from time import localtime, strftime

h = strftime("%H", localtime())
hour = int(h)

if 4 <= hour < 12:
    print("Have a Good Morning!")
elif 12 <= hour < 17:
    print("Have a Good Afternoon!")
elif 17 <= hour < 19:
    print("Have a Good Evening!")
elif 19 <= hour < 24:
    print("Have a Good Night!")
elif 0< hour < 4:
    print("Go to Bed!")
else:
    print("Have a good time")
