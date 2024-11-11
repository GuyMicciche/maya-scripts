def attrNode(**data):
    return data
parentList=['window','columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=True
replace=True
def baseNode():
    return attrNode(
    procName='rowColumnLayout',
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

    attrData.append(attrNode(
    longName='numberOfColumns',
    shortName='nc', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[1,None]
    ))

    attrData.append(attrNode(
    longName='numberOfRows',
    shortName='nr', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[1,None]
    ))

    attrData.append(attrNode(
    longName='columnWidth',
    shortName='cw', 
    type='list_int',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='rowHeight',
    shortName='rh', 
    type='list_int',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='columnAlign',
    shortName='cal', 
    type='list_align',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='rowAlign',
    shortName='ral', 
    type='list_align',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='columnSpacing',
    shortName='cs', 
    type='list_int',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='rowSpacing',
    shortName='rs', 
    type='list_int',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData