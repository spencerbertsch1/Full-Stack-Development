# Planning a break
# Udacity OOD python course
import webbrowser
import time

print("Program start time:", (time.ctime()))

for i in range(3):
    time.sleep(2) # time.sleep(2*60*60) <-- sleeps for 2 hours!
    webbrowser.open('https://www.google.com/search?q=cats&oq=cats&aqs=chrome..69i57j69i60l2j69i65l2j69i60.659j0j1&sourceid=chrome&ie=UTF-8')
    print("Break number:", i)



#Same code using a while loop
number_of_breaks = 2
current_break = 0

while(current_break <= number_of_breaks):
    time.sleep(2)
    webbrowser.open('https://www.google.com/search?q=cats&oq=cats&aqs=chrome..69i57j69i60l2j69i65l2j69i60.659j0j1&sourceid=chrome&ie=UTF-8')
    print("Break number:", current_break+1)
    current_break = current_break + 1
