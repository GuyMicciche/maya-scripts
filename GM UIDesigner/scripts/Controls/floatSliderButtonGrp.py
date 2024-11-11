def attrNode(**data):
    return data
parentList=['window','columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='floatSliderButtonGrp',
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
    longName='field',
    shortName='f', 
    type='boolean',
    mode='c',
    value=True,
    active=1,
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
    longName='minValue',
    shortName='min', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='maxValue',
    shortName='max', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='fieldMinValue',
    shortName='fmn', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='fieldMaxValue',
    shortName='fmx', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))


    attrData.append(attrNode(
    longName='precision',
    shortName='pre', 
    type='int',
    mode='c',
    value=3,
    active=0,
    option=[0,16]
    ))

    attrData.append(attrNode(
    longName='step',
    shortName='s', 
    type='float',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='fieldStep',
    shortName='fs', 
    type='float',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='sliderStep',
    shortName='ss', 
    type='float',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='value',
    shortName='v', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='buttonLabel',
    shortName='bl', 
    type='string',
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

    attrData.append(attrNode(
    longName='buttonCommand',
    shortName='bv', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData