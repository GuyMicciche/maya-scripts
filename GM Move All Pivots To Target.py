import maya.cmds as cmds

def move_all_pivots_to_target():
    selection = cmds.ls(selection=True)
    if len(selection) < 2:
        cmds.error('Select the source object and at least one target object.')

    source_obj = selection[0]
    target_objs = selection[1:]

    # Get the translation values of the source object's pivot
    source_pivot = cmds.xform(source_obj, query=True, worldSpace=True, rotatePivot=True)

    # Move the pivot point of each target object to the pivot point of the source object
    for target_obj in target_objs:
        cmds.xform(target_obj, worldSpace=True, pivots=source_pivot)
        cmds.makeIdentity(target_obj, apply=True, t=1, r=1, s=1, n=0)

# Example usage
move_all_pivots_to_target()