VRayAttrDict = {}
#vray-materials:
VRayAttrDict['Material ID'] = ['vray_material_id','vrayMaterialId']
VRayAttrDict['V-Ray material override'] = ['vray_specific_mtl','vrayEnableAllOverrides']
VRayAttrDict['Closed Volume Shading'] = ['vray_closed_volume','vrayClosedVolume']
#materials:
#VRayAttrDict['Material ID'] = ['vray_material_id','vrayMaterialId']
#VRayAttrDict['V-Ray material override'] = ['vray_specific_mtl','vrayEnableAllOverrides']
#mesh:
VRayAttrDict['Subdivision'] = ['vray_subdivision','vraySubdivEnable']
VRayAttrDict['Subdivision and Displacement Quality'] = ['vray_subquality','vrayOverrideGlobalSubQual']
VRayAttrDict['Displacement control'] = ['vray_displacement','vrayDisplacementNone']
VRayAttrDict['Round edges'] = ['vray_roundedges','vrayRoundEdges']
VRayAttrDict['User attributes'] = ['vray_user_attributes','vrayUserAttributes']
VRayAttrDict['Object ID'] = ['vray_objectID','vrayObjectID']
VRayAttrDict['Fog fade out radius'] = ['vray_fogFadeOut','vrayFogFadeOut']
VRayAttrDict['Phoenix Object Properties'] = ['vray_phoenix_object','vrayPhoenixObjVoxels']
#nurbsCurve:
VRayAttrDict['Renderable'] = ['vray_nurbscurve_renderable','vrayNurbsCurveRenderable']
#nurbsSurface:
#VRayAttrDict['Object ID'] = ['vray_objectID','vrayObjectID']
#VRayAttrDict['User attributes'] = ['vray_user_attributes','vrayUserAttributes']
#transform:
#VRayAttrDict['User attributes'] = ['vray_user_attributes','vrayUserAttributes']
VRayAttrDict['Skip Rendering'] = ['vray_skip_export','vraySkipExport']
#camera:
VRayAttrDict['Physical Camera'] = ['vray_cameraPhysical','vrayCameraPhysicalOn']
VRayAttrDict['Camera Settings'] = ['vray_cameraOverrides','vrayCameraOverridesOn']
VRayAttrDict['Dome Camera'] = ['vray_cameraDome','vrayCameraDomeOn']
#file:
VRayAttrDict['Texture input gamma'] = ['vray_file_gamma','vrayFileGammaEnable']
VRayAttrDict['Allow negative colors'] = ['vray_file_allow_neg_colors','vrayFileAllowNegColors']
VRayAttrDict['Image file list (IFL)'] = ['vray_file_ifl','vrayFileIFLStartFrame']
VRayAttrDict['Texture filter'] = ['vray_texture_filter','vrayOverrideTextureFilter']
#imagePlane:
#VRayAttrDict['Texture input gamma'] = ['vray_file_gamma','vrayFileGammaEnable']
#VRayAttrDict['Allow negative colors'] = ['vray_file_allow_neg_colors','vrayFileAllowNegColors']
#place2dTexture:
VRayAttrDict['2D Placement Options'] = ['vray_2d_placement_options','vrayUVSetName']
#samplerInfo:
VRayAttrDict['Additional outputs'] = ['vray_samplerinfo_extra_tex','vrayNormalObj']
#pointLight, spotLight:
VRayAttrDict['Light Attributes (Point)'] = ['vray_pointLight','vrayPhotonSubdivs']
#directionalLight:
VRayAttrDict['Light Attributes (Direct)'] = ['vray_directlight','vrayPhotonSubdivs']
#ambientLight:
VRayAttrDict['Light Attributes (Ambient)'] = ['vray_light','vrayPhotonSubdivs']
#areaLight:
VRayAttrDict['Light Attributes (Area)'] = ['vray_arealight','vrayPhotonSubdivs']
#vray-lights:
#VRayAttrDict['Object ID'] = ['vray_objectID','vrayObjectID']
VRayAttrDict['Light Path Expressions label'] = ['vray_lpe_label','vrayLPELabel']
#other
VRayAttrDict['Local ray server'] = ['vray_localrayserver','vrayLocalRayserver']

def apply_vray_attribute(attr_key, action=True, *args):
    vray_attribute_group = VRayAttrDict[attr_key][0]
    for node in cmds.ls(sl=True, dag=True, shapes=True, long=True):
        cmds.vray("addAttributesFromGroup", node, vray_attribute_group, 1 if action else 0)

def vray_attribute_exists(attr_key, node):
    return cmds.attributeQuery(VRayAttrDict[attr_key][1], node=node, exists=True)

selected_nodes = cmds.ls(sl=True, dag=True, shapes=True, long=True)

if not selected_nodes:
    cmds.confirmDialog(title='Error', message='No objects selected.', button=['OK'], defaultButton='OK')
else:
    if cmds.window('window1', q=True, ex=True):
        cmds.deleteUI('window1')

    cmds.window('window1', title="VRay Attributes", mb=True, mnb=False, mxb=False, sizeable=False)
    main_layout = cmds.columnLayout(adjustableColumn=True)
    checkbox_layout = cmds.columnLayout(parent=main_layout, adjustableColumn=False, rowSpacing=5, columnAttach=('left', 5))

    cmds.separator()

    for attr_key in sorted(VRayAttrDict):
        initial_state = vray_attribute_exists(attr_key, selected_nodes[0])
        cmds.checkBox(
            label=attr_key, 
            value=initial_state, 
            onc=partial(apply_vray_attribute, attr_key, True),
            ofc=partial(apply_vray_attribute, attr_key, False)
        )

    cmds.separator()
    cmds.showWindow('window1')