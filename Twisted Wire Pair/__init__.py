bl_info = {
    "name": "Twisted Wire Pair",
    "description": "Creates a twisted wire pair",
    "author": "Mark Lagana",
    "version": (1, 0),
    "blender": (3, 10, 0),
    "location": "View3D > UI > Twisted Wire Pair",
    "warning": "",
    "doc_url": "https://github.com/technisculpt/blender-twisted-wire-pair",
    "support": "COMMUNITY",
    "category": "3D View",
}

import importlib
import bpy

from . import twisted_pair
importlib.reload(twisted_pair)
from . import ui
importlib.reload(ui)

classes = (
    twisted_pair.Twisted_Pair,
    ui.Twisted_Pair_Settings,
    ui.TwistedPair_PT,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.twisted_pair = bpy.props.PointerProperty(type=ui.Twisted_Pair_Settings)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.twisted_pair

if __name__ == '__main__':
    register()