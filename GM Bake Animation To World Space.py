import maya.cmds as cmds

def bake_animation_to_world_space(selected_objects, isSimulation):
	# Set time range to current animation range
	start_time = cmds.playbackOptions(query=True, minTime=True)
	end_time = cmds.playbackOptions(query=True, maxTime=True)

	bakeList = []
	# Bake animation to world space for each selected object
	for obj in selected_objects:	
		# Duplicate object								
		duplObj = cmds.duplicate(obj, name=obj+'_bakedToWorld', rc=True, rr=True, ic=True)
		
		# Delete duplicated children
		childrenTd = cmds.listRelatives(duplObj, c=True, pa=True)[1:]
		for c in childrenTd:
			cmds.delete(c)

		# Check if selected object is a child of an object	
		par = cmds.listRelatives(obj, parent=True)
		if par == None:
			print('%s has no Parent Object' %n)
			toBake = duplObj
		else:
			#unparent object
			toBake = cmds.parent(duplObj, w=True)
		
		# Add constraints and append it to bake List	
		bakeList.append(toBake)
		cmds.parentConstraint(obj, toBake, mo=False)
		cmds.scaleConstraint(obj, toBake, mo=False)
	
	# Bake animation to world space for current object and delete contraints
	for bakeObj in bakeList:
		cmds.bakeResults(bakeObj, simulation=isSimulation, time=(start_time, end_time), sampleBy=1, disableImplicitControl=True, preserveOutsideKeys=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True, controlPoints=False, shape=True)
		cmds.delete(bakeObj[0] + '*Constraint*')
		
	print("Animation baked to world space.")

# Get selected objects
selected_objects = cmds.ls(selection=True)
isSimulation = False

# Call function to bake animation to world space
bake_animation_to_world_space(selected_objects, isSimulation)