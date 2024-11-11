# coding=utf-8

__author__ = "Guy Micciche (king.guy@outlook.com)"
__version__ = "1.0.0.0"

from maya import cmds
import sys
import maya.mel as mm
import functools
import re
import copy
import os

from maya import cmds
class GenerateOptionEditor():
    winTitle='GEM_GenerateOptionEditor'
    def __init__(self,isModal=False):
        self.isModal=isModal
        self.outData=None
        self.inputData=None

    def dockEditorPrompt(self,form=None):
        if(form==None):
            form=cmds.setParent(q=1)
        #cmds.formLayout(form,e=1,w=500,h=500)
        cmds.tabLayout('goOptionTL',tv=False,cr=True)
        cmds.columnLayout('goOptionCL',adj=True)
        cmds.radioButtonGrp('goFlagRBG',nrb=2,sl=1,l='Flag : ',l1='Short Name',l2='Long Name')
        cmds.radioButtonGrp('goBoolRBG',nrb=2,sl=1,l='Boolean : ',l1='True | False',l2='0 | 1')
        cmds.radioButtonGrp('goIndentRGB',nrb=2,sl=1,l='Indent : ',l1='Tab',l2='4-Space')
        cmds.radioButtonGrp('goCtrlIDRBG',nrb=2,sl=1,l='Control ID : ',l1='Need',l2='Force All')
        cmds.textFieldButtonGrp('goFuncParamTFBG',l='UI Function Parameter: ',ed=False,bl='Enable',bc=functools.partial(self.enableTextField,'goFuncParamTFBG'))
        cmds.textFieldButtonGrp('goCallFuncParamTFBG',l='Call Function Parameter: ',ed=False,bl='Enable',bc=functools.partial(self.enableTextField,'goCallFuncParamTFBG'))
        cmds.button('goOkB',p=form,l='OK',c=functools.partial(self.quitMode,'ok'))
        cmds.button('goCancelB',p=form,l='Cancel',c=functools.partial(self.quitMode,'cancel'))
        cmds.formLayout(form,e=1,af=[['goOptionTL', 'top', 5], ['goOptionTL', 'left', 5], ['goOptionTL', 'right', 5], ['goOkB', 'left', 5], ['goOkB', 'bottom', 5], ['goCancelB', 'right', 5], ['goCancelB', 'bottom', 5]],ac=[['goOptionTL', 'bottom', 5, 'goOkB'], ['goCancelB', 'left', 5, 'goOkB']],ap=[['goOkB', 'right', 0, 50]])
        self.setInputData()

    def setInputData(self):
        if(self.inputData==None):
            self.inputData=self.getDefultData()
        cmds.radioButtonGrp('goFlagRBG',e=1,sl=self.inputData['flagType'])
        cmds.radioButtonGrp('goBoolRBG',e=1,sl=self.inputData['booleanType'])
        cmds.radioButtonGrp('goIndentRGB',e=1,sl=self.inputData['indentType'])
        cmds.radioButtonGrp('goCtrlIDRBG',e=1,sl=self.inputData['ctrlIdType'])
        cmds.textFieldButtonGrp('goFuncParamTFBG',e=1,ed=(self.inputData['funcParam']!=''),tx=self.inputData['funcParam'])
        cmds.textFieldButtonGrp('goCallFuncParamTFBG',e=1,ed=(self.inputData['callFuncParam']!=''),tx=self.inputData['callFuncParam'])

    def enableTextField(self,ctrlId):
        typ=cmds.textFieldButtonGrp(ctrlId,q=1,bl=1)
        if(typ=='Enable'):
            cmds.textFieldButtonGrp(ctrlId,e=1,ed=True,bl='Disable')
        else:
            cmds.textFieldButtonGrp(ctrlId,e=1,ed=False,tx='',bl='Enable')

    def getOutputData(self):
        self.outData={}
        self.outData['flagType']=cmds.radioButtonGrp('goFlagRBG',q=1,sl=1)
        self.outData['booleanType']=cmds.radioButtonGrp('goBoolRBG',q=1,sl=1)
        self.outData['indentType']=cmds.radioButtonGrp('goIndentRGB',q=1,sl=1)
        self.outData['ctrlIdType']=cmds.radioButtonGrp('goCtrlIDRBG',q=1,sl=1)
        self.outData['funcParam']=cmds.textFieldButtonGrp('goFuncParamTFBG',q=1,tx=1)
        self.outData['callFuncParam']=cmds.textFieldButtonGrp('goCallFuncParamTFBG',q=1,tx=1)

    def getDefultData(self):
        defuldata={'flagType':1,'booleanType':1,'indentType':1,'ctrlIdType':1,'funcParam':'','callFuncParam':''}
        return defuldata

    def quitMode(self,*argc):
        self.getOutputData()
        if self.isModal:
            cmds.layoutDialog(dis=argc[0])
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)

    def show(self,inputData=None):
        self.inputData=inputData
        if self.isModal:
            ret=cmds.layoutDialog(ui=self.dockEditorPrompt)
            if(ret=='ok'):
                return self.outData
            else:
                return
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)
            self.winTitle=cmds.window(self.winTitle,w=500,h=500,s=1)
            form=cmds.formLayout('goMainFL')
            self.dockEditorPrompt(form)
            cmds.showWindow(self.winTitle)

class AlphaEditor():
    winTitle='GEM_AlphaEditor'
    def __init__(self,isModal=False):
        self.isModal=isModal
        self.outData=None
        self.inputData=None
  
    def dockEditorPrompt(self,form=None):
        if(form==None):
            form=cmds.setParent(q=1)
        #cmds.formLayout(form,e=1,w=500,h=500)
        cmds.floatSliderGrp('aeAlphaFSG',p=form,cw=[[1, 50]],f=True,l='Alpha',max=1.0,v=0.25,pre=3)
        cmds.button('aeOKB',p=form,l='OK',c=functools.partial(self.quitMode,'ok'))
        cmds.button('aeCancelB',p=form,l='Cancel',c=functools.partial(self.quitMode,'cancel'))
        cmds.formLayout(form,e=1,af=[['aeAlphaFSG', 'top', 5], ['aeAlphaFSG', 'left', 5], ['aeAlphaFSG', 'right', 5], ['aeOKB', 'left', 5], ['aeOKB', 'bottom', 5], ['aeCancelB', 'right', 5], ['aeCancelB', 'bottom', 5]],ac=[['aeCancelB', 'left', 5, 'aeOKB']],ap=[['aeOKB', 'right', 5, 50]])
        self.setInputData()

    def setInputData(self):
        cmds.floatSliderGrp('aeAlphaFSG',e=1,v=self.inputData)

    def getOutputData(self):
        self.outData=cmds.floatSliderGrp('aeAlphaFSG',q=1,v=1)

    def quitMode(self,*argc):
        self.getOutputData()
        if self.isModal:
            cmds.layoutDialog(dis=argc[0])
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)

    def show(self,inputData=0.25):
        self.inputData=inputData
        if self.isModal:
            ret=cmds.layoutDialog(ui=self.dockEditorPrompt)
            if(ret=='ok'):
                return self.outData
            else:
                return
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)
            self.winTitle=cmds.window(self.winTitle,w=500,h=500,s=1)
            form=cmds.formLayout('aeMainFL')
            self.dockEditorPrompt(form)
            cmds.showWindow(self.winTitle)

class DockEditor():
    winTitle='GEM_DockEditor'
    def __init__(self,isModal=False):
        self.isModal=isModal
        self.outData=None
        self.inputDataList=None
  
    def dockEditorPrompt(self,form=None):
        if(form==None):
            form=cmds.setParent(q=1)
        #cmds.formLayout(form,e=1,w=500,h=500)
        cmds.columnLayout('dtMainCL',p=form,adj=1)
        cmds.optionMenuGrp('dtTypeOMG',adj=2,ebg=1,cw=[[1, 70], [2, 200]],l='Dock Type : ',cc=self.typeChange)
        cmds.menuItem(l='window')
        cmds.menuItem(l='dockControl')
        cmds.menuItem(l='toolBar')

        cmds.columnLayout('dtOptionCL',p='dtMainCL',adj=1,en=0)
        cmds.textFieldGrp('dtLabelTFG',p='dtOptionCL',cw=[[1, 70]],adj=2,l='Label : ')
        cmds.optionMenuGrp('dtAreaOMG',p='dtOptionCL',adj=2,cw=[[1, 70], [2, 200]],l='Area : ')
        cmds.menuItem(l='top')
        cmds.menuItem(l='bottom')
        cmds.menuItem(l='left')
        cmds.menuItem(l='right')
        cmds.optionMenuGrp('dtAreaOMG',e=1,v='right')
        cmds.checkBoxGrp('dtAllowCBG',p='dtOptionCL',cw=[[1, 70], [2, 60], [3, 60], [4, 60], [5, 60]],ncb=4,l='AllowedArea : ',l1='top',l2='bottom',l3='left',l4='right',v1=1,v2=1,v3=1,v4=1)

        cmds.button('dtOkB',p=form,l='OK',c=functools.partial(self.quitMode,'ok'))
        cmds.button('dtCanceB',p=form,l='Cancel',c=functools.partial(self.quitMode,'cancel'))
        cmds.formLayout(form,e=1,af=[['dtMainCL', 'top', 5], ['dtMainCL', 'left', 5], ['dtMainCL', 'right', 5], ['dtOkB', 'left', 5], ['dtOkB', 'bottom', 5], ['dtCanceB', 'right', 5], ['dtCanceB', 'bottom', 5]],ac=[['dtMainCL', 'bottom', 5, 'dtOkB'], ['dtCanceB', 'left', 5, 'dtOkB']],ap=[['dtOkB', 'right', 0, 50]])
        self.setInputData()

    def setInputData(self):
        if(self.inputDataList==None):
            return
        typ,label,area,allowedAreaList=self.inputDataList
        cmds.optionMenuGrp('dtTypeOMG',e=1,v=typ)
        cmds.textFieldGrp('dtLabelTFG',e=1,tx=label)
        cmds.optionMenuGrp('dtAreaOMG',e=1,v=area)
        cmds.checkBoxGrp('dtAllowCBG',e=1,v1=0)
        cmds.checkBoxGrp('dtAllowCBG',e=1,v2=0)
        cmds.checkBoxGrp('dtAllowCBG',e=1,v3=0)
        cmds.checkBoxGrp('dtAllowCBG',e=1,v4=0)
        for i in allowedAreaList:
            if(i=='top'):
                cmds.checkBoxGrp('dtAllowCBG',e=1,v1=1)
            elif(i=='bottom'):
                cmds.checkBoxGrp('dtAllowCBG',e=1,v2=1)
            elif(i=='left'):
                cmds.checkBoxGrp('dtAllowCBG',e=1,v3=1)
            elif(i=='right'):
                cmds.checkBoxGrp('dtAllowCBG',e=1,v4=1)
        self.typeChange()

    def getOutputData(self):
        idx=cmds.optionMenuGrp('dtTypeOMG',q=1,sl=1)
        if(idx==1):
            self.outData=None
        typ=cmds.optionMenuGrp('dtTypeOMG',q=1,v=1)
        label=cmds.textFieldGrp('dtLabelTFG',q=1,tx=1)
        area=cmds.optionMenuGrp('dtAreaOMG',q=1,v=1)
        allowedAreaList=[]
        if(cmds.checkBoxGrp('dtAllowCBG',q=1,v1=1)):
            allowedAreaList.append('top')
        if(cmds.checkBoxGrp('dtAllowCBG',q=1,v2=1)):
            allowedAreaList.append('bottom')
        if(cmds.checkBoxGrp('dtAllowCBG',q=1,v3=1)):
            allowedAreaList.append('left')
        if(cmds.checkBoxGrp('dtAllowCBG',q=1,v4=1)):
            allowedAreaList.append('right')
        self.outData=[str(typ),str(label),str(area),allowedAreaList]

    def typeChange(self,*argc):
        idx=cmds.optionMenuGrp('dtTypeOMG',q=1,sl=1)
        cmds.columnLayout('dtOptionCL',e=1,en=idx>1)

    def quitMode(self,*argc):
        self.getOutputData()
        if self.isModal:
            cmds.layoutDialog(dis=argc[0])
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)

    def show(self,inputDataList=None):
        self.inputDataList=inputDataList
        if self.isModal:
            ret=cmds.layoutDialog(ui=self.dockEditorPrompt)
            if(ret=='ok'):
                return self.outData
            else:
                return
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)
            self.winTitle=cmds.window(self.winTitle,w=500,h=500,s=1)
            form=cmds.formLayout('icMainFL')
            self.dockEditorPrompt(form)
            cmds.showWindow(self.winTitle)

class PaletteEditor():
    winTitle='GEM_PaletteEditor'
    def __init__(self,isModal=False):
        self.isModal=isModal
        self.outData=None
  
    def paletteEditorPrompt(self,form=None):
        if(form==None):
            form=cmds.setParent(q=1)
        cmds.formLayout(form,e=1,w=500,h=500)
        self.palettePP=cmds.palettePort('pePalettePP',p=form,dim=(5,5),ced=0,cc=self.selectChange)
        cmds.button('peOKB',l='OK',w=80,p=form,c=functools.partial(self.quitMode,'ok'))
        cmds.button('peCancelB',l='Cancel',w=80,p=form,c=functools.partial(self.quitMode,'cancel'))
        self.rgbF=cmds.floatFieldGrp('peRGBF',nf=3,pre=3,cc=self.rgbChange)
        cmds.formLayout(form,e=1,af=[['peOKB', 'bottom', 2], ['pePalettePP', 'top', 2], ['pePalettePP', 'left', 2], ['pePalettePP', 'right', 2], ['peCancelB', 'right', 2], ['peCancelB', 'bottom', 2], ['peRGBF', 'bottom', 2], ['peRGBF', 'left', 2]],ac=[['pePalettePP', 'bottom', 2, 'peOKB'], ['peOKB', 'right', 2, 'peCancelB'], ['peRGBF', 'right', 2, 'peOKB']])
        self.selectChange()
        #colList=[[0, 1.0, 0.0, 0.0], [1,0, 0.1770833134651184, 0.0], [2, 1.0, 0.3541666269302368, 0.0], [3, 1.0, 0.53125, 0.0], [4, 1.0, 0.7083333134651184, 0.0], [5, 1.0, 0.8854166865348816, 0.0], [6, 0.9375, 1.0, 0.0], [7, 0.7604166269302368, 1.0, 0.0], [8, 0.5833333730697632, 1.0, 0.0], [9, 0.40625, 1.0, 0.0], [10, 0.22916662693023682, 1.0, 0.0], [11, 0.052083373069763184, 1.0, 0.0], [12, 0.0, 1.0, 0.125], [13, 0.0, 1.0, 0.30208325386047363], [14, 0.0, 1.0, 0.47916674613952637], [15, 0.0, 1.0, 0.65625], [16, 0.0, 1.0, 0.8333332538604736], [17, 0.0, 0.9895832538604736, 1.0], [18, 0.0, 0.8125, 1.0], [19, 0.0, 0.6354167461395264, 1.0], [20, 0.0, 0.45833325386047363, 1.0], [21, 0.0, 0.28125, 1.0], [22, 0.0, 0.10416674613952637, 1.0], [23, 0.07291650772094727, 0.0, 1.0], [24, 0.25, 0.0, 1.0]]
        #for i in colList:
        #     cmds.palettePort('pePalettePP',e=1,rgb=i)

    def selectChange(self,*argc):
        idx=cmds.palettePort(self.palettePP,q=1,scc=1)
        rgb=cmds.palettePort(self.palettePP,q=1,rgb=idx+1)
        cmds.floatFieldGrp(self.rgbF,e=1,v1=rgb[0],v2=rgb[1],v3=rgb[2])

    def rgbChange(self,*argc):
        idx=cmds.palettePort(self.palettePP,q=1,scc=1)
        rgb=cmds.floatFieldGrp(self.rgbF,q=1,v=1)
        cmds.palettePort(self.palettePP,e=1,rgb=[idx,rgb[0],rgb[1],rgb[2]],r=1)

    def getPaletteData(self):
        dim=cmds.palettePort(self.palettePP,q=1,dim=1)
        self.outData=[]
        for idx in range(dim[0]*dim[1]):
            cmds.palettePort(self.palettePP,e=1,scc=idx)
            rgb=cmds.palettePort(self.palettePP,q=1,rgb=idx+1)
            self.outData.append([idx,rgb[0],rgb[1],rgb[2]])

    def quitMode(self,*argc):
        self.getPaletteData()
        if self.isModal:
            cmds.layoutDialog(dis=argc[0])
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)

    def show(self):
        if self.isModal:
            ret=cmds.layoutDialog(ui=self.paletteEditorPrompt)
            if(ret=='ok'):
                return self.outData
            else:
                return
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)
            self.winTitle=cmds.window(self.winTitle,w=500,h=500,s=1)
            form=cmds.formLayout('icMainFL')
            self.paletteEditorPrompt(form)
            cmds.showWindow(self.winTitle)

