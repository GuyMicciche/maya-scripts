"""
GEM Set Driven Key Tool by Guy Micciche

Description:
This tool is designed to streamline the process of creating Set Driven Keys in Maya. It provides a GUI
that allows the user to select a driver object and its corresponding attributes, as well as one or
multiple driven objects and their attributes. Once selected, the user can then set a driven key based
on the current attribute values.

Features:
- UI that provides a visual representation of driver and driven objects and their attributes.
- Easy selection and updating of driver and driven attributes.
- Buttons to load current selections into the driver or driven lists.
- Ability to key driven attributes based on the current value of the driver attribute.

Usage:
1. Ensure that the Maya environment is properly set up and the necessary libraries are imported.
2. Run the script.
3. Use the 'Load Driver' and 'Load Driven' buttons to populate the lists.
4. Select the attributes from both the driver and driven lists.
5. Press the 'Key' button to set a driven key based on the current values.
"""

import maya.cmds as cmds
import maya.mel as mel
from functools import partial

class SetDrivenKeyTool:
    # Initialization function
    def __init__(self):
        # Initial settings for the window
        self.window = 'sdktWindow'
        self.title = 'GEM Set Driven Key Tool'

        # Check if the window already exists, if so, delete it
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)

        # Create a new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=(390, 530), sizeable=True)

        # Create layouts for the UI elements
        setDrivenForm = cmds.formLayout()
        objectsForm = cmds.formLayout(parent=setDrivenForm)

        # Driver layout
		# Create UI for selecting driver (the attribute that will control others)
        driverLayout = cmds.frameLayout(label='Driver', collapsable=False, marginHeight=10, marginWidth=10, parent=objectsForm)
        driverForm = cmds.formLayout(parent=driverLayout)
        self.driverObjects = cmds.textScrollList(allowMultiSelection=False, parent=driverForm)
        self.driverChannelsUI = cmds.textScrollList(allowMultiSelection=False, selectCommand=self.updateKeyButton, parent=driverForm)
        self.driverSlider = cmds.floatFieldGrp(label='Attribute ', precision=5, numberOfFields=1, changeCommand=self.updateDriverAttributeFromFloatField, enable=0, parent=driverForm)
        
        cmds.textScrollList(self.driverObjects, e=True, selectCommand=partial(self.selectListItems, self.driverObjects, self.driverChannelsUI, self.driverSlider))
        
        cmds.formLayout(driverForm, edit=True,
                        attachForm=[
                            [self.driverObjects, 'top', 0],
                            [self.driverObjects, 'left', 0],
                            [self.driverObjects, 'bottom', 30],
                            [self.driverChannelsUI, 'top', 0],
                            [self.driverChannelsUI, 'right', 0],
                            [self.driverChannelsUI, 'bottom', 30],
                            [self.driverSlider, 'left', 0],
                            [self.driverSlider, 'right', 0],
                            [self.driverSlider, 'bottom', 0]],
                        attachControl=[
                            [self.driverChannelsUI, 'left', 0, self.driverObjects],
                            [self.driverSlider, 'top', 0, self.driverChannelsUI]],
                        attachPosition=[
                            [self.driverObjects, 'right', 0, 50]
                        ])

        # Driven layout
		# Create UI for selecting driven (the attributes that will be controlled by the driver)
        drivenLayout = cmds.frameLayout(label='Driven', collapsable=False, marginHeight=10, marginWidth=10, parent=objectsForm)
        drivenForm = cmds.formLayout(parent=drivenLayout)
        self.drivenObjects = cmds.textScrollList(allowMultiSelection=True, parent=drivenForm)        
        self.drivenChannelsUI = cmds.textScrollList(allowMultiSelection=True, selectCommand=self.updateKeyButton, parent=drivenForm)
        self.drivenSlider = cmds.floatFieldGrp(label='Attribute ', precision=5, numberOfFields=1, changeCommand=self.updateDrivenAttributeFromFloatField, enable=0, parent=drivenForm)
        
        cmds.textScrollList(self.drivenObjects, e=True, selectCommand=partial(self.selectListItems, self.drivenObjects, self.drivenChannelsUI, self.drivenSlider))

		# UI for buttons
        cmds.formLayout(drivenForm, edit=True,
                        attachForm=[
                            [self.drivenObjects, 'top', 0],
                            [self.drivenObjects, 'left', 0],
                            [self.drivenObjects, 'bottom', 30],
                            [self.drivenChannelsUI, 'top', 0],
                            [self.drivenChannelsUI, 'right', 0],
                            [self.drivenChannelsUI, 'bottom', 30],
                            [self.drivenSlider, 'left', 0],
                            [self.drivenSlider, 'right', 0],
                            [self.drivenSlider, 'bottom', 0]],
                        attachControl=[
                            [self.drivenChannelsUI, 'left', 0, self.drivenObjects],
                            [self.drivenSlider, 'top', 0, self.drivenChannelsUI]],
                        attachPosition=[
                            [self.drivenObjects, 'right', 0, 50]
                        ])

        cmds.formLayout(objectsForm, edit=True,
                        attachForm=[
                            [driverLayout, 'top', 2],
                            [driverLayout, 'left', 2],
                            [driverLayout, 'right', 2],
                            [drivenLayout, 'left', 2],
                            [drivenLayout, 'right', 2],
                            [drivenLayout, 'bottom', 2]],
                        attachControl=[
                            [drivenLayout, 'top', 2, driverLayout]],
                        attachPosition=[
                            [driverLayout, 'bottom', 2, 50]
                        ])

        buttonForm = cmds.formLayout(parent=setDrivenForm)
        self.keyButton = cmds.button(label='Key', enable=False, command=self.setDrivenKey, parent=buttonForm)
        self.updateDriver = cmds.button(label='Load Driver', command=self.loadDriver, parent=buttonForm)
        self.updateDriven = cmds.button(label='Load Driven', command=self.loadDriven, parent=buttonForm)
        self.closeButton = cmds.button(label='Close', command=('cmds.window("' + self.window + '", edit=True, visible=False)'), parent=buttonForm)

        cmds.formLayout(buttonForm, edit=True,
                        attachForm=[
                            [self.keyButton, 'top', 5],
                            [self.keyButton, 'left', 2],                            
                            [self.keyButton, 'bottom', 5],
                            [self.updateDriver, 'top', 5],
                            [self.updateDriver, 'bottom', 5],
                            [self.updateDriven, 'top', 5],
                            [self.updateDriven, 'bottom', 5],
                            [self.closeButton, 'top', 5],
                            [self.closeButton, 'right', 2],
                            [self.closeButton, 'bottom', 5]],
                        attachControl=[
                            [self.keyButton, 'right', 2, self.updateDriver],
                            [self.closeButton, 'left', 2, self.updateDriven]],
                        attachPosition=[
                            [self.updateDriver, 'left', 5, 25],
                            [self.updateDriver, 'right', 1, 50],
                            [self.updateDriven, 'left', 1, 50],
                            [self.updateDriven, 'right', 5, 75]
                        ])
                        
        cmds.formLayout(setDrivenForm, edit=True,
                        attachForm=[
                            [buttonForm, 'bottom', 5],
                            [buttonForm, 'left', 5],
                            [buttonForm, 'right', 5],
                            [objectsForm, 'top', 5],
                            [objectsForm, 'left', 5],
                            [objectsForm, 'right', 5]],
                        attachControl=[
                            [objectsForm, 'bottom', 5, buttonForm]
                        ])
						
		# Display the window
        cmds.showWindow(self.window)

	# Method to handle selecting items from a list in the GUI
    def selectListItems(self, list, channelListUI, slider):
        cmds.floatFieldGrp(slider, edit=True, enable=0)
        cmds.floatFieldGrp(slider, edit=True, label='Attribute ')
        cmds.floatFieldGrp(slider, edit=True, value1=0.0)
        cmds.textScrollList(channelListUI, edit=True, deselectAll=True)
        cmds.button(self.keyButton, edit=True, enable=False)
        if cmds.optionVar(query='SDKselectListItems'):
            objects = cmds.textScrollList(list, query=True, selectItem=True)
            if objects and objects[0] != 'setDrivenKeyNothingSelected':
                cmds.select(objects, replace=True)
    
	# Load driver objects into the UI from the current selection	
    def loadDriver(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textScrollList(self.driverObjects, edit=True, removeAll=True)
            cmds.textScrollList(self.driverObjects, edit=True, append=sel)
            cmds.textScrollList(self.driverObjects, edit=True, selectIndexedItem=1)
            cmds.button(self.keyButton, edit=True, enable=False)
            self.selectListItems(self.driverObjects, self.driverChannelsUI, self.driverSlider)
            self.populateDriverAttrs(sel[0])
            mel.eval('copyAEWindow')

	# Load driven objects into the UI from the current selection
    def loadDriven(self, *args):
        sel = cmds.ls(selection=True)
        if sel:
            cmds.textScrollList(self.drivenObjects, edit=True, removeAll=True)
            cmds.textScrollList(self.drivenObjects, edit=True, append=sel)
            numItems = cmds.textScrollList(self.drivenObjects, query=True, numberOfItems=True)
            cmds.textScrollList(self.drivenObjects, edit=True, selectIndexedItem=range(1, numItems+1))
            cmds.button(self.keyButton, edit=True, enable=False)
            self.selectListItems(self.drivenObjects, self.drivenChannelsUI, self.drivenSlider)
            self.populateDrivenAttrs(sel)

	# Populate attributes of the driver in the UI
    def populateDriverAttrs(self, driver):
        attrs = cmds.listAttr(driver, keyable=True)
        cmds.textScrollList(self.driverChannelsUI, edit=True, removeAll=True)
        if attrs:
            for attr in attrs:
                cmds.textScrollList(self.driverChannelsUI, edit=True, append=attr)

	# Populate attributes of the driven objects in the UI
    def populateDrivenAttrs(self, driven):
        cmds.textScrollList(self.drivenChannelsUI, edit=True, removeAll=True)
        common_attrs = cmds.listAttr(driven[0], keyable=True)
        for attr in common_attrs:
            cmds.textScrollList(self.drivenChannelsUI, edit=True, append=attr)
   
	# Update the UI to enable or disable the key button based on the selection
    def updateKeyButton(self, *args):
        if (cmds.textScrollList(self.driverChannelsUI, query=True, numberOfSelectedItems=True) != 0 
            and cmds.textScrollList(self.drivenChannelsUI, query=True, numberOfSelectedItems=True) != 0):
            cmds.button(self.keyButton, edit=True, enable=True)
        else:
            cmds.button(self.keyButton, edit=True, enable=False)
        self.updateSliderValues()

	# Update the values displayed in the sliders based on the current attribute values
    def updateSliderValues(self):
        driver = cmds.textScrollList(self.driverObjects, query=True, selectItem=True)
        driven = cmds.textScrollList(self.drivenObjects, query=True, selectItem=True)
        driverAttr = cmds.textScrollList(self.driverChannelsUI, query=True, selectItem=True)
        drivenAttr = cmds.textScrollList(self.drivenChannelsUI, query=True, selectItem=True)

        if driver and driverAttr:
            driver_value = cmds.getAttr('{}.{}'.format(driver[0], driverAttr[0]))
            cmds.floatFieldGrp(self.driverSlider, edit=True, label=driverAttr[0]+' ', value1=driver_value, enable=1)

        if driven and drivenAttr:
            # For simplicity, assuming all driven objects have the same value for the selected attribute
            driven_value = cmds.getAttr('{}.{}'.format(driven[0], drivenAttr[0]))
            cmds.floatFieldGrp(self.drivenSlider, edit=True, label=drivenAttr[0]+' ', value1=driven_value, enable=1)

	# Update the driver object's attribute based on the slider's value
    def updateDriverAttributeFromFloatField(self, *args):
        # Driver
        selectedAttr = cmds.textScrollList(self.driverChannelsUI, query=True, selectItem=True)
        selectedObj = cmds.textScrollList(self.driverObjects, query=True, selectItem=True)
        attrValue = cmds.floatFieldGrp(self.driverSlider, query=True, value1=True)
        if selectedAttr and selectedObj:
            cmds.setAttr(selectedObj[0] + '.' + selectedAttr[0], attrValue)
       
	# Update the driven objects' attributes based on the slider's value
    def updateDrivenAttributeFromFloatField(self, *args):
        # Driven
        selectedAttrs = cmds.textScrollList(self.drivenChannelsUI, query=True, selectItem=True)
        selectedObjs = cmds.textScrollList(self.drivenObjects, query=True, selectItem=True)
        attrValue = cmds.floatFieldGrp(self.drivenSlider, query=True, value1=True)
    
        if selectedAttrs and selectedObjs:
            for obj in selectedObjs:
                for attr in selectedAttrs:
                    cmds.setAttr(obj + '.' + attr, attrValue)

	# Create a set driven key between the selected driver and driven attributes
    def setDrivenKey(self, *args):
        driver = cmds.textScrollList(self.driverObjects, query=True, selectItem=True)
        driven = cmds.textScrollList(self.drivenObjects, query=True, selectItem=True)
        driverAttrs = cmds.textScrollList(self.driverChannelsUI, query=True, selectItem=True)
        drivenAttrs = cmds.textScrollList(self.drivenChannelsUI, query=True, selectItem=True)

        if not driver or not driven or not driverAttrs or not drivenAttrs:
            return

        for driverAttr in driverAttrs:
            for drv in driver:
                for obj in driven:
                    for drivenAttr in drivenAttrs:
                        cmds.setDrivenKeyframe('%s.%s' % (obj, drivenAttr), 
                                               currentDriver='%s.%s' % (drv, driverAttr))

# Run the tool if the script is executed
if __name__ == '__main__':
    # Ensure that the optionVar 'SDKselectListItems' is set to True
    cmds.optionVar(intValue=('SDKselectListItems', 1))
    SetDrivenKeyTool()  # Create an instance of the tool and display the GUI