0bulkSoapExporter iterates through a number of light locations, soap colors and soap transmission levels. It calls the 1rendererExporter repeadly to do so.

1rendererExporter uses the 2soapSceneGenerator function to generate a scene, then exports an image to file. 

2soapSceneGenerator calls the resetSceneFunction, lightGenerator, wallAndFloorGenerator and soapGenerator functions to create a scene. 
