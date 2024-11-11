"""
V-Ray Attribute Manager
Version: 1.0.0
Author: Guy Micciche
Year: 2023

Description:
    This script provides a user interface for managing V-Ray attributes in Autodesk Maya.
    Users can easily select nodes and apply or remove specific V-Ray attributes.

Usage:
    - Run the script in Maya's Python Script Editor.
    - Choose the type of node (Shape or Transform) using the radio buttons.
    - The script will display relevant V-Ray attributes for the selected node type.
    - Check or uncheck the boxes to apply or remove attributes, respectively.

Notes:
    This script relies on several helper functions (not shown here) such as:
    - `get_api_type_of_selected`
    - `get_relevant_vray_attrs`
    - `vray_attribute_exists`
    - `apply_vray_attribute`
    Ensure these functions are defined and available when using this script.

Changelog:
    1.0.0 - Initial version. Basic UI and V-Ray attribute management.

Disclaimer:
    Use at your own risk. Always keep backups of your scene before using any script.
"""

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
from functools import partial

def get_all_vray_attrs():
    """Given a Maya node type, return a list of relevant V-Ray attributes."""
    # V-Ray attributes categorized by full name.
    vray_attrs = {
        #vray-materials:
        "Material ID": ['vray_material_id','vrayColorId'],
        "V-Ray material override": ['vray_specific_mtl','vrayEnableAllOverrides'],
        "Closed Volume Shading": ['vray_closed_volume','vrayClosedVolume'],
		"Light Path Expressions label": ['vray_lpe_label','vrayLPELabel'],
        #materials:
        #"Material ID": ['vray_material_id','vrayColorId'],
        #"V-Ray material override": ['vray_specific_mtl','vrayEnableAllOverrides'],
        #mesh:
        "Subdivision": ['vray_subdivision','vraySubdivEnable'],
        "Subdivision and Displacement Quality": ['vray_subquality','vrayOverrideGlobalSubQual'],
        "Displacement control": ['vray_displacement','vrayDisplacementNone'],
        "Round edges": ['vray_roundedges','vrayRoundEdges'],
        "User attributes": ['vray_user_attributes','vrayUserAttributes'],
        "Object ID": ['vray_objectID','vrayObjectID'],
        "Fog fade out radius": ['vray_fogFadeOut','vrayFogFadeOut'],
        "Phoenix Object Properties": ['vray_phoenix_object','vrayPhoenixObjVoxels'],
        #nurbsCurve:
        "Renderable": ['vray_nurbscurve_renderable','vrayNurbsCurveRenderable'],
        #nurbsSurface:
        #"Object ID": ['vray_objectID','vrayObjectID'],
        #"User attributes": ['vray_user_attributes','vrayUserAttributes'],
        #transform:
        #"User attributes": ['vray_user_attributes','vrayUserAttributes'],
        "Skip Rendering": ['vray_skip_export','vraySkipExport'],
        #camera:
        "Physical Camera": ['vray_cameraPhysical','vrayCameraPhysicalOn'],
        "Camera Settings": ['vray_cameraOverrides','vrayCameraOverridesOn'],
        "Dome Camera": ['vray_cameraDome','vrayCameraDomeOn'],
		"Stereoscopic camera": ['vray_cameraStereoscopic','vrayCameraStereoscopicOn'],
        #file:
        "Texture input gamma": ['vray_file_gamma','vrayFileGammaEnable'],
        "Allow negative colors": ['vray_file_allow_neg_colors','vrayFileAllowNegColors'],
        "Image file list (IFL)": ['vray_file_ifl','vrayFileIFLStartFrame'],
        "Texture filter": ['vray_texture_filter','vrayOverrideTextureFilter'],
		"Texture Filter Blur": ['vray_texture_filter_blur','vrayTextureFilterBlur'],
        "Ignore Data Window": ['vray_ignore_data_window','vrayIgnoreDataWindow'],
		"Override Maya-style Alpha Detection": ['vray_use_maya_alpha_detection','vrayMayaAlphaDetection'],
		#imagePlane:
        #"Texture input gamma": ['vray_file_gamma','vrayFileGammaEnable'],
        #"Allow negative colors": ['vray_file_allow_neg_colors','vrayFileAllowNegColors'],
        #place2dTexture:
        "2D Placement Options": ['vray_2d_placement_options','vrayUVSetName'],
        #samplerInfo:
        "Additional outputs": ['vray_samplerinfo_extra_tex','vrayNormalObj'],
        #pointLight, spotLight:
        "Light Attributes (Point)": ['vray_pointLight','vrayPhotonSubdivs'],
        #directionalLight:
        "Light Attributes (Direct)": ['vray_directlight','vrayPhotonSubdivs'],
        #ambientLight:
        "Light Attributes (Ambient)": ['vray_light','vrayPhotonSubdivs'],
        #areaLight:
        "Light Attributes (Area)": ['vray_arealight','vrayPhotonSubdivs'],
        #"Object ID": ['vray_objectID','vrayObjectID'],
        #other
        "Local ray server": ['vray_localrayserver','vrayLocalRayserver']
    }
    return vray_attrs

def get_relevant_vray_attrs(node_type):
    """Given a Maya node type, return a list of relevant V-Ray attributes."""
    # V-Ray attributes categorized by Maya node types.
    vray_attrs_by_type = {
        "kMesh": ["vray_subdivision", "vray_subquality", "vray_displacement", "vray_opensubdiv", "vray_roundedges", "vray_user_attributes", "vray_objectID", "vray_fogFadeOut", "vray_localrayserver"],
        "xgmSubdPatch": ["vray_subdivision", "vray_subquality", "vray_displacement", "vray_opensubdiv", "vray_user_attributes", "vray_objectID", "vray_localrayserver"],
        "kSubdiv": ["vray_subquality", "vray_displacement", "vray_objectID", "vray_user_attributes"],
        "kParticle": ["vray_particle_export_attributes", "vray_sprite_orient", "vray_point_size"],
        "kNParticle": ["vray_particle_export_attributes", "vray_sprite_orient", "vray_point_size", "vray_particle_cache", "vray_instancer_overrides"],
        "kSpotLight": ["vray_pointLight"],
        "kAreaLight": ["vray_arealight"],
        "kPointLight": ["vray_pointLight"],
        "kDirectionalLight": ["vray_directlight"],
        "kAmbientLight": ["vray_light"],
        "kNurbsSurface": ["vray_nusrbsStaticGeom", "vray_objectID", "vray_user_attributes"],
        "kBlinn": ["vray_materialsGlossiness", "vray_material_id", "vray_specific_mtl"],
        "kPhong": ["vray_materialsGlossiness", "vray_material_id", "vray_specific_mtl"],
        "kPhongExplorer": ["vray_materialsGlossiness", "vray_material_id", "vray_specific_mtl"],
        "kLambert": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "kAnisotropy": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "kRampShader": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "kSurfaceShader": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "kAssembly": ["vray_scene_assembly"],
        "VRayMtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl", "vray_closed_volume", "vray_roundedges"],
        "VRayToonMtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl", "vray_closed_volume"],
        "VRayMtl2Sided": ["vray_material_id", "vray_specific_mtl"],
        "VRayLightMtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayFastSSS2": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRaySkinMtl": ["vray_material_id", "vray_specific_mtl"],
        "VRayBlendMtl": ["vray_material_id", "vray_specific_mtl", "vray_roundedges"],
        "VRaySimbiont": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayBumpMtl": ["vray_material_id", "vray_specific_mtl"],
        "VRayCarPaintMtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayCarPaint2Mtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayFlakesMtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayMtlWrapper": ["vray_material_id"],
        "VRayMtlRenderStats": ["vray_material_id"],
        "VRayMeshMaterial": ["vray_material_id", "vray_specific_mtl"],
        "VRayPluginNodeMtl": ["vray_material_id", "vray_specific_mtl"],
        "VRayMtlGLSL": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayMtlHair2": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayMtlHair3": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayHairNextMtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayVismatMtl": ["vray_material_id", "vray_specific_mtl"],
        "VRayAlSurface": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl", "vray_roundedges"],
        "VRayScannedMtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "bifrostLiquidMaterial": ["vray_bifrost_mtl", "vray_material_id", "vray_specific_mtl"],
        "bifrostShape": ["vray_bifrost_shape", "vray_fluid_shading_quality", "vray_fluid_legacy_phoenix_fd_shading"],
        "kCamera": ["vray_cameraPhysical", "vray_cameraOverrides", "vray_cameraDome", "vray_cameraStereoscopic"],
        "kStereoCameraMaster": ["vray_cameraPhysical", "vray_cameraOverrides", "vray_cameraDome", "vray_cameraStereoscopic"],
        "kShadingEngine": ["vray_specific_mtl", "vray_material_id", "vray_roundedges"],
        "kTransform": ["vray_skip_export", "vray_objectID", "vray_user_attributes"],
        "kLodGroup": ["vray_skip_export", "vray_objectID"],
        "VRayDisplacement": ["vray_subdivision", "vray_displacement", "vray_opensubdiv", "vray_subquality", "vray_localrayserver"],
        "VRayPtex": ["vray_file_gamma", "vray_file_ifl"],
        "kFileTexture": ["vray_file_gamma", "vray_file_allow_neg_colors", "vray_file_ifl", "vray_texture_filter", "vray_texture_filter_blur", "vray_ignore_data_window", "vray_use_maya_alpha_detection"],
        "substance": ["vray_file_gamma", "vray_file_allow_neg_colors", "vray_texture_filter", "vray_texture_format"],
        "kImagePlane": ["vray_file_gamma", "vray_file_allow_neg_colors", "vray_texture_filter"],
        "kFluid": ["vray_fluid_shading_quality", "vray_fluid_legacy_phoenix_fd_shading"],
        "kNurbsCurve": ["vray_nurbscurve_renderable"],
        "kSamplerInfo": ["vray_samplerinfo_extra_tex", "vray_2d_placement_options"],
        "VRayLightRect": ["vray_objectID"],
        "VRayLightSphere": ["vray_objectID"],
        "VRayLightDome": ["vray_objectID"],
        "kProjection": ["vray_projection_options"],
        "kPlace2dTexture": ["vray_2d_placement_options"],
        "kPlace3dTexture": ["vray_3d_placement_options", "vray_motion_blur_samples"],
        "kHairSystem": ["vray_hair_shader", "vray_hair_geom"],
        "xgmSplineDescription": ["vray_hair_geom"],
        "HairShape": ["vray_hair_geom"],
        "kSurfaceLuminance": ["vray_surface_luminance"],
        "gpuCache": ["vray_subdivision", "vray_subquality", "vray_displacement", "vray_roundedges", "vray_user_attributes", "vray_objectID", "vray_fogFadeOut"],
        "VRayVolumeGrid": ["vray_pointLight"],
        "VRayMetaball": ["vray_objectID"],
        "rfrk_particler4": ["vray_rfrk_particler"],
        "rfrk_particler5": ["vray_rfrk_particler"],
        "partioVisualizer": ["vray_partio"],
        "partioInstancer": ["vray_partio"],
        "kLeather": ["vray_legacy_look"],
        "kCloth": ["vray_legacy_look"],
        "VRayProxy": ["vray_subdivision", "vray_subquality", "vray_displacement", "vray_roundedges", "vray_user_attributes", "vray_objectID", "vray_fogFadeOut", "vray_localrayserver"],
        "VRayStochasticFlakesMtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
        "VRayFlakes2Mtl": ["vray_material_id", "vray_lpe_label", "vray_specific_mtl"],
    }    
    return vray_attrs_by_type.get(node_type, [])

