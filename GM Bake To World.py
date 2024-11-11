Selectd object will be bake down and keyed to world transformations.


from maya import cmds
from math import trunc

frameStartControl = "GEMFrameStart"
frameEndControl = "GEMFrameEnd"
radioCollectionControl = "GEMRadioCollection"
createLocatorControl = "GEMCreateLocator"
moreToWorldControl = "GEMMoveToWorld"
bothControl = "GEMBoth"


windowWidth = 100
labelWidth = 40

bakeOptions = 0
# OR
bakeryOptions = ['Create locator', 'Move to world', 'Both']


def SetupUI():
    if(cmds.window('window1',q=1,ex=1)):cmds.deleteUI('window1')
    win = cmds.window('window1', w=100, title='GM Bake To World', rtf=True, sizeable=False)
    #cmds.formLayout( 'formLayout1', width=(windowWidth+16), nd=100 )
    
    cmds.frameLayout('frameLayout1', p='window1', l='Frame Range')
    
    cmds.columnLayout('columnLayout3', adj=True, rs=5, columnAttach=["both", 16], columnAlign='center')   
    
    cmds.textFieldButtonGrp(frameStartControl, label="Start:", buttonLabel=" [ ", cl3=["left", "left", "left"], adj=True, ad2=True, ad3=True, ad4=True, ad5=True, ad6=True, cw=[1, labelWidth], buttonCommand=SetStartFrame)
    cmds.textFieldButtonGrp(frameEndControl, label="End:", buttonLabel=" ] ", cl3=["left", "left", "left"], adj=True, ad2=True, ad3=True, ad4=True, ad5=True, ad6=True, cw=[1, labelWidth], buttonCommand=SetEndFrame)
    
    cmds.frameLayout('frameLayout2', p='window1', l='Options')
    
    cmds.rowLayout('rowLayout3', numberOfColumns=3, adjustableColumn=2, adj=True, columnAttach=[(1, 'both', 16), (2, 'both', 16), (3, 'both', 16)])
    cmds.radioCollection(radioCollectionControl)
    cmds.radioButton(createLocatorControl, l=bakeryOptions[0], sl=True, onCommand=lambda x:selection_changed(0))
    cmds.radioButton(moreToWorldControl, l=bakeryOptions[1], onCommand=lambda x:selection_changed(1))
    cmds.radioButton(bothControl, l=bakeryOptions[2], onCommand=lambda x:selection_changed(2))

    cmds.setParent( ".." )
    
    cmds.button(l='BAKE', h=30, bgc=[0,0.75,0.99], command=OvenBake)
    cmds.separator()
    
    cmds.text("Created by Guy Micciche")
    	
    cmds.window(win, e=True, rtf=True, sizeable=False)
    cmds.showWindow(win)
    
def selection_changed(option):
    global bakeOptions
    bakeOptions = option

def SetStartFrame(*args):
     cmds.textFieldButtonGrp( frameStartControl, e=True, text=int(cmds.playbackOptions(q=True, min=True)) )
    
def SetEndFrame(*args):
    cmds.textFieldButtonGrp( frameEndControl, e=True, text=int(cmds.playbackOptions(q=True, max=True)) )

def OvenBake(*args):
    start = int(cmds.textFieldButtonGrp( frameStartControl, q=True, text=True ))
    end = int(cmds.textFieldButtonGrp( frameEndControl, q=True, text=True ))
        
    #options = cmds.radioCollection(radioCollectionControl, q=True, cia=True)
    radioBtn = cmds.radioCollection(radioCollectionControl, query=True, sl=True)    
    radioLabel = cmds.radioButton(radioBtn, query=True, label=True)
    options = bakeryOptions.index(radioLabel)
    
    BakeToWorld(start, end, options)
    
def BakeToWorld(start, end, bakeType):
    sel=cmds.ls(sl=1)
    locs = []
    for o in sel:
        sl=cmds.spaceLocator(n=(str(o) + "_loc"))
        locs.append(sl[0])
        
    x=start
    while x<=end:
        cmds.currentTime(x)
        y=0
        for each in sel:
            pos=cmds.xform(each, q=1, rp=1, ws=1)
            rot=cmds.xform(each, q=1, ro=1, ws=1)
            cmds.move(pos[0], pos[1], pos[2], locs[y], xyz=1, rpr=1)
            cmds.xform(locs[y], ro=(rot[0], rot[1], rot[2]), ws=1)
            cmds.setKeyframe(locs[y])
            y+=1            
        x+=1        
    
    cmds.currentTime(start)
    
    if (bakeType!=0):
        u=0
        for each in sel:
            try:
                cmds.parent(each, w=1)                    
            except:
                print(each + " is already a parent of the world.")
            finally:
                cmds.copyKey(locs[u], at=["tx", "ty", "tz", "rx", "ry", "rz"], t=(), f=())
                cmds.pasteKey(each, at=["tx", "ty", "tz", "rx", "ry", "rz"], connect=True, time=(1,1))
                if (bakeType==1):
                    cmds.delete( locs[u] )
                u+=1
    
SetupUI()
SetStartFrame()
SetEndFrame()