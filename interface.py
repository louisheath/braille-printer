import tkinter
from tkinter import *
import os

# Edit this to the path of your blender package (more info in README.md)
# e.g. blenderLocation = "/Applications/blender-2.79-macOS-10.6/blender.app/Contents/MacOS/blender"
blenderLocation = "blender"

#-------------------------------------------------------------------------------
#
#   Interface
#
#-------------------------------------------------------------------------------

# window
w = tkinter.Tk()
w.title("3D Braille Printer")
w.geometry("300x135")

# function to run when input text is ready
def submitInput ():
    os.system(blenderLocation + " --background  output.blend --python blend.py -- " + inEntry.get())
    clearButton['state'] = NORMAL
    inButton['state'] = DISABLED

# function that reacts to 'return' key
def onEnter (event):
    submitInput()

def clearFile ():
    os.system(blenderLocation + " --background  output.blend --python clear.py")
    clearButton['state'] = DISABLED
    inButton['state'] = NORMAL

# set 'return' key to always react with onEnter function
w.bind('<Return>', onEnter)

# label requesting input
inLabel = Label (w, text="Enter text to convert to braille:")

# text input field
inEntry = Entry (w)

# submit button for when input text is ready
inButton = Button (w, text="Convert", command=submitInput)

# label to indicate output area
clearLabel = Label (w, text="Clear .blend file:")

# button for user to retrieve processed blender file
clearButton = Button (w, text="Clear", state=DISABLED, command=clearFile)

inLabel.pack()
inEntry.pack()
inButton.pack()
clearLabel.pack()
clearButton.pack()
w.mainloop()
