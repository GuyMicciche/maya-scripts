import maya.cmds as cmds

def match_object_size_from_selection():
    """
    Resize the first selected object to match the size of the second selected object.
    """
    # Get the selected objects
    selection = cmds.ls(selection=True)
    
    if len(selection) != 2:
        cmds.error("Please select exactly two objects: source first, then target.")
        return
    
    source, target = selection
    
    # Get the bounding box of both objects
    source_bbox = cmds.exactWorldBoundingBox(source)
    target_bbox = cmds.exactWorldBoundingBox(target)
    
    # Calculate the size of each object in x, y, z
    source_size = [source_bbox[3] - source_bbox[0],  # width (x)
                   source_bbox[4] - source_bbox[1],  # height (y)
                   source_bbox[5] - source_bbox[2]]  # depth (z)]
                   
    target_size = [target_bbox[3] - target_bbox[0],  # width (x)
                   target_bbox[4] - target_bbox[1],  # height (y)
                   target_bbox[5] - target_bbox[2]]  # depth (z)]
    
    # Calculate scale factors for each axis
    scale_factors = [t / s if s != 0 else 1 for s, t in zip(source_size, target_size)]
    
    # Find the uniform scale factor
    uniform_scale = min(scale_factors)  # Use the smallest scale factor to avoid distortion
    
    # Apply the scale to the source object
    cmds.scale(uniform_scale, uniform_scale, uniform_scale, source, relative=True)
    
    print(f"Resized '{source}' to match '{target}'.")

# Example usage: call the function
match_object_size_from_selection()