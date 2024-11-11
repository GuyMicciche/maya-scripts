def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='componentBox',
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
    longName='rowHeight',
    shortName='rh', 
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
    longName='precision',
    shortName='pre', 
    type='int',
    mode='e',
    value=None,
    active=0,
    option=[0,16]
    ))
    return attrData
