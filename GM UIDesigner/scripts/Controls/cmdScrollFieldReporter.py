def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='cmdScrollFieldReporter',
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
    longName='filterSourceType',
    shortName='fst', 
    type='menu',
    mode='c',
    value=None,
    active=0,
    option=['mel','python','']
    ))

    attrData.append(attrNode(
    longName='echoAllCommands',
    shortName='eac', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='lineNumbers',
    shortName='ln', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='stackTrace',
    shortName='st', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='suppressResults',
    shortName='sr', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='suppressInfo',
    shortName='si', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='suppressWarnings',
    shortName='sw', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='suppressErrors',
    shortName='se', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='suppressStackTrace',
    shortName='sst', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData