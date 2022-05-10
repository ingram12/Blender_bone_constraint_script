import bpy

rig_name = "rig"

for bone in bpy.context.selected_pose_bones:
    nc = bone.constraints.new(type='COPY_LOCATION')
    nc.target = bpy.data.objects[rig_name]
    nc.subtarget = bone.name
    nc = bone.constraints.new(type='COPY_ROTATION')
    nc.target = bpy.data.objects[rig_name]
    nc.subtarget = bone.name