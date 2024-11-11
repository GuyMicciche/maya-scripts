def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=True
def baseNode():
    return attrNode(
    procName='iconTextRadioCollection',
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

    # attrData.append(attrNode(
    # longName='gl',
    # shortName='gl', 
    # type='boolean',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    # attrData.append(attrNode(
    # longName='select',
    # shortName='sl', 
    # type='string',
    # mode='c',
    # value=None,
    # active=0,
    # ))
    return attrData
