import bpy
from bpy.types import Operator

class TestPanel_1(bpy.types.Panel):
    bl_label = "Selecionar Idioma"
    bl_idname = "VIEW3D_PT_TestPanel_1"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Panel'

    words = { 
        "English": {"en": "English", "pt": "Inglês"},
        "Portuguese": {"en": "Portuguese", "pt": "Português"}
    }

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()        
        if bpy.context.window_manager.language == "en":
            row.operator("wm.set_language", text=self.words["Portuguese"][bpy.context.window_manager.language]).language = "pt"
            row.operator("wm.set_language", text=self.words["English"][bpy.context.window_manager.language]).language = "en"
        else:
            row.operator("wm.set_language", text=self.words["Portuguese"][bpy.context.window_manager.language]).language = "pt"
            row.operator("wm.set_language", text=self.words["English"][bpy.context.window_manager.language]).language = "en"

class SetLanguageOperator(Operator):
    bl_idname = "wm.set_language"
    bl_label = "Set Language"
    language: bpy.props.StringProperty(name="Language")
    
    def execute(self, context):
        for panel_class in [TestPanel_1, TestPanel_2, TestPanel_3, TestPanel_4, TestPanel_5, TestPanel_6]:
            bpy.context.window_manager.language = self.language
        return {'FINISHED'}