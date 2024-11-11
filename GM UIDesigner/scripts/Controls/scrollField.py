def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='scrollField',
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
    longName='wordWrap',
    shortName='ww', 
    type='boolean',
    mode='c',
    value=False,
    active=0,
    ))


    attrData.append(attrNode(
    longName='font',
    shortName='fn', 
    type='menu',
    mode='c',
    value='boldLabelFont',
    active=0,
    option=['boldLabelFont', 'smallBoldLabelFont', 'tinyBoldLabelFont', 'plainLabelFont', 'smallPlainLabelFont', 'obliqueLabelFont', 'smallObliqueLabelFont', 'fixedWidthFont' ,'smallFixedWidthFont']
    ))

    attrData.append(attrNode(
    longName='text',
    shortName='tx', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='insertionPosition',
    # shortName='ip', 
    # type='int',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='editable',
    shortName='ed', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))


    attrData.append(attrNode(
    longName='enterCommand',
    shortName='ec', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='keyPressCommand',
    shortName='kpc', 
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