#this function generates a single light based on an argument regarding the light's location on the y axis.  

import bpy

def generateLight(y_location):

    # Add a point light, note the y axis location is the argument above. 
    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(25, y_location, 15))

    # Access the active object (which is the newly added light)
    light_object = bpy.context.active_object

    # Set light properties (adjust as needed)
    light_object.data.energy = 30000.0  # Light intensity
    light_object.data.color = (1, 1, 1)  # Light color