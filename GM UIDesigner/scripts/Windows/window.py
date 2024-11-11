def attrNode(**data):
    return data
parentList=[]
selected=True
def baseNode():
    return attrNode(
    procName='window',
    expend=False,
    renamed=False,
    ctrlType='Window',
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
    longName='title',
    shortName='t', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='iconName',
    shortName='iconName',
    type='image',
    mode='c',
    value=None,
    active=0
    ))

    attrData.append(attrNode(
    longName='sizeable',
    shortName='s',
    type='boolean',
    mode='c',
    value=None,
    active=0
    ))

    attrData.append(attrNode(
    longName='titleBar',
    shortName='tb',
    type='boolean',
    mode='c',
    value=None,
    active=0
    ))

    attrData.append(attrNode(
    longName='minimizeButton',
    shortName='mnb',
    type='boolean',
    mode='c',
    value=None,
    active=0
    ))

    attrData.append(attrNode(
    longName='maximizeButton',
    shortName='mxb',
    type='boolean',
    mode='c',
    value=None,
    active=0
    ))

    attrData.append(attrNode(
    longName='menuBar',
    shortName='mb',
    type='boolean',
    mode='c',
    value=1,
    active=0
    ))

    attrData.append(attrNode(
    longName='toolbox',
    shortName='tlb',
    type='boolean',
    mode='c',
    value=None,
    active=0
    ))

    attrData.append(attrNode(
    longName='titleBarMenu',
    shortName='tbm',
    type='boolean',
    mode='c',
    value=None,
    active=0
    ))

    attrData.append(attrNode(
    longName='menuBarVisible',
    shortName='mbv',
    type='boolean',
    mode='c',
    value=None,
    active=0
    ))

    # attrData.append(attrNode(
    # longName='topEdge',
    # shortName='te',
    # type='int',
    # mode='c',
    # value=None,
    # active=0
    # ))

    # attrData.append(attrNode(
    # longName='leftEdge',
    # shortName='le',
    # type='int',
    # mode='c',
    # value=None,
    # active=0
    # ))

    # attrData.append(attrNode(
    # longName='width',
    # shortName='w',
    # type='int',
    # mode='c',
    # value=None,
    # active=0,
    # option=[0,None]
    # ))

    # attrData.append(attrNode(
    # longName='height',
    # shortName='h',
    # type='int',
    # mode='c',
    # value=None,
    # active=0,
    # option=[0,None]
    # ))
    # attrData.append(attrNode(
    # longName='topLeftCorner',
    # shortName='tlc',
    # type='int2',
    # mode='c',
    # value=None,
    # active=1,
    # option=[0,None]
    # ))

    attrData.append(attrNode(
    longName='widthHeight',
    shortName='wh',
    type='int2',
    mode='c',
    value=None,
    active=0,
    option=[1,None]
    ))

    # attrData.append(attrNode(
    # longName='retain',
    # shortName='ret',
    # type='boolean',
    # mode='c',
    # value=1,
    # active=1
    # ))

    attrData.append(attrNode(
    longName='visible',
    shortName='vis',
    type='boolean',
    mode='c',
    value=None,
    active=0
    ))

    # attrData.append(attrNode(
    # longName='iconify',
    # shortName='i',
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0
    # ))

    # attrData.append(attrNode(
    # longName='backgroundColor',
    # shortName='bgc',
    # type='color',
    # mode='c',
    # value=None,
    # active=0
    # ))

    attrData.append(attrNode(
    longName='resizeToFitChildren',
    shortName='rtf',
    type='boolean',
    mode='c',
    value=None,
    active=0
    ))

    attrData.append(attrNode(
    longName='DockType',
    shortName='dt', 
    type='dock',
    mode='a',
    value=None,
    active=0
    ))
    return attrData
