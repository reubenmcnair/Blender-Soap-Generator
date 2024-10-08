import bpy
from math import radians

def GenerateWallsAndFloor():
    
    ##create material for floor 
    floorMat = bpy.data.materials.new("Floor Mat")

    floorMat.use_nodes = True #specify that we are using nodes
    nodes = floorMat.node_tree.nodes #shortcut 

    #generate the required nodes and edit any values/elements
    material_output = nodes.get("Material Output") #find the material output node and save as var
    textureCoordinate = nodes.new(type="ShaderNodeTexCoord") #add a node 
    
    mapping = nodes.new(type="ShaderNodeMapping")
    mapping.inputs[3].default_value = [1.0, -0.2, 1.0]
    
    noiseTexture = nodes.new(type="ShaderNodeTexNoise")
    noiseTexture.inputs[1].default_value = 50.0
    noiseTexture.inputs[2].default_value = 25.0
    noiseTexture.inputs[3].default_value = 0.75

    colourRamp = nodes.new(type="ShaderNodeValToRGB")
    colourRamp.color_ramp.elements[0].position = 0.25 #change distance of first node along color ramp
    colourRamp.color_ramp.elements[0].color = (0.7, 0.25, 0.028, 1) #change the first node RGBA
    
    colourRamp.color_ramp.elements[1].position = (0.75) #change distance of second node along color ramp
    colourRamp.color_ramp.elements[1].color = (0.7, 0.5, 0.3, 1) #change the second node RGBA
    
    Principled_BSDF = nodes.get("Principled BSDF") #find the Principled_BSDF node
    Principled_BSDF.inputs[7].default_value = 0.5 #change specular
    Principled_BSDF.inputs[8].default_value = 0.5 #change specular tint
    Principled_BSDF.inputs[9].default_value = 0.5 #change roughness
    Principled_BSDF.inputs[17].default_value = 0 #change transmission
    
    #link all the nodes up
    links = floorMat.node_tree.links #create reference to links via var
    
    links.new(textureCoordinate.outputs[2],mapping.inputs[0])
    links.new(mapping.outputs[0],noiseTexture.inputs[0])
    links.new(noiseTexture.outputs[0],colourRamp.inputs[0])
    links.new(colourRamp.outputs[0],Principled_BSDF.inputs[0])
    links.new(Principled_BSDF.outputs[0],material_output.inputs[0]) #link the output of Principled_BSDF to the input of Material Output 

    ##create material for walls 
    wallMat = bpy.data.materials.new("Walls Mat")

    wallMat.use_nodes = True #specify that we are using nodes
    nodes = wallMat.node_tree.nodes #shortcut 

    #generate the required nodes and edit any values/elements
    material_output = nodes.get("Material Output") #find the material output node and save as var
    textureCoordinate = nodes.new(type="ShaderNodeTexCoord") #add a node 
    
    mapping = nodes.new(type="ShaderNodeMapping")
    mapping.inputs[3].default_value = [1.0, 1.0, 1.0]
    
    noiseTexture = nodes.new(type="ShaderNodeTexNoise")
    noiseTexture.inputs[1].default_value = 5000.0
    noiseTexture.inputs[2].default_value = 2500.0
    noiseTexture.inputs[3].default_value = 0.75

    colourRamp = nodes.new(type="ShaderNodeValToRGB")
    colourRamp.color_ramp.elements[0].position = 0.25 #change distance of first node along color ramp
    colourRamp.color_ramp.elements[0].color = (0.75, 0.8, 0.75, 1) #change the first node RGBA
    
    colourRamp.color_ramp.elements[1].position = (0.75) #change distance of second node along color ramp
    colourRamp.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1) #change the second node RGBA
    
    Principled_BSDF = nodes.get("Principled BSDF") #find the Principled_BSDF node
    Principled_BSDF.inputs[7].default_value = 0.5 #change specular
    Principled_BSDF.inputs[8].default_value = 0.5 #change specular tint
    Principled_BSDF.inputs[9].default_value = 0.5 #change roughness
    Principled_BSDF.inputs[17].default_value = 0 #change transmission
    
    #link all the nodes up
    links = wallMat.node_tree.links #create reference to links via var
    
    links.new(textureCoordinate.outputs[2],mapping.inputs[0])
    links.new(mapping.outputs[0],noiseTexture.inputs[0])
    links.new(noiseTexture.outputs[0],colourRamp.inputs[0])
    links.new(colourRamp.outputs[0],Principled_BSDF.inputs[0])
    links.new(Principled_BSDF.outputs[0],material_output.inputs[0]) #link the output of Principled_BSDF to the input of Material Output 

      
    
    ###Create floor and walls
    wallSize= 100
    
    # Create the floor plane
    bpy.ops.mesh.primitive_plane_add(size=wallSize, enter_editmode=False, align='WORLD', location=(0, 0, 0))

    #Scale the floor plane
    bpy.context.active_object.scale = (1, 1, 0.1)

    obj = bpy.context.active_object #var from active object

    obj.data.materials.append(floorMat)


    ##Create first wall (left)
    bpy.ops.mesh.primitive_plane_add(size=wallSize, enter_editmode=False, align='WORLD', location=(-50, 0, 50))

    #Scale the first wall
    bpy.context.active_object.scale = (1, 1, 1)

    # Rotate the floor plane
    bpy.context.active_object.rotation_euler = (0, radians(90), 0)

    obj = bpy.context.active_object #var from active object

    #link wall material to object 
    obj.data.materials.append(wallMat)


    ##Create second wall(right)
    bpy.ops.mesh.primitive_plane_add(size=wallSize, enter_editmode=False, align='WORLD', location=(0, 50, 50))

    # Scale the second wall
    bpy.context.active_object.scale = (1, 1, 1)

    # Rotate the floor plane
    bpy.context.active_object.rotation_euler = ( radians(90), 0, 0)

    obj = bpy.context.active_object #var from active object

    #link wall material to object 
    obj.data.materials.append(wallMat)
