import maya.cmds as cmds

def get_full_path(node):
    return cmds.ls(node, long=True)[0].split(":")[-1]

def get_newly_created_node(before, after):
    return list(after - before)[0]

def copy_alembic_node_attrs(src, dest):
    """
    Copies attributes from the source AlembicNode to the destination AlembicNode.
    """
    attrs = cmds.listAttr(src, keyable=True)
    for attr in attrs:
        try:
            val = cmds.getAttr(src + '.' + attr)
            cmds.setAttr(dest + '.' + attr, val)
        except:
            pass  # Skip any attributes that can't be set

# Get all selected objects
selected_nodes = cmds.ls(sl=True, long=True)

# Check if anything is selected
if not selected_nodes:
    cmds.warning("Please select at least one geometry with Alembic and one locator!")
    exit()

alembic_geo = selected_nodes[0]
original_hierarchy = get_full_path(alembic_geo)

# Ensure alembic_geo is a transform node
if cmds.nodeType(alembic_geo) != "transform":
    cmds.warning("Selected node is not a transform node!")
    exit()

shape_node = cmds.listRelatives(alembic_geo, shapes=True, f=True)[0]

# Check for AlembicNode connection
alembic_node = cmds.listConnections(shape_node, type="AlembicNode")

if not alembic_node:
    cmds.warning("No AlembicNode attached to the selected geometry!")
    exit()

alembic_node = alembic_node[0]
alembic_path = cmds.getAttr(alembic_node + '.abc_File')

# Check for selected locators
locator_transforms = [node for node in selected_nodes[1:] if cmds.nodeType(node) == 'transform' and cmds.listRelatives(node, shapes=True, type='locator')]

if not locator_transforms:
    cmds.warning("No locators selected!")
    exit()

for loc in locator_transforms:
    # Store current top-level nodes
    top_level_before = set(cmds.ls(assemblies=True))
    
    # Import Alembic
    new_alembic_node = cmds.AbcImport(alembic_path, mode='import', fitTimeRange=False)
    
    # Determine the newly created top node
    newly_created = get_newly_created_node(top_level_before, set(cmds.ls(assemblies=True)))    

    # Construct the path for the new Alembic transform based on whether it's part of a group or not
    if '|' in original_hierarchy:
        new_alembic_transform = "|".join([newly_created] + original_hierarchy.split("|")[1:])
    else:
        new_alembic_transform = newly_created
    
    copy_alembic_node_attrs(alembic_node, new_alembic_node)

    # Apply position, rotation, and scale
    for attr in ['translate', 'rotate', 'scale']:
        for axis in ['X', 'Y', 'Z']:
            val = cmds.getAttr(loc + f".{attr}{axis}")
            cmds.setAttr(new_alembic_transform + f".{attr}{axis}", val)

    cmds.parentConstraint(loc, new_alembic_transform, maintainOffset=True)
    cmds.scaleConstraint(loc, new_alembic_transform, maintainOffset=True)