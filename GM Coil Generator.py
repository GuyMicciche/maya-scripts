import maya.cmds as cmds
from math import cos, sin

def create_spiral(radius=1, height=1, num_turns=5, num_points_per_turn=10, taper=1.0):
    points = []
    for i in range(num_turns * num_points_per_turn):
        angle = 2.0 * 3.14159265 * (i / float(num_points_per_turn))
        z = height * (i / float(num_turns * num_points_per_turn))
        r = radius * pow(taper, z/height)
        x = r * cos(angle)
        y = r * sin(angle)
        points.append((x, y, z))
    return cmds.curve(d=1, p=points)

def update_spiral(curve_name, **kwargs):
    new_curve = create_spiral(**kwargs)
    cmds.delete(curve_name)
    cmds.rename(new_curve, curve_name)

def create_ui():
    if cmds.window('spiralUI', exists=True):
        cmds.deleteUI('spiralUI')

    cmds.window('spiralUI', title='Spiral Coil Helix Generator', widthHeight=(250, 250))
    cmds.columnLayout(adjustableColumn=True, columnOffset=('both', 10))

    taper_slider = cmds.floatSliderGrp(label='Taper', field=True, value=1.0)
    radius_slider = cmds.floatSliderGrp(label='Radius', field=True, value=1.0)
    height_slider = cmds.floatSliderGrp(label='Height', field=True, value=1.0)
    turns_slider = cmds.intSliderGrp(label='Number of Turns', field=True, value=5)
    points_slider = cmds.intSliderGrp(label='CVs per Turn', field=True, value=10)

    spiral_name = create_spiral()

    def on_slider_change(*args):
        taper_value = cmds.floatSliderGrp(taper_slider, query=True, value=True)
        radius_value = cmds.floatSliderGrp(radius_slider, query=True, value=True)
        height_value = cmds.floatSliderGrp(height_slider, query=True, value=True)
        turns_value = cmds.intSliderGrp(turns_slider, query=True, value=True)
        points_value = cmds.intSliderGrp(points_slider, query=True, value=True)
        
        update_spiral(spiral_name, taper=taper_value, radius=radius_value, height=height_value, num_turns=turns_value, num_points_per_turn=points_value)

    # Assign the callback function to the sliders
    cmds.floatSliderGrp(taper_slider, edit=True, dc=on_slider_change, dragCommand=on_slider_change)
    cmds.floatSliderGrp(radius_slider, edit=True, dc=on_slider_change, dragCommand=on_slider_change)
    cmds.floatSliderGrp(height_slider, edit=True, dc=on_slider_change, dragCommand=on_slider_change)
    cmds.intSliderGrp(turns_slider, edit=True, dc=on_slider_change, dragCommand=on_slider_change)
    cmds.intSliderGrp(points_slider, edit=True, dc=on_slider_change, dragCommand=on_slider_change)

    cmds.showWindow('spiralUI')

create_ui()