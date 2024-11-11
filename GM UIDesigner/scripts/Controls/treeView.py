def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='treeView',
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
    longName='numberOfButtons',
    shortName='nb', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,5]
    ))

    # attrData.append(attrNode(
    # longName='hideButtons',
    # shortName='hb', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='allowReparenting',
    shortName='arp', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='attachButtonRight',
    shortName='abr', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='allowHiddenParents',
    shortName='ahp', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='editLabelCommand',
    shortName='elc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='itemRenamedCommand',
    shortName='irc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='selectCommand',
    shortName='sc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='selectionChangedCommand',
    shortName='scc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='contextMenuCommand',
    shortName='cmc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='expandCollapseCommand',
    shortName='ecc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='dragAndDropCommand',
    shortName='dad', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    return attrData
