import bpy

class Twisted_Wire_Settings(bpy.types.PropertyGroup):

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

    wires : bpy.props.IntProperty(
        name="Wires",
        description="Wires",
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
        default=100.0,
        min=0.1, max=1000.0,
    )

    union : bpy.props.EnumProperty(
                name = "Join method",
                description = "Join method",
                items= [('0', 'Unjoined', ''),
                        ('1', 'Joined', ''),
                        ('2', 'Boolean union', '')]
    )

    name: bpy.props.StringProperty(
        name="Wire Name",
        default="Twisted Wire"
    )

class TwistedWire_PT(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = 'Twisted Wire'
    bl_context = 'objectmode'
    bl_category = 'Twisted Wire'
    bl_idname  = 'VIEW_3D_PT_twisted_wire'


    def draw(self, context):
        layout = self.layout
        scene = context.scene.twisted_wire

        col = layout.column(align=True)
        col.prop(scene, 'cap_fill', text='Cap Fill Type')

        col = layout.column(align=True)
        col.prop(scene, 'vert_segs', text='Vertical Segments')

        col = layout.column(align=True)
        col.prop(scene, 'cyl_segs', text='Cylinder Segments')
        
        col = layout.column(align=True)
        col.prop(scene, 'turns', text='Turns')
        
        col = layout.column(align=True)
        col.prop(scene, 'wires', text='Wires')

        col = layout.column(align=True)
        col.prop(scene, 'radius', text='Wire Radius')

        col = layout.column(align=True)
        col.prop(scene, 'length', text='Length')

        col = layout.column(align=True)
        col.prop(scene, 'gap', text='Gap')

        col = layout.column(align=True)
        col.prop(scene, 'union', text='Join Wires')

        col = layout.column(align=True)
        col.prop(scene, 'name', text='Name')

        col = layout.column(align=True)
        col.operator('twisted_wire.create_wire', text = 'Create', icon='ADD')
