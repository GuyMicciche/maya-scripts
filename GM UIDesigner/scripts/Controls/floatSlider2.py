def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='floatSlider2',
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
    longName='minimum',
    shortName='min', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='maximum',
    shortName='max', 
    type='float',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='polarity',
    shortName='pol', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[1,None]
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
    longName='positionControl1',
    shortName='pc1', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))
    attrData.append(attrNode(
    longName='positionControl2',
    shortName='pc2', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData