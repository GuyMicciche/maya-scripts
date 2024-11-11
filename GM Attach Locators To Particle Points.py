import maya.cmds as cmds
import functools
import math

def create_locators(num_locators, add_rotations):
    selected_particle_transform = cmds.ls(selection=True, type="transform")
    if not selected_particle_transform:
        #cmds.error("Please select a particle transform node.")
        cmds.confirmDialog(title='Error!', message='Please select a particle transform node.', button=['OK'], defaultButton='OK')
        return

    particle_transform = selected_particle_transform[0]
    particle_shape = cmds.listRelatives(particle_transform, shapes=True, type=["particle", "nParticle"])
    if not particle_shape:
        #cmds.error("Selected node is not a valid particle transform.")
        cmds.confirmDialog(title='Error!', message='Selected node is not a valid particle transform.', button=['OK'], defaultButton='OK')
        return

    particle_shape = particle_shape[0]

    particle_ids = cmds.getAttr(particle_shape + ".id")
    if particle_ids is None:
        return

    num_particles = len(particle_ids)
    if num_locators > num_particles:
        num_locators = num_particles

    locators = []
    for i in range(num_locators):
        locator = cmds.spaceLocator(name="locator{}".format(i+1))[0]
        locators.append(locator)

    for i, locator in enumerate(locators):
        script = """
string $particleShape = "{particle_shape}"; // Replace with your particle shape's name
int $particleId = {particle_id}; // Replace with the particle ID you want to check

// Get all particle IDs from the particle shape
float $ids[] = `getAttr ($particleShape + ".id")`;

// Check if particle ID exists in the particle shape
int $exists = 0;
for ($i = 0; $i < size($ids); $i++) {{
    if ($ids[$i] == $particleId) {{
        $exists = 1;
        break;
    }}
}}

if ($exists == 1)
{{
    float $position[] = `getParticleAttr -at position ($particleShape + ".pt["+$particleId+"]")`;
    {locator_name}.translateX = $position[0];
    {locator_name}.translateY = $position[1];
    {locator_name}.translateZ = $position[2];
}}
else
{{
    {locator_name}.translateX = 0;
    {locator_name}.translateY = 0;
    {locator_name}.translateZ = 0;
}}"""
        if add_rotations:
            script = script + """
            
if ($exists == 1)
{{
    float $rotation[] = `getParticleAttr -at rotationPP ($particleShape + ".pt["+$particleId+"]")`;
    {locator_name}.rotateX = $rotation[0];
    {locator_name}.rotateY = $rotation[1];
    {locator_name}.rotateZ = $rotation[2];
}}
else
{{
    {locator_name}.rotateX = 0;
    {locator_name}.rotateY = 0;
    {locator_name}.rotateZ = 0;
}}"""

        particle_id = math.floor(particle_ids[i])
        script_name = "locator{}_script".format(i+1)
        script_cmd = script.format(particle_shape=particle_shape, particle_id=particle_id, locator_name=locator)
        #cmds.scriptNode(st=2, bs=script_cmd, n=script_name) # this create a script node
        cmds.expression( s=script_cmd ) # this create an expression

    return locators

def create_locators_ui():
    window_name = "LocatorCreationWindow"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name, window=True)

    cmds.window(window_name, title="Locator Creation", widthHeight=(300, 100))
    cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="Enter the number of locators to create:")
    locator_count_field = cmds.intField(minValue=1, value=1)
    add_rotations_field = cmds.checkBox(label="Rotation")

    def create_locators_callback(*args):
        locator_count = cmds.intField(locator_count_field, query=True, value=True)
        add_rotations = cmds.checkBox(add_rotations_field, query=True, value=True)
        locators = create_locators(locator_count, add_rotations)

        if locators:
            print("Locators created successfully.")
        else:
            print("Could not create locators. Make sure you scroll to a time where there are particles on screen.")

    cmds.button(label="Create Locators", command=functools.partial(create_locators_callback))

    cmds.showWindow(window_name)

create_locators_ui()