#produces in bulk scenes combined from lists of light location, soap colour and soap transmission

import bpy

#in this first section, the permutations of light location, soap color and transmission are set
        
#set light locations on the y axis and associated names
lightLocations = (0, 20)
lightNames = ('Center', 'Right')
assert len(lightLocations) == len(lightNames), f"Light locations and names not equal in length"

#set the soap colors and associated names
soapColors = ([0.3, 0.3, 1.0, 1.0],[0.3, 1.0, 0.3, 1.0])
colorNames = ('Blue', 'Green')
assert len(soapColors) == len(colorNames), f"Colours and names not equal in length"
 
#set the soap transmission levels and associated names)
soapTransmissions = (3.0, 0.5)
transmissionNames = ('Translucent', 'Opaque')
assert len(soapTransmissions) == len(transmissionNames), f"Transmissions and names not equal in length"

index = 0 #this index is used at the start of file names

#the nested loops then iterate though each combination of light location, soap color and transmission; this is passed into the render export function to produce an image for each combination. 

for LightIndex, lightLocation in enumerate(lightLocations): 
    
    for colourIndex, soapColor in enumerate(soapColors): 
            
            for transmissionIndex, soapTransmission in enumerate(soapTransmissions): 
                
                #create name vars based on current index of light location, soap colour and transmission
                lightName = lightNames[LightIndex]
                colorName= colorNames[colourIndex]
                transmissionName = transmissionNames[transmissionIndex]
                fileName = f"{index}soap{lightName}{colorName}{transmissionName}" #creates a file name for the renderExport function
                index += 1 #increase the filename index for the next file
                
                #call the sceneGenerator function to create the scene
                rendererExporter = bpy.data.texts["1rendererExporter"].as_module()
                rendererExporter.renderExport(lightLocation, soapColor, soapTransmission, fileName)