#this function creates an object (the soap) based on colour and transmission arguments within the scene. 

import bpy
import random

def generateSoap(colour, transmission): 
    
    ### create empty object to hold texture coords, from Kate's https://github.com/tinyrobots/shared_notebooks/blob/main/blender_object_generation_example_script.py
    empty = bpy.ops.object.empty_add(location=(0,0,0))
    
    ### create object
    bpy.ops.mesh.primitive_cube_add() #adds a cube

    obj = bpy.context.active_object #select active object (cube)
    
    #randomly define the size of the objects within the specified bounds
    xSize = random.uniform(13.0,17.0)
    ySize = random.uniform(18.0,22.0)
    zSize = random.uniform(7.0,10.0)
    obj.dimensions = (xSize, ySize, zSize) 

    #apply modifiers to shape the soap

    #add bevel modifier
    bevel_modifier = obj.modifiers.new(name="Bevel", type='BEVEL')
    bevel_modifier.width = 0.1  # Set the bevel width
    bpy.ops.object.modifier_apply({"object": obj}, modifier="Bevel")

    #apply subdivision surface modifier which splits mesh into smaller faces to smooth apearance 
    mod_subsurf = obj.modifiers.new("Modifier",'SUBSURF') 
    modLevels = 4
    mod_subsurf.levels = modLevels #change viewport surface subs
    mod_subsurf.render_levels = modLevels #change render surface subs
    bpy.ops.object.modifier_apply({"object": obj}, modifier="Subdivision Surface")

    #random modifiers for shape deformation, from Kate's https://github.com/tinyrobots/shared_notebooks/blob/main/blender_object_generation_example_script.py 
    mod_disp = obj.modifiers.new("My Displacement","DISPLACE")
    #link texture coords to empty object
    mod_disp.texture_coords = "OBJECT"
    mod_disp.texture_coords_object = bpy.data.objects["Empty"]
    bpy.data.objects["Empty"].location[0] = random.uniform(-10.0,10.0)
    bpy.data.objects["Empty"].location[1] = random.uniform(-10.0,10.0)
    bpy.data.objects["Empty"].location[2] = random.uniform(-10.0,10.0)

    new_text = bpy.data.textures.new("Micro Perterbations","MUSGRAVE")
    new_text.noise_basis = "VORONOI_F1"
    new_text.musgrave_type = "RIDGED_MULTIFRACTAL"
    new_text.noise_scale = 0.005
    new_text.lacunarity = 1.0
    new_text.intensity = 1.0
    mod_disp.strength = 0.005
    
    # assign this texture to displacement modifier
    mod_disp.texture = new_text
    
    #smooth the shading
    bpy.ops.object.shade_smooth() 

    #move the object to position it on the floor https://blender.stackexchange.com/questions/22888/how-to-place-any-object-on-the-floor-of-a-scene
    mx = obj.matrix_world
    minz = min((mx @ v.co)[2] for v in obj.data.vertices)
    mx.translation.z -= minz
    
    ###create material 
    cube_mat = bpy.data.materials.new("Cube Mat")
    cube_mat.use_nodes = True 
    nodes = cube_mat.node_tree.nodes #shortcut

    #retrive the default material output and principled BSDF as variables 
    material_output = nodes.get("Material Output") 
    Principled_BSDF = nodes.get("Principled BSDF")

    Principled_BSDF.inputs[0].default_value = colour #change colour
    Principled_BSDF.inputs[2].default_value = [.1, .1, .1] #subsurface radius' for r g and b values 
    Principled_BSDF.inputs[3].default_value = colour #subsurface colour, same as base colour
    Principled_BSDF.inputs[4].default_value = 1.5 #subsurface IOR
    Principled_BSDF.inputs[9].default_value = .1 #change roughness
    Principled_BSDF.inputs[16].default_value = 3
    Principled_BSDF.inputs[17].default_value = transmission #change transmission
    
    new_link = cube_mat.node_tree.links.new(Principled_BSDF.outputs[0],material_output.inputs[0])
    
    obj.data.materials.append(cube_mat) #apply the material to the soap object