# Import pyttsx3 - https://pypi.org/project/pyttsx3/ 
import pyttsx3

# Define pyttsx3 objexct
pyobj = pyttsx3.init()

# Set voice used 0 for male 1 for female
voices = pyobj.getProperty('voices') 
pyobj.setProperty('voice', voices[1].id) 

# Open, read and close file - \\ for linux / for windows path
fo = open ('C:/Users/Hal/Desktop/speech.txt','r')
ip = fo.read()
fo.close()

# Set speed playback
pyobj.setProperty('rate', 150)

# Set volume level 0.0 to 1.0
pyobj.setProperty('volume', 1.0)

# Text to voice - edit text to change output
# pyobj.say('Welcome to Python Programming')

# Save text to mp3 - edit file name and or location
# pyobj.save_to_file(ip, 'C:/Users/Hal/Desktop/sample.mp3')

pyobj.runAndWait()