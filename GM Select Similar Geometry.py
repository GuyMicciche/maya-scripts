"""
This script compares the UVs and faces of the selected geometry against all 
other geometries in the scene and selects those with matching characteristics.

:Author: Guy Micciche
"""
import maya.cmds as cmds

def compare_and_select_similar_geometry():
    # Get the list of selected objects
    selected_objs = cmds.ls(sl=True, tr=True)
    if not selected_objs:
        # If no objects are selected, raise a warning
        cmds.warning("No objects selected.")
        return

    # Select all geometries in the scene
    cmds.SelectAllGeometry()
    scene_meshes = cmds.ls(sl=True, tr=True)

    # If there are no geometries in the scene, raise a warning
    if not scene_meshes:
        cmds.warning("No geometry in the scene.")
        return

    save_similar = []

    # Iterate over each selected object
    for each_s in selected_objs:
        cmds.select(each_s, replace=True)
        for mesh in scene_meshes:
            # Compare the UVs and face details of the selected object with other geometries in the scene
            compare_result = cmds.polyCompare(fd=True, uv=True, e1=each_s, e2=mesh)
            
            # If the compare result is 0, it indicates that the UVs and faces are similar
            if compare_result == 0:
                save_similar.append(mesh)

    # Select the similar geometries
    cmds.select(save_similar, replace=True)

# Call the function to execute it
compare_and_select_similar_geometry()
