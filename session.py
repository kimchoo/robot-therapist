from facecam import *
import time

break_condition = False
mood_reactions = {
    "Sad": "Have a nice day!",
    "Lonely": "I your friend.",
    "Happy": "Your on fire!!",
    "Focused": "Good work.",
    "Bored": "Read a good book...."
    } 

wait_time = 5 #In minutes

while break_condition is False:

    time.sleep(60*wait_time)
    face =  snap()
    react = mood_reactions[mood_detect(face)]
    create_notification(react)
