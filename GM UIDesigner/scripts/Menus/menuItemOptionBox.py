def attrNode(**data):
    return data
parentList=['menuItem','radioMenuItem']
selected=False
def baseNode():
    return attrNode(
    procName='menuItem',
    expend=False,
    renamed=False,
    ctrlType='Menu',
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
    virtual=True
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
    longName='optionBox',
    shortName='ob', 
    type='boolean',
    mode='s',
    value=True,
    active=1,
    ))

    attrData.append(attrNode(
    longName='command',
    shortName='c', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData