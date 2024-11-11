"""
Author: Guy Micciche
Date: 6/20/2023
Version: 1.0
Description: This script creates a UI window in Maya for graphing materials
in the Hypershade panel. It allows the user to select objects, view their
assigned materials, and graph the materials in the Hypershade graph. The UI
includes a checkbox for controlling the display of input and output
connections and a button to initiate the graphing process.
"""

import maya.cmds as cmds
import maya.mel as mel

def graph_selected(*args):    
    ## Open the panel, doesn't re-open if already up and sets focus
    cmds.HypershadeWindow()
    ## Get the name of the hsPanel
    hsPanel = cmds.getPanel(withFocus=True)
    ## Clear the graph
    mel.eval("hyperShadePanelGraphCommand(\"%s\", \"clearGraph\")" % hsPanel)    
    
    checkbox_state = cmds.checkBox("inputOutputCheckbox", query=True, value=True)
    if checkbox_state:
        mel.eval("hyperShadePanelGraphCommand(\"%s\", \"showUpAndDownstream\")" % hsPanel)

    nodes = cmds.ls(selection=True, dag=True)
    
    for node in nodes:
        if len(nodes) > 0:
            ## Select a node
            cmds.select(node, r=1)
            ## List the materials assigned to the object
            cmds.hyperShade(shaderNetworksSelectMaterialNodes=1)
            ## Create an array of the materials
            materialSelection = cmds.ls(sl=1)
            ## Loop over the materials and graph them        
            for material in materialSelection:
                cmds.select(material, r=1)
                mel.eval("hyperShadePanelGraphCommand(\"%s\", \"addSelected\")" % hsPanel)

        else:
            cmds.warning("Please select an object")

def create_ui():
    if cmds.window("graphWindow", exists=True):
        cmds.deleteUI("graphWindow", window=True)

    cmds.window("graphWindow", title="Graph Materials", s=0, widthHeight=(200, 70))
    cmds.columnLayout(adjustableColumn=True, columnAttach=("both", 10), rowSpacing=4)

    cmds.checkBox("inputOutputCheckbox", label="Input and output connections", value=True)
    cmds.separator(height=4, style="none")
    cmds.button(label="Graph", command=graph_selected)

    cmds.showWindow("graphWindow")

create_ui()