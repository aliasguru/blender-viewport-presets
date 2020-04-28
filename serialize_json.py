'''
Created on 28.04.2020

@author: r.trummer
'''
import bpy
import json
import logging

from bpy.types import Operator

from . import viewport_presets_addonprefs as vp

preset_dir = 'json_presets'
logger = logging.getLogger(__package__)


def get_presets():
	prefs = bpy.context.preferences.addons[__package__].preferences

	for _preset in prefs.presets:
		_keys, _values = _preset.keys(), _preset.values()
		yield dict(zip(_keys, _values))


class VIEW3D_OT_Save_Viewport_Preset_JSON(bpy.types.Operator):
	bl_idname = "object.save_viewport_preset_json"
	bl_label = "Save Viewport Preset To JSON"
	bl_description = 'saves all viewport presets to a .json file'
	bl_options = {'REGISTER'}

	@classmethod
	def poll(cls, context):
		return True

	def execute(self, context):
		_presets = get_presets()

		logger.warning(json.dumps(list(_presets)))

		return {'FINISHED'}
