__version__ = '1.0.3'

bl_info = {
	"name": "Viewport Presets",
	"author": "Andrew Charlton, Rainer Trummer",
	"version": (1, 1, 0),
	"blender": (2, 82, 0),
	"location": "3D Viewport Header",
	"description": "Adds a preset popup to allow easy saving and recall of viewport shading, overlays and gizmos",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"category": "3D View"
}

if 'bpy' in locals():
	import importlib

	for x in view3d_pt_presets, viewport_presets_addonprefs, view3d_applypreset, view3d_savepreset, view3d_deletepreset, serialize_json:
		importlib.reload(x)

else:
	from . import view3d_pt_presets, viewport_presets_addonprefs, view3d_applypreset, view3d_savepreset, view3d_deletepreset, serialize_json

import bpy

__classes__ = (
	view3d_pt_presets.ViewportPresets,
	viewport_presets_addonprefs.ViewportPreset,
	viewport_presets_addonprefs.ViewportPresetsAddonPreferences,
	view3d_applypreset.ApplyPreset,
	view3d_deletepreset.DeletePreset,
	view3d_savepreset.SavePreset,
	#    serialize_json.SomeThing
	)


def register():
	for c in __classes__:
		bpy.utils.register_class(c)

	prefs = bpy.context.preferences.addons[__package__].preferences
	prefs.selected_index = -1
	bpy.types.VIEW3D_HT_header.append(view3d_pt_presets.view3d_presets_draw)


def unregister():

	bpy.types.VIEW3D_HT_header.remove(view3d_pt_presets.view3d_presets_draw)


if __name__ == "__main__":
	register()
