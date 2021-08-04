# Import pyttsx3 - https://pypi.org/project/pyttsx3/ 
import pyttsx3

# Define pyttsx3 objexct
pyobj = pyttsx3.init()

# Set voice used 0 for male 1 for female
voices = pyobj.getProperty('voices') 
pyobj.setProperty('voice', voices[0].id) 

# # Open, read and close file - \\ for linux / for windows path
# fo = open ('C:/Users/Hal/Desktop/speech.txt','r')
# ip = fo.read()
# fo.close()

# Set speed playback
pyobj.setProperty('rate', 150)

# Set volume level 0.0 to 1.0
pyobj.setProperty('volume', 1.0)

# Text to voice - edit text to change output
# pyobj.say('''
# Welcome to Python Programming. 

# Python is an interpreted high-level general-purpose programming language. 

# Python's design philosophy emphasizes code readability with its notable use of significant indentation. 
# Its language constructs as well as its object-oriented approach aim to help programmers write clear 
# logical code for small and large-scale projects.

# Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms,
# including structured (particularly, procedural), object-oriented and functional programming. 
# Python is often described as a "batteries included" language due to its comprehensive standard library.

# Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language,
# and first released it in 1991 as Python 0.9.0.

# Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using
# reference counting. 

# Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible,
# and much Python 2 code does not run unmodified on Python 3. Python 2 was discontinued with version 2.7.18 in 2020.

# Python consistently ranks as one of the most popular programming languages.

# ''')

# Save text to mp3 - edit file name and or location
pyobj.save_to_file(zip, 'C:/Users/Hal/Desktop/sample.mp3')

pyobj.runAndWait()