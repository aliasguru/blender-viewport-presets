import bpy
from bpy.types import Operator
from bl_operators.presets import AddPresetBase
from . import viewport_presets_addonprefs



class SavePreset(Operator):
    bl_idname = "view3d.savepreset"
    bl_label = "Save preset"

    index: bpy.props.IntProperty(default=-1)

    def execute(self, context):
        prefs = bpy.context.preferences.addons[__package__].preferences

        space = context.area.spaces[0]

        if (self.index >= 0):
            preset = prefs.presets[self.index]
        else:
            preset = prefs.presets.add()
            preset.name = "New preset"
        
       
        params = preset.__annotations__.keys()

        prefs.selected_index = len(prefs.presets) -1

        for param in params:
            if param == "shading_type":
                preset.shading_type = space.shading.type 

            elif hasattr(space.shading, param):
                setattr(preset, param, getattr(space.shading, param))

            elif hasattr(space.overlay, param):
                setattr(preset, param, getattr(space.overlay, param))

            elif hasattr(space, param):
                setattr(preset, param, getattr(space, param))


        return {'FINISHED'}

class VIEW3D_OT_Add_Viewport_Preset(Operator):
    pass

def register():
    bpy.utils.register_class(SavePreset)

def unregister():
    bpy.utils.unregister_class(SavePreset)
