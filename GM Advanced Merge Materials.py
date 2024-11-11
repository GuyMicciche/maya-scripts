"""
Script Name: GEM Advanced Merge Materials.py
Author: Guy Micciche
Created: May 2023

Description:
    This script merges materials in a Maya scene. Given a selection of materials, 
    the script compares selected attributes across all other materials of the same type. 
    If those materials have the same values for the selected attributes, their polygons 
    are reassigned to the original material and the identical materials are deleted.
    This script also includes a GUI for attribute selection, with a configurable minimum 
    number of attributes to select (minAttrs).

Constants:
    minAttrs: Minimum number of attributes to select in the GUI for attribute comparison.

Methods:
    1. delete_unused_materials() - Deletes any unused material nodes in the scene.
    2. compare_materials(mat1, mat2, attrs_to_compare) - Compares two materials based on the given attributes.
    3. maya_main_window() - Returns the main Maya window as a QWidget.
    4. AttributeSelector(QDialog) - A QDialog that allows users to select the attributes to compare for a given material.
    5. merge_materials() - The main function. Handles the material selection, comparison, reassignment, and cleanup process.

Usage:
    Run the merge_materials() function with a selection of materials in Maya.
"""

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QWidget, QListWidget, QAbstractItemView
from shiboken2 import wrapInstance

# minimum number of attributes needed for compare
minAttrs = 3

def delete_unused_materials():
    # delete unused nodes
    mel.eval('MLdeleteUnused;')

def compare_materials(mat1, mat2, attrs_to_compare):
    for attr in attrs_to_compare:
        val1 = cmds.getAttr(mat1 + '.' + attr)
        val2 = cmds.getAttr(mat2 + '.' + attr)
        if val1 != val2:
            return False
    return True

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QWidget)

class AttributeSelector(QDialog):
    def __init__(self, material, parent=maya_main_window()):
        super(AttributeSelector, self).__init__(parent)

        self.setWindowTitle("Select " + str(minAttrs) + " Attributes for {}".format(material))
        self.setWindowFlag(Qt.Tool)

        self.material = material
        self.attrs_to_compare = []

        self.build_ui()
        self.populate_list()

    def build_ui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.attr_list = QListWidget()
        self.attr_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.main_layout.addWidget(self.attr_list)

        self.ok_button = QPushButton("OK")
        self.main_layout.addWidget(self.ok_button)

        self.ok_button.clicked.connect(self.on_ok)

    def populate_list(self):
        attr_list = cmds.listAttr(self.material)
        self.attr_list.addItems(attr_list)
		
		# select "color" attribute if available
        color_item = self.attr_list.findItems("color", Qt.MatchExactly)
        if color_item:
            color_item[0].setSelected(True)

    def on_ok(self):
        selected_attrs = self.attr_list.selectedItems()
        if len(selected_attrs) < minAttrs:
            cmds.warning("Please select at least " + str(minAttrs) + " attributes to compare.")
        else:
            self.attrs_to_compare = [attr.text() for attr in selected_attrs]
            self.accept()

def merge_materials():
    # get selected materials
    selected_materials = cmds.ls(sl=True, materials=True)

    if len(selected_materials) < 1:
        cmds.error("Please pick at least one material.")

    selected_materials.sort()  # sort materials by name
    last_material_type = None
    attrs_to_compare = []

    for material in selected_materials:
        mat_type = cmds.nodeType(material)
        # If material type changed, select new attributes to compare
        if mat_type != last_material_type:
            attr_selector = AttributeSelector(material)
            attr_selector.exec_()
            attrs_to_compare = attr_selector.attrs_to_compare if attr_selector.attrs_to_compare else attrs_to_compare
            last_material_type = mat_type

        if attrs_to_compare:
            # Get all materials of the same type in the scene
            all_materials = cmds.ls(type=mat_type)

            # Filter materials identical to the current selected material
            identical_materials = [mat for mat in all_materials if compare_materials(material, mat, attrs_to_compare) and mat != material]

            # Merge identical materials to the selected material
            for identical_material in identical_materials:
                # select all polys using identical material
                cmds.hyperShade(objects=identical_material)
                # assign the current selected material
                cmds.hyperShade(assign=material)

        # delete unused nodes    
        delete_unused_materials()

merge_materials()