def attrNode(**data):
    return data
parentList=['window','columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout']
selected=True
replace=True
def baseNode():
    return attrNode(
    procName='frameLayout',
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
    longName='borderVisible',
    shortName='bv', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='borderStyle',
    shortName='bs', 
    type='menu',
    mode='c',
    value=None,
    active=0,
    option=['in','out','etchedIn','etchedOut']
    ))

    attrData.append(attrNode(
    longName='collapse',
    shortName='cl', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='collapsable',
    shortName='cll', 
    type='boolean',
    mode='c',
    value=True,
    active=1,
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
    longName='labelVisible',
    shortName='lv', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='labelAlign',
    shortName='la', 
    type='menu',
    mode='c',
    value=None,
    active=0,
    option=['top','center','bottom']
    ))

    attrData.append(attrNode(
    longName='labelIndent',
    shortName='li', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='labelWidth',
    shortName='lw', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='font',
    shortName='fn', 
    type='menu',
    mode='c',
    value=None,
    active=0,
    option=['boldLabelFont','smallBoldLabelFont','tinyBoldLabelFont','plainLabelFont','smallPlainLabelFont','obliqueLabelFont','smallObliqueLabelFont','fixedWidthFont','smallFixedWidthFont']
    ))

    attrData.append(attrNode(
    longName='marginHeight',
    shortName='mh', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='marginWidth',
    shortName='mw', 
    type='int',
    mode='c',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='collapseCommand',
    shortName='cc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='expandCommand',
    shortName='ec', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='preCollapseCommand',
    shortName='pcc', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='preExpandCommand',
    shortName='pec', 
    type='script',
    mode='c',
    value=None,
    active=0,
    ))
    return attrData