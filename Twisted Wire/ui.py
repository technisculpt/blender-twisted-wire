import bpy
from bpy.app.handlers import persistent

def update_wires(self, context):
    wire_rads = context.scene.twisted_wire.wires
    _custom = context.scene.custom_group
    _custom.clear()
    for wire_obj in range(wire_rads):
        item = _custom.add()
        item.name = f"Wire {wire_obj + 1}"
        item.radius =  context.scene.twisted_wire.radius

@persistent
def on_load(_scene):
    _self = None
    update_wires(_self, bpy.context)

class PropertyCollection(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="", default="")
    radius: bpy.props.FloatProperty(name="",  default=0.0, min=0.1, max=1000.0,)

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
        min=1, max=100,
        update=update_wires
    )

    radius : bpy.props.FloatProperty(
        name="Diameter",
        description="Radius of wire",
        default=1.0,
        min=0.1, max=1000.0,
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
        _scene = context.scene.twisted_wire
        _custom = context.scene.custom_group

        col = layout.column(align=True)
        col.prop(_scene, 'cap_fill', text='Cap Fill Type')

        col = layout.column(align=True)
        col.prop(_scene, 'vert_segs', text='Vertical Segments')

        col = layout.column(align=True)
        col.prop(_scene, 'cyl_segs', text='Cylinder Segments')
        
        col = layout.column(align=True)
        col.prop(_scene, 'turns', text='Turns')
        
        col = layout.column(align=True)
        col.prop(_scene, 'wires', text='Wires')

        col = layout.column(align=True)
        col.prop(_scene, 'radius', text='Wire Radius')

        col = layout.column(align=True)
        col.prop(_scene, 'length', text='Length')

        col = layout.column(align=True)
        col.prop(_scene, 'gap', text='Gap')

        col = layout.column(align=True)
        col.prop(_scene, 'union', text='Join Wires')

        col = layout.column(align=True)
        col.prop(_scene, 'name', text='Name')

        col = layout.column(align=True)
        col.operator('twisted_wire.create_wire', text = 'Create', icon='ADD')

        for item in _custom:
            col = layout.column(align=True)
            col.prop(item, "radius", text=f"Radius for {item.name}")
