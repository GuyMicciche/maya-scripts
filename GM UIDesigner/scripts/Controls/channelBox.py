def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='channelBox',
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
    longName='precision',
    shortName='pre', 
    type='int',
    mode='e',
    value=None,
    active=0,
    option=[0,16]
    ))

    attrData.append(attrNode(
    longName='longNames',
    shortName='ln', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='niceNames',
    shortName='nn', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='niceNames',
    # shortName='nn', 
    # type='boolean',
    # mode='e',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='attributeEditorMode',
    shortName='aem', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='enableLabelSelection',
    shortName='els', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='maxWidth',
    shortName='mw', 
    type='int',
    mode='e',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='maxHeight',
    shortName='mh', 
    type='int',
    mode='e',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='labelWidth',
    shortName='lw', 
    type='int',
    mode='e',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='fieldWidth',
    shortName='fw', 
    type='int',
    mode='e',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='showTransforms',
    shortName='st', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='mainListConnection',
    shortName='mlc', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='fixedAttrList',
    # shortName='fal', 
    # type='objectList',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='useManips',
    shortName='mnp', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='takeFocus',
    # shortName='tf', 
    # type='boolean',
    # mode='e',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='hyperbolic',
    shortName='hyp', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='speed',
    shortName='spd', 
    type='float',
    mode='c',
    value=None,
    active=0,
    option=[0,100]
    ))

    attrData.append(attrNode(
    longName='showNamespace',
    shortName='sn', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='attrColor',
    shortName='ac', 
    type='color',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='attrBgColor',
    shortName='bc', 
    type='color',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='nodeRegex',
    shortName='nr', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='attrRegex',
    shortName='ar', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='attrFilter',
    shortName='af', 
    type='string',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='containerAtTop',
    shortName='cat', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))
    return attrData