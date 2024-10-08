#This function amalgomates functions which reset the scene and generate lights, camera and objects 

def generateScene(lightLocation, soapColor, soapTransmission):

    import bpy

    #import internal text files for required functions 
    resetSceneFunction = bpy.data.texts["resetSceneFunction"].as_module()
    lightGenerator = bpy.data.texts["lightGenerator"].as_module()
    wallAndFloorGenerator = bpy.data.texts["wallAndFloorGenerator"].as_module()
    soapGenerator = bpy.data.texts["soapGenerator"].as_module()

    #call functions to generate scene

    resetSceneFunction.resetScene() #reset the scene by deleting objects, lights and cameras (important when looping across permutations). Note this also sets the camera location.  

    lightGenerator.generateLight(lightLocation) #add a point light

    wallAndFloorGenerator.GenerateWallsAndFloor() #add walls and floor
                        
    soapGenerator.generateSoap(soapColor, soapTransmission) #add the soap object to the scene

