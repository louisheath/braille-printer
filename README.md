# braille-printer

braille-printer is our solution to the CSS & Bloomberg Accessibility Hackathon. It is a python program with a simple GUI which takes a string and produces a braille sign for 3D printing.

The aim of the solution is to simplify the process of producing braille signs for use in local businesses, schools etc, as otherwise they are usually custom ordered online.

Developed in Python using Tkinter and Blender by Louis Heath, Muntazim Ali, [Miklos Borsi](https://github.com/borsimiklos) and Kenny Lomas.

### Running

To run braille-printer you must have python3 and blender installed. 

On Mac, use command `python3 interface.py` in the terminal which start the GUI.

`interface.py` runs the terminal command `blender --background --python blend.py -- <arg>`, so an alias may be necessary for `blender` on some machines.
