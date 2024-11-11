def attrNode(**data):
    return data
parentList=['toolCollection']
selected=False
def baseNode():
    return attrNode(
    procName='toolButton',
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
    longName='image1',
    shortName='i1', 
    type='image',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='image2',
    shortName='i2', 
    type='image',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='image3',
    shortName='i3', 
    type='image',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='imageOverlayLabel',
    shortName='iol', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='toolImage1',
    shortName='ti1', 
    type='toolImage',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='toolImage2',
    shortName='ti2', 
    type='toolImage',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='toolImage3',
    shortName='ti3', 
    type='toolImage',
    mode='c',
    value=None,
    active=0,
    ))


    attrData.append(attrNode(
    longName='style',
    shortName='st', 
    type='menu',
    mode='c',
    value='iconOnly',
    active=0,
    option=['iconOnly', 'textOnly', 'iconAndTextHorizontal', 'iconAndTextVertical']
    ))

    attrData.append(attrNode(
    longName='select',
    shortName='sl', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='tool',
    shortName='t', 
    type='tool',
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
    longName='offCommand',
    shortName='ofc', 
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

    attrData.append(attrNode(
    longName='doubleClickCommand',
    shortName='dcc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData