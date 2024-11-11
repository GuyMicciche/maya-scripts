'''

melToPymelUI v1.0

Convert MEL code to Python code. The script is based on the function mel2py.mel2pyStr plus some modifications for formatting

Install/Use:
1. Copy this script to your Maya script folder : C:\\Users\\Your_Username\\Documents\\maya\\scripts
2. To open the UI run the following code in Maya's Python script editor window

try:
    # For Python 3
    from importlib import reload as reload_module
except ImportError:
    # For Python 2
    try:
        from imp import reload as reload_module
    except ImportError:
        # Neither Python 2 nor 3
        pass
import melToPymelUI as melToPymelUI
reload(melToPymelUI)
melToPymelUI.UI()

3. Copy the MEL code into the top window and click convert
4. Find the resulting Python code in the bottom window, copy and paste it into the script editor of your choice

created by Monika Gelbmann
07/2019
'''
from PySide2 import QtWidgets, QtGui
import maya.OpenMayaUI as mui
import shiboken2
import pymel.core as pm
import pymel.tools.mel2py as mel2py

textbox_out = ''
target_language = 'pymel'


def getMayaWin():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(pointer), QtWidgets.QMainWindow)


def convert(meltext):
    global target_language
    global textbox_out
    try:
        if target_language == 'cmds':
            pmAnswer = mel2py.mel2pyStr(meltext, pymelNamespace='cmds')
            pmCode = pmAnswer.replace("pymel.all", "maya.cmds")
            pmCode = pmCode.replace("pm.pm.cmds.", "cmds.")

        else:
            pmAnswer = mel2py.mel2pyStr(meltext, pymelNamespace='pm')
            # get rid of old all
            pmCode = pmAnswer.replace("pymel.all", "pymel.core")
            pmCode = pmCode.replace("pm.pm.cmds.", "pm.")

        print(pmCode)
        textbox_out.setPlainText(pmCode)

    except:
        pmCode = '## Error converting ##\n## Check Script Editor for details ##'
        textbox_out.setPlainText(pmCode)
        raise
    return pmCode


def UI():
    ui_name = "ui_window"
    # check existing
    if pm.window(ui_name, exists=True):
        pm.deleteUI(ui_name, wnd=True)
    # window
    ui_parent = getMayaWin()
    ui_window = QtWidgets.QMainWindow(ui_parent)
    ui_window.setObjectName(ui_name)
    ui_window.setFixedWidth(800)
    ui_window.setWindowTitle("GEM MEL to Pymel/Cmds")

    # widget
    ui_widget = QtWidgets.QWidget()
    ui_window.setCentralWidget(ui_widget)

    # layout
    ui_layout = QtWidgets.QVBoxLayout(ui_widget)

    # create font
    ui_font = QtGui.QFont()
    ui_font.setPointSize(12)
    ui_font.setBold(False)
    code_font = QtGui.QFont()
    code_font.setFamily("Courier")
    code_font.setPointSize(8)

    # label
    label_mel = QtWidgets.QLabel()
    label_mel.setText("MEL")
    label_mel.setFont(QtGui.QFont("Arial", 12))
    ui_layout.addWidget(label_mel)

    # textbox
    textbox_in = QtWidgets.QTextEdit()
    textbox_in.resize(480, 280)
    textbox_in.setFont(code_font)

    #textbox_in.setTextBackgroundColor(QtGui.QColor("blue"))

    p = textbox_in.viewport().palette()
    p.setColor(textbox_in.viewport().backgroundRole(), QtGui.QColor("black"))
    textbox_in.viewport().setPalette(p)

    ui_layout.addWidget(textbox_in)

    # radiobuttons

    rb_pymel = QtWidgets.QRadioButton("pymel")
    rb_pymel.setChecked(True)
    rb_pymel.toggled.connect(lambda: set_output_lang("pymel"))
    rb_pymel.setFont(QtGui.QFont("Arial", 12))

    rb_cmds = QtWidgets.QRadioButton("maya.cmds")
    rb_cmds.setChecked(False)
    rb_cmds.toggled.connect(lambda: set_output_lang("cmds"))
    rb_cmds.setFont(QtGui.QFont("Arial", 12))

    # bn_layout.addWidget(b1)
    bn_layout = QtWidgets.QHBoxLayout()
    ui_layout.addLayout(bn_layout)
    bn_layout.addWidget(rb_pymel)
    bn_layout.addWidget(rb_cmds)

    # textbox
    global textbox_out
    textbox_out = QtWidgets.QTextEdit()
    textbox_out.resize(480, 280)
    textbox_out.setFont(code_font)
    ui_layout.addWidget(textbox_out)

    # button
    ui_button_convert = QtWidgets.QPushButton(" Convert ")
    ui_layout.addWidget(ui_button_convert)
    ui_button_convert.setFont(ui_font)

    ui_button_convert.setStyleSheet("background-color: rgb(33,55,55);")
    ui_button_convert.clicked.connect(lambda: convert(textbox_in.toPlainText()))

    # credits
    label_credits = QtWidgets.QLabel()
    label_credits.setText("Guy Micciche 2023")
    label_credits.setFont(QtGui.QFont("Arial", 6))
    ui_layout.addWidget(label_credits)

    ui_window.show()

    # @classmethod
    # def showUI(cls):
    #     ins = cls()
    #     ins.UI()


def set_output_lang(lang_string):
    global target_language
    if lang_string == 'pymel':
        target_language = 'pymel'
    elif lang_string == 'cmds':
        target_language = 'cmds'