from facecam import *
import time
#Psuedo Code for a robo-therapist:
#   using the snap function the camera checks for your face.
#   using the returned face image, the hypothetical mood_detect method returns your mood based on your face
#   the returned mood is used as the key to direct the create_notification

#Note: the code is constantly  but only proceeds every 5 minutes
#Note: the break condition would changed based on the user closing the progam, hardware limits, or if the computer goes to sleep.

break_condition = False #Alter the break_condition based on the conditions to shut down the program
mood_reactions = {
    "Sad": "Have a nice day!",
    "Lonely": "I your friend.",
    "Happy": "Your on fire!!",
    "Focused": "Good work.",
    "Bored": "Read a good book...."
    } #Using a dictionary to link the user mood to an appropriate reaction

wait_time = 5 #In minutes

while break_condition is False:

    time.sleep(60*wait_time) #Making it so the program will run constantly but only compute/proceed every X minute.
    face =  snap() #Put the faces of the user into a variable
    react = mood_reactions[mood_detect(face)] #Look up a reaction to the user mood.
    create_notification(react) #Apply the mood the notification functionrunning