class ToolImageEditor():
    winTitle='GEM_ToolImageEditor'
    def __init__(self,isModal=True):
        self.isModal=isModal
        self.imageSelect=IconChooser()
        self.outData=None
        self.editorType='tool'

    def toolImageEditorPrompt(self,form=None):
        if(form==None):
            form=cmds.setParent(q=1)
        cmds.formLayout(form,e=1,w=700)
        cmds.text('tieToolT',p=form,l='ToolContext :',w=75)
        self.toolContextTSL=cmds.textScrollList('tieToolTLS',p=form,ams=0)
        ctxList=cmds.lsUI(ctx=1)
        for i in ctxList:
            cmds.textScrollList('tieToolTLS',e=1,a=i)
        if(len(ctxList)>0):
            cmds.textScrollList('tieToolTLS',e=1,sii=1)

        if(self.editorType=='toolIamge'):
            chForm=cmds.formLayout('tieToolTF')
            self.imageSelect.iconChoisePrompt(chForm)
            cmds.button(self.imageSelect.OKB,e=1,c=functools.partial(self.quitMode,'ok'))
            cmds.button(self.imageSelect.cancelB,e=1,c=functools.partial(self.quitMode,'cancel'))
            cmds.formLayout(form,e=1,af=[['tieToolT', 'top', 2], ['tieToolT', 'left', 2], ['tieToolTLS', 'left', 2], ['tieToolTLS', 'right', 2], ['tieToolTF', 'right', 2], ['tieToolTF', 'left', 2], ['tieToolTF', 'bottom', 2]],ac=[['tieToolTLS', 'top', 2, 'tieToolT'], ['tieToolTLS', 'bottom', 2, 'tieToolTF']])
        else:
            cmds.text('tieToolTF',l='')
            cmds.button('tieOKB',l='OK',p=form,c=functools.partial(self.quitMode,'ok'))
            cmds.button('tieCancelB',l='Cancel',p=form,c=functools.partial(self.quitMode,'cancel'))
            cmds.formLayout(form,e=1,af=[['tieToolT', 'top', 2], ['tieToolT', 'left', 2], ['tieToolTLS', 'left', 2], ['tieToolTLS', 'right', 2], ['tieToolTF', 'right', 2], ['tieToolTF', 'left', 2], ['tieOKB', 'bottom', 2], ['tieOKB', 'left', 2], ['tieCancelB', 'bottom', 2], ['tieCancelB', 'right', 2]],ap=[['tieOKB', 'right', 0, 50]],ac=[['tieToolTLS', 'top', 2, 'tieToolT'], ['tieCancelB', 'left', 2, 'tieOKB'], ['tieToolTF', 'bottom', 2, 'tieOKB'], ['tieToolTLS', 'bottom', 2, 'tieToolTF']])

    def quitMode(self,*argc):
        toolContext=cmds.textScrollList(self.toolContextTSL,q=1,si=1)
        if(self.editorType=='toolIamge'):
            toolImage=self.imageSelect.selIcon
            if(toolContext!=None and toolImage!=''):
                self.outData=[toolContext[0],toolImage]
        else:
            self.outData=toolContext[0]
        if self.isModal:
            cmds.layoutDialog(dis=argc[0])
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)

    def show(self,editorType='toolIamge'):
        self.editorType=editorType
        if self.isModal:
            ret=cmds.layoutDialog(ui=self.toolImageEditorPrompt)
            if(ret=='ok'):
                return self.outData
            else:
                return
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)
            self.winTitle=cmds.window(self.winTitle,w=700,h=300,s=1)
            form=cmds.formLayout('icMainFL')
            self.toolImageEditorPrompt(form)
            cmds.showWindow(self.winTitle)

class ListEditor():
    winTitle='GEM_ListEditorView'
    def __init__(self,isModal=True):
        self.isModal=isModal
        self.itemNum=8
        self.itemTypeList=['int2','int','string','align']
        self.alignList=['left','center','right']
        self.editType='int2'
        self.DataList=[]

    def listEditorPrompt(self,form=None):
        if(form==None):
            form=cmds.setParent(q=1)
        cmds.formLayout(form,e=1,w=300)
        mainCL=cmds.columnLayout('MainCL',p=form,adj=1)
        self.ctrlList=[]
        for i in range(self.itemNum):
            cmds.rowLayout(nc=len(self.itemTypeList)+2,p=mainCL)
            cmds.text(l='Index%s:'%(i+1),w=60)

            if(self.editType=='int'):
                vCtrl=cmds.intField('lve%sIF#'%i,min=0,v=0,w=200,en=0)
            elif(self.editType=='int2'):
                vCtrl=cmds.intFieldGrp('lve%sIF#'%i,v1=0,v2=0,nf=2,cw2=[100,100],en=0)
            elif(self.editType=='string'):
                vCtrl=cmds.textField('lve%sIF#'%i,tx='',w=200,en=0)
            elif(self.editType=='align'):
                vCtrl=cmds.optionMenu('lve%sIF#'%i,w=200,en=0)
                for cal in self.alignList:
                    cmds.menuItem(l=cal)

            cmds.button(l='Enable',w=60,c=functools.partial(self.enableChange,vCtrl))
            self.ctrlList.append(vCtrl)
        cmds.button('OKB',p=form,l='OK',c=functools.partial(self.quitMode,'ok'))
        cmds.button('CancelB',p=form,l='Cancel',c=functools.partial(self.quitMode,'cancel'))
        cmds.formLayout(form,e=1,af=[['OKB', 'bottom', 2], ['OKB', 'left', 2], ['CancelB', 'right', 2], ['CancelB', 'bottom', 2], ['MainCL', 'top', 2], ['MainCL', 'left', 2], ['MainCL', 'right', 2]],ap=[['OKB', 'right', 0, 50]],ac=[['CancelB', 'left', 2, 'OKB'], ['MainCL', 'bottom', 2, 'OKB']])
        self.initUIByInputData()

    def initUIByInputData(self):
        if(self.inputDataList==None):
            return
        for i in self.inputDataList:
            vCtrl=self.ctrlList[i[0]-1]
            if(self.editType=='int'):
                cmds.intField(vCtrl,e=1,v=i[1],en=1)
            elif(self.editType=='int2'):
                cmds.intFieldGrp(vCtrl,e=1,v1=i[1],v2=i[2],en=1)
            elif(self.editType=='string'):
                cmds.textField(vCtrl,e=1,tx=i[1],en=1)
            elif(self.editType=='align'):
                cmds.optionMenu(vCtrl,q=1,v=i[1],en=1)

    def enableChange(self,*argc):
        vCtrl=argc[0]
        if(self.editType=='int'):
            env=cmds.intField(vCtrl,q=1,en=1)
            cmds.intField(vCtrl,e=1,en=not env)
        elif(self.editType=='int2'):
            env=cmds.intFieldGrp(vCtrl,q=1,en=1)
            cmds.intFieldGrp(vCtrl,e=1,en=not env)
        elif(self.editType=='string'):
            env=cmds.textField(vCtrl,q=1,en=1)
            cmds.textField(vCtrl,e=1,en=not env)
        elif(self.editType=='align'):
            env=cmds.optionMenu(vCtrl,q=1,en=1)
            cmds.optionMenu(vCtrl,e=1,en=not env)

    def getReturnData(self,*argc):
        self.outputDataList=[]
        for i in range(self.itemNum):
            vCtrl=self.ctrlList[i]
            value=None
            if(self.editType=='int'):
                env=cmds.intField(vCtrl,q=1,en=1)
                if(env):value=cmds.intField(vCtrl,q=1,v=1)
            elif(self.editType=='int2'):
                env=cmds.intFieldGrp(vCtrl,q=1,en=1)
                if(env):value=cmds.intFieldGrp(vCtrl,q=1,v=1)
            elif(self.editType=='string'):
                env=cmds.textField(vCtrl,q=1,en=1)
                if(env):value=cmds.textField(vCtrl,q=1,tx=1)
            elif(self.editType=='align'):
                env=cmds.optionMenu(vCtrl,q=1,en=1)
                if(env):value=cmds.optionMenu(vCtrl,q=1,v=1)

            if(value):
                DataList=[i+1]
                if(isinstance(value,list)):
                    DataList.extend(value)
                else:
                    DataList.append(value)
                self.outputDataList.append(DataList)
        if(len(self.outputDataList)==0):
            self.outputDataList=None

    def quitMode(self,*argc):
        self.getReturnData()
        if self.isModal:
            cmds.layoutDialog(dis=argc[0])
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)

    def show(self,editType,itemNum,inputDataList):
        self.itemNum=itemNum
        self.editType=editType
        self.inputDataList=inputDataList

        if self.isModal:
            ret=cmds.layoutDialog(ui=self.listEditorPrompt)
            if(ret=='ok'):
                return self.outputDataList
            else:
                return
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)
            self.winTitle=cmds.window(self.winTitle,w=350,h=420,s=1)
            form=cmds.formLayout('MainFL')
            self.listEditorPrompt(form)
            cmds.showWindow(self.winTitle)

class FormEditor():
    winTitle='GEM_AttachForm'
    def __init__(self,isModal=True):
        self.isModal=isModal
        self.childList=['sssd','ssss2']
        self.childData=None
        self.edge=['top','left','right','bottom']
        self.af='attachForm'
        self.ap='attachPosition'
        self.ac='attachControl'
        self.upDataFunction=None
        self.argc=None

    def formEditorPrompt(self,form=None):
        if(form==None):
            form=cmds.setParent(q=1)

        cmds.gridLayout('afMiddleGL',p=form,cw=150,w=455,ch=75)
        cmds.text(l='')

        cmds.columnLayout('afMidTopCL',adj=1)
        topOff=cmds.intField('afTopOffIF',en=0,max=100,min=0,vis=0,cc=self.valueChange)
        topPos=cmds.intField('afTopPosIF',en=0,max=100,min=0,vis=0,cc=self.valueChange)
        topCtr=cmds.optionMenu('afTopCtrIF',en=0,vis=0,cc=self.valueChange)
        topB=cmds.button('afMidTopB',l='Top',h=25)
        cmds.popupMenu('afMidTopPM')
        cmds.radioMenuItemCollection()
        topI1=cmds.menuItem(l='None',rb=1)
        topI2=cmds.menuItem(l=self.af,rb=0)
        topI3=cmds.menuItem(l=self.ap,rb=0)
        topI4=cmds.menuItem(l=self.ac,rb=0)
        self.topCtrlList=[topOff,topPos,topCtr,topB,[topI1,topI2,topI3,topI4]]
        cmds.button(topB,e=1,c=functools.partial(self.enableChange,self.topCtrlList,'Top'))
        cmds.menuItem(topI1,e=1,c=functools.partial(self.enableUpdata,self.topCtrlList,'Top'))
        cmds.menuItem(topI2,e=1,c=functools.partial(self.enableUpdata,self.topCtrlList,'Top'))
        cmds.menuItem(topI3,e=1,c=functools.partial(self.enableUpdata,self.topCtrlList,'Top'))
        cmds.menuItem(topI4,e=1,c=functools.partial(self.enableUpdata,self.topCtrlList,'Top'))
   
        cmds.text(p='afMiddleGL',l='')

        cmds.columnLayout('afMidLeftCL',p='afMiddleGL',adj=1)
        leftOff=cmds.intField('afLeftOffIF',en=0,max=100,min=0,vis=0,cc=self.valueChange)
        leftPos=cmds.intField('afLeftPosIF',en=0,max=100,min=0,vis=0,cc=self.valueChange)
        leftCtr=cmds.optionMenu('afLeftCtrIF',en=0,vis=0,cc=self.valueChange)
        leftB=cmds.button('afMidLeftB',l='Left',h=25)
        cmds.popupMenu('afMidLeftPM')
        cmds.radioMenuItemCollection()
        leftI1=cmds.menuItem(l='None',rb=1)
        leftI2=cmds.menuItem(l=self.af,rb=0)
        leftI3=cmds.menuItem(l=self.ap,rb=0)
        leftI4=cmds.menuItem(l=self.ac,rb=0)
        self.leftCtrlList=[leftOff,leftPos,leftCtr,leftB,[leftI1,leftI2,leftI3,leftI4]]
        cmds.button(leftB,e=1,c=functools.partial(self.enableChange,self.leftCtrlList,'Left'))
        cmds.menuItem(leftI1,e=1,c=functools.partial(self.enableUpdata,self.leftCtrlList,'Left'))
        cmds.menuItem(leftI2,e=1,c=functools.partial(self.enableUpdata,self.leftCtrlList,'Left'))
        cmds.menuItem(leftI3,e=1,c=functools.partial(self.enableUpdata,self.leftCtrlList,'Left'))
        cmds.menuItem(leftI4,e=1,c=functools.partial(self.enableUpdata,self.leftCtrlList,'Left'))

        cmds.text(p='afMiddleGL',l='')

        cmds.columnLayout('afMidRightCL',p='afMiddleGL',adj=1)
        rightOff=cmds.intField('afRightOffIF',en=0,max=100,min=0,vis=0,cc=self.valueChange)
        rightPos=cmds.intField('afRightPosIF',en=0,max=100,min=0,vis=0,cc=self.valueChange)
        rightCtr=cmds.optionMenu('afRightCtrIF',en=0,vis=0,cc=self.valueChange)
        rightB=cmds.button('afMidRightB',l='Right',h=25)
        cmds.popupMenu('afMidLeftPM')
        cmds.radioMenuItemCollection()
        rightI1=cmds.menuItem(l='None',rb=1)
        rightI2=cmds.menuItem(l=self.af,rb=0)
        rightI3=cmds.menuItem(l=self.ap,rb=0)
        rightI4=cmds.menuItem(l=self.ac,rb=0)
        self.rightCtrlList=[rightOff,rightPos,rightCtr,rightB,[rightI1,rightI2,rightI3,rightI4]]
        cmds.button(rightB,e=1,c=functools.partial(self.enableChange,self.rightCtrlList,'Right'))
        cmds.menuItem(rightI1,e=1,c=functools.partial(self.enableUpdata,self.rightCtrlList,'Right'))
        cmds.menuItem(rightI2,e=1,c=functools.partial(self.enableUpdata,self.rightCtrlList,'Right'))
        cmds.menuItem(rightI3,e=1,c=functools.partial(self.enableUpdata,self.rightCtrlList,'Right'))
        cmds.menuItem(rightI4,e=1,c=functools.partial(self.enableUpdata,self.rightCtrlList,'Right'))

        cmds.text(p='afMiddleGL',l='')

        cmds.columnLayout('afMidBottomCL',p='afMiddleGL',adj=1)
        bottomOff=cmds.intField('afBottomOffIF',en=0,max=100,min=0,vis=0,cc=self.valueChange)
        bottomPos=cmds.intField('afBottomPosIF',en=0,max=100,min=0,vis=0,cc=self.valueChange)
        bottomCtr=cmds.optionMenu('afBottomCtrIF',en=0,vis=0,cc=self.valueChange)
        bottomB=cmds.button('afMidBottomB',l='Bottom',h=25)
        cmds.popupMenu('afMidLeftPM')
        cmds.radioMenuItemCollection()
        bottomI1=cmds.menuItem(l='None',rb=1)
        bottomI2=cmds.menuItem(l=self.af,rb=0)
        bottomI3=cmds.menuItem(l=self.ap,rb=0)
        bottomI4=cmds.menuItem(l=self.ac,rb=0)
        self.bottomCtrlList=[bottomOff,bottomPos,bottomCtr,bottomB,[bottomI1,bottomI2,bottomI3,bottomI4]]
        cmds.button(bottomB,e=1,c=functools.partial(self.enableChange,self.bottomCtrlList,'Bottom'))
        cmds.menuItem(bottomI1,e=1,c=functools.partial(self.enableUpdata,self.bottomCtrlList,'Bottom'))
        cmds.menuItem(bottomI2,e=1,c=functools.partial(self.enableUpdata,self.bottomCtrlList,'Bottom'))
        cmds.menuItem(bottomI3,e=1,c=functools.partial(self.enableUpdata,self.bottomCtrlList,'Bottom'))
        cmds.menuItem(bottomI4,e=1,c=functools.partial(self.enableUpdata,self.bottomCtrlList,'Bottom'))

        cmds.text(p='afMiddleGL',l='')
        self.ctrlIdOM=cmds.optionMenu('afCtrlIdOM',p=form,cc=self.omSelectChange)
        for i in self.childList:
            cmds.menuItem(l=i)

        self.DataMsgF=cmds.textField('afDataMsgF',p=form,ed=0,h=25)
        cmds.button('afOkB',p=form,w=80,l='Ok',h=25,c=functools.partial(self.quitMode,'ok'))
        cmds.button('afCancelB',p=form,w=80,l='Cancel',h=25,c=functools.partial(self.quitMode,'ok'))
        cmds.formLayout(form,e=1,af=[['afCtrlIdOM', 'top', 2], ['afCtrlIdOM', 'left', 2], ['afCtrlIdOM', 'right', 2], ['afDataMsgF', 'bottom', 2], ['afDataMsgF', 'left', 2], ['afCancelB', 'bottom', 2], ['afCancelB', 'right', 2], ['afOkB', 'bottom', 2], ['afMiddleGL', 'left', 2]],ac=[['afOkB', 'right', 2, 'afCancelB'], ['afDataMsgF', 'right', 2, 'afOkB'], ['afMiddleGL', 'top', 2, 'afCtrlIdOM']])
        cmds.formLayout(form,e=1,w=455)

        self.DataCtrlList=[self.topCtrlList,self.leftCtrlList,self.rightCtrlList,self.bottomCtrlList]
        self.initChildData()
        self.omSelectChange()

    def initChildData(self):
        self.childData={}
        for i in self.childList:
            self.childData[i]={self.edge[0]:[],self.edge[1]:[],self.edge[2]:[],self.edge[3]:[]}
        if(self.afDataList!=None):
            for i in self.afDataList:
                ctrlId=i[0]
                edge=i[1]
                if(ctrlId in self.childData):
                    self.childData[ctrlId][edge]=[self.af]+i[2:]
        if(self.apDataList!=None):
            for i in self.apDataList:
                ctrlId=i[0]
                edge=i[1]
                if(ctrlId in self.childData):
                    self.childData[ctrlId][edge]=[self.ap]+i[2:]
        if(self.acDataList!=None):
            for i in self.acDataList:
                ctrlId=i[0]
                edge=i[1]
                if(ctrlId in self.childData):
                    self.childData[ctrlId][edge]=[self.ac]+i[2:]

    def getReturnData(self):
        outAfDataList=[]
        outApDataList=[]
        outAcDataList=[]
        for ctrlId in self.childList:
            ctrlData=self.childData[ctrlId]
            for edge in self.edge:
                vData=ctrlData[edge]
                if(len(vData)>0):
                    if(vData[0]==self.af):
                        outList=[str(ctrlId),edge,vData[1]]
                        outAfDataList.append(outList)
                    elif(vData[0]==self.ap):
                        outList=[str(ctrlId),edge,vData[1],vData[2]]
                        outApDataList.append(outList)
                    elif(vData[0]==self.ac):
                        outList=[str(ctrlId),edge,vData[1],str(vData[2])]
                        outAcDataList.append(outList)

        if(len(outAfDataList)==0):
            outAfDataList=None
        if(len(outApDataList)==0):
            outApDataList=None
        if(len(outAcDataList)==0):
            outAcDataList=None
        return outAfDataList,outApDataList,outAcDataList

    def omSelectChange(self,*argc):
        ctrlId=cmds.optionMenu(self.ctrlIdOM,q=1,v=1)
        if(ctrlId==None):
            return
        for i in range(4):
            edge=self.edge[i]
            ctrlList=self.DataCtrlList[i]
            menuitemList=ctrlList[4]
            curData=self.childData[ctrlId][edge]

            itemList=cmds.optionMenu(ctrlList[2],q=1,ils=1)
            if(itemList!=None):
                for item in itemList:
                    cmds.deleteUI(item,mi=1)
            for item in self.childList:
                if(ctrlId!=item):
                    cmds.menuItem(p=ctrlList[2],l=item)

            cmds.intField(ctrlList[0],e=1,en=0,vis=0)
            cmds.intField(ctrlList[1],e=1,en=0,vis=0)
            cmds.optionMenu(ctrlList[2],e=1,en=0,vis=0)
            cmds.button(ctrlList[3],e=1,l=edge)
            cmds.menuItem(menuitemList[0],e=1,rb=1)
            if(len(curData)>0):
                cmds.button(ctrlList[3],e=1,l=curData[0])
                cmds.intField(ctrlList[0],e=1,v=curData[1],en=1,vis=1)
                cmds.menuItem(menuitemList[1],e=1,rb=1)
                if(curData[0]==self.ap):
                    cmds.intField(ctrlList[1],e=1,v=curData[2],en=1,vis=1)
                    cmds.menuItem(menuitemList[2],e=1,rb=1)
                if(curData[0]==self.ac):
                    cmds.optionMenu(ctrlList[2],e=1,v=curData[2],en=1,vis=1)
                    cmds.menuItem(menuitemList[3],e=1,rb=1)

        self.upDataDataMsgInfo()

    def enableChange(self,*argc):
        menuitemList=argc[0][4]
        itemType=self.getRadioItemType(menuitemList)
        cmds.menuItem(menuitemList[self.itemLoop(itemType)],e=1,rb=1)
        self.enableUpdata(*argc)
    def itemLoop(self,itemType):
        itemType+=1
        if(itemType==4):
            itemType=0
        return itemType
    def getRadioItemType(self,itemList):
        for i in range(len(itemList)):
            if(cmds.menuItem(itemList[i],q=1,rb=1)):
                return i

    def enableUpdata(self,*argc):
        ctrlList=argc[0]
        menuitemList=ctrlList[4]
        typ=argc[1]

        itemType=self.getRadioItemType(menuitemList)
        cmds.intField(ctrlList[0],e=1,en=0,vis=0)
        cmds.intField(ctrlList[1],e=1,en=0,vis=0)
        cmds.optionMenu(ctrlList[2],e=1,en=0,vis=0)

        if(itemType==0):
            cmds.button(ctrlList[3],e=1,l=typ)
        elif(itemType==1):
            cmds.intField(ctrlList[0],e=1,en=1,vis=1)
            cmds.button(ctrlList[3],e=1,l=self.af)
        elif(itemType==2):
            cmds.intField(ctrlList[0],e=1,en=1,vis=1)
            cmds.intField(ctrlList[1],e=1,en=1,vis=1)
            cmds.button(ctrlList[3],e=1,l=self.ap)
        elif(itemType==3):
            cmds.intField(ctrlList[1],e=1,en=1,vis=1)
            cmds.optionMenu(ctrlList[2],e=1,en=1,vis=1)
            cmds.button(ctrlList[3],e=1,l=self.ac)

        self.valueChange()

    def upDataDataMsgInfo(self):
        ctrlId=cmds.optionMenu(self.ctrlIdOM,q=1,v=1)
        if(ctrlId==None):
            return
        outStr=''
        for i in range(4):
            edge=self.edge[i]
            curData=self.childData[ctrlId][edge]
            if(len(curData)>0):
                outData=[ctrlId,edge]
                outData.extend(curData[1:])
                outStr+='%s , '%outData
        cmds.textField(self.DataMsgF,e=1,tx=outStr.strip(' , '))

    def valueChange(self,*argc):
        ctrlId=cmds.optionMenu(self.ctrlIdOM,q=1,v=1)
        for i in range(4):
            ctrlList=self.DataCtrlList[i]
            edge=self.edge[i]

            menuitemList=ctrlList[4]
            itemType=self.getRadioItemType(menuitemList)

            bl=cmds.button(ctrlList[3],q=1,l=1)

            if(itemType>0):
                offV=cmds.intField(ctrlList[0],q=1,v=1)
                if(itemType==1):
                    curData=[bl,offV]
                elif(itemType==2):
                    posV=cmds.intField(ctrlList[1],q=1,v=1)
                    curData=[bl,offV,posV]
                elif(itemType==3):
                    ctrV=cmds.optionMenu(ctrlList[2],q=1,v=1)
                    curData=[bl,offV,ctrV]
                self.childData[ctrlId][edge]=curData
            else:
                self.childData[ctrlId][edge]=[]
        self.upDataDataMsgInfo()
        self.upDataFunction(self.argc,self.getReturnData())

    def quitMode(self,*argc):
        if self.isModal:
            cmds.layoutDialog(dis=argc[0])
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)

    def show(self,upDataFunction,argc,childList,inputDataList):
        self.upDataFunction=upDataFunction
        self.argc=argc
        self.childList=childList
        self.afDataList,self.apDataList,self.acDataList=inputDataList

        if self.isModal:
            ret=cmds.layoutDialog(ui=self.formEditorPrompt)
            if(ret=='ok'):
                return self.getReturnData()
            else:
                return
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)
            self.winTitle=cmds.window(self.winTitle,w=455,s=1)
            form=cmds.formLayout('icMainFL',w=455)
            self.formEditorPrompt(form)
            cmds.showWindow(self.winTitle)

