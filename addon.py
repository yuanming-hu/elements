import bpy

from . import tree, categories, nodes, sockets, operators, handlers

addon_modules = [tree, sockets, nodes, categories, operators, handlers]


def register():
    bpy.types.Scene.elements_nodes = {}
    for addon_module in addon_modules:
        addon_module.register()
    bpy.types.NODE_HT_header.append(operators.draw_render_operator)


def unregister():
    bpy.types.NODE_HT_header.remove(operators.draw_render_operator)
    for addon_module in reversed(addon_modules):
        addon_module.unregister()
    del bpy.types.Scene.elements_nodes
