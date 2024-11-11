def attrNode(**data):
    return data
parentList=['window','columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout','attrColorSliderGrp','attrControlGrp','attrFieldGrp','attrFieldSliderGrp','attrNavigationControlGrp','button','canvas','channelBox','checkBox','checkBoxGrp','cmdScrollFieldExecuter','cmdScrollFieldReporter','cmdShell','colorIndexSliderGrp','colorSliderButtonGrp','colorSliderGrp','commandLine','componentBox','floatField','floatFieldGrp','floatScrollBar','floatSlider','floatSlider2','floatSliderButtonGrp','floatSliderGrp','gradientControl','gradientControlNoAttr','helpLine','iconTextButton','iconTextCheckBox','iconTextRadioButton','iconTextRadioCollection','iconTextScrollList','iconTextStaticLabel','image','intField','intFieldGrp','intScrollBar','intSlider','intSliderGrp','layerButton','messageLine','nameField','palettePort','picture','progressBar','radioButton','radioButtonGrp','radioCollection','rangeControl','scriptTable','scrollField','separator','shelfButton','swatchDisplayPort','switchTable','symbolButton','symbolCheckBox','text','textField','textFieldButtonGrp','textFieldGrp','textScrollList','toolButton','toolCollection','treeView']
selected=True
def baseNode():
    return attrNode(
    procName='popupMenu',
    expend=False,
    renamed=False,
    ctrlType='MenuLayout',
    attrList=getAttrList()
    )

def getAttrList():
    attrData=[]
    attrData.append(attrNode(
    longName='parent',
    shortName='p', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='altModifier',
    shortName='alt', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='ctrlModifier',
    shortName='ctl', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='shiftModifier',
    shortName='sh', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='button',
    shortName='b', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[1,3]
    ))

    attrData.append(attrNode(
    longName='allowOptionBoxes',
    shortName='aob', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='markingMenu',
    shortName='mm', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='postMenuCommandOnce',
    shortName='pmo', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))


    attrData.append(attrNode(
    longName='postMenuCommand',
    shortName='pmc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData