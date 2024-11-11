def attrNode(**data):
    return data
parentList=['window','columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='checkBoxGrp',
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
    longName='numberOfCheckBoxes',
    shortName='ncb', 
    type='int',
    mode='c',
    value=4,
    active=1,
    option=[1,4]
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
    longName='label1',
    shortName='l1', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='label2',
    shortName='l2', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='label3',
    shortName='l3', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='label4',
    shortName='l4', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='value1',
    shortName='v1', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='value2',
    shortName='v2', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='value3',
    shortName='v3', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='value4',
    shortName='v4', 
    type='boolean',
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
    longName='editable',
    shortName='ed', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='vertical',
    shortName='vr', 
    type='booleanF',
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
    longName='changeCommand1',
    shortName='cc1', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='changeCommand2',
    shortName='cc2', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='changeCommand3',
    shortName='cc3', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='changeCommand4',
    shortName='cc4', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='onCommand',
    shortName='onc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='onCommand1',
    shortName='onc1', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='onCommand2',
    shortName='onc2', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='onCommand3',
    shortName='onc3', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='onCommand4',
    shortName='onc4', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='offCommand',
    shortName='ofc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='offCommand1',
    shortName='ofc1', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='offCommand2',
    shortName='ofc2', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='offCommand3',
    shortName='ofc3', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='offCommand4',
    shortName='ofc4', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData



