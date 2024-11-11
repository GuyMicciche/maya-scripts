from maya import cmds, mel
import sys

def follow_camera():
    group_name = "followCameraGroup"
    
    # Delete Unused Follow Panel And Camera
    model_panels = cmds.getPanel(type='modelPanel')
    follow_panels = []
    is_run_delete = False
    for panel in model_panels:
        panel_label = cmds.panel(panel, q=True, label=True)
        if "follow_camera_" in panel_label:
            follow_panels.append(panel)
    invisible_panels = cmds.getPanel(invisiblePanels=True)
    for fpanel in follow_panels:
        if fpanel in invisible_panels:
            camera_name = cmds.modelPanel(fpanel, q=True, camera=True)
            if cmds.objExists(camera_name):
                camera_obj = cmds.listRelatives(camera_name, parent=True)
                cmds.delete(camera_obj)
            cmds.deleteUI(fpanel, panel=True)
            is_run_delete = True
    if cmds.objExists(group_name):
        children = cmds.listRelatives(group_name) or None
        if children is None:
            cmds.delete(group_name)
    
    # Check Selection Valid
    selections = cmds.ls(sl=True) or None
    if selections is None:
        if is_run_delete:
            sys.stdout.write("Delete unused panel and camera.")
        else:
            cmds.warning("Not found selection.")
        return
        
    # Check Focus Panel
    focus_panel = cmds.getPanel(withFocus=True)
    if "modelPanel" not in focus_panel:
        cmds.warning("modelPanel is not focused.")
        return
        
    # Create Camera
    new_cam_id = len(cmds.ls("follow_camera_*", type="camera"))
    before = cmds.ls(assemblies=True)
    cmds.CreateCameraFromView()
    after = cmds.ls(assemblies=True)
    new_camera = list(set(after) - set(before)) or None
    if new_camera is None:
        cmds.warning("Camera create faled.")
        return
    new_camera = cmds.rename(new_camera[0], "follow_camera_{}".format(new_cam_id))
    cmds.parentConstraint(selections, new_camera, maintainOffset=True)
    
    attrs = ["tx", "ty", "tz", "rx", "ry", "rz"]
    for attr in attrs:
        cmds.setAttr("{}.{}".format(new_camera, attr), lock=True)
        
    # Cheack Camera Parent
    if not cmds.objExists(group_name):
        cmds.createNode("transform", name=group_name)
    cmds.parent(new_camera, group_name)
    
    # Tear Of Copy...
    copy_panel = cmds.modelPanel(tearOffCopy="{}".format(focus_panel), label="follow_camera_{}".format(new_cam_id))

    # Back To Persp Panel
    mel.eval("lookThroughModelPanel persp {};".format(focus_panel))
    
follow_camera()