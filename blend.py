import bpy
import sys
import os

argv = sys.argv
argv = argv[argv.index("--") + 1:]

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )

import engToBraille

#input = [[1,0,1,1,0,0],[1,0,0,1,0,0],[1,0,1,0,1,0],[1,0,1,0,1,0],[1,0,0,1,1,0],[0,0,0,0,0,0],[0,1,1,1,0,1],[1,0,0,1,1,0],[1,0,1,1,1,0],[1,0,1,0,1,0],[1,1,0,1,0,0]]
input = engToBraille.translate(argv[0])

def createBraille(my_bool,x,y):
    #create cube
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(x, y, 0.5), rotation=(1.57, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    #change dimensions of cube to (1, 1, 1)
    bpy.ops.transform.resize(value=(0.25, 0.25, 0.125), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    if(my_bool):
        #add cylinder
        bpy.ops.mesh.primitive_cylinder_add(radius=0.125, depth=0.125, view_align=False, enter_editmode=False, location=(x, y, 0.625), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    
        
        
# when moving the cuboid = bpy.ops.transform.translate(value=(0.140409, 4.04676, 0.14149), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

initialX = 0
initialY = -8
letterCount = 0
lineCount = 0

for letter in input:
    letterCount += 1
    for i in range(0,3):
        createBraille(letter[2*i],initialX,initialY)
        createBraille(letter[2*i+1],initialX,initialY+0.5)
        createBraille(0,initialX,initialY+1)
        initialX += 0.5
    initialY += 1.5
    if letterCount == 6:
        letterCount = 0
        initialX = 1.5*lineCount
        initialX += 1.5
        lineCount += 1
        initialY = -8
    else:
        initialX = 1.5*lineCount
        
bpy.ops.wm.save_as_mainfile()

