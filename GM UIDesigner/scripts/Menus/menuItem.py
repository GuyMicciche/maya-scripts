def attrNode(**data):
    return data
parentList=['menu','subMenuItem','optionMenu','optionMenuGrp','popupMenu']
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
    longName='checkBox',
    shortName='cb', 
    type='boolean',
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
    longName='imageOverlayLabel',
    shortName='iol', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='familyImage',
    # shortName='fi', 
    # type='image',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='mnemonic',
    # shortName='mn', 
    # type='string',
    # mode='c',
    # value=None,
    # active=0,
    # ))


    attrData.append(attrNode(
    longName='radialPosition',
    shortName='rp', 
    type='menu',
    mode='c',
    value='N',
    active=0,
    option=['N', 'NW', 'W', 'SW', 'S', 'SE', 'E' , 'NE']
    ))

    # attrData.append(attrNode(
    # longName='postMenuCommandOnce',
    # shortName='pmo', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='keyEquivalent',
    # shortName='ke', 
    # type='string',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='altModifier',
    # shortName='alt', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='optionModifier',
    # shortName='opt', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='ctrlModifier',
    # shortName='ctl', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='commandModifier',
    # shortName='cmd', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='shiftModifier',
    # shortName='sh', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='enableCommandRepeat',
    # shortName='ecr', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='echoCommand',
    shortName='ec', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='italicized',
    shortName='itl', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='boldFont',
    shortName='bld', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
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