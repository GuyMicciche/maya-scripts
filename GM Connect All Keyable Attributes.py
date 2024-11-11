import maya.cmds as cmds

scriptJobID = None
original_values = {}  # Dictionary to store original values

def populate_attributes_list():
    """
    Populates the list with attributes of the first object selected.
    """
    sel = cmds.ls(sl=True)
    attributes = []
    print(sel)
    if sel and len(sel) > 1:
        first_obj = sel[0]
        attributes = cmds.listAttr(first_obj, k=True, v=True)  # only keyable attributes
    
    if cmds.textScrollList('attributesList', exists=True):
        cmds.textScrollList('attributesList', edit=True, removeAll=True)
        if attributes:
            cmds.textScrollList('attributesList', edit=True, append=attributes)

def store_original_values(attr, target_objs):
    """
    Stores original values of attributes for target objects.
    """
    for target_obj in target_objs:
        if target_obj not in original_values:
            original_values[target_obj] = {}

        if attr not in original_values[target_obj]:
            original_values[target_obj][attr] = cmds.getAttr(f'{target_obj}.{attr}')

def restore_original_values(attr, target_objs):
    """
    Restore the original values of the provided attribute for each of the target objects.
    """
    for target_obj in target_objs:
        connection = cmds.listConnections(f'{target_obj}.{attr}', source=True, plugs=True)
        if connection:
            cmds.disconnectAttr(connection[0], f'{target_obj}.{attr}')
            print(original_values[target_obj][attr])

        if target_obj in original_values and attr in original_values[target_obj]:
            cmds.setAttr(f'{target_obj}.{attr}', original_values[target_obj][attr])
            original_values[target_obj].pop(attr)

def connect_selected_attributes(*args):
    """
    Connects or disconnects selected attributes from the first object 
    to or from all other selected objects based on list selection.
    """
    sel = cmds.ls(sl=True)
    if len(sel) < 2:
        cmds.warning("Please select at least two objects.")
        return
        
    source_obj = sel[0]
    target_objs = sel[1:]

    selected_attrs = cmds.textScrollList('attributesList', query=True, selectItem=True)
    if not selected_attrs:
        selected_attrs = []

    all_attrs = cmds.textScrollList('attributesList', query=True, allItems=True)
    deselected_attrs = [attr for attr in all_attrs if attr not in selected_attrs]

    for attr in selected_attrs:
        store_original_values(attr, target_objs)
        for target_obj in target_objs:
            try:
                cmds.connectAttr(f'{source_obj}.{attr}', f'{target_obj}.{attr}')
                print(f'Connected {attr} from {source_obj} to {target_obj}')
            except:
                cmds.warning(f'Failed to connect {attr} from {source_obj} to {target_obj}.')

    for attr in deselected_attrs:
        try:
            restore_original_values(attr, target_objs)
        except Exception as e:
            cmds.warning(f'Failed to restore value {attr}.')
        

def create_attribute_connector_ui():
    """
    Creates the UI for connecting attributes.
    """
    global scriptJobID

    if cmds.window('attributeConnector', exists=True):
        cmds.deleteUI('attributeConnector', window=True)

    cmds.window('attributeConnector', title='Attribute Connector', widthHeight=(350, 400), closeCommand=cleanup_scriptJob)
    cmds.columnLayout(adjustableColumn=True, columnAlign='left', columnOffset=('both', 10))

    cmds.text(label='Attributes of first selected object:')
    cmds.textScrollList('attributesList', allowMultiSelection=True, selectCommand=connect_selected_attributes)

    cmds.showWindow('attributeConnector')
    populate_attributes_list()

    # Create a scriptJob to monitor selection changes and repopulate the list when it changes
    scriptJobID = cmds.scriptJob(event=["SelectionChanged", populate_attributes_list])

def cleanup_scriptJob():
    """
    Removes the scriptJob when the window is closed.
    """
    global scriptJobID
    if scriptJobID:
        if cmds.scriptJob(exists=scriptJobID):
            cmds.scriptJob(kill=scriptJobID, force=True)

# Call the UI creation function
create_attribute_connector_ui()