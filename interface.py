#!/usr/local/bin/python

import tkinter
from tkinter import *
import engToBraille


# window
w = tkinter.Tk()
w.title("3D Braille Printer")
w.geometry("300x135")

# label requesting input
inLabel = Label (w, text="Enter text to convert to braille:")
inLabel.pack()

# text input field
inEntry = Entry (w)
inEntry.pack()

# function to run when input text is ready
def submitInput ():
    braille = engToBraille.translate(inEntry.get())
    for b in braille:
        print(b)
    # subprocess.call("blender --background --python myscript.py")
    outButton['state'] = NORMAL

# function that reacts to 'return' key
def onEnter (event):
    submitInput()

# set 'return' key to always react with onEnter function
w.bind('<Return>', onEnter)

# submit button for when input text is ready
inButton = Button (w, text="Submit", command=submitInput)
inButton.pack()

# label to indicate output area
outLabel = Label (w, text="Processed blender file:")
outLabel.pack()

# button for user to retrieve processed blender file
outButton = Button (w, text="Copy Blender File", state=DISABLED)
outButton.pack()

w.mainloop()
