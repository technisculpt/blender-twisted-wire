import bpy

class Twisted_Pair(bpy.types.Operator):
    bl_idname = 'twisted_pair.create_pair'
    bl_label = 'twisted pair op'
    bl_options = {'INTERNAL'}
    bl_description = "Create Twisted Pair"

    def execute(self, context):

        print(context.scene.twisted_pair.cap_fill)

        self.report({'INFO'}, "FINISHED")
        return {'FINISHED'}