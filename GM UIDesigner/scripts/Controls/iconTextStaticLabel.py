def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='iconTextStaticLabel',
    expend=False,
    renamed=False,
    ctrlType='Control',
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
    longName='enable',
    shortName='en', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='width',
    shortName='w', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[1,None]
    ))

    attrData.append(attrNode(
    longName='height',
    shortName='h', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[1,None]
    ))

    attrData.append(attrNode(
    longName='visible',
    shortName='vis', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='preventOverride',
    shortName='po', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='annotation',
    shortName='ann', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='backgroundColor',
    shortName='bgc', 
    type='color',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='enableBackground',
    shortName='ebg', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='image',
    shortName='i', 
    type='image',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='image1',
    shortName='i1', 
    type='image',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='image2',
    shortName='i2', 
    type='image',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='image3',
    shortName='i3', 
    type='image',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='disabledImage',
    shortName='di', 
    type='image',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='imageOverlayLabel',
    shortName='iol', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='overlayLabelColor',
    shortName='olc', 
    type='color',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='overlayLabelBackColor',
    shortName='olb', 
    type='colorA',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='label',
    shortName='l', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='style',
    shortName='st', 
    type='menu',
    mode='c',
    value=None,
    active=0,
    option=['iconOnly', 'textOnly', 'iconAndTextHorizontal', 'iconAndTextVertical','iconAndTextCentered']
    ))

    attrData.append(attrNode(
    longName='align',
    shortName='al', 
    type='menu',
    mode='c',
    value=None,
    active=0,
    option=['left', 'right', 'center']
    ))

    attrData.append(attrNode(
    longName='labelOffset',
    shortName='lo', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='marginWidth',
    shortName='mw', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='marginHeight',
    shortName='mh', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='font',
    shortName='fn', 
    type='menu',
    mode='c',
    value=None,
    active=0,
    option=['boldLabelFont', 'smallBoldLabelFont', 'tinyBoldLabelFont', 'plainLabelFont', 'smallPlainLabelFont', 'obliqueLabelFont', 'smallObliqueLabelFont', 'fixedWidthFont' ,'smallFixedWidthFont']
    ))
    return attrData