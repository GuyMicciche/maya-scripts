def attrNode(**data):
    return data
parentList=['menu','popupMenu']
selected=True
def baseNode():
    return attrNode(
    procName='menuItem',
    expend=False,
    renamed=False,
    ctrlType='MenuLayout',
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
    longName='label',
    shortName='l', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='optionBox',
    shortName='ob', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))


    attrData.append(attrNode(
    longName='subMenu',
    shortName='sm', 
    type='boolean',
    mode='s',
    value=True,
    active=1,
    ))

    attrData.append(attrNode(
    longName='tearOff',
    shortName='to', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    query=False,
    ))

    attrData.append(attrNode(
    longName='radialPosition',
    shortName='rp', 
    type='menu',
    mode='c',
    value='N',
    active=0,
    option=['N', 'NW', 'W', 'SW', 'S', 'SE', 'E' , 'NE']
    ))

    attrData.append(attrNode(
    longName='boldFont',
    shortName='bld', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))
    
    return attrData