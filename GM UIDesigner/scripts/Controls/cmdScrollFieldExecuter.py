def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='cmdScrollFieldExecuter',
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
    longName='sourceType',
    shortName='st', 
    type='menu',
    mode='c',
    value=None,
    active=0,
    option=['mel','python']
    ))

    attrData.append(attrNode(
    longName='showLineNumbers',
    shortName='sln', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='commandCompletion',
    shortName='cco', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='objectPathCompletion',
    shortName='opc', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='showTooltipHelp',
    shortName='sth', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='spacesPerTab',
    shortName='spt', 
    type='int',
    mode='c',
    value=4,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='tabsForIndent',
    shortName='tfi', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData

