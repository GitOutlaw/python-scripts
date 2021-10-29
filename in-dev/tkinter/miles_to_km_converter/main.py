from tkinter import *


def convert_distance():
    '''Convers miles to kilometers. Conversion factor 1.60934'''
    # Use to test button.
    print("I got clicked")
    # Conversion factor.
    miles = float(input.get()) * 1.6
    print(miles)
    result_label.config(text=miles)


# Tkinter window.
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

# Equal Label.
equal_label = Label(text="I am a Label", font=("Arial", 16, "bold"))
equal_label.config(text="is equal to")
equal_label.grid(column=0, row=1)

# Results label.
result_label = Label(text="I am a Label", font=("Arial", 16, "bold"))
result_label.config(text=0)
result_label.grid(column=1, row=1)

# Kilometer label.
km_label = Label(text="I am a Label", font=("Arial", 16, "bold"))
km_label.config(text="Km")
km_label.grid(column=2, row=1)

# Entry.
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

# Miles label.
miles_label = Label(font=("Arial", 16, "bold"))
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# Button
button = Button(text="Calculate", command=convert_distance)
button.grid(column=1, row=2)

# Keep window open.
window.mainloop()