class ScriptEditor():
    winTitle='GEM_ScriptEditorView'
    def __init__(self,UIDesigner,isModal=True):
        self.UIDesigner=UIDesigner
        self.isModal=isModal
        self.inputData=None
    def scriptEditorPrompt(self,form=None):
        if(form==None):
            form=cmds.setParent(q=1)
        cmds.formLayout(form,e=1,w=700 ,h=430)
        cmds.rowLayout('sevOptionRL',nc=3,h=25)
        cmds.iconTextRadioCollection()
        cmds.text(l='Type:',w=38)
        self.scriptITRB=cmds.iconTextRadioButton('sevScriptTypeITRB',st='textOnly',l='Function Address',w=150,sl=not self.inputData[0])
        cmds.iconTextRadioButton(st='textOnly',l='String Script',w=150,sl=self.inputData[0])

        self.cmdCSEF=cmds.cmdScrollFieldExecuter('sevSriptSTF',st=self.getSourceType(),p=form,t=self.inputData[2])

        cmds.button('sevOKB',p=form,l='OK',h=25,c=functools.partial(self.quitMode,'ok'))
        cmds.button('sevCancelB',p=form,l='Cancel',h=25,c=functools.partial(self.quitMode,'cancel'))
        cmds.formLayout(form,e=1,af=[['sevSriptSTF', 'right', 2], ['sevSriptSTF', 'left', 2], ['sevOKB', 'left', 2], ['sevCancelB', 'bottom', 2], ['sevCancelB', 'right', 2], ['sevOKB', 'bottom', 2], ['sevOptionRL', 'top', 2], ['sevOptionRL', 'left', 2], ['sevOptionRL', 'right', 2]],ap=[['sevOKB', 'right', 0, 50]],ac=[['sevCancelB', 'left', 2, 'sevOKB'], ['sevSriptSTF', 'bottom', 2, 'sevOKB'], ['sevSriptSTF', 'top', 2, 'sevOptionRL']])

        self.UIDesigner.cmdSFESet.setAttr(self.cmdCSEF)

    def quitMode(self,*argc):
        typ=not cmds.iconTextRadioButton(self.scriptITRB,q=1,sl=1)
        st=self.getSourceType()
        scriptTx=cmds.cmdScrollFieldExecuter(self.cmdCSEF,q=1,t=1)
        self.inputData=[typ,st,scriptTx]

        if self.isModal:
            cmds.layoutDialog(dis=argc[0])
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)

    def getSourceType(self):
        return self.UIDesigner.getSourceType()

    def show(self,inputData=[0,'']):
        if(inputData==None):
            self.inputData=[0,self.getSourceType(),'']
        else:
            self.inputData=inputData
            if(len(inputData)==2):
                self.inputData=[inputData[0],self.getSourceType(),inputData[1]]

        if self.isModal:
            ret=cmds.layoutDialog(ui=self.scriptEditorPrompt,t=self.getSourceType())
            if(ret=='ok'):
                return self.inputData
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)
            self.winTitle=cmds.window(self.winTitle,w=700,h=420,s=1)
            form=cmds.formLayout('icMainFL')
            self.scriptEditorPrompt(form)
            cmds.showWindow(self.winTitle)

class IconChooser():
    AllIconFormat=['bmp','pcx','tiff','gif','jpg','jpeg','tga','exif','fpx','svg','psd','cdr','pcd','dxf','ufo','eps','png','hdri','ai','raw','xpm']
    SelIconFormat=['bmp','tiff','jpg','jpeg','tga','svg','png','xpm']
    iconSize=32
    winTitle='GEM_IconChooser'
    def __init__(self,isModal=True):
        self.isModal=isModal
        self.pathList=(os.environ['XBMLANGPATH'].split(';'))
        self.pathList.append('Internal Icons')
        self.iconData={}
        self.gLayout=None
        self.selIcon=None
        self.searchText=None
 
    def listPathIcon(self,rootPath,subPath=''):
        if(rootPath=='Internal Icons'):
            return cmds.resourceManager(nf='*.*')
        iconList=[]
        path=rootPath+subPath
        if os.path.isdir(path):
            files = os.listdir(path)
            if not files:
                return iconList
            for i in files:
                if(os.path.isdir(path+'/'+i)):
                    subList=self.listPathIcon(rootPath,subPath+'/'+i)
                    iconList.extend(subList)
                else:
                    filePath=subPath+'/'+i
                    filePath=filePath.strip('/')
                    suf=os.path.splitext(filePath)[1]
                    if(len(suf)<=1):
                        continue
                    suf=suf[1:]
                    suf.lower()
                    if suf in self.SelIconFormat:
                        iconList.append(filePath)

        return iconList

    def iconChoisePrompt(self,form=None):
        if(form==None):
            form=cmds.setParent(q=1)
        cmds.formLayout(form,e=1,w=700 ,h=430)
        self.pathOM=cmds.optionMenu('icPathOM',p=form,cc=self.loadIcons)
        for i in self.pathList:
            cmds.menuItem(l=i)
        self.mainSL=cmds.scrollLayout('icViewGridSL',p=form,cr=1)

        self.iconNameTF=cmds.textField('icNameF',p=form,w=300,ed=0,h=25)
        self.OKB=cmds.button('icOKB',p=form,w=80,h=25,l='OK',c=functools.partial(self.quitMode,'ok'))
        self.cancelB=cmds.button('icCancelB',p=form,w=80,h=25,l='Cancel',c=functools.partial(self.quitMode,'cancel'))
        cmds.iconTextButton('icrefreshB',p=form,w=20,i='out_grid.png',h=20)#'out_grid.png'
        cmds.popupMenu(b=1)
        cmds.radioMenuItemCollection()
        cmds.menuItem(l='16*16',c=functools.partial(self.setIconSize,16),rb=(self.iconSize==16))
        cmds.menuItem(l='32*32',c=functools.partial(self.setIconSize,32),rb=(self.iconSize==32))
        cmds.menuItem(l='64*64',c=functools.partial(self.setIconSize,64),rb=(self.iconSize==64))
        cmds.menuItem(l='128*128',c=functools.partial(self.setIconSize,128),rb=(self.iconSize==128))
        cmds.menuItem(l='256*256',c=functools.partial(self.setIconSize,256),rb=(self.iconSize==256))
        self.searchTF=cmds.textField('icSearchF',p=form,h=20,w=100,aie=1,ec=self.setSearchText)
        self.searchB=cmds.iconTextButton('icSearchB',p=form,w=20,i='zoom.png',h=20,c=self.changeSearchMode)

        cmds.formLayout(form,e=1,ac=[['icOKB', 'right', 2, 'icCancelB'], ['icNameF', 'right', 2, 'icOKB'], ['icViewGridSL', 'top', 2, 'icPathOM'], ['icViewGridSL', 'bottom', 2, 'icNameF'], ['icPathOM', 'right', 2, 'icrefreshB'], ['icPathOM', 'left', 2, 'icrefreshB'], ['icPathOM', 'right', 2, 'icSearchF'], ['icSearchF', 'right', 0, 'icSearchB']],af=[['icPathOM', 'top', 2], ['icPathOM', 'left', 2], ['icCancelB', 'bottom', 2], ['icCancelB', 'right', 2], ['icOKB', 'bottom', 2], ['icNameF', 'bottom', 2], ['icNameF', 'left', 2], ['icViewGridSL', 'left', 2], ['icViewGridSL', 'right', 2], ['icrefreshB', 'top', 2], ['icrefreshB', 'left', 2], ['icSearchF', 'top', 2], ['icSearchB', 'top', 2], ['icSearchB', 'right', 2]])
        self.selIcon=None
        self.loadIcons()

    def setSearchText(self,*argc):
        self.searchText=cmds.textField(self.searchTF,q=1,tx=1)
        if(self.searchText==''):
            self.qiutSearch()
        else:
            cmds.iconTextButton(self.searchB,e=1,i='SP_FileDialogBack.png')
            self.loadIcons()

    def qiutSearch(self,*argc):
        self.searchText=None
        cmds.textField(self.searchTF,e=1,tx='')
        cmds.iconTextButton(self.searchB,e=1,i='zoom.png')
        self.loadIcons()

    def changeSearchMode(self,*argc):
        iconName=cmds.iconTextButton(self.searchB,q=1,i=1)
        if(iconName=='zoom.png'):
            self.setSearchText()
        else:
            self.qiutSearch()

    def setIconSize(self,*size):
        self.iconSize=size[0]
        self.loadIcons()

    def loadIcons(self,*argc):
        rootPath=cmds.optionMenu(self.pathOM,q=1,v=1)
        if(self.gLayout!=None):
            if(cmds.gridLayout(self.gLayout,q=1,ex=1)):
                cmds.deleteUI(self.gLayout)
        iconList=self.listPathIcon(rootPath)
        self.gLayout=cmds.gridLayout('icViewGridFL',p=self.mainSL,nc=700/self.iconSize,cwh=[self.iconSize,self.iconSize])
        self.itbList=[]
        for i in iconList:
            if(self.searchText!=None):  
                if(i.find(self.searchText)==-1):
                    continue

            itb=cmds.iconTextButton(st='iconOnly',p=self.gLayout,i=i,c=functools.partial(self.setCurIconName,i),dcc=functools.partial(self.setCurIconNameDB,i))
            self.itbList.append(itb)

    def setCurIconNameDB(self,*argc):
        self.setCurIconName(*argc)
        self.quitMode('ok')

    def setCurIconName(self,*argc):
        self.selIcon=argc[0]
        cmds.textField(self.iconNameTF,e=1,tx=self.selIcon)

    def quitMode(self,*argc):
        if self.isModal:
            cmds.layoutDialog(dis=argc[0])
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)

    def show(self):
        if self.isModal:
            ret=cmds.layoutDialog(ui=self.iconChoisePrompt)
            if(ret=='ok'):
                return self.selIcon
            else:
                return
        else:
            if(cmds.window(self.winTitle,q=1,ex=1)):cmds.deleteUI(self.winTitle)
            self.winTitle=cmds.window(self.winTitle,w=700,h=420,s=1)
            form=cmds.formLayout('icMainFL')
            self.iconChoisePrompt(form)
            cmds.showWindow(self.winTitle)

