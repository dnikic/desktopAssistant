#run this script from blenders text edtor via Run Script button, or make it execute at startup in User Preferencess
#after runining this script you will be able to use custom hotkeys to execute python macros



bl_info = {
    "name": "Work Macro",
    "category": "Object",
}

import bpy


class WorkMacro(bpy.types.Operator):
    """Work Macro"""
    bl_idname = "object.work_macro"
    bl_label = "Work Macro"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
# you can coppy content of the info otput console and paste it below to reproduce your workflow via pythn macro script        

        bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


        
        print("do work here")

        return {'FINISHED'}


# store keymaps here to access after registration
addon_keymaps = []


def register():
    bpy.utils.register_class(WorkMacro)

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(WorkMacro.bl_idname, 'Q', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append(km)

def unregister():
    bpy.utils.unregister_class(WorkMacro)

    # handle the keymap
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # clear the list
    del addon_keymaps[:]


if __name__ == "__main__":
    register()
