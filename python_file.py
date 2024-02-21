from pushbullet import Pushbullet

API_KEY = "o.app55lfFlDcQBOLzu3"

# API KEY IS CHANGED IN THIS CODE FOR PRIVACY REASONS

file = "/Users/mac/Desktop/IEEE/tx.txt"

with open(file, mode='r') as f:
    text = f.read()

pb = Pushbullet(API_KEY)

push = pb.push_note("REMINDER",text)

#TO GET THE NOTIFICATION EVERYDAY
# WE USE PYTHON ANYWHERE

