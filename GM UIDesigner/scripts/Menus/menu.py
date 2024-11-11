def attrNode(**data):
    return data
parentList=['window','menuBarLayout']
selected=True
def baseNode():
    return attrNode(
    procName='menu',
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
    longName='helpMenu',
    shortName='hm', 
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
    longName='mnemonic',
    shortName='mn', 
    type='string',
    mode='c',
    value='',
    active=0,
    ))

    attrData.append(attrNode(
    longName='tearOff',
    shortName='to', 
    type='boolean',
    mode='c',
    value=False,
    active=0,
    query=False,
    ))

    attrData.append(attrNode(
    longName='allowOptionBoxes',
    shortName='aob', 
    type='boolean',
    mode='c',
    value=True,
    active=0,
    ))

    attrData.append(attrNode(
    longName='familyImage',
    shortName='fi', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='postMenuCommand',
    shortName='pmc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='postMenuCommandOnce',
    shortName='pmo', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    return attrData
