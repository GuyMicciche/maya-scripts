def attrNode(**data):
    return data
parentList=['window','columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=True
replace=True
def baseNode():
    return attrNode(
    procName='scrollLayout',
    expend=False,
    renamed=False,
    ctrlType='Layout',
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

    # attrData.append(attrNode(
    # longName='horizontalScrollBarThickness',
    # shortName='hst', 
    # type='int',
    # mode='c',
    # value=0,
    # active=0,
    # option=[0,None]
    # ))


    # attrData.append(attrNode(
    # longName='verticalScrollBarThickness',
    # shortName='vst', 
    # type='int',
    # mode='c',
    # value=0,
    # active=0,
    # option=[0,None]
    # ))

    attrData.append(attrNode(
    longName='childResizable',
    shortName='cr', 
    type='boolean',
    mode='c',
    value=True,
    active=1,
    ))

    attrData.append(attrNode(
    longName='minChildWidth',
    shortName='mcw', 
    type='int',
    mode='c',
    value=0,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='resizeCommand',
    shortName='rc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))
    return attrData
