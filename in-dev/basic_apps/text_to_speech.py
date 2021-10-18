# Import pyttsx3 - https://pypi.org/project/pyttsx3/
import pyttsx3

# Define pyttsx3 object
pyobj = pyttsx3.init()

# Set voice used male = 0 - female = 1
voices = pyobj.getProperty('voices')
pyobj.setProperty('voice', voices[1].id)

# # Open, read and close file - \\ for linux / for windows path
# fo = open ('C:/Users/Hal/Desktop/speech.txt','r')
# ip = fo.read()
# fo.close()

# Set speed playback
pyobj.setProperty('rate', 150)

# Set volume level 0.0 to 1.0
pyobj.setProperty('volume', 1.0)

# Text to speech - edit text to change output
pyobj.say('''
Welcome to Python Programming. 

Python is an interpreted high-level general-purpose programming language. 

Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
Its language constructs as well as its object-oriented approach aim to help programmers write clear 
logical code for small and large-scale projects.
''')

# Save text to mp3 - edit file name and or location
# pyobj.save_to_file(ip, 'C:/Users/Hal/Desktop/sample.mp3')

pyobj.runAndWait()
