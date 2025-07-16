"""
Object Material Splitter for Maya

This script is designed for Autodesk Maya. It separates objects based on their shading groups (materials). 
For each unique material applied to an object, a duplicate of the object is created with only the 
faces associated with that material.

Author: Guy Micciche
"""

from maya import cmds

def getSGs(in_obj_name):
    """
    Retrieve shading groups associated with the given object.
    
    Args:
    - in_obj_name (str): Name of the object.
    
    Returns:
    - list[str]: List of shading groups.
    """
    
    # Check if the object exists in the scene
    if not cmds.objExists(in_obj_name): return []
    
    # Initialize an empty set to store unique shading engines (materials)
    shadingEngines = set()
    
    # Get shape nodes related to the object
    ShapeNodes = cmds.listRelatives(in_obj_name, shapes=1, children=1) or []
    if not ShapeNodes: return []
    
    # Loop through each shape node to find connected shading engines
    for shape in ShapeNodes:
        dest = cmds.listConnections(shape, source=False, plugs=False, destination=True, type="shadingEngine")
        if not dest: continue
        shadingEngines.update(dest)
        
    return list(shadingEngines)

def sepMat(objectName, suffixName = "_Splitted"):
    """
    Separate the object based on its materials.
    
    Args:
    - objectName (str): Name of the object to be separated.
    - suffixName (str, optional): Suffix for the parent group of separated objects. Defaults to "_Splitted".
    """
    
    # Get shading groups (materials) associated with the object
    shadingGroups = getSGs(objectName)
    
    # If there's only one material or none, no need to separate
    if len(shadingGroups) <= 1: return

    # Create a parent node for the separated objects
    nodeParentName = objectName + suffixName
    if not cmds.objExists(nodeParentName): 
        nodeParentName = cmds.group(empty=1, n=nodeParentName)
    
    # Loop through each shading group to create duplicates of the object
    for curMatSg in shadingGroups:
        
        # Name the duplicate based on the original object and shading group
        cloneObjName = objectName + "_" + curMatSg
        
        # Duplicate the object and parent it to the nodeParentName
        cloneObjName = cmds.duplicate(objectName, n=cloneObjName)[0]
        cloneObjName = cmds.parent(cloneObjName, nodeParentName)[0]
        
        # Create sets for faces to determine which ones to keep based on the shading group
        polyFacesSet = cmds.sets(cloneObjName + '.f[0:]')
        sgFacesSet = cmds.sets(cmds.sets(curMatSg, un=polyFacesSet))
        
        # Delete unnecessary faces that don't belong to the current shading group
        cmds.delete(cmds.sets(polyFacesSet, subtract=sgFacesSet), polyFacesSet, sgFacesSet)
    
    # Delete the original object after creating all duplicates
    cmds.delete(objectName)

def runScript(*args, **kw):
    """
    Execute the material separation on selected objects in Maya.
    """
    
    # Get the current selection in Maya
    selection = cmds.ls(sl=True, objectsOnly=True, noIntermediate=True)
    
    # Loop through each selected object and try to separate based on materials
    for sel in selection:
        try:
            sepMat(sel)
        except:
            continue
        
    # Clear the selection after processing
    cmds.select(cl=True)

if __name__ == "__main__":
    runScript()
