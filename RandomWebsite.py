
import webbrowser
import time 
import random 

while True:
    sites = random.choice(['www.youtube.com/watch?v=dQw4w9WgXcQ, www.youtube.com/watch?v=rTgj1HxmUbg'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    second = random.randrange(5, 100)
    time.sleep(second)