def add_selection_changed_script_job():
    global selection_changed_script_job_id

    # Ensure any pre-existing scriptJob with the same function is killed before creating a new one
    if 'selection_changed_script_job_id' in globals():
        cmds.scriptJob(kill=selection_changed_script_job_id, force=True)

    # This scriptJob triggers the show_attributes function whenever the user changes their selection in Maya
    selection_changed_script_job_id = cmds.scriptJob(event=["SelectionChanged", show_attributes])

def kill_script_jobs(*args):
    if 'selection_changed_script_job_id' in globals():
        cmds.scriptJob(kill=selection_changed_script_job_id, force=True)
    
def apply_vray_attribute(selected_nodes, attr_key, action=True, *args):
    vray_attribute_group = get_all_vray_attrs()[attr_key][0]
    for node in selected_nodes:
        cmds.vray("addAttributesFromGroup", node, vray_attribute_group, 1 if action else 0)

def vray_attribute_exists(attr_key, node):
    return cmds.attributeQuery(get_all_vray_attrs()[attr_key][1], node=node, exists=True)
    
def get_api_type_of_selected(selected_nodes):
    # Get the list of currently selected objects.
    sel = selected_nodes

    if not sel:  # Check if anything is selected
        return None

    # Take the first selected object for this example.
    selected_obj = sel[0]

    # Create an MSelectionList object.
    sel_list = OpenMaya.MSelectionList()
    sel_list.add(selected_obj)

    # Create an MObject for our object.
    obj = OpenMaya.MObject()
    sel_list.getDependNode(0, obj)

    # Return the API type of the object.
    return obj.apiTypeStr() if not obj.apiTypeStr().startswith("kPlugin") else cmds.nodeType(selected_obj)

