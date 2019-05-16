from facecam import *
import time

#Psuedo Code for a robo-therapist:
#   using the snap function the camera checks for your face.
#   using the returned face image, the hypothetical mood_detect method returns your mood based on your face
#   the returned mood is used as the key to direct the create_notification

#Note: the code is constantly running but only proceeds every 5 minutes

#Note: the break condition would changed based on the user closing the progam, hardware limits, or if the computer goes to sleep.

break_condition = False

mood_reactions = {

    "Sad": "Have a nice day!",
    "Lonely": "I your friend.",
    "Happy": "Your on fire!!",
    "Focused": "Good work.",
    "Bored": "Read a good book....",
    }

wait_time = 5 #In minutes

while break_condition is False:

    time.sleep(60*wait_time)
    face =  snap()
    create_notification(mood_reactions[mood_detect(face)])
