import bpy
from bpy.types import Operator

class TestPanel_5(bpy.types.Panel):
    bl_label = "Configurar Cena"
    bl_idname = "VIEW3D_PT_TestPanel_5"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Panel'
    
    words = {
        "Set Up Scene": {"en": "Set Up Scene", "pt": "Configurar Cena"}
    }
        
    def draw(self, context):
        layout = self.layout
        scene = context.scene
                
        row = layout.row()
        row.operator("render.collection", text=self.words["Set Up Scene"][bpy.context.window_manager.language])
        
        
class RENDER_OT_collection(bpy.types.Operator):
    bl_idname = "render.collection"
    bl_label = "Add Output Path"

    def execute(self, context):
        collection = bpy.data.collections.new('DEMO')
        collection.name = 'Data Collection'
        bpy.context.scene.collection.children.link(collection)
        data_coll = bpy.data.collections['Data Collection']

        scene_coll = bpy.context.scene.collection.objects

        bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        data_coll.objects.link(bpy.data.objects['Point'])
        scene_coll.unlink(bpy.data.objects['Point'])

        return {'FINISHED'}