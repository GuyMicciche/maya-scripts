# Author: Guy Micciche
# Description: This script is designed to perform UV unwrapping on selected objects within Maya. 
# It operates by detecting UV border edges, detaching them, and then adjusting the vertices of the new object 
# based on the UVs and bounding box dimensions.

import maya.cmds as cmds

def UV_unwrap(object, axisPlane):
    # Evaluating polygonal components and bounding box of the object
    PolyValues = cmds.polyEvaluate(object, vertex=True, edge=True, face=True, uv=True, shell=True, area=True)
    PolyValuesBounding = cmds.polyEvaluate(object, boundingBox=True)

    NumVertex = PolyValues["vertex"]
    NumEdge = PolyValues["edge"]
    UV_BorderEdge = []
    
    # Identifying UV border edges
    for i in range(NumEdge):
        uvMap = cmds.polyListComponentConversion(object + ".e[" + str(i) + "]", fromEdge=True, toUV=True)
        UV_flatten = cmds.ls(uvMap, flatten=True)
        
        if len(UV_flatten) > 2:
            UV_BorderEdge.append(i)

    # Selecting the detected UV border edges
    cmds.select(object + ".e[" + str(UV_BorderEdge[0]) + "]", replace=True)
    for j in UV_BorderEdge[1:]:
        cmds.select(object + ".e[" + str(j) + "]", toggle=True)
    
    # Detaching the UV border edges
    cmds.DetachEdgeComponent()
    # Duplicating the object after detachment
    newObjects = cmds.duplicate(object, returnRootsOnly=True)
    
    # Re-evaluating the polygonal components and bounding box for the new object
    PolyValues = cmds.polyEvaluate(newObjects[0], vertex=True, edge=True)
    PolyValuesBounding = cmds.polyEvaluate(newObjects[0], boundingBox=True)

    NumVertex_new = PolyValues["vertex"]
    
    # Adjusting vertex positions based on UVs and bounding box dimensions
    for i in range(NumVertex_new):
        uvMap = cmds.polyListComponentConversion(newObjects[0] + ".vtx[" + str(i) + "]", fromVertexFace=True, toUV=True)
        UVvalues = cmds.polyEditUV(uvMap, query=True)
        
        BoundingX = abs(PolyValuesBounding[0][1] - PolyValuesBounding[0][0])
        BoundingY = abs(PolyValuesBounding[1][1] - PolyValuesBounding[1][0])
        BoundingZ = abs(PolyValuesBounding[2][1] - PolyValuesBounding[2][0])

        print(PolyValuesBounding[0], PolyValuesBounding[1], BoundingX, BoundingZ)
        
        cmds.xform(newObjects[0] + ".vtx[" + str(i) + "]", absolute=True, translation=[((UVvalues[0] * axisPlane[0] * BoundingX - PolyValuesBounding[0][1]) * 2), 0, ((UVvalues[1] * axisPlane[2] * BoundingZ - PolyValuesBounding[2][1]) * 2)])
    
    newObjectsName = object + "_UVUnwrapped"  # Creating the new name
    newObjects = cmds.rename(newObjects[0], newObjectsName)  # Renaming the newObjects
    
    # Scaling the final unwrapped mesh to double its size
    cmds.scale(2, 2, 2, newObjects)
    cmds.makeIdentity(newObjects, apply=True, t=1, r=1, s=1, n=0, pn=1) 
    
    # Selecting the new object after renaming
    cmds.select(newObjects)


# Main execution starts here:

# Get currently selected objects
ListObjects = cmds.ls(selection=True)
axisPlane = [1,0,1]

# Iterate through each selected object and apply the UV unwrap function
for object in ListObjects:
    objectDuplicate = cmds.duplicate(object, returnRootsOnly=True)
    
    # Freeze transformations on the duplicated object to normalize its scale to 1    
    cmds.xform(objectDuplicate, centerPivots=True)
    cmds.move(0, 0, 0, objectDuplicate, absolute=True, rpr=True)
    cmds.makeIdentity(objectDuplicate, apply=True, t=1, r=1, s=1, n=0, pn=1)   

    UV_unwrap(objectDuplicate[0], axisPlane)

    # Deleting the objectDuplicate after the UV unwrap
    cmds.delete(objectDuplicate)