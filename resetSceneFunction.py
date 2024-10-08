#this function resets the scene by deleting objects, lights and cameras and setting the camera location. 

import bpy

def resetScene():
 
    # Clear all objects, including meshes, lights, and cameras
    # Delete meshes 
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Delete lights
    bpy.ops.object.select_by_type(type='LIGHT')
    bpy.ops.object.delete()

    # Delete cameras
    bpy.ops.object.select_by_type(type='CAMERA')
    bpy.ops.object.delete()

    #create and toggle camera view
    # Set the camera location and rotation
    camera_location = (40, -40, 15)  
    camera_rotation = (1.4, 0, .8)  

    # Add a new camera
    bpy.ops.object.camera_add(location=camera_location, rotation=camera_rotation)

    # Set the scene camera to the newly added camera
    scene = bpy.context.scene
    scene.camera = bpy.context.object

    # Update the scene
    bpy.context.view_layer.update()

    #this is not necessary for the export, but is useful when testing/previewing by snaping to the 3d viewport
    for area in bpy.context.screen.areas: #loop through areas in current blender scene
        if area.type == 'VIEW_3D': #check if current is view 3d
            override = bpy.context.copy() #create copy of current situation (with 3d view)
            override['area'] = area #set area to current 3d view, specifies where operator will be executed 
            bpy.ops.view3d.object_as_camera(override, 'INVOKE_DEFAULT') #sets active view to the camera view in view area
            
