def attrNode(**data):
    return data
parentList=['window','columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='floatFieldGrp',
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
    longName='columnWidth',
    shortName='cw', 
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
    longName='adjustableColumn',
    shortName='adj', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,6]
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
    longName='extraLabel',
    shortName='el', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='numberOfFields',
    shortName='nf', 
    type='int',
    mode='c',
    value=4,
    active=1,
    option=[1,4]
    ))

    attrData.append(attrNode(
    longName='precision',
    shortName='pre', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,16]
    ))

    attrData.append(attrNode(
    longName='value1',
    shortName='v1', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))
    attrData.append(attrNode(
    longName='value2',
    shortName='v2', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))
    attrData.append(attrNode(
    longName='value3',
    shortName='v3', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))
    attrData.append(attrNode(
    longName='value4',
    shortName='v4', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='enable1',
    shortName='en1', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='enable2',
    shortName='en2', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='enable3',
    shortName='en3', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='enable4',
    shortName='en4', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='changeCommand',
    shortName='cc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='dragCommand',
    shortName='dc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData

