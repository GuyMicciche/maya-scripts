def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='progressBar',
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
    longName='progress',
    shortName='pr', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='step',
    shortName='s', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='minValue',
    shortName='min', 
    type='int',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='maxValue',
    shortName='max', 
    type='int',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='isInterruptable',
    shortName='ii', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='beginProgress',
    # shortName='bp', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))
    return attrData