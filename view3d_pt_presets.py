import bpy


class ViewportPresets(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Viewport presets panel"
    bl_idname = "VIEW3D_PT_presets"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        prefs = context.preferences.addons[__package__].preferences

        layout.label(text = "Presets")

        row = layout.row()
        col = row.column(align = True)

        i = 0

        for preset in prefs.presets:
            op = col.operator('view3d.applypreset', text = preset.name, depress = (prefs.selected_index == i))
            op.index = i
            params = op.preset.__annotations__.keys()

            for param in params:
                setattr(op.preset, param, getattr(preset, param))

            i = i + 1

        _add = row.operator("view3d.savepreset", text = "", icon = 'ADD', emboss = False)
        _add.index = -1

        if (prefs.selected_index >= 0):
            layout.prop(prefs.presets[prefs.selected_index], "name", text = "Rename")
            row = layout.row()
            row.operator('view3d.savepreset', text = 'Update').index = prefs.selected_index
            row.operator('view3d.deletepreset', text = 'Delete').index = prefs.selected_index

        row = layout.row()
        row.operator("wm.save_userpref")


def view3d_presets_draw(self, context):
    layout = self.layout

    self.layout.popover(
        panel = "VIEW3D_PT_presets",
        text = "",
        icon = "PRESET"
    )