class PropertyDelegate():
    BaseNodeList=None
    def __init__(self,UIDesigner,pLayout,baseNode):
        self.UIDesigner=UIDesigner
        self.pLayout=pLayout
        self.UIData={}
        attrList=baseNode['attrList']
        self.className=baseNode['className']
        self.createEditor(self.className,attrList)

    def createEditor(self,className,attrList):
        self.mainRCL=cmds.rowColumnLayout('uidP%sRL'%className,p=self.pLayout,nc=3,cal=[2,'left'],cw=[3,120],cs=[[1,2],[2,2],[3,2]],rs=[[1,2],[2,2],[3,2]])
        #self.activeCL=cmds.columnLayout('uidPA%sCL'%className,p=self.mainRL,adj=1,rs=10)
        #self.attrNameCL=cmds.columnLayout('uidPN%sCL'%className,p=self.mainRL,adj=1,cal='left',rs=5)
        #self.attrValueCL=cmds.columnLayout('uidPV%sCL'%className,p=self.mainRL,adj=0,rs=5)
        for attrIdx,i in enumerate(attrList[1:]):
            attrIdx+=1
            attrType=i['type']
            acFunc=functools.partial(self.valueChangeWrap,i['longName'],'active')
            aCtrl=cmds.iconTextCheckBox(p=self.mainRCL,h=20,w=20,cc=acFunc)
            lCtrl=cmds.text(p=self.mainRCL,l=i['longName'],h=20)

            ccFunc=functools.partial(self.valueChangeWrap,i['longName'],attrType)
            if(attrType=='string'):
                vCtrl=cmds.textField('uidPD%s#'%className,p=self.mainRCL,tx='',w=100,h=18,cc=ccFunc)
            elif(attrType=='boolean' or attrType=='booleanF'):
                vCtrl=cmds.checkBox('uidPD%s#'%className,p=self.mainRCL,l='',h=20,cc=ccFunc)
            elif(attrType=='float'):
                vCtrl=cmds.floatField('uidPD%s#'%className,p=self.mainRCL,h=20,w=50,cc=ccFunc)
                limit=i.get('option',None)
                if(limit and limit[0]):cmds.floatField(vCtrl,e=1,v=limit[0],min=limit[0])
                if(limit and limit[1]):cmds.floatField(vCtrl,e=1,max=limit[1])
            elif(attrType=='int'):
                vCtrl=cmds.intField('uidPD%s#'%className,p=self.mainRCL,h=20,w=50,cc=ccFunc)
                limit=i.get('option',None)
                if(limit and limit[0]):cmds.intField(vCtrl,e=1,v=limit[0],min=limit[0])
                if(limit and limit[1]):cmds.intField(vCtrl,e=1,max=limit[1])
            elif(attrType=='int2'):
                vCtrl=cmds.intFieldGrp('uidPD%s#'%className,p=self.mainRCL,adj=0,nf=2,v1=0,v2=0,h=20,cw2=[50,50],cc=ccFunc)
            elif(attrType=='color' or attrType=='colorA'):
                vCtrl=cmds.iconTextButton('uidPD%s#'%className,p=self.mainRCL,bgc=(1,0,0),w=100,h=20,c=functools.partial(self.selectColor,i['longName'],attrType,attrIdx))
            elif(attrType=='menu'):
                vCtrl=cmds.optionMenu('uidPD%s#'%className,p=self.mainRCL,l='',cc=ccFunc)
                for a in i['option']:
                    cmds.menuItem(l=a)
            elif(attrType=='image'):
                vCtrl=cmds.textFieldButtonGrp('uidPD%s#'%className,p=self.mainRCL,bc=functools.partial(self.selectIcon,i['longName'],attrType),bl='...',ed=0,h=20,adj=1,cc=ccFunc)
                cmds.popupMenu()
                cmds.menuItem(l='Enable editor',c=functools.partial(self.enableIconPathEditor,vCtrl))
            elif(attrType=='script'):
                vCtrl=cmds.button('uidPD%s#'%className,p=self.mainRCL,l='Edit',h=20,w=100,c=functools.partial(self.scriptEditor,i['longName'],attrType,attrIdx))
            elif(attrType=='form'):
                vCtrl=cmds.button('uidPD%s#'%className,p=self.mainRCL,l='Edit',h=20,w=100,c=functools.partial(self.formEditor,i['longName'],attrType))
            elif(attrType in ['list_int2','list_int','list_align','list_string']):
                editorType=attrType.split('_')[-1]
                vCtrl=cmds.button('uidPD%s#'%className,p=self.mainRCL,l='Edit',h=20,w=100,c=functools.partial(self.listEditor,i['longName'],attrType,attrIdx,editorType))
            elif(attrType=='toolImage'):
                vCtrl=cmds.button('uidPD%s#'%className,p=self.mainRCL,l='Edit',h=20,w=100,c=functools.partial(self.toolImageEditor,i['longName'],attrType,attrIdx,'toolImage'))
            elif(attrType=='tool'):
                vCtrl=cmds.button('uidPD%s#'%className,p=self.mainRCL,l='Edit',h=20,w=100,c=functools.partial(self.toolImageEditor,i['longName'],attrType,attrIdx,'tool'))
            elif(attrType=='dock'):
                vCtrl=cmds.button('uidPD%s#'%className,p=self.mainRCL,l='Edit',h=20,w=100,c=functools.partial(self.dockEditor,i['longName'],attrType,attrIdx,'tool'))
            else:
                vCtrl=cmds.text('uidPD%s#'%className,p=self.mainRCL,l='miss..',h=20)

            self.UIData[i['longName']]=[attrType,aCtrl,lCtrl,vCtrl]

    def show(self):
        cmds.rowColumnLayout(self.mainRCL,e=1,vis=1)

    def hide(self):
        cmds.rowColumnLayout(self.mainRCL,e=1,vis=0)

    def enableIconPathEditor(self,*argc):
        ctrlId=argc[0]
        cmds.textFieldButtonGrp(ctrlId,e=1,ed=1)

    def setCurrentCtrlBaseNode(self,baseNodelist):
        attrList=baseNodelist[0]['attrList']
        for i in attrList[1:]:
            self.setPanelValue(i)
        self.BaseNodeList=baseNodelist
    def setPanelValue(self,i):
        attrType=i['type']
        aCtrl=self.UIData[i['longName']][1]
        active=i['active']
        cmds.iconTextCheckBox(aCtrl,e=1,v=active)
        value=i['value']
        vCtrl=self.UIData[i['longName']][3]
        if(value):
            if(attrType=='string'):
                cmds.textField(vCtrl,e=1,tx=value)
            elif(attrType=='boolean' or attrType=='booleanF'):
                if(isinstance(value,list)):value=value[0]
                cmds.checkBox(vCtrl,e=1,v=value)
            elif(attrType=='float'):
                cmds.floatField(vCtrl,e=1,v=value)
            elif(attrType=='int'):
                cmds.intField(vCtrl,e=1,v=value)
            elif(attrType=='int2'):
                cmds.intFieldGrp(vCtrl,e=1,v1=value[0],v2=value[1])
            elif(attrType=='color' or attrType=='colorA'):
                cmds.iconTextButton(vCtrl,e=1,bgc=[value[0],value[1],value[2]])
            elif(attrType=='menu'):
                cmds.optionMenu(vCtrl,e=1,v=value)
            elif(attrType=='image'):
                cmds.textFieldButtonGrp(vCtrl,e=1,tx=value,ed=0)
            elif(attrType=='script'):
                cmds.button(vCtrl,e=1,ann=value[1])
            elif(attrType in ['list_int2','list_int','list_align','list_string','form','toolImage','tool','dock']):
                cmds.button(vCtrl,e=1,ann=str(value))
            else:
                pass
        else:
            if(attrType=='string'):
                cmds.textField(vCtrl,e=1,tx='')
            elif(attrType=='boolean' or attrType=='booleanF'):
                cmds.checkBox(vCtrl,e=1,v=0)
            elif(attrType=='float'):
                limit=i.get('option',None)
                if(limit==None or limit[0]==None):
                    minV=0
                else:
                    minV=limit[0]
                cmds.floatField(vCtrl,e=1,v=minV)
            elif(attrType=='int'):
                limit=i.get('option',None)
                if(limit==None or limit[0]==None):
                    minV=0
                else:
                    minV=limit[0]
                cmds.intField(vCtrl,e=1,v=minV)
            elif(attrType=='int2'):
                cmds.intFieldGrp(vCtrl,e=1,v1=0,v2=0)
            elif(attrType=='color' or attrType=='colorA'):
                cmds.iconTextButton(vCtrl,e=1,bgc=[1,0,0])
            elif(attrType=='menu'):
                cmds.optionMenu(vCtrl,e=1,sl=1)
            elif(attrType=='image'):
                cmds.textFieldButtonGrp(vCtrl,e=1,tx='',ed=0)
            elif(attrType=='script'):
                cmds.button(vCtrl,e=1,ann='')
            elif(attrType in ['list_int2','list_int','list_align','list_string','form','toolImage','tool','dock']):
                cmds.button(vCtrl,e=1,ann='')
            else:
                pass

    def getPanelValue(self,attrType,vCtrl):
        value=None
        if(attrType=='string'):
            value=cmds.textField(vCtrl,q=1,tx=1)
        elif(attrType=='boolean' or attrType=='booleanF'):
            value=cmds.checkBox(vCtrl,q=1,v=1)
        elif(attrType=='float'):
            value=cmds.floatField(vCtrl,q=1,v=1)
        elif(attrType=='int'):
            value=cmds.intField(vCtrl,q=1,v=1)
        elif(attrType=='int2'):
            v1=cmds.intFieldGrp(vCtrl,q=1,v1=1)
            v2=cmds.intFieldGrp(vCtrl,q=1,v2=1)
            value=[v1,v2]
        elif(attrType=='color'):
            value=cmds.iconTextButton(vCtrl,q=1,bgc=1)
        elif(attrType=='colorA'):
            value=cmds.iconTextButton(vCtrl,q=1,bgc=1)
            value=[value[0],value[1],value[2],0.25]
        elif(attrType=='menu'):
            value=cmds.optionMenu(vCtrl,q=1,v=1)
        return value

    def dockEditor(self,*argc):
        longName=argc[0]
        attrType=argc[1]
        attrIdx=argc[2]
        retList=self.getFlagValue(attrIdx)
        retList=self.UIDesigner.dockEditor.show(retList)
        if(retList!=None):
            vCtrl=self.UIData[longName][3]
            cmds.button(vCtrl,e=1,ann=retList[1])
            self.valueChangeWrap(longName,attrType,retList)

    def toolImageEditor(self,*argc):
        longName=argc[0]
        attrType=argc[1]
        attrIdx=argc[2]
        editorType=argc[3]
        retList=self.getFlagValue(attrIdx)
        retList=self.UIDesigner.toolImageEditor.show(editorType)
        if(retList!=None):
            vCtrl=self.UIData[longName][3]
            cmds.button(vCtrl,e=1,ann=retList[1])
            self.valueChangeWrap(longName,attrType,retList)

    def listEditor(self,*argc):
        longName=argc[0]
        attrType=argc[1]
        attrIdx=argc[2]
        editorType=argc[3]

        className=self.getClassName()
        oldDataList=self.getFlagValue(attrIdx)
        itemNum=6
        if(longName=='paneSize' and className=='paneLayout'):
            cn=self.getFlagValue('configuration')
            itemNum=self.getPaneSizeItemNum(cn)
        if(longName=='label' and className=='scriptTable'):
            itemNum=self.getFlagValue('columns')
        if(className in ['rowLayout','shelfTabLayout','tabLayout']):
            if(longName in ['columnWidth','columnAlign','tabLabelIndex']):
                itemNum=len(self.UIDesigner.gem_getSelectItemChild())
        if(className=='rowColumnLayout'):
            if(longName in ['columnWidth','columnAlign','columnSpacing']):
                itemNum=self.getFlagValue('numberOfColumns')
            if(longName in ['rowHeight','rowAlign','rowSpacing']):
                itemNum=self.getFlagValue('numberOfRows')
        print(editorType,itemNum,oldDataList)

        outDataList=self.UIDesigner.listEditor.show(editorType,itemNum,oldDataList)
        if(outDataList!=None):
            vCtrl=self.UIData[longName][3]
            cmds.button(vCtrl,e=1,ann=str(outDataList))
            self.valueChangeWrap(longName,attrType,outDataList)

    def getPaneSizeItemNum(self,cn):
        if(cn==None):return 4
        itemNum=1
        if(cn in ['horizontal2','vertical2']):itemNum=2
        if(cn in ['horizontal3','vertical3','top3','left3','bottom3','right3']):itemNum=3
        if(cn in ['horizontal4','vertical4','top4','left4','bottom4','right4','quad']):itemNum=4
        return itemNum

    def getFlagValue(self,flag):
        baseNode=self.BaseNodeList[0]
        attrList=baseNode['attrList']
        if(isinstance(flag,str)):
            for i in attrList:
                if(i['longName']==flag):
                    return i['value']
        elif(isinstance(flag,int)):
            return attrList[flag]['value']
    def getClassName(self):
        baseNode=self.BaseNodeList[0]
        return baseNode['className']

    def formEditor(self,*argc):
        afDataList=self.getFlagValue('attachForm')
        apDataList=self.getFlagValue('attachPosition')
        acDataList=self.getFlagValue('attachControl')

        childList=self.UIDesigner.gem_getSelectItemChild()
        outDataList=self.UIDesigner.formEditor.show(self.formEditorUpData,argc,childList,[afDataList,apDataList,acDataList])
        self.formEditorUpData(argc,outDataList)

    def formEditorUpData(self,argc,outDataList):
        longName=argc[0]
        attrType=argc[1]
        if(outDataList!=None):
            afDataList,apDataList,acDataList=outDataList
            if(afDataList!=None):
                vCtrl=self.UIData['attachForm'][3]
                cmds.button(vCtrl,e=1,ann=str(outDataList))
                self.valueChangeWrap('attachForm',attrType,afDataList)
            else:
                self.valueChangeWrap('attachForm','active',False)
            if(apDataList!=None):
                vCtrl=self.UIData['attachPosition'][3]
                cmds.button(vCtrl,e=1,ann=str(outDataList))
                self.valueChangeWrap('attachPosition',attrType,apDataList)
            else:
                self.valueChangeWrap('attachPosition','active',False)
            if(acDataList!=None):
                vCtrl=self.UIData['attachControl'][3]
                cmds.button(vCtrl,e=1,ann=str(outDataList))
                self.valueChangeWrap('attachControl',attrType,acDataList)
            else:
                self.valueChangeWrap('attachControl','active',False)
            self.refreshWindow()

    def scriptEditor(self,*argc):
        longName=argc[0]
        attrType=argc[1]
        attrIdx=argc[2]
        scriptText=self.getFlagValue(attrIdx)
        scriptText=self.UIDesigner.scriptEditor.show(scriptText)
        if(scriptText!=None):
            vCtrl=self.UIData[longName][3]
            cmds.button(vCtrl,e=1,ann=scriptText[1])
            self.valueChangeWrap(longName,attrType,scriptText)

    def selectIcon(self,*argc):
        iconName=self.UIDesigner.iconChooser.show()
        if(iconName!=None):
            longName=argc[0]
            attrType=argc[1]
            vCtrl=self.UIData[longName][3]
            cmds.textFieldButtonGrp(vCtrl,e=1,tx=iconName)
            self.valueChangeWrap(longName,attrType,iconName)

    def selectColor(self,*argc):
        longName=argc[0]
        attrType=argc[1]
        attrIdx=argc[2]
        cValue=self.getFlagValue(attrIdx)
        if(cValue==None):
            ret=cmds.colorEditor()
        else:
            ret=cmds.colorEditor(rgb=cValue[:3])
        buf=ret.split()
        if(buf[3]=='1'):
            longName=argc[0]
            attrType=argc[1]
            value=cmds.colorEditor(q=1, rgb=1)
            vCtrl=self.UIData[longName][3]

            if(attrType=='colorA'):
                if(cValue==None):
                    alpha=self.UIDesigner.alphaEditor.show()
                else:
                    alpha=self.UIDesigner.alphaEditor.show(cValue[-1])
                value=[value[0],value[1],value[2],alpha]
            cmds.iconTextButton(vCtrl,e=1,bgc=value[:3],en=1)
            self.valueChangeWrap(longName,attrType,value)

    def valueChangeWrap(self,*argc):
        longName=argc[0]
        attrType=argc[1]

        aCtrl=self.UIData[longName][1]
        vCtrl=self.UIData[longName][3]

        active=True
        if(attrType=='active'):
            active=argc[2]
            if(active):
                value=self.getPanelValue(self.UIData[longName][0],vCtrl)
            else:
                value=None

        else:
            if(len(argc)==3):
                value=argc[2]
            else:
                value=argc[2:]

        cmds.iconTextCheckBox(aCtrl,e=1,v=active)
        self.valueChange(longName,active,value)

    def valueChange(self,longName,active,value):
        if(self.BaseNodeList==None):
            return
        typ=None
        for baseNode in self.BaseNodeList:
            attrList=baseNode['attrList']
            for i in attrList:

                if(i['longName']==longName):
                    if(i['mode']=='s'):
                        return
                    i['active']=active
                    i['value']=value
                    typ=i['type']
        if(typ!='form'):
            self.refreshWindow()

    def refreshWindow(self):
        self.UIDesigner.gem_generateCode()
        self.UIDesigner.gem_showItemProperty()
        self.UIDesigner.addUndoAndClearRedo('valueChange')

class CmdSFESet():
    def __init__(self):
        self.st='python'    #sourceType
        self.sln=True       #showLineNumbers
        self.cco=False       #commandCompletion
        self.sth=False       #showTooltipHelp
        self.opc=False       #objectPathCompletion
    def setAttr(self,ctrlId):
        if(ctrlId!=None and cmds.cmdScrollFieldExecuter(ctrlId,q=1,ex=1)):
            cmds.cmdScrollFieldExecuter(ctrlId,e=1,sln=self.sln,cco=self.cco,sth=self.sth,opc=self.opc)

