def attrNode(**data):
    return data
parentList=['menu','subMenuItem','popupMenu']
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
    longName='divider',
    shortName='d', 
    type='boolean',
    mode='s',
    value=True,
    active=1,
    ))

    return attrData