# When a bullet is selected
def on_bullet_selected(*args):
    selected_index = cmds.radioButtonGrp(radio_buttons, query=True, select=True)
    selected_label = cmds.radioButtonGrp(radio_buttons, query=True, labelArray=True)[selected_index-1]
    apply_vray_attribute(selected_label)
    
def show_attributes(*args):
    # Delete existing checkboxes from the checkboxLayout
    children = cmds.columnLayout('checkboxLayout', query=True, childArray=True)
    if children:
        for child in children:
            cmds.deleteUI(child)
    
    # Get selected node type from the radio buttons
    selected_type = cmds.radioButtonGrp(radio_buttons, query=True, labelArray2=True)[cmds.radioButtonGrp(radio_buttons, query=True, select=True) - 1]
    
    if selected_type == "Shape":
        selected_nodes = cmds.ls(sl=True, dag=True, shapes=True, long=True)
    else:  # Assuming Transform
        selected_nodes = cmds.ls(sl=True)

    if not cmds.ls(sl=True):
        cmds.text(label="Make a selection.", parent='checkboxLayout')
        return
        
    node_type = get_api_type_of_selected(selected_nodes)
    if node_type is not None and selected_nodes:
        cmds.text(label=node_type + " selected:", parent='checkboxLayout')
    else:
        #cmds.confirmDialog(title='Error', message='No objects selected.', button=['OK'], defaultButton='OK')
        cmds.text(label="No "+selected_type.lower()+" node for "+cmds.ls(sl=True)[0]+".", parent='checkboxLayout')
        return        

    # Dictionary to hold matched attributes
    matched_vray_attrs = {}

    for attr in get_relevant_vray_attrs(node_type):
        for key, vray_attr_list in get_all_vray_attrs().items():
            if attr == vray_attr_list[0]:  # If it matches the first item in the get_all_vray_attrs value list
                matched_vray_attrs[key] = vray_attr_list
    
    if matched_vray_attrs:  # If there are matched V-Ray attributes
        #for attr_key in sorted(matched_vray_attrs):
        for attr_key in matched_vray_attrs:
            initial_state = vray_attribute_exists(attr_key, selected_nodes[0])
            cmds.checkBox(
                label=attr_key,
                value=initial_state,
                onc=partial(apply_vray_attribute, selected_nodes, attr_key, True),
                ofc=partial(apply_vray_attribute, selected_nodes, attr_key, False),
                parent='checkboxLayout'
            )
    else:  # If there are no matched V-Ray attributes
        cmds.text(label="No applicable V-Ray Extra Attributes on "+selected_type.lower()+" node.", parent='checkboxLayout')

def createUI():
    global radio_buttons, main_layout, checkbox_layout
    
    # Check if the window exists
    if cmds.window("vrayAttributeWindow", exists=True):
        cmds.deleteUI("vrayAttributeWindow", window=True)

    # Create the main window
    cmds.window("vrayAttributeWindow", title="V-Ray Attribute Manager", closeCommand=kill_script_jobs)

    # Create the main layout
    main_layout = cmds.columnLayout(adjustableColumn=True)
    
    cmds.text(label="Select Node Type:")
    
    # Add the radio button for Shape or Transform selection and center align radio buttons using rowLayout
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(100, 200, 100), adjustableColumn=2)
    cmds.separator(width=100, style='none')  # Empty spacer on the left side
    radio_buttons = cmds.radioButtonGrp(labelArray2=["Shape", "Transform"], numberOfRadioButtons=2, select=1, onCommand=show_attributes, width=200)
    cmds.separator(width=100, style='none')  # Empty spacer on the right side
    cmds.setParent('..')  # Move back to the main layout

    cmds.separator(parent=main_layout)
    
    # Create the checkbox layout
    checkbox_layout = cmds.columnLayout('checkboxLayout', parent=main_layout, adjustableColumn=True, rowSpacing=5, columnAttach=('left', 5))

    cmds.separator(parent=main_layout)
    
    # Display the window
    cmds.showWindow("vrayAttributeWindow")
    
# Initialize UI
def initializeUI():
    createUI()
    add_selection_changed_script_job()
    show_attributes()

initializeUI()