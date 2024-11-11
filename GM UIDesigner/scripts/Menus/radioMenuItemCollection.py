def attrNode(**data):
    return data
parentList=['menu','subMenuItem','popupMenu']
selected=True
def baseNode():
    return attrNode(
    procName='radioMenuItemCollection',
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
    return attrData

