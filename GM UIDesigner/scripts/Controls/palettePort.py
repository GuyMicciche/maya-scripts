def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='palettePort',
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
    longName='dimensions',
    shortName='dim', 
    type='int2',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='actualTotal',
    shortName='at', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='topDown',
    shortName='td', 
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
    longName='colorEditable',
    shortName='ced', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='redraw',
    # shortName='r', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='rgbValue',
    # shortName='rgb', 
    # type='palette',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='transparent',
    shortName='t', 
    type='int',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='setCurCell',
    shortName='scc', 
    type='int',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='colorEdited',
    shortName='ce', 
    type='script',
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
    return attrData