class UIDesigner():
    winTitle='GEM_UIDesigner'
    modulesList=['Layouts','Controls','Menus','Customs']

    def __init__(self,path):
        self.uidFilePath=path#'C:/Users/sundongdong/Desktop/uidFile'

        self.cmdSFESet=CmdSFESet()
        self.iconChooser=IconChooser(True)
        self.scriptEditor=ScriptEditor(self,True)
        self.formEditor=FormEditor(True)
        self.listEditor=ListEditor(True)
        self.toolImageEditor=ToolImageEditor(True)
        self.dockEditor=DockEditor(True)
        self.alphaEditor=AlphaEditor(True)
        self.generateOptionEditor=GenerateOptionEditor(True)
        self.nameRegex=re.compile('^[\w][\w]*$')

        self.propertyDelegateData={}
        self.uidGLData=None
        self.widgetBoxITBList=None
        self.copyList=None
        self.replaceList=None
        self.currentFilePath=None
        self.UICmdSFE=None
        self.UIFuncSFE=None

        self.undoDataList=[]
        self.redoDataList=[]
        self.winTLC=None
        self.CmdTextPos={}
        self.linesep='\n'
        self.setupUI()

    def setupUI(self):
        if(cmds.window(self.winTitle,q=1,ex=1)):
            cmds.deleteUI(self.winTitle)
        cmds.window(self.winTitle,title='GM UI Designer',h=700,w=1000,mb=1)
        cmds.menu('uidFileM',label='File', tearOff=True )
        cmds.menuItem( label='New',c=self.newFile)
        cmds.menuItem( label='Open',c=self.openFile)
        cmds.menuItem( label='Save',c=self.saveFile)
        cmds.menuItem( label='Save as',c=self.saveFileAs)
        cmds.menuItem( divider=True )
        #cmds.menuItem( label='Convert',sm=1)
        #cmds.menuItem('uidMToPM',label='Mel to Python')
        #cmds.menuItem('uidPToMM',label='Python to Mel')
        #cmds.menuItem( divider=True ,p='uidFileM')

        cmds.menuItem( label='Quit',p='uidFileM')
        cmds.menu( label='Help', helpMenu=True )
        cmds.menuItem(l='Original: SunDongDong')
        cmds.menuItem(l='Updated: Guy Micciche')
        cmds.menuItem(l='E-mail: king.guy@outlook.com')

        cmds.formLayout('uidMainFL')
        #cmds.frameLayout('uidToolBarTL',h=32,lv=0)
        cmds.tabLayout('uidToolBarTL',h=32,tv=0)

        # ToolBar==========================================================================
        cmds.rowLayout('uidToolBarRL',nc=20)
        cmds.iconTextButton(p='uidToolBarRL',i='ShortOpenBar.png')

        cmds.iconTextButton(p='uidToolBarRL',i='SP_FileIcon.png',ann='New',w=23,h=23,c=self.newFile)
        cmds.iconTextButton(p='uidToolBarRL',i='SP_DirOpenIcon.png',ann='Open',w=23,h=23,c=self.openFile)
        cmds.iconTextButton('uidFileSaveB',p='uidToolBarRL',i='SP_DriveFDIcon.png',ann='Save',w=23,h=23,c=self.saveFile)

        #cmds.separator(hr=0,h=23,w=5)
        cmds.iconTextButton(p='uidToolBarRL',i='ShortOpenBar.png')
        cmds.iconTextButton('uidUndoITB',p='uidToolBarRL',i='rotateUVccw.png',w=23,h=23,c=self.undo)
        cmds.iconTextButton('uidRedoITB',p='uidToolBarRL',i='rotateUVcw.png',w=23,h=23,c=self.redo)

        cmds.iconTextButton(p='uidToolBarRL',i='ShortOpenBar.png')

        cmds.iconTextRadioCollection()
        cmds.iconTextRadioButton('uidPyModeITRB',p='uidToolBarRL',sl=1,i='pythonFamily.xpm',iol='py',ann='Python Mode',w=23,h=23,onc=functools.partial(self.setSourceType,'python'))
        cmds.iconTextRadioButton('uidMelModeITRB',p='uidToolBarRL',i='commandButton.xpm',iol='mel',ann='Mel Mode',w=23,h=23,onc=functools.partial(self.setSourceType,'mel'))
        cmds.iconTextCheckBox('uidWinCacheITB',p='uidToolBarRL',v=1,i='deleteCacheHistory.png',ann='Delete Window Cache',w=23,h=23,cc=self.gem_generateCode)
        cmds.iconTextCheckBox('uidDebugModeITB',p='uidToolBarRL',v=0,i='rvIPRStop.png',ann='Debug Code',w=23,h=23,cc=self.gem_generateCode)
        cmds.iconTextButton(p='uidToolBarRL',i='refEdFileList.png',ann='Generate Option',w=23,h=23,c=self.setGenrateOption)
        #cmds.popupMenu('uidGenrateOptionPM',b=1)
        #cmds.menuItem(l='Flag',sm=1)
        #cmds.radioMenuItemCollection()
        #cmds.menuItem(l='Short Name',rb=1,c=functools.partial(self.setFlagNameType,'short'))
        #cmds.menuItem(l='Long Name',rb=0,c=functools.partial(self.setFlagNameType,'long'))

        #cmds.menuItem(d=1,p='uidGenrateOptionPM')
        #cmds.radioMenuItemCollection()
        #cmds.menuItem(l='Boolean Type',p='uidGenrateOptionPM',sm=1)
        #cmds.menuItem(l='True | False',rb=1,c=functools.partial(self.setBoolType,'bool'))
        #cmds.menuItem(l='0 | 1',rb=0,c=functools.partial(self.setBoolType,'int'))

        #cmds.menuItem(d=1,p='uidGenrateOptionPM')
        #cmds.radioMenuItemCollection()
        #cmds.menuItem(l='Indent',p='uidGenrateOptionPM',sm=1)
        #cmds.menuItem(l='Tab',rb=1,c=functools.partial(self.setIndentType,'\t'))
        #cmds.menuItem(l='4 Space',rb=0,c=functools.partial(self.setIndentType,'    '))

        #cmds.menuItem(d=1,p='uidGenrateOptionPM')
        #cmds.radioMenuItemCollection()
        #cmds.menuItem(l='Control Name',p='uidGenrateOptionPM',sm=1)
        #cmds.menuItem(l='Need',rb=1,c=functools.partial(self.setControlIdType,'need'))
        #cmds.menuItem(l='Force All',rb=0,c=functools.partial(self.setControlIdType,'all'))

        #cmds.menuItem(d=1,p='uidGenrateOptionPM')
        #cmds.radioMenuItemCollection()
        #cmds.menuItem(l='Function',p='uidGenrateOptionPM',sm=1)
        #cmds.menuItem(l='None',rb=1,c=functools.partial(self.setFunctionType,'None'))
        #cmds.menuItem(l='Add To Output',rb=0,c=functools.partial(self.setFunctionType,'Add'))

        #cmds.separator(hr=0,h=23,w=5)
        cmds.iconTextButton(p='uidToolBarRL',i='ShortOpenBar.png')
        cmds.iconTextButton(p='uidToolBarRL',i='clearHistory.png',w=23,h=23,c=self.clearHistory)
        cmds.iconTextButton(p='uidToolBarRL',i='showLineNumbers.png',w=23,h=23,c=self.showLine)
        cmds.iconTextButton(p='uidToolBarRL',i='toolSettings.png',w=23,h=23)
        cmds.popupMenu(b=1)
        cmds.menuItem(l='Command Completion',cb=self.cmdSFESet.cco,c=self.commandCompletion)
        cmds.menuItem(l='ObjectPath Completion',cb=self.cmdSFESet.sth,c=self.objectPathCompletion)
        cmds.menuItem(l='Show Tooltip Help',cb=self.cmdSFESet.opc,c=self.showTooltipHelp)

        cmds.iconTextButton(p='uidToolBarRL',i='ShortOpenBar.png')
        cmds.iconTextButton(p='uidToolBarRL',i='redrawPaintEffects.png',w=23,h=23,c=self.gem_refreshWindow)

        cmds.paneLayout('uidMiddlePL',p='uidMainFL',ps=[[3, 20, 20], [1, 20, 20], [2, 30, 30]],cn='vertical4')
        cmds.paneLayout('uidMidLeftPL',cn='horizontal4')

        # WidgetBox==========================================================================
        cmds.formLayout('uidWidgetBoxFL',en=0)
        cmds.textField('uidSearchF',p='uidWidgetBoxFL',tx='',w=250,cc=self.widgetBoxSearch)
        cmds.iconTextButton('uidSearchB',p='uidWidgetBoxFL',w=20,i='zoom.png',h=20,c=self.clearSearch)

        cmds.scrollLayout('uidWidgetBoxSL',p='uidWidgetBoxFL',cr=1)
        #cmds.tabLayout('uidWidgetBoxMainTL')
        cmds.formLayout('uidWidgetBoxFL',e=1,af=[['uidWidgetBoxSL', 'left', 0], ['uidWidgetBoxSL', 'right', 0], ['uidWidgetBoxSL', 'bottom', 0],['uidSearchF', 'top', 0],['uidSearchF', 'left', 0],['uidSearchB', 'right', 0],['uidSearchB', 'top', 0]], ac=[['uidWidgetBoxSL', 'top', 0,'uidSearchF'],['uidSearchF', 'right', 0,'uidSearchB']])

        #cmds.columnLayout('uidWidgetBoxMainCL',adj=1)

        # Hierarchy==========================================================================
        cmds.formLayout('uidHierarchyFL',p='uidMidLeftPL',en=0)
        cmds.rowLayout('uidTreeToolRL',h=23,nc=8)
        cmds.iconTextButton('uidSufNameB',p='uidTreeToolRL',i='quickRename.png',ann='Reaname Suffix',w=35,h=23,c=self.renameSuffixName)
        cmds.iconTextButton('uidTreeReplaceB',p='uidTreeToolRL',i='syncOn.png',ann='Replace Layout',w=23,h=23)
        cmds.popupMenu('uidTreeReplacePM',b=1)

        cmds.iconTextButton('uidTreeMoveUpB',p='uidTreeToolRL',i='moveButtonUp.png',ann='Move Up',w=23,h=23,c=functools.partial(self.moveControl,'Up'))
        cmds.iconTextButton('uidTreeMoveDnB',p='uidTreeToolRL',i='moveButtonDown.png',ann='Move Down',w=23,h=23,c=functools.partial(self.moveControl,'Down'))

        cmds.iconTextButton(p='uidTreeToolRL',i='cutUV.png',ann='cut',w=23,h=23,c=self.cutControl)
        cmds.iconTextButton(p='uidTreeToolRL',i='copyUV.png',ann='Copy',w=23,h=23,c=self.copyControl)
        cmds.iconTextButton('uidTreePasteB',p='uidTreeToolRL',i='pasteUV.png',ann='Paste',en=0,w=23,h=23,c=self.pasteControl)
        cmds.iconTextButton(p='uidTreeToolRL',i='removeRenderable.png',ann='Delete',w=23,h=23,c=self.deleteControl)

        cmds.treeView('uidHierarchyTV',p='uidHierarchyFL',elc=self.treeItemRenameLabel,scc=self.gem_treeSelectChange,ecc=self.treeViewExpendChange,dad=self.treeItemHierarchyChange)
        #dad=gem_dragAndDrop,elc=gem_treeViewRenameLabel,scc='gem_treeViewSelectChange()',ecc=gem_treeViewExpendChange
        cmds.popupMenu()
        cmds.menuItem(l='Copy',c=self.copyControl)
        cmds.menuItem(l='Paste',c=self.pasteControl)
        cmds.menuItem(d=1)
        cmds.menuItem(l='Cut',c=self.cutControl)
        cmds.menuItem(d=1)
        cmds.menuItem(l='Delete',c=self.deleteControl)
        #cmds.tabLayout('uidWidgetBoxMainTL')

        cmds.formLayout('uidHierarchyFL',e=1,af=[['uidHierarchyTV', 'left', 0], ['uidHierarchyTV', 'right', 0], ['uidHierarchyTV', 'bottom', 0],['uidTreeToolRL', 'top', 0],['uidTreeToolRL', 'right', 0]], ac=[['uidHierarchyTV', 'top', 0,'uidTreeToolRL']])

        # CodeView==========================================================================
        cmds.paneLayout('uidCodeViewPL',p='uidMiddlePL',cn='horizontal4')
        cmds.cmdScrollFieldReporter('uidCmdReporter')
        cmds.tabLayout('uidCmdExecuterTL')
        cmds.popupMenu(mm=1)
        cmds.menuItem(l='New Tab...',rp='N',c=functools.partial(self.newCmdExecuter,'default'))
        cmds.menuItem(ob=1,c=functools.partial(self.newCmdExecuter,'query'))
        cmds.menuItem(l='Delete Current Tab',rp='SW',c=self.deleteCmdExecuter)
        cmds.menuItem(l='Save To File',rp='SE',c=self.saveCurrentTabCmdToFile)

        # Property==========================================================================
        cmds.scrollLayout('uidPropertySL',p='uidMiddlePL',en=0,cr=1)
        cmds.columnLayout('uidPropertyMainCL',adj=1)
        cmds.frameLayout('uidPAttrFL',l='Property')
        # cmds.columnLayout('uidPAttrMainFL')

        # cmds.frameLayout('uidPCommandFL',p='uidPropertyMainCL',l='Command')
        # cmds.columnLayout('uidPCommandMainCL')

        cmds.frameLayout('uidHelpFL',p='uidMainFL',lv=0,w=1,h=20)
        cmds.helpLine()

        cmds.formLayout('uidMainFL',e=1,ac=[['uidMiddlePL', 'top', 0, 'uidToolBarTL'],['uidMiddlePL', 'bottom', 0, 'uidHelpFL']],af=[['uidHelpFL', 'bottom', 0],['uidHelpFL', 'left', 0],['uidHelpFL', 'right', 0],['uidToolBarTL', 'top', 0], ['uidToolBarTL', 'left', 0], ['uidToolBarTL', 'right', 0], ['uidMiddlePL', 'left', 0], ['uidMiddlePL', 'right', 0]])

        self.gem_loadUIWidget()
        self.updateUndoRedoBtn()
        self.updateCmdExecuter()

    #undo redo============================================
    def undo(self,*argc):
        self.redoDataList.append(self.undoDataList.pop())
        dateStr=self.undoDataList.pop()
        self.uidGLData=self.gem_eval(dateStr)

        self.updateUndoRedoBtn()
        self.gem_refreshWindow()
        self.gem_treeSelectChange()
        self.updateFunctionCmd()
        self.addUndoData()

    def redo(self,*argc):
        dateStr=self.redoDataList.pop()
        self.uidGLData=self.gem_eval(dateStr)
        self.updateUndoRedoBtn()
        self.gem_refreshWindow()
        self.gem_treeSelectChange()
        self.addUndoData()

    def updateUndoRedoBtn(self):
        if(cmds.iconTextButton('uidUndoITB',q=1,ex=1)):
            cmds.iconTextButton('uidUndoITB',e=1,en=len(self.undoDataList)>1)
            cmds.iconTextButton('uidRedoITB',e=1,en=len(self.redoDataList))

    def clearUndoRedo(self):
        self.undoDataList=[]
        self.redoDataList=[]
        self.updateUndoRedoBtn()

    def addUndoAndClearRedo(self,*argc):
        self.redoDataList=[]
        self.undoDataList.append(str(self.uidGLData))
        self.updateUndoRedoBtn()
    def addUndoData(self,*argc):
        self.undoDataList.append(str(self.uidGLData))
        self.updateUndoRedoBtn()

    def setGenrateOption(self,*argc):
        if(self.uidGLData==None):
            return
        gData=self.generateOptionEditor.show(self.uidGLData.get('generateOptions',None))
        self.uidGLData['generateOptions']=gData
        self.gem_generateCode()
    def getGenrateOption(self,typ):
        gData=self.uidGLData.get('generateOptions',None)
        if(gData==None):
            self.uidGLData['generateOptions']=self.generateOptionEditor.getDefultData()
        gData=self.uidGLData.get('generateOptions',None)
        return gData[typ]

    def setSourceType(self,*argc):
        if(self.uidGLData==None):
            return
        st=argc[0]
        if(st==self.getSourceType()):
            return
        ret=cmds.confirmDialog( title='Confirm', message='If you convert the source type, function and the flag needs to be rewritten . Are you sure convert?', button=['Yes','Cancel'], defaultButton='Yes', cancelButton='Cancel', dismissString='Cancel' )
        if(ret!='Yes'):
            self.updateSourceTypeBtn()
            return
        self.uidGLData['sourceType']=argc[0]
        self.updateCmdExecuter()
        self.clearUndoRedo()
        self.gem_generateCode()

    def updateSourceTypeBtn(self):
        if(self.getSourceType()=='python'):
             cmds.iconTextRadioButton('uidPyModeITRB',e=1,sl=1)
        else:
            cmds.iconTextRadioButton('uidMelModeITRB',e=1,sl=1)

    def getSourceType(self):
        if(self.uidGLData==None):
            if(cmds.iconTextRadioButton('uidPyModeITRB',q=1,sl=1)):
                return 'python'
            else:
                return 'mel'
        return self.uidGLData.get('sourceType','python')

    def setFunctionData(self,*argc):
        st=cmds.cmdScrollFieldExecuter(self.UIFuncSFE,q=1,st=1)
        scriptTx=cmds.cmdScrollFieldExecuter(self.UIFuncSFE,q=1,t=1)
        self.uidGLData['function']=[st,scriptTx]
        self.addUndoAndClearRedo('setFunctionData')
        self.gem_generateCode()

    def clearFunctionData(self,*argc):
        ret=cmds.confirmDialog( t='Clear Function', m='Are you sure to empty function?', b=['Yes','No'], db='No', cb='No', ds='No' )
        if(ret=='No'):
            return
        cmds.cmdScrollFieldExecuter(self.UIFuncSFE,e=1,t='')
        self.uidGLData['function']=None
        self.addUndoAndClearRedo('clearFunctionData')
        self.gem_generateCode()

    def getFuncionStr(self):
        if(self.uidGLData==None):
            return ''
        sData=self.uidGLData.get('function',None)
        if(sData==''):
            self.uidGLData['function']=None
            return ''
        if(sData==None):
            return ''
        st=sData[0]
        if(st!=self.getSourceType()):
            return ''
        return sData[1]

    def updateFunctionCmd(self):
        cmds.cmdScrollFieldExecuter(self.UIFuncSFE,e=1,t=self.getFuncionStr())

    def updateCmdExecuter(self):
        chList=cmds.tabLayout('uidCmdExecuterTL',q=1,ca=1)
        if(chList!=None):
            for i in chList:
                cmds.deleteUI(i)
        self.customCmdList=[]

        self.UICmdSFE=cmds.cmdScrollFieldExecuter('uidUICodeSFE',p='uidCmdExecuterTL',st=self.getSourceType())
        cmds.formLayout('uidFuncCmdFL',p='uidCmdExecuterTL')
        self.UIFuncSFE=cmds.cmdScrollFieldExecuter('uidFunctionCodeSFE',st=self.getSourceType())
        cmds.button('uidClearFuncB',l='Clear',w=38,c=self.clearFunctionData)
        cmds.button('uidUpdateFuncB',l='Update To Output',c=self.setFunctionData)
        cmds.formLayout('uidFuncCmdFL',e=1,af=[['uidUpdateFuncB', 'right', 0],['uidUpdateFuncB', 'bottom', 0],['uidClearFuncB', 'left', 0], ['uidClearFuncB', 'bottom', 0], ['uidFunctionCodeSFE', 'top', 0], ['uidFunctionCodeSFE', 'left', 0], ['uidFunctionCodeSFE', 'right', 0]],ac=[['uidFunctionCodeSFE', 'bottom', 2, 'uidClearFuncB'],['uidUpdateFuncB', 'left', 2,'uidClearFuncB']])

        cmds.tabLayout('uidCmdExecuterTL',e=1,tli=[(1,'Output'),(2,'Function')])
        chList=cmds.tabLayout('uidCmdExecuterTL',q=1,ca=1)
        if(len(chList)>1):
            cmds.tabLayout('uidCmdExecuterTL',e=1,mt=[1,len(chList)])
            cmds.tabLayout('uidCmdExecuterTL',e=1,mt=[1,len(chList)])

        self.customCmdList.append(self.UICmdSFE)
        self.customCmdList.append(self.UIFuncSFE)

        cmds.cmdScrollFieldExecuter(self.UICmdSFE,e=1,t=os.linesep)
        self.linesep=cmds.cmdScrollFieldExecuter('uidUICodeSFE',q=1,t=1)

        self.updateCmdOption()

    def newCmdExecuter(self,*argc):
        typ=argc[0]
        if(typ=='query'):
            ret=cmds.confirmDialog( t='source Type', m='Specify executer source language:', b=['Mel','Python','Cancel'], db='Mel', cb='Cancel', ds='Cancel' )
            if(ret=='Cancel'):
                return
            st=ret.lower()
        else:
            st=self.getSourceType()
        cCmd=cmds.cmdScrollFieldExecuter(p='uidCmdExecuterTL',st=st)
        chList=cmds.tabLayout('uidCmdExecuterTL',q=1,ca=1)
        cmds.tabLayout('uidCmdExecuterTL',e=1,tli=[(len(chList),st)],sti=len(chList))
        self.customCmdList.append(cCmd)
        self.updateCmdOption()

    def deleteCmdExecuter(self,*argc):
        chList=cmds.tabLayout('uidCmdExecuterTL',q=1,ca=1)
        idx=cmds.tabLayout('uidCmdExecuterTL',q=1,sti=1)
        idx-=1
        if(idx<2):return
        cmds.deleteUI(chList[idx])
        del self.customCmdList[idx]

    def saveCurrentTabCmdToFile(self,*argc):
        chList=cmds.tabLayout('uidCmdExecuterTL',q=1,ca=1)
        idx=cmds.tabLayout('uidCmdExecuterTL',q=1,sti=1)
        idx-=1
        cmds.cmdScrollFieldExecuter(chList[idx],e=1,sv=1)

    def showLine(self):
        self.cmdSFESet.sln=not self.cmdSFESet.sln
        self.updateCmdOption()

    def commandCompletion(self,*argc):
        self.cmdSFESet.cco=argc[0]
        self.updateCmdOption()

    def showTooltipHelp(self,*argc):
        self.cmdSFESet.sth=argc[0]
        self.updateCmdOption()

    def objectPathCompletion(self,*argc):
        self.cmdSFESet.opc=argc[0]
        self.updateCmdOption()

    def updateCmdOption(self):
        for i in self.customCmdList:
            self.cmdSFESet.setAttr(i)

    def clearHistory(self):
        cmds.cmdScrollFieldReporter('uidCmdReporter',e=1,clr=1)
        self.clearUndoRedo()

    #file editor============================================
    def newFile(self,*argc):
        self.clearHistory()
        self.saveFile()
        path=cmds.fileDialog2(ff='UIDesigner Files (*.uid)',fm=0)
        if(path==None):return
        self.setFilePath(path[0])
        self.close()
        self.enableUI(1)
        self.gem_initTreeView()
        self.saveFile()
        sys.stdout.write('Save success .')

    def getUIFuncName(self):
        baseName=os.path.basename(self.currentFilePath)
        fName=os.path.splitext(baseName)[0]
        return fName

    def openFile(self):
        self.clearHistory()
        self.saveFile()
        path=cmds.fileDialog2(ff='UIDesigner Files (*.uid)',fm=1)
        if(path==None):return
        self.setFilePath(path[0])
        with open(self.currentFilePath,'r') as fileHandle:
            dataStr=fileHandle.read()
        newData=self.gem_eval(dataStr)
        if(newData==None):return
        self.enableUI(1)

        self.uidGLData=newData
        self.updateSourceTypeBtn()
        self.updateCmdExecuter()
        self.updateFunctionCmd()
        self.gem_refreshWindow()

        self.clearUndoRedo()

    def setFilePath(self,path):
        self.currentFilePath=path
        wintitle = os.path.basename(path)+' - GM UI Designer: '+path.replace("/", "\\")
        cmds.window(self.winTitle,e=1,t=wintitle)

    def enableUI(self,en):
        self.updateCmdExecuter()
        cmds.treeView('uidHierarchyTV',e=1,ra=1)
        cmds.formLayout('uidWidgetBoxFL',e=1,en=en)
        cmds.formLayout('uidHierarchyFL',e=1,en=en)
        cmds.scrollLayout('uidPropertySL',e=1,en=en)

    def saveFileAs(self,*argc):
        path=cmds.fileDialog2(ff='UIDesigner Files (*.uid)',fm=0)
        if(path==None):return
        self.setFilePath(path[0])
        try:
            fileHandle=open(self.currentFilePath,'w')
            fileHandle.write(str(self.uidGLData))
        except:
            sself.dd_warning('Save %s Error!'%self.currentFilePath)
        finally:
            try:
                fileHandle.close()
            except:
                pass

    def saveFile(self,showMsg=True):
        if(self.currentFilePath==None):
            return
        with open(self.currentFilePath,'w') as fileHandle:
            fileHandle.write(str(self.uidGLData))
            if(showMsg):
                print('Save To %s'%self.currentFilePath)

    def show(self):
        cmds.showWindow(self.winTitle)
        cmds.scriptJob(uid=[self.winTitle,self.close])

    def close(self,*argc):
        self.saveFile()
        if(self.uidGLData==None):return
        self.deleteWindow()
        self.clearUndoRedo()

    def moveControl(self,*argc):
        typ=argc[0]
        selI=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selI==None):return
        selI=selI[0]

        childList=self.getSameLevelList(selI)
        if(len(childList)<=1):return

        ctrlSort=self.uidGLData['ctrlSort']
        idx=childList.index(selI)

        if(typ=='Up' and idx==0):
            return
        if(typ=='Down' and idx==len(childList)-1):
            return

        newSort=ctrlSort[:]

        selChild=cmds.treeView('uidHierarchyTV',q=1,ch=selI)
        for i in selChild:
            chIdx=newSort.index(i)
            del newSort[chIdx]
        if(typ=='Up'):
            swapI=childList[idx-1]
            swapIdx=newSort.index(swapI)
            insIdx=swapIdx
        else:
            swapI=childList[idx+1]
            swapIChild=cmds.treeView('uidHierarchyTV',q=1,ch=swapI)
            insIdx=newSort.index(swapIChild[-1])+1

        selChild.reverse()
        for i in selChild:
            newSort.insert(insIdx,i)
        self.uidGLData['ctrlSort']=newSort

        self.gem_refreshWindow()
        self.updateMoveLevelButton()
        self.addUndoAndClearRedo('moveControl')

    def updateMoveLevelButton(self):
        cmds.iconTextButton('uidTreeMoveUpB',e=1,en=0)
        cmds.iconTextButton('uidTreeMoveDnB',e=1,en=0)
        selI=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selI==None):return
        selI=selI[0]
        childList=self.getSameLevelList(selI)
        if(len(childList)<=1):return
        ctrlSort=self.uidGLData['ctrlSort']
        idx=childList.index(selI)
        cmds.iconTextButton('uidTreeMoveUpB',e=1,en=(idx!=0))
        cmds.iconTextButton('uidTreeMoveDnB',e=1,en=(idx!=len(childList)-1))

    def getSameLevelList(self,selI):
        pLayout=self.gem_getParentId(selI)
        allChildList=cmds.treeView('uidHierarchyTV',q=1,ch=pLayout)
        childList=[]
        for i in allChildList:
            pCtrl=cmds.treeView('uidHierarchyTV',q=1,ip=i)
            if(pCtrl==pLayout):
                childList.append(i)
        return childList

    def cutControl(self,*argc):
        self.copyControl()
        self.deleteControl(False)
        self.addUndoAndClearRedo('cutControl')

    def copyControl(self,*argc):
        selI=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selI==None):return
        sameLevelList=self.getSameLevelList(selI[0])
        selList=[]
        for i in sameLevelList:
            if(i in selI) and self.uidGLData[i]['className']!='window':
                selList.append(i)
        if(len(selList)==0):return
        cmds.treeView('uidHierarchyTV',e=1,cs=1)
        for i in selList:
            cmds.treeView('uidHierarchyTV',e=1,si=[i,True])

        self.copyData={}
        self.copyData['ctrlSort']=[]
        self.copyData['selList']=selList
        for i in selList:
            chList=cmds.treeView('uidHierarchyTV',q=1,ch=i)
            for ch in chList:
                if not(ch in self.copyData['ctrlSort']):
                    self.copyData['ctrlSort'].append(ch)
                    self.copyData[ch]=self.uidGLData[ch]
        cmds.iconTextButton('uidTreePasteB',e=1,en=1)

    def pasteControl(self,*argc):
        selI=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selI==None):return
        pLayout=selI[0]
        pType=self.uidGLData[pLayout]['className']

        if(self.copyData==None):return

        pasteList=self.copyData['selList']
        for ctrlId in pasteList:
            parentList=self.copyData[ctrlId]['parentList']
            if not(pType in parentList):
                self.gem_warning('Cann\'t parent %s to %s'%(ctrlId,pLayout))
                return

        pasteSort=self.copyData['ctrlSort']

        newSort=[]
        newBaseNodeList=[]

        for ctrlId in pasteSort:
            baseNode=self.copyData[ctrlId]
            moduleName=baseNode['moduleName']
            className=baseNode['className']
            if not(ctrlId in self.uidGLData['ctrlSort']):
                newCtrlId,newBaseNode=ctrlId,baseNode
            else:
                newCtrlId,newBaseNode,selected=self.createBaseNode(moduleName,className)
            self.copyAttrData(baseNode,newBaseNode)
            newSort.append(newCtrlId)
            newBaseNodeList.append(newBaseNode)

            self.uidGLData['ctrlSort'].append(newCtrlId)
            self.uidGLData[newCtrlId]=newBaseNode
        #rename child
        for i in range(len(pasteSort)):
            oldIdName=pasteSort[i]
            newIdName=newSort[i]
            for baseNode in newBaseNodeList:
                attrList=baseNode['attrList']
                pFlagName=attrList[0]['value']
                if(pFlagName==oldIdName):
                    attrList[0]['value']=newIdName
        #set paste item parent
        for i in range(len(pasteSort)):
            oldIdName=pasteSort[i]
            if(oldIdName in pasteList):
                baseNode=newBaseNodeList[i]
                attrList=baseNode['attrList']
                attrList[0]['value']=pLayout

        self.gem_refreshWindow()
        self.addUndoAndClearRedo('pasteControl')

    def copyAttrData(self,baseNode,newBaseNode):
        newBaseNode['expend']=baseNode['expend']
        newBaseNode['attrList']=copy.deepcopy(baseNode['attrList'])

    def deleteControl(self,isQuery=True):
        if(isQuery):
            ret=cmds.confirmDialog(t='Delete Control', message='Are you sure delete This Control?',b=['Yes','No'], db='Yes', cb='No', ds='No' )
            if(ret=='No'):return

        selI=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selI==None):return
        ctrlSort=self.uidGLData['ctrlSort']
        winId=ctrlSort[0]
        #select parent
        pLayout=self.gem_getParentId(selI[0])
        if(pLayout==None):
            pLayout=self.uidGLData['ctrlSort'][0]
        self.gem_setSelectTreeItem(pLayout)
        for i in selI:
            if(i==winId):continue
            chList=cmds.treeView('uidHierarchyTV',q=1,ch=i)
            for child in chList:
                if(child in ctrlSort):
                    del ctrlSort[ctrlSort.index(child)]
                if(child in self.uidGLData):
                    del self.uidGLData[child]
        self.gem_refreshWindow()
        self.addUndoAndClearRedo('deleteControl')

    def gem_loadUIWidget(self):
        if not(self.uidFilePath in sys.path):
            sys.path.append(self.uidFilePath)

        self.replaceList=[]
        self.widgetBoxITBList=[]
        for idx,mStr in enumerate(self.modulesList):
            rootModule=__import__(mStr)
            cmds.frameLayout('uid%sFL'%mStr,p='uidWidgetBoxSL',l=mStr,cll=1,ec=self.widgetBoxSearch)
            #cmds.columnLayout('uid%sCL'%mStr,p='uidWidgetBoxMainTL',adj=1,vis=0)
            #cmds.tabLayout('uidWidgetBoxMainTL',e=1,tli=[idx+1,mStr])
            for i in rootModule.__all__:
                itb=cmds.iconTextButton('uid%sITB'%i,st='iconAndTextHorizontal', l=i,c=functools.partial(self.gem_addWidget,mStr,i))
                self.widgetBoxITBList.append(itb)

                itemModule=getattr(rootModule,i)
                if(hasattr(itemModule,'replace')):
                    cmds.menuItem(p='uidTreeReplacePM',l=i,c=functools.partial(self.replaceLayout,mStr,i))
                    self.replaceList.append(i)

        self.widgetBoxSearch()

    def replaceLayout(self,*argc):
        moduleName=argc[0]
        className=argc[1]

        ctrlId=cmds.treeView('uidHierarchyTV',q=1,si=1)[0]
        pItem=self.gem_getParentId(ctrlId)
        newCtrlId,newBaseNode,selected=self.createBaseNode(moduleName,className)

        self.renameChangeData(ctrlId,newCtrlId)
        del self.uidGLData[ctrlId]
        self.uidGLData[newCtrlId]=newBaseNode

        self.uidGLData[newCtrlId]['expend']=True
        self.gem_setParentAttr(newCtrlId,pItem)

        self.gem_refreshWindow()
        self.gem_setSelectTreeItem(newCtrlId)
        self.addUndoAndClearRedo('replaceLayout')

    def renameSuffixName(self,*argc):
        suf=self.getSufName()
        result=cmds.promptDialog(t='Rename Suffix',tx=suf,m='Enter Suffix:',b=['OK', 'Cancel'],db='OK',cb='Cancel',ds='Cancel')
        if result == 'OK':
            suf = cmds.promptDialog(q=True, tx=True)
            self.setSufName(suf)

    def widgetBoxSearch(self,*argc):
        sStr=cmds.textField('uidSearchF',q=1,tx=1)
        sStr=sStr.lower()
        for i in self.widgetBoxITBList:
            label=cmds.iconTextButton(i,q=1,l=1)
            label=label.split('.')[0]
            label=label.lower()
            cmds.iconTextButton(i,e=1,vis=(label.find(sStr)!=-1))
        if(sStr==''):
            cmds.iconTextButton('uidSearchB',e=1,i='zoom.png')
        else:
            cmds.iconTextButton('uidSearchB',e=1,i='SP_FileDialogBack.png')

    def clearSearch(self,*argc):
        st=cmds.iconTextButton('uidSearchB',q=1,i=1)
        if(st=='SP_FileDialogBack.png'):
            cmds.textField('uidSearchF',e=1,tx='')
        self.widgetBoxSearch()

    def gem_initTreeView(self):
        self.uidGLData={'ctrlSort':[],'curSelTreeItem':None,'sourceType':'python','suffix':'_ui'}
        self.gem_addWidget('Windows','window')

    def gem_addWidget(self,moduleName,className):
        ctrlId,baseNode,selected=self.createBaseNode(moduleName,className)
        self.uidGLData['ctrlSort'].append(ctrlId)
        self.uidGLData[ctrlId]=baseNode
        self.uidGLData[ctrlId]['expend']=True
        pItem=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(pItem==None):
            pItem=self.uidGLData['ctrlSort'][0]
        self.gem_setParentAttr(ctrlId,pItem)
        self.gem_refreshWindow()
        if(selected):
            self.gem_setSelectTreeItem(ctrlId)
        else:
            self.gem_setSelectTreeItem(pItem[0])
        self.addUndoAndClearRedo('gem_addWidget')

    def getModule(self,moduleName):
        module=sys.modules.get(moduleName,None)
        if(module==None):
            module=__import__(moduleName)
        return module

    def createBaseNode(self,moduleName,className):
        module=self.getModule(moduleName)
        ctrlModule=getattr(module,className)
        baseNode=ctrlModule.baseNode()

        baseNode['parentList']=ctrlModule.parentList
        baseNode['moduleName']=moduleName
        baseNode['className']=className
        procName=baseNode['procName']
        ctrlId=self.gem_getNonRepeatName(procName,className)
        return ctrlId,baseNode,ctrlModule.selected

    def gem_setSelectTreeItem(self,item):
        cmds.treeView('uidHierarchyTV',e=1,cs=1)
        cmds.treeView('uidHierarchyTV',e=1,si=[item,True])
        self.gem_treeSelectChange()
        cmds.treeView('uidHierarchyTV',e=1,en=1,shi=item)

    def treeItemHierarchyChange(self,*argc):
        chList,oldPList,oldIdxList,newPname,newIdxList,oldExlist,newExList=argc
        pType=self.uidGLData[newPname]['className']
        for chName in chList:
            parentList=self.uidGLData[chName]['parentList']
            if not(pType in parentList):
                self.gem_warning('Cann\'t parent %s  to %s'%(chName,newPname))
                self.gem_refreshWindow()
                return
        for chName in chList:
            self.gem_setParentAttr(chName,newPname)

        self.uidGLData['ctrlSort']=cmds.treeView('uidHierarchyTV',q=1,ch='')
        self.gem_refreshWindow()
        self.addUndoAndClearRedo('treeItemHierarchyChange')

    def treeViewExpendChange(self,*argc):
        ctrlId=argc[0]
        expend=argc[1]
        self.uidGLData[ctrlId]['expend']=expend

    def gem_treeSelectChange(self):
        selItem=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selItem==None):
            for i in self.getTreeSelection():
                if(i in self.uidGLData['ctrlSort']):
                    cmds.treeView('uidHierarchyTV',e=1,si=[i,True])

        selItem=cmds.treeView('uidHierarchyTV',q=1,si=1)
        self.setTreeSelection(selItem)
        self.gem_updateCButtonState()
        self.updateMoveLevelButton()
        self.updateReplaceButton()
        self.gem_showItemProperty()
        cmdPos=self.CmdTextPos.get(selItem[0],None)
        if(cmdPos):
            cmds.cmdScrollFieldExecuter(self.UICmdSFE,e=1,sl=cmdPos)

    def updateReplaceButton(self):
        cmds.iconTextButton('uidTreeReplaceB',e=1,en=0)
        selItem=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selItem==None):return
        if(len(selItem)!=1):return
        className=self.uidGLData[selItem[0]]['className']
        cmds.iconTextButton('uidTreeReplaceB',e=1,en=(className in self.replaceList))

    def treeItemRenameLabel(self,*argc):
        oldName=argc[0]
        newName=argc[1]
        if(oldName==newName or newName==''):
            return ''
        if(not self.nameRegex.match(newName)):
            self.gem_warning('The name is not in conformity with the rules!')
            return ''
        baseNode=self.uidGLData[oldName]
        procName=baseNode['procName']

        exists=self.gem_uiExists(procName,newName)
        if(exists):
            self.gem_warning('The name is repeated!')
            return ''
        self.renameChangeData(oldName,newName)
        self.uidGLData[newName]=self.uidGLData[oldName]
        self.uidGLData[newName]['renamed']=True
        del self.uidGLData[oldName]
        if(procName=='window'):
            self.deleteWindow(oldName)
        self.gem_refreshWindow()
        self.gem_setSelectTreeItem(newName)
        self.addUndoAndClearRedo('treeItemRenameLabel')

    def deleteWindow(self,winId=None):
        if(winId==None):
            winId=self.uidGLData['ctrlSort'][0]
        winId=self.getCtrlId(winId)
        if(cmds.window(winId,q=1,ex=1)):
            self.winTLC=cmds.window(winId,q=1,tlc=1)
            cmds.deleteUI(winId)
        else:
            self.winTLC=None

        if(cmds.toolBar(winId+'_dock',q=1,ex=1)):
            cmds.deleteUI(winId+'_dock')
        if(cmds.dockControl(winId+'_dock',q=1,ex=1)):
            cmds.deleteUI(winId+'_dock')

    def renameChangeData(self,oldName,newName):
        ctrlSort=self.uidGLData['ctrlSort']
        self.renameFormData(oldName,newName)

        for ctrlId in ctrlSort:
            pName=self.gem_getParentId(ctrlId)
            if(pName==oldName):
                self.gem_setParentAttr(ctrlId,newName)

        idx=ctrlSort.index(oldName)
        ctrlSort[idx]=newName

    def gem_refreshSelectTreeItem(self):
        treeSelection=self.getTreeSelection()
        if(treeSelection==None):
            self.setTreeSelection([self.uidGLData['ctrlSort'][0]])
        cmds.treeView('uidHierarchyTV',e=1,cs=1)
        for i in self.getTreeSelection():
            if(i in self.uidGLData['ctrlSort']):
                cmds.treeView('uidHierarchyTV',e=1,si=[i,True])
            cmds.treeView('uidHierarchyTV',e=1,en=1,shi=i)

        selI=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selI==None):
            cmds.treeView('uidHierarchyTV',e=1,si=[self.uidGLData['ctrlSort'][0],True])

    def getTreeSelection(self):
        return self.uidGLData.get('curSelTreeItem',None)

    def setTreeSelection(self,value):
        self.uidGLData['curSelTreeItem']=value
   
    def gem_showItemProperty(self):
        selItem=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selItem==None):return
        ctrlIdList=selItem
        baseNode=self.uidGLData[ctrlIdList[0]]
        className=baseNode['className']
        baseNodeList=[]
        for ctrlId in ctrlIdList:
            baseNode=self.uidGLData[ctrlId]
            if(baseNode['className']==className):
                baseNodeList.append(baseNode)
        pd=self.propertyDelegateData.get(className,None)
        for i in self.propertyDelegateData:
            self.propertyDelegateData[i].hide()
        if(pd==None):
            self.propertyDelegateData[className]=PropertyDelegate(self,'uidPropertySL',baseNode)
        pd=self.propertyDelegateData.get(className)
        pd.show()

        label=pd.className
        if(len(ctrlIdList)>1):
            label+='...'
        cmds.frameLayout('uidPAttrFL',e=1,l=label)
        self.gem_getDefultData(ctrlIdList[0])
        pd.setCurrentCtrlBaseNode(baseNodeList)

    def gem_updateCButtonState(self):
        selItem=cmds.treeView('uidHierarchyTV',q=1,si=1)
        if(selItem==None):return
        ctrlId=selItem[0]
        baseNode=self.uidGLData[ctrlId]
        className=baseNode['className']
        for mStr in self.modulesList:
            rootModule=self.getModule(mStr)
            for i in rootModule.__all__:
                model=getattr(rootModule,i)
                cmds.iconTextButton('uid%sITB'%i,e=1,en=(className in model.parentList))

    def checkNeedParentFlag(self,ctrlId):
        className=self.uidGLData[ctrlId]['className']
        if(className=='window'):
            return False
        if(className=='menuItem'):
            pCtrl=self.gem_getRealParent(ctrlId)
            pClassName=self.uidGLData[pCtrl]['className']
            if(pClassName in ['menu','subMenuItem']):
                return True
            else:
                return False
        if(className=='popupMenu'):
            return True

        pCtrl=self.gem_getRealParent(ctrlId)
        chList=self.getRealChildList(pCtrl)
        idx=chList.index(ctrlId)
        for i in chList[:idx]:
            if(self.uidGLData[i]['ctrlType']=='Layout' or self.uidGLData[i]['ctrlType']=='MenuLayout'):
                return True
        return False

    def checkNeedControlID(self,ctrlId):
        if(self.getGenrateOption('ctrlIdType')==2):
            return True
        if(self.uidGLData[ctrlId]['ctrlType']=='Window'):
            return True
        if(self.uidGLData[ctrlId]['renamed']):
            return True

        chList=self.getRealChildList(ctrlId)

        for i in chList:
            if(self.checkNeedParentFlag(i)):
                return True

        attrList=self.gem_getAttrList(ctrlId)
        for attr in attrList:
            mode=attr['mode']
            value=attr['value']
            if(mode=='e' and value!=None):
                return True
        return self.checkFormDataInfo(ctrlId)

    def renameFormData(self,oldName,newName):
        pLayout=self.gem_getRealParent(oldName)
        if(pLayout==None):
            return
        if(self.uidGLData[pLayout]['className']!='formLayout'):
            return
        attrList=self.gem_getAttrList(pLayout)
        for attr in attrList:
            if(attr['active'] and attr['type']=='form' and attr['value']!=None):
                for form in attr['value']:
                    for i in range(len(form)):
                        if(form[i]==oldName):
                            form[i]=newName

    def checkFormDataInfo(self,ctrlId):
        pLayout=self.gem_getRealParent(ctrlId)

        if(self.uidGLData[pLayout]['className']!='formLayout'):
            return False
        attrList=self.gem_getAttrList(pLayout)
        for attr in attrList:
            if(attr['active'] and attr['type']=='form' and attr['value']!=None):
                formList=attr['value']
                for form in formList:
                    for strId in form:
                        if(strId==ctrlId):
                            return True
        return False

    def gem_generateCode(self,*argc):
        if(self.uidGLData==None):
            return
        self.checkValidity()
        self.deleteOldUI()
        if(self.getSourceType()=='python'):
            self.generatePyCode()
        else:
            self.generateMelCode()
        self.saveFile(showMsg=False)
        # cmds.cmdScrollFieldExecuter('uidMainCodeSFE',e=1,exa=1)

    def getScriptWidgetCode(self,attrList):
        value=attrList[1]['value']
        if(attrList[1]['active']):
            if(value!=None):
                if(value[1]==self.getSourceType()):
                    return value[2]+self.linesep
        return ''

    def getIndentStr(self):
        if(self.getGenrateOption('booleanType')==1):
            return '\t'
        return '    '

    def generatePyCode(self):
        ctrlSort=self.uidGLData['ctrlSort']
        outputStr='from maya import cmds%s'%self.linesep

        funcName=self.getUIFuncName()
        paramStr=self.getGenrateOption('funcParam')
        outputStr+='def %s(%s):%s'%(funcName,paramStr,self.linesep)
        winId=self.getCtrlId(ctrlSort[0])
        if(self.getGenrateOption('flagType')==1):
            if(self.getGenrateOption('booleanType')==2):
                outputStr+='%sif(cmds.window(\'%s\',q=1,ex=1)):cmds.deleteUI(\'%s\')%s'%(self.getIndentStr(),winId,winId,self.linesep)
            else:
                outputStr+='%sif(cmds.window(\'%s\',q=True,ex=True)):cmds.deleteUI(\'%s\')%s'%(self.getIndentStr(),winId,winId,self.linesep)
        else:
            if(self.getGenrateOption('booleanType')==2):
                outputStr+='%sif(cmds.window(\'%s\',query=1,exists=1)):cmds.deleteUI(\'%s\')%s'%(self.getIndentStr(),winId,winId,self.linesep)
            else:
                outputStr+='%sif(cmds.window(\'%s\',query=True,exists=True)):cmds.deleteUI(\'%s\')%s'%(self.getIndentStr(),winId,winId,self.linesep)

        prefStr=''
        if(cmds.iconTextCheckBox('uidWinCacheITB',q=1,v=1)):
            prefStr='%sif(cmds.windowPref(\'%s\',ex=1)):cmds.windowPref(\'%s\',r=1)%s'%(self.getIndentStr(),winId,winId,self.linesep)

        outputEditStr=''
        debugStr=outputStr+prefStr

        dockCode=None
        for ctrlId in ctrlSort:
            baseNode=self.uidGLData[ctrlId]
            procName=baseNode['procName']
            attrList=self.gem_getAttrList(ctrlId)
            flagStr=''
            editFlagStr=''
            tlcflagStr=''
            if(procName=='scriptWidget'):
                scriptStr=self.getScriptWidgetCode(attrList)
                outputStr+=scriptStr
                debugStr+=scriptStr
                continue
            #parent flag
            pFlagStr=self.gem_getPyOutputValue(ctrlId,attrList[0])
            #other flag
            for attr in attrList[1:]:
                flagName=self.getFlagName(attr)
                if(attr['active'] and (attr['value']!=None)):
                    if(attr['mode']=='c' or attr['mode']=='s'):
                        flagStr+=self.gem_getPyOutputValue(ctrlId,attr)
                    elif(attr['mode']=='e'):
                        editFlagStr+=self.gem_getPyOutputValue(ctrlId,attr)
                    elif(attr['mode']=='a'):
                        if(attr['type']=='dock'):
                            winId=ctrlSort[0]
                            dockCode=self.getDockPyCode(winId,attr)
            #debug mode window pos
            if(procName=='window' and self.winTLC):
                tlcflagStr+=',tlc=%s'%str(self.winTLC)
            debugStr+='%scmds.%s(%s%s%s%s)%s'%(self.getIndentStr(),procName,self.getPyControlId(ctrlId,True),pFlagStr,tlcflagStr,flagStr,self.linesep)
            #output
            flagStr=pFlagStr+flagStr
            ctrlIdStr=self.getPyControlId(ctrlId,False)
            if(ctrlIdStr==''):
                flagStr=flagStr.strip(',')
            ctrlStr='%scmds.%s(%s%s)'%(self.getIndentStr(),procName,ctrlIdStr,flagStr)
            self.saveTextCmdPos(ctrlId,outputStr,ctrlStr)
            outputStr+=ctrlStr+self.linesep
            if(editFlagStr!=''):
                outputEditStr+='%scmds.%s(%s,e=1%s)%s'%(self.getIndentStr(),procName,ctrlIdStr,editFlagStr,self.linesep)

        outputStr+=outputEditStr
        debugStr+=outputEditStr

        if(dockCode):
            showStr=dockCode
        else:
            showStr='%scmds.showWindow(\'%s\')%s'%(self.getIndentStr(),winId,self.linesep)

        outputStr+=showStr
        debugStr+=showStr

        funcStr=self.getFuncionStr()+self.linesep

        outputStr+=funcStr
        debugStr+=funcStr

        callFuncParamStr=self.getGenrateOption('callFuncParam')
        callStr='%s(%s)'%(funcName,callFuncParamStr)

        outputStr+=callStr
        debugStr+=callStr

        cmds.cmdScrollFieldExecuter(self.UICmdSFE,e=1,t=debugStr)
        cmds.cmdScrollFieldExecuter(self.UICmdSFE,e=1,exa=1)

        if not(cmds.iconTextCheckBox('uidDebugModeITB',q=1,v=1)):
            cmds.cmdScrollFieldExecuter(self.UICmdSFE,e=1,t=outputStr)

    def saveTextCmdPos(self,ctrlId,outputStr,ctrlStr):

        #cmds.cmdScrollFieldExecuter(self.UICmdSFE,e=1,t=outputStr)
        #outLen=cmds.cmdScrollFieldExecuter(self.UICmdSFE,q=1,tl=1)
        outLen=len(outputStr)
        # cmds.cmdScrollFieldExecuter(self.UICmdSFE,e=1,t=ctrlStr)
        # ctrlLen=cmds.cmdScrollFieldExecuter(self.UICmdSFE,q=1,tl=1)
        ctrlLen=len(ctrlStr)
        self.CmdTextPos[ctrlId]=[outLen,outLen+ctrlLen-1]

    def getPyControlId(self,ctrlId,debug):
        if(self.checkNeedControlID(ctrlId) or debug):
            return '\'%s\''%self.getCtrlId(ctrlId)
        return ''

    def getFlagName(self,attr):
        if(self.getGenrateOption('flagType')==1):
            return attr['shortName']
        else:
            return attr['longName']

    def getDockPyCode(self,winId,attr):
        typ,label,area,allowedAreaList=attr['value']
        if(self.getGenrateOption('flagType')==1):
            if(len(label)>0):
                label=',l=\'%s\''%label
            area=',a=\'%s\''%area
            allowedArea=',aa='+str(allowedAreaList)
            content=',con=\'%s\''%winId
            return '%scmds.%s(\'%s\'%s%s%s%s)'%(self.getIndentStr(),typ,winId+'_dock',label,content,area,allowedArea)
        else:
            if(len(label)>0):
                label=',label=\'%s\''%label
            area=',area=\'%s\''%area
            allowedArea=',allowedArea='+str(allowedAreaList)
            content=',content=\'%s\''%winId
            return '%scmds.%s(\'%s\'%s%s%s%s)'%(self.getIndentStr(),typ,winId+'_dock',label,content,area,allowedArea)

    def getFormValue(self,attr):
        attrList=[]
        longName=attr['longName']
        for i in attr['value']:
            if(longName=='attachForm'):
                attrList.append([self.getCtrlId(str(i[0])),i[1],i[2]])
            elif(longName=='attachPosition'):
                attrList.append([self.getCtrlId(str(i[0])),i[1],i[2],i[3]])
            else:
                attrList.append([self.getCtrlId(str(i[0])),i[1],i[2],self.getCtrlId(str(i[3]))])
        return attrList

    def gem_getPyOutputValue(self,ctrlId,attr):
        flagName=self.getFlagName(attr)
        if(attr['longName']=='parent'):
            if(self.checkNeedParentFlag(ctrlId)):
                pName=self.gem_getRealParent(ctrlId,attr)
                pName=self.getCtrlId(pName)
                if(self.checkNeedParentFlag(ctrlId)):
                    return ',%s=\'%s\''%(flagName,pName)
            return ''
        attrType=attr['type']
        if(attrType=='string' or attrType=='image'):
            return ',%s=u\'%s\''%(flagName,attr['value'])
        elif(attrType=='menu'):
            return ',%s=u\'%s\''%(flagName,attr['value'])
        elif(attrType=='script'):
            if(len(attr['value'])==2):
                return ''
            st=attr['value'][1]
            if(st!=self.getSourceType()):
                return ''
            if(attr['value'][0]):
                return ',%s=\'%s\''%(flagName,attr['value'][2])
            return ',%s=%s'%(flagName,attr['value'][2])
        elif((attrType=='boolean' or attrType=='booleanF') and self.getGenrateOption('booleanType')==2):
            return ',%s=%s'%(flagName,int(attr['value']))
        elif(attrType=='form'):
            return ',%s=%s'%(flagName,self.getFormValue(attr))
        else:
            return ',%s=%s'%(flagName,attr['value'])

    def generateMelCode(self):
        ctrlSort=self.uidGLData['ctrlSort']
        winId=self.getCtrlId(ctrlSort[0])

        funcName=self.getUIFuncName()

        paramStr=self.getGenrateOption('funcParam')
        outputStr='global proc %s(%s){%s'%(funcName,paramStr,self.linesep)
        if(self.getGenrateOption('flagType')==1):
            outputStr+='%sif(`window -q -ex "%s"`)deleteUI("%s");%s'%(self.getIndentStr(),winId,winId,self.linesep)
        else:
            outputStr+='%sif(`window -query -exists "%s"`)deleteUI("%s");%s'%(self.getIndentStr(),winId,winId,self.linesep)
        outputEditStr=''
        prefStr=''
        if(cmds.iconTextCheckBox('uidWinCacheITB',q=1,v=1)):
            prefStr='%sif(`windowPref -ex "%s"`)windowPref -r "%s";%s'%(self.getIndentStr(),winId,winId,self.linesep)

        debugStr=outputStr+prefStr
        dockCode=None
        for ctrlId in ctrlSort:
            baseNode=self.uidGLData[ctrlId]
            procName=baseNode['procName']
            attrList=self.gem_getAttrList(ctrlId)
            flagStr=''
            editFlagStr=''
            tlcflagStr=''

            if(procName=='scriptWidget'):
                scriptStr=self.getScriptWidgetCode(attrList)
                outputStr+=scriptStr
                debugStr+=scriptStr
                continue

            #parent flag
            pFlagStr=self.gem_getMelOutputValue(ctrlId,attrList[0])

            #other flag
            for attr in attrList[1:]:
                if(attr['active'] and (attr['value']!=None)):
                    if(attr['mode']=='c' or attr['mode']=='s'):
                        flagStr+=self.gem_getMelOutputValue(ctrlId,attr)
                    elif(attr['mode']=='e'):
                        editFlagStr+=self.gem_getMelOutputValue(ctrlId,attr)
                    elif(attr['mode']=='a'):
                        if(attr['type']=='dock'):
                            dockCode=self.getDockMelCode(winId,attr)

            #debug mode window pos
            if(procName=='window' and self.winTLC):
                tlcflagStr+=' -tlc %s %s'%(self.winTLC[0],self.winTLC[1])
            debugStr+='%s%s%s%s%s%s;%s'%(self.getIndentStr(),procName,pFlagStr,tlcflagStr,flagStr,self.getMelControlId(ctrlId,True),self.linesep)

            #output
            ctrlIdStr=self.getMelControlId(ctrlId,False)
            ctrlStr='%s%s%s%s%s;'%(self.getIndentStr(),procName,pFlagStr,flagStr,ctrlIdStr)
            self.saveTextCmdPos(ctrlId,outputStr,ctrlStr)
            outputStr+=ctrlStr+self.linesep

            if(editFlagStr!=''):
                outputEditStr+='%s%s -e%s%s;%s'%(self.getIndentStr(),procName,editFlagStr,ctrlIdStr,self.linesep)

        outputStr+=outputEditStr
        debugStr+=outputEditStr

        if(dockCode):
            showStr=dockCode
        else:
            showStr='%sshowWindow "%s";%s}%s'%(self.getIndentStr(),winId,self.linesep,self.linesep)

        outputStr+=showStr
        debugStr+=showStr

        funcStr=self.getFuncionStr()+self.linesep

        outputStr+=funcStr
        debugStr+=funcStr

        callFuncParamStr=self.getGenrateOption('callFuncParam')
        callStr='%s(%s);'%(funcName,callFuncParamStr)

        outputStr+=callStr
        debugStr+=callStr

        if(cmds.iconTextCheckBox('uidDebugModeITB',q=1,v=1)):
            cmds.cmdScrollFieldExecuter(self.UICmdSFE,e=1,t=debugStr)
        else:
            cmds.cmdScrollFieldExecuter(self.UICmdSFE,e=1,t=outputStr)
        mm.eval(debugStr)

    def getMelControlId(self,ctrlId,debug):
        if(self.checkNeedControlID(ctrlId) or debug):
            return ' "%s"'%self.getCtrlId(ctrlId)
        return ''

    def getDockMelCode(self,winId,attr):
        typ,label,area,allowedAreaList=attr['value']
        if(self.getGenrateOption('flagType')==1):
            if(len(label)>0):
                label=' -l "%s"'%label
            area=' -a "%s"'%area
            allowedArea=''
            for i in allowedAreaList:
                allowedArea+=' -aa "%s"'%i
            content=' -con "%s"'%winId
            return '%s%s%s%s%s%s "%s";%s}'%(self.getIndentStr(),typ,label,content,area,allowedArea,winId+'_dock',self.linesep)
        else:
            if(len(label)>0):
                label=' -label "%s"'%label
            area=' -area "%s"'%area
            allowedArea=''
            for i in allowedAreaList:
                allowedArea+=' -allowedArea "%s"'%i
            content=' -content "%s"'%winId
            return '%s%s%s%s%s%s "%s";%s}'%(self.getIndentStr(),typ,label,content,area,allowedArea,winId+'_dock',self.linesep)

    def gem_getMelOutputValue(self,ctrlId,attr):
        flagName=self.getFlagName(attr)
        if(attr['longName']=='parent'):
            if(self.checkNeedParentFlag(ctrlId)):
                pName=self.gem_getRealParent(ctrlId,attr)
                pName=self.getCtrlId(pName)
                if(self.checkNeedParentFlag(ctrlId)):
                    return ' -%s "%s"'%(flagName,pName)
            return ''

        attrType=attr['type']
        if(attrType in ['string','menu','image']):
            return ' -%s "%s"'%(flagName,attr['value'])
        elif(attrType=='script'):
            st=attr['value'][1]
            if(st!=self.getSourceType()):
                return ''
            if(attr['value'][0]):
                return ' -%s "%s"'%(flagName,attr['value'][2].replace('\"','\\\"'))
            return ' -%s %s'%(flagName,attr['value'][2])
        elif(attrType=='boolean'):
            if(self.getGenrateOption('booleanType')==2):
                return ' -%s %s'%(flagName,int(attr['value']))
            if(attr['value']):
                return ' -%s true'%(flagName)
            return ' -%s false'%(flagName)
        elif(attrType=='booleanF'):
            if(attr['value']):
                return ' -%s'%(flagName)
            return ''

        elif(attrType in ['color','colorA','int2','toolImage']):
            retStr=' -%s'%flagName
            for value in attr['value']:
                retStr+=' %s'%value
            return retStr
        elif(attrType in ['form','list_int2','list_int','list_align','list_string']):
            return self.getMelListStr(flagName,ctrlId,attr,attrType)
        else:
            return ' -%s %s'%(flagName,attr['value'])

    def getMelListStr(self,flagName,ctrlId,attr,attrType):
        retStr=''
        valueList=attr['value']
        if(attrType=='form'):
            valueList=self.getFormValue(attr)

        for value in valueList:
            retStr+=' -%s'%flagName
            retStr+=self.autoGetTypeStrValue(value)
        return retStr

    def autoGetTypeStrValue(self,value):
        if(isinstance(value,str)):
            ret=' "%s"'%value
        elif(isinstance(value,bool)):
            if(self.getGenrateOption('booleanType')==2):
                ret=' %s'%(int(value))
            else:
                if(value):
                    ret=' true'
                else:
                    ret=' false'
        elif(isinstance(value,list)):
            ret=''
            for i in value:
                ret+=self.autoGetTypeStrValue(i)
        else:
            ret=' %s'%value
        return ret

    def deleteOldUI(self):
        self.deleteWindow()
        ctrlSort=self.uidGLData['ctrlSort']
        for ctrlId in ctrlSort[1:]:
            procName=self.uidGLData[ctrlId]['procName']
            ctrlId=self.getCtrlId(ctrlId)
            if(procName=='scriptWidget'):
                continue
            exStr='if(cmds.%s("%s",q=1,ex=1)):cmds.deleteUI("%s")'%(procName,ctrlId,ctrlId)
            exec(exStr)

    def checkValidity(self):
        ctrlSort=self.uidGLData['ctrlSort']
        for ctrlId in ctrlSort:
            baseNode=self.uidGLData[ctrlId]
            className=baseNode['className']
            attrList=baseNode['attrList']

            chList=self.gem_getSelectItemChild(ctrlId)
            if(className=='window'):
                for i in attrList:
                    if(i['longName']=='menuBar'):
                        i['value']=self.checkHasMenu(chList)
                        if(i['value']):i['active']=True

            elif(className=='rowLayout'):
                for i in attrList:
                    if(i['longName']=='numberOfColumns'):
                        i['value']=max(1,len(chList))
                    if(i['longName'] in ['columnWidth','columnAlign']):
                        i['value']=self.checkIdxValidity(i['value'],chList)

            elif(className=='shelfTabLayout' or className=='tabLayout'):
                for i in attrList:
                    if(i['longName']=='tabLabelIndex'):
                        i['value']=self.checkIdxValidity(i['value'],chList)

            elif(className=='formLayout'):
                for i in attrList:
                    if(i['longName'] in ['attachForm','attachControl','attachPosition']):
                        i['value']=self.checkCtrlIdValidity(i['longName'],i['value'],chList)

    def checkHasMenu(self,chList):
        if(chList==None):
            return False
        for i in chList:
            baseNode=self.uidGLData[i]
            className=baseNode['className']
            if(className=='menu'):
                return True
        return False

    def checkCtrlIdValidity(self,typ,valueList,chList):
        if(valueList==None):return 
        newList=[]
        for i in valueList:
            if(typ=='attachForm' or typ=='attachPosition'):
                if(i[0] in chList):
                    newList.append(i)
            else:
                if((i[0] in chList) and (i[-1] in chList)):
                    newList.append(i)
        return newList

    def checkIdxValidity(self,valueList,chList):
        if(valueList==None):return 
        newList=[]
        for i in valueList:
            if(i[0]<=len(chList)):
                newList.append(i)
        return newList

        # formLayout attachForm attachControl attachPosition
        # shelfTabLayout tabLabelIndex
        # tabLayout tabLabelIndex

    def gem_getDefultData(self,ctrlId):
        self.gem_checkPreviewWindow()
        self.checkValidity()

        baseNode=self.uidGLData[ctrlId]
        procName=baseNode['procName']
        attrList=self.gem_getAttrList(ctrlId)

        if(procName=='scriptWidget'):
            return

        qStr='cmds.%s("%s",q=1,ex=1)'%(procName,self.getCtrlId(ctrlId))
        if(not self.gem_eval(qStr)):
            procName='control'
            return

        for attr in attrList[1:]:
            if(not attr['type'] in ['boolean','booleanF','color','colorA','int','int2','string','float','float2','menu','image']):
                continue
            if(attr['active']):
                continue
            if(attr.get('query',True)==False):
                continue
            qStr='cmds.%s("%s",q=1,%s=1)'%(procName,self.getCtrlId(ctrlId),attr['shortName'])

            try:
                value=self.gem_eval(qStr)
                if(value!=None and (attr['type']=='float' or attr['type']=='int')):
                    value=max(-1000,min(1000,value))
            except:
                value=None
            attr['value']=value

    def gem_checkPreviewWindow(self):
        winId=self.uidGLData['ctrlSort'][0]
        winId=self.getCtrlId(winId)
        if(not cmds.window(winId,q=1,ex=1)):
            self.gem_generateCode()

    def gem_deleteWindowPref(self,*argc):
        winId=self.uidGLData['ctrlSort'][0]
        winId=self.getCtrlId(winId)
        tlc=None
        if(cmds.window(winId,q=1,ex=1)):
            tlc=cmds.window(winId,q=1,tlc=1)
            cmds.deleteUI(winId)

        if(cmds.windowPref(winId,ex=1)):
            cmds.windowPref(winId,r=1)
        self.gem_generateCode()
        if(tlc!=None):
            cmds.window(winId,e=1,tlc=tlc)

    def gem_getRealParent(self,ctrlId,attr=None):
        ctrlSort=self.uidGLData['ctrlSort']
        if(attr==None):
            attrList=self.uidGLData[ctrlId]['attrList']
            for i in attrList:
                if(i['longName']=='parent'):
                    attr=i
                    break
        if(attr.get('virtual',False)):
            virtualParent=attr['value']
            realparent=self.gem_getParentId(virtualParent)
            return realparent
        else:
            return attr['value']

    def gem_getSelectItemChild(self,selCtrl=None):
        if(selCtrl==None):
            selCtrl=self.getTreeSelection()[0]
        return self.getRealChildList(selCtrl)
    def getRealChildList(self,ctrlId):
        ctrlSort=self.uidGLData['ctrlSort']
        childList=[]
        for i in ctrlSort:
            pName=self.gem_getRealParent(i)
            if(pName==ctrlId):
                childList.append(i)
        return childList

    def gem_getNonRepeatName(self,procName,className,i=1):
        suf=self.getSufName()
        while self.gem_uiExists(procName,className+str(i)):i+=1
        return className+str(i)

    def gem_uiExists(self,procName,newName):
        if(procName=='window'):
            return mm.eval('%s -q -ex "%s";'%(procName,self.getCtrlId(newName) ))
        else:
            return newName in self.uidGLData['ctrlSort']

    def getSufName(self):
        suf=self.uidGLData.get('suffix',None)
        if(suf==None):
            suf='_ui'
            self.uidGLData['suffix']=suf
        return suf

    def setSufName(self,suf):
        old=self.getSufName()
        if(old==suf):
            return

        if(suf!=''):
            if(not self.nameRegex.match(suf)):
                self.gem_warning('The Suffix name is not in conformity with the rules!')
                return
        self.uidGLData['suffix']=suf
        self.gem_refreshWindow()

    def getCtrlId(self,ctrlId):
        suf=self.getSufName()
        return ctrlId+suf

    def gem_refreshWindow(self,*argc):
        if(self.uidGLData==None):
            return
        ctrlSort=self.uidGLData['ctrlSort']
        cmds.treeView('uidHierarchyTV',e=1,ra=1)
        for i in ctrlSort:
            baseNode=self.uidGLData[i]
            cmds.treeView('uidHierarchyTV',e=1,ai=[i,self.gem_getParentId(i)],ei=[i,baseNode['expend']])
            cmds.treeView('uidHierarchyTV',e=1,dls=[i,self.getSufName()])

        self.uidGLData['ctrlSort']=cmds.treeView('uidHierarchyTV',q=1,ch=1)

        self.gem_generateCode()
        self.gem_refreshSelectTreeItem()

    def gem_setParentAttr(self,ctrlId,pItem):
        if(pItem==None):
            return
        if(isinstance(pItem,list)):
            pItem=pItem[0] 
        if(pItem==ctrlId):
            return
        attrList=self.gem_getAttrList(ctrlId)
        attrList[0]['value']=pItem
        attrList[0]['active']=1

    def gem_getParentId(self,ctrlId):
        attrList=self.gem_getAttrList(ctrlId)
        return attrList[0]['value']

    def gem_getAttrList(self,ctrlId):
        baseNode=self.uidGLData[ctrlId]
        return baseNode['attrList']

    def gem_eval(self,sCmd):
        return sys.modules['builtins'].eval(sCmd)

    def gem_warning(self,wStr):
        mm.eval('warning "%s"'%wStr)