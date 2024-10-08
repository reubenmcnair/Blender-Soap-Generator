#calls the scene generator function to produce a scene, then exports an image. 

import bpy 

def renderExport(lightLocation, soapColor, soapTransmission, fileName):

    #set render engine, and time limit per render (seconds), denoise on
    bpy.data.scenes["Scene"].render.engine = 'CYCLES'
    bpy.data.scenes["Scene"].cycles.time_limit = 10
    bpy.data.scenes["Scene"].cycles.use_denoising = True


    #call the sceneGenerator function to create the scene
    soapSceneGenerator = bpy.data.texts["2soapSceneGenerator"].as_module()
    soapSceneGenerator.generateScene(lightLocation, soapColor, soapTransmission) #run the scene generation

    #set the file path for the output image
    output_path = f"/Users/reuben/Documents/Blender/Soap Gen 2/Exported Images/{fileName}.jpg"

    # Set the resolution and output format
    bpy.context.scene.render.resolution_x = 1920  # Set your desired resolution
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.image_settings.file_format = 'JPEG'

    #render the image
    bpy.ops.render.render(write_still=True)

    #save the rendered image
    bpy.data.images['Render Result'].save_render(filepath=output_path)