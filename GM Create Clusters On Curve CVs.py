import maya.cmds as cmds

# Get the selected objects
selected = cmds.ls(selection=True)

# Loop through each selected object
for obj in selected:
    # Check if the selected object is a curve
    shapes = cmds.listRelatives(obj, shapes=True)
    if shapes and cmds.nodeType(shapes[0]) == "nurbsCurve":
        # Get the CVs of the curve
        cvs = cmds.ls(obj + ".cv[*]", flatten=True)

        # Create a cluster at each CV
        for cv in cvs:
            cluster = cmds.cluster(cv)[1]
    else:
        cmds.warning("Object \"" + obj + "\" is not a nurbsCurve.")