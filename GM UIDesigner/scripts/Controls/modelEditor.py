def attrNode(**data):
    return data
parentList=['columnLayout','flowLayout','formLayout','frameLayout','gridLayout','paneLayout','rowColumnLayout','rowLayout','scrollLayout','shelfLayout','shelfTabLayout','tabLayout','menuBarLayout']
selected=False
def baseNode():
    return attrNode(
    procName='modelEditor',
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
    longName='mainListConnection',
    shortName='mlc', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='forceMainConnection',
    shortName='fmc', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='selectionConnection',
    shortName='slc', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='highlightConnection',
    shortName='hlc', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='filter',
    shortName='f', 
    type='string',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='lockMainConnection',
    shortName='lck', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='unlockMainConnection',
    shortName='ulk', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='updateMainConnection',
    shortName='upd', 
    type='boolean',
    mode='c',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='camera',
    shortName='cam', 
    type='string',
    mode='e',
    value=None,
    active=0,
    ))

    # attrData.append(attrNode(
    # longName='cameraName',
    # shortName='cn', 
    # type='string',
    # mode='c',
    # value=None,
    # active=0,
    # ))

    attrData.append(attrNode(
    longName='displayLights',
    shortName='dl', 
    type='menu',
    mode='e',
    value=None,
    active=0,
    option=['selected','active','all','default','none']
    ))

    attrData.append(attrNode(
    longName='bufferMode',
    shortName='bm', 
    type='menu',
    mode='e',
    value=None,
    active=0,
    option=['single','double']
    ))

    attrData.append(attrNode(
    longName='activeOnly',
    shortName='ao', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='interactive',
    shortName='i', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='default',
    shortName='d', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='ignorePanZoom',
    shortName='ipz', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='twoSidedLighting',
    shortName='tsl', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='displayAppearance',
    shortName='da', 
    type='menu',
    mode='e',
    value=None,
    active=0,
    option=['wireframe','points','boundingBox','smoothShaded','flatShaded']
    ))

    attrData.append(attrNode(
    longName='wireframeOnShaded',
    shortName='wos', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='headsUpDisplay',
    shortName='hud', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='selectionHiliteDisplay',
    shortName='sel', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='useDefaultMaterial',
    shortName='udm', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='useColorIndex',
    shortName='uci', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='useColorIndex',
    shortName='uci', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='userNode',
    shortName='un', 
    type='string',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='wireframeBackingStore',
    shortName='wbs', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='useRGBImagePlane',
    shortName='ip', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='updateColorMode',
    shortName='ucm', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='backfaceCulling',
    shortName='bfc', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='xray',
    shortName='xr', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='jointXray',
    shortName='jx', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='activeComponentsXray',
    shortName='acx', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='maxConstantTransparency',
    shortName='mct', 
    type='float',
    mode='e',
    value=None,
    active=0,
    option=[0,1]
    ))

    attrData.append(attrNode(
    longName='displayTextures',
    shortName='dtx', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='smoothWireframe',
    shortName='swf', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='lineWidth',
    shortName='lw', 
    type='float',
    mode='e',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='textureMaxSize',
    shortName='tms', 
    type='int',
    mode='e',
    value=None,
    active=0,
    option=[0,None]
    ))

    attrData.append(attrNode(
    longName='textureAnisotropic',
    shortName='ta', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='textureSampling',
    shortName='ts', 
    type='int',
    mode='e',
    value=None,
    active=0,
    option=[1,2]
    ))

    attrData.append(attrNode(
    longName='textureDisplay',
    shortName='td', 
    type='string',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='textureHilight',
    shortName='th', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='fogging',
    shortName='fg', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='fogSource',
    shortName='fsc', 
    type='string',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='fogMode',
    shortName='fmd', 
    type='menu',
    mode='e',
    value=None,
    active=0,
    option=['linear','exponent','exponent2']
    ))

    attrData.append(attrNode(
    longName='fogDensity',
    shortName='fdn', 
    type='float',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='fogEnd',
    shortName='fen', 
    type='float',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='fogStart',
    shortName='fst', 
    type='float',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='fogColor',
    shortName='fcl', 
    type='colorA',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='shadows',
    shortName='sdw', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='rendererName',
    shortName='rnm', 
    type='menu',
    mode='e',
    value=None,
    active=0,
    option=['base_OpenGL_Renderer','hwRender_OpenGL_Renderer']
    ))

    attrData.append(attrNode(
    longName='colorResolution',
    shortName='crz', 
    type='int2',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='bumpResolution',
    shortName='brz', 
    type='int2',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='transparencyAlgorithm',
    shortName='tal', 
    type='menu',
    mode='e',
    value=None,
    active=0,
    option=['frontAndBackCull','perPolygonSort']
    ))

    attrData.append(attrNode(
    longName='transpInShadows',
    shortName='tis', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='cullingOverride',
    shortName='cov', 
    type='menu',
    mode='e',
    value=None,
    active=0,
    option=['none','doubleSided','singleSided']
    ))

    attrData.append(attrNode(
    longName='lowQualityLighting',
    shortName='lql', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='occlusionCulling',
    shortName='ocl', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='useBaseRenderer',
    shortName='ubr', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='nurbsCurves',
    shortName='nc', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='nurbsSurfaces',
    shortName='ns', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='polymeshes',
    shortName='pm', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='subdivSurfaces',
    shortName='sds', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='planes',
    shortName='pl', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='lights',
    shortName='lt', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='cameras',
    shortName='ca', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='controlVertices',
    shortName='cv', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='grid',
    shortName='gr', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='hulls',
    shortName='hu', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='joints',
    shortName='j', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='ikHandles',
    shortName='ikh', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='deformers',
    shortName='df', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='fluids',
    shortName='fl', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='hairSystems',
    shortName='hs', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='follicles',
    shortName='fo', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='nCloths',
    shortName='ncl', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='nParticles',
    shortName='npa', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='nRigids',
    shortName='nr', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='dynamicConstraints',
    shortName='dc', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='locators',
    shortName='lc', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))
    attrData.append(attrNode(
    longName='manipulators',
    shortName='m', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))
    
    attrData.append(attrNode(
    longName='dimensions',
    shortName='dim', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='handles',
    shortName='ha', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='pivots',
    shortName='pv', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='textures',
    shortName='tx', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='strokes',
    shortName='str', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))
    attrData.append(attrNode(
    longName='allObjects',
    shortName='alo', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='useInteractiveMode',
    shortName='ui', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))
    
    attrData.append(attrNode(
    longName='sortTransparent',
    shortName='st', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))

    attrData.append(attrNode(
    longName='viewSelected',
    shortName='vs', 
    type='boolean',
    mode='e',
    value=None,
    active=0,
    ))
    return attrData
