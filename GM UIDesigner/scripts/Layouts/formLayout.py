def attrNode(**data):
    return data
parentList=['window','columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout']
selected=True
replace=True
def baseNode():
    return attrNode(
    procName='formLayout',
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
    longName='numberOfDivisions',
    shortName='nd', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[1,None]
    ))

    attrData.append(attrNode(
    longName='attachForm',
    shortName='af', 
    type='form',
    mode='e',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='attachOppositeForm',
    # shortName='aof', 
    # type='Custom',
    # mode='e',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='attachControl',
    shortName='ac', 
    type='form',
    mode='e',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='attachOppositeControl',
    # shortName='aoc', 
    # type='Custom',
    # mode='e',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='attachPosition',
    shortName='ap', 
    type='form',
    mode='e',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='attachNone',
    # shortName='an', 
    # type='Custom',
    # mode='e',
    # value=None,
    # active=0,
    # ))
    return attrData

