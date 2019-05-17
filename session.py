from facecam import *
from sys_notifications import *
from emotion_detection import *
import time

mood_reactions = {
    "Sad": "Have a nice day!",
    "Lonely": "I your friend.",
    "Happy": "Your on fire!!",
    "Focused": "Good work.",
    "Bored": "Read a good book...."
    }

wait_time = 5 #In minutes

run_condition = True
step = 0 

while run_condition:
    
    time.sleep(.1)    #(60*wait_time)
    
    face, grey_img =  cam_snap()

    react = mood_reactions[mood_detect(face, grey_img)]
    
    create_notification(react)

    if step >= 10: run_condition = False

    step += 1
