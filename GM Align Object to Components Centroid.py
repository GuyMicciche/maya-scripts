import maya.cmds as cmds

def align_obj_to_verts():
    sel = cmds.ls(sl=True, fl=True)
    if len(sel) < 2:
        print("Error: Please select at least one group of components and one object.")
        return
    obj = sel[-1]
    verts = sel[:-1]
    bb = cmds.exactWorldBoundingBox(verts)
    average_pos = ((bb[0] + bb[3]) / 2, (bb[1] + bb[4]) / 2, (bb[2] + bb[5]) / 2)
    cmds.xform(obj, ws=True, t=average_pos)

align_obj_to_verts()