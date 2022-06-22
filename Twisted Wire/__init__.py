bl_info = {
    "name": "Twisted Wires",
    "description": "Creates a twisted wire set",
    "author": "Mark Lagana",
    "version": (1, 0),
    "blender": (3, 10, 0),
    "location": "View3D > UI > Twisted Wire",
    "warning": "",
    "doc_url": "https://github.com/technisculpt/blender-twisted-wire-pair",
    "support": "COMMUNITY",
    "category": "3D View",
}

import importlib
import bpy

from . import twisted_wire
importlib.reload(twisted_wire)
from . import ui
importlib.reload(ui)

classes = (
    twisted_wire.Twisted_Wire,
    ui.Twisted_Wire_Settings,
    ui.TwistedWire_PT,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.twisted_wire = bpy.props.PointerProperty(type=ui.Twisted_Wire_Settings)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.twisted_wire

if __name__ == '__main__':
    register()