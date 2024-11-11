import maya.cmds as cmds
import maya.app.renderSetup.model.renderSetup as renderSetup

# Get a list of selected objects
selected_objects = cmds.ls(selection=True)

# Iterate over each selected object
for obj in selected_objects:
    # Create a new render layer and rename it to the object name plus "_RL"
    layer_name = obj + "_RL"
    layer = renderSetup.instance().createRenderLayer(layer_name)

    # Create a new collection and rename it to the object name plus "_COL"
    collection_name = obj + "_COL"
    collection = layer.createCollection(collection_name)

    # Add the object to the collection
    collection.getSelector().staticSelection.set([obj])
