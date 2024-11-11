"""
Author: Guy Micciche
Date: 07/05/2023
Version: 1.0
Description: This script performs operations in Maya to extract polygons by material from selected objects.
It collects all the materials assigned to the selected objects and segregates the polygons accordingly.
The script also provides the functionality of grouping the separated pieces based on their materials.
The pivot point of each group is set to match the pivot of the original object.
The script is also optimized for undo operations with each separate action group bundled into an undo chunk.
"""

import maya.cmds as cmds

def extract_polygons_by_material(reGroup=True):
    selected_objects = cmds.ls(selection=True)
    
    # A dictionary to store objects and their corresponding materials
    material_objects = {}

    # An optimized loop that simultaneously gets shader groups, materials, and populates the material_objects dictionary
    for obj in selected_objects:
        shader_groups = cmds.listConnections(cmds.listHistory(obj))
        materials = cmds.ls(cmds.listConnections(shader_groups), materials=True)        
        for mat in materials:
           material_objects.setdefault(mat, set()).add(obj) # Use set() instead of [] to avoid duplication of obj

    for mat, objects in material_objects.items():
        for obj in objects:
            # Get all faces in scene with the current material
            all_faces = cmds.sets(cmds.listConnections(mat, type='shadingEngine'), q=True)
            # Get all faces in object with the current material
            faces_in_obj = [face for face in all_faces if face.startswith(obj)]
            cmds.select(faces_in_obj, replace=True)
            cmds.polyChipOff(duplicate=False)
    
    # Iterate over the selected objects again to perform polySeparate and grouping operations
    for obj in selected_objects:
        cmds.select(obj, replace=True)
        pieces = cmds.polySeparate(name=obj, constructionHistory=False)

        # If reGroup is True, group pieces by material
        if reGroup:
            pivot_position = cmds.xform(obj, query=True, rotatePivot=True, worldSpace=True)
            material_piece_groups = {material: [] for material in material_objects.keys()}

            for piece in pieces:
                materials = cmds.ls(cmds.listConnections(cmds.listHistory(piece)), materials=True)
                for material in materials:
                    material_piece_groups[material].append(piece)

            # Group the pieces based on their materials
            for material, pieces in material_piece_groups.items():
                if pieces:  # Ignore empty groups
                    group_name = cmds.group(pieces, name=f'{material}_group')
                    cmds.xform(group_name, pivots=pivot_position, worldSpace=True)

    print("Polygons extracted into new objects based on assigned materials.")

# Start the undo group with a name
cmds.undoInfo(openChunk=True, chunkName='Separate Objects by Shader')
# Call the function to extract polygons by material
extract_polygons_by_material(reGroup=True) # reGroup allows the pieces to be grouped by material name
# Always make sure to close the undo group
cmds.undoInfo(closeChunk=True)