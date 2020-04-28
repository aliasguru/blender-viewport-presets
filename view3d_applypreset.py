import bpy
from . import viewport_presets_addonprefs


class ApplyPreset(bpy.types.Operator):
    bl_idname = "view3d.applypreset"
    bl_label = "Apply preset"

    preset: bpy.props.PointerProperty(type = viewport_presets_addonprefs.ViewportPreset)
    index: bpy.props.IntProperty()

    def execute(self, context):

        space = context.area.spaces[0]

        params = self.preset.__annotations__.keys()

        prefs = context.preferences.addons[__package__].preferences

        prefs.selected_index = self.index

        for param in params:
            if param == 'shading_type':
                space.shading.type = self.preset.shading_type

            elif hasattr(space.shading, param):
                try:
                    setattr(space.shading, param, getattr(self.preset, param))
                except:
                    pass    #    not available in current mode - ignore

            elif hasattr(space.overlay, param):
                setattr(space.overlay, param, getattr(self.preset, param))

            elif hasattr(space, param):
                setattr(space, param, getattr(self.preset, param))

        return {'FINISHED'}

