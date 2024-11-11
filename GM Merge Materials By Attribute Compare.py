import maya.cmds as cmds
import maya.mel as mel

def delete_unused_materials():
    # delete unused nodes
    mel.eval('MLdeleteUnused;')

def merge_materials():
    # get selected materials
    materials = cmds.ls(sl=True, materials=True)

    if len(materials) < 2:
        cmds.error("Please pick two or more materials")

    for material in materials[1:]:
        # select all polys using material
        cmds.hyperShade(objects=material)
        # assign the first
        cmds.hyperShade(assign=materials[0])

    # delete unused nodes    
    delete_unused_materials()

merge_materials()