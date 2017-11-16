# braille-printer

braille-printer is our solution to the CSS & Bloomberg Accessibility Hackathon. It is a python program with a simple GUI which takes a string and produces a braille sign for 3D printing.

The aim of the solution is to simplify the process of producing braille signs for use in local businesses, schools etc, as otherwise they are usually custom ordered online.

Developed in Python using Tkinter and Blender by Louis Heath, Muntazim Ali, [Miklos Borsi](https://github.com/borsimiklos) and Kenny Lomas.

### Running

To run braille-printer you must have python3 and blender installed.

Type `python3 interface.py` in your terminal to get it started.

We didn't encounter any problems running braille-printer on Ubuntu, however on Mac you'll likely want to change the alias for blender, which by default is hard-coded as `blender`

1. Navigate to your blender installation folder (perhaps in "Applications")
2. Right click on the blender app and select "Show Package Contents"
3. Burrow down to Contents->MacOS->blender
4. Copy the file path of the blender executable
5. Paste it in-between the quote marks on line 8 of `blender.py`
