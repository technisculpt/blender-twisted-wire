import bpy

class Twisted_Pair_Settings(bpy.types.PropertyGroup):

    cap_fill : bpy.props.EnumProperty(
                name = "Cap Fill Type",
                description = "Cap Fill Type",
                items= [('0', 'Triangle Fan', ''),
                        ('1', 'N-Gon', ''),
                        ('2', 'Nothing', '')]
    )

    vert_segs : bpy.props.IntProperty(
        name="Vertical Segments",
        description="Vertical Segments",
        default=2,
        min=1, max=1000,
    )

    cyl_segs : bpy.props.IntProperty(
        name="Cylindrical Segments",
        description="Cylindrical Segments",
        default=20,
        min=3, max=1000,
    )    

    turns : bpy.props.IntProperty(
        name="Turns",
        description="Turns",
        default=2,
        min=1, max=1000,
    )

    radius : bpy.props.FloatProperty(
        name="Diameter",
        description="Radius of wire",
        default=1.0,
        min=0.1, max=1000.0, # cam we re,pve max limit?
    )

    gap : bpy.props.FloatProperty(
        name="Gap",
        description="Gap between wire pair",
        default=0.0,
        min=0.1, max=1000.0,
    )

    length : bpy.props.FloatProperty(
        name="Length",
        description="Length of Wire Pair",
        default=0.0,
        min=0.1, max=1000.0,
    )

class TwistedPair_PT(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Twisted Wire Pair'
    bl_context = 'objectmode'
    bl_category = 'Twisted Wire Pair'
    bl_idname  = 'VIEW_3D_PT_twisted_pair'


    def draw(self, context):
        layout = self.layout
        scene = context.scene.twisted_pair

        col = layout.column(align=True)
        col.use_property_split = True
        col.prop(scene, 'cap_fill', text='Cap Fill Type')

        col = layout.column(align=True)
        col.use_property_split = True
        col.prop(scene, 'vert_segs', text='Vertical Segments')

        col = layout.column(align=True)
        col.use_property_split = True
        col.prop(scene, 'cyl_segs', text='Cylinder Segments')
        
        col = layout.column(align=True)
        col.use_property_split = True
        col.prop(scene, 'turns', text='Turns')

        col = layout.column(align=True)
        col.use_property_split = True
        col.prop(scene, 'radius', text='Wire Radius')

        col = layout.column(align=True)
        col.use_property_split = True
        col.prop(scene, 'length', text='Length')

        col = layout.column(align=True)
        col.use_property_split = True
        col.prop(scene, 'gap', text='Gap')

        col = layout.column(align=True)
        col.use_property_split = True
        col.operator('twisted_pair.create_pair', text = 'Create', icon='ADD')
