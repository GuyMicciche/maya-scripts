"""
Oscillation UI Tool for Maya by [Your Name Here]

Description:
This tool provides a UI for Maya users to apply oscillating animations to selected object attributes using an expression.
The UI features amplitude and frequency sliders with corresponding spin boxes, allowing users to control the oscillation's properties.
Additionally, users can select the desired attribute from a dropdown menu that updates dynamically based on the currently selected object in Maya.
There's also a feature to remove any existing oscillation expression from the chosen attribute.

Usage:
1. Ensure Maya is running and that the required libraries are imported.
2. Run the script.
3. Adjust the amplitude and frequency using the provided sliders or spin boxes.
4. Select the attribute you wish to apply the oscillation to from the dropdown menu.
5. Click 'Apply Oscillation' to set the oscillation expression.
6. If you wish to remove an existing oscillation expression from an attribute, click 'Remove Expression'.
"""

import maya.cmds as cmds
import maya.api.OpenMaya as om
from PySide2 import QtWidgets, QtCore


class SelectionWatcher(QtCore.QObject):
    """Watches for selection changes in Maya and emits a signal when detected."""
    selectionChanged = QtCore.Signal()

    def __init__(self):
        super(SelectionWatcher, self).__init__()
        self.callback_id = None

    def start_watching(self):
        """Start monitoring for selection changes."""
        self.callback_id = om.MEventMessage.addEventCallback("SelectionChanged", self.emit_selection_changed)

    def stop_watching(self):
        """Stop monitoring for selection changes."""
        if self.callback_id is not None:
            om.MEventMessage.removeCallback(self.callback_id)
            self.callback_id = None

    def emit_selection_changed(self, *args):
        """Emit the 'selectionChanged' signal."""
        self.selectionChanged.emit()


class OscillationUI(QtWidgets.QDialog):
    """The main Oscillation UI class."""
    def __init__(self):
        super(OscillationUI, self).__init__()

        self.setWindowTitle("Oscillation UI")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)  # Keep the window always on top

        # Amplitude widgets
        amplitude_label = QtWidgets.QLabel("Amplitude (value):")
        self.amplitude_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.amplitude_slider.setMinimum(0)
        self.amplitude_slider.setMaximum(360)
        self.amplitude_slider.setValue(5)

        self.amplitude_spinbox = QtWidgets.QSpinBox()
        self.amplitude_spinbox.setMinimum(0)
        self.amplitude_spinbox.setMaximum(360)
        self.amplitude_spinbox.setValue(5)
        self.amplitude_slider.valueChanged.connect(self.amplitude_spinbox.setValue)
        self.amplitude_spinbox.valueChanged.connect(self.amplitude_slider.setValue)

        # Frequency widgets
        frequency_label = QtWidgets.QLabel("Frequency (frames):")
        self.frequency_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.frequency_slider.setMinimum(1)
        self.frequency_slider.setMaximum(1000)
        self.frequency_slider.setValue(48)

        self.frequency_spinbox = QtWidgets.QSpinBox()
        self.frequency_spinbox.setMinimum(1)
        self.frequency_spinbox.setMaximum(1000)
        self.frequency_spinbox.setValue(48)
        self.frequency_slider.valueChanged.connect(self.frequency_spinbox.setValue)
        self.frequency_spinbox.valueChanged.connect(self.frequency_slider.setValue)

        # Attribute dropdown
        attribute_label = QtWidgets.QLabel("Attribute:")
        self.attribute_dropdown = QtWidgets.QComboBox()

        # Apply and Remove buttons
        self.apply_button = QtWidgets.QPushButton("Apply Oscillation")
        self.apply_button.clicked.connect(self.apply_oscillation)
        
        self.remove_button = QtWidgets.QPushButton("Remove Expression")
        self.remove_button.clicked.connect(self.remove_expression_from_attribute)

        # Layout setup
        layout.addWidget(amplitude_label)
        layout.addWidget(self.amplitude_slider)
        layout.addWidget(self.amplitude_spinbox)
        layout.addWidget(frequency_label)
        layout.addWidget(self.frequency_slider)
        layout.addWidget(self.frequency_spinbox)
        layout.addWidget(attribute_label)
        layout.addWidget(self.attribute_dropdown)
        layout.addSpacing(20)
        layout.addWidget(self.remove_button)  # Added remove button
        layout.addWidget(self.apply_button)

        self.setLayout(layout)

        # Monitor selection changes in Maya
        self.selection_watcher = SelectionWatcher()
        self.selection_watcher.selectionChanged.connect(self.update_attribute_dropdown)
        self.selection_watcher.start_watching()

        self.update_attribute_dropdown()

    def update_attribute_dropdown(self):
        """Updates the attribute dropdown based on the currently selected object in Maya."""
        selected_objects = cmds.ls(selection=True)
        if not selected_objects:
            self.attribute_dropdown.clear()
            return

        last_selected_object = selected_objects[-1]
        obj_attributes = cmds.listAttr(last_selected_object, keyable=True) or []

        self.attribute_dropdown.clear()
        self.attribute_dropdown.addItems(obj_attributes)

    def delete_expression(self, node_name, attribute_name):
        """Deletes expression connected to the provided node's attribute."""
        full_attribute_name = '{}.{}'.format(node_name, attribute_name)
        connections = cmds.listConnections(full_attribute_name, type='expression')
        if connections:
            cmds.delete(connections)

    def apply_oscillation(self):
        """Applies an oscillation expression to the selected object's attribute."""
        amplitude = self.amplitude_spinbox.value()
        frequency = self.frequency_spinbox.value()

        oscillation_expression = '''
        int $frame = `currentTime -q`;
        float $amplitude = {};
        float $frequency = {};
        float $phase = $frame % $frequency;
        float $angle = $amplitude * (sin(2 * 3.14159 * $phase / $frequency) + 1) - $amplitude;
        {}.{} = $angle;
        '''

        selected_objects = cmds.ls(selection=True)
        if not selected_objects:
            return

        attribute = self.attribute_dropdown.currentText()
        if not attribute:
            return

        for obj in selected_objects:
            self.delete_expression(obj, attribute)
            formatted_expression = oscillation_expression.format(amplitude, frequency, obj, attribute)
            cmds.expression(object=obj, attribute=attribute, string=formatted_expression)

    def remove_expression_from_attribute(self):
        """Removes any existing oscillation expression from the selected attribute."""
        selected_objects = cmds.ls(selection=True)
        if not selected_objects:
            return

        attribute = self.attribute_dropdown.currentText()
        if not attribute:
            return

        for obj in selected_objects:
            self.delete_expression(obj, attribute)

    def closeEvent(self, event):
        """Ensures the selection watcher stops when the window is closed."""
        self.selection_watcher.stop_watching()
        event.accept()


if __name__ == "__main__":
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])

    dialog = OscillationUI()
    dialog.show()

    app.exec_()