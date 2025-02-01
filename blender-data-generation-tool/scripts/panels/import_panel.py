import bpy
from bpy.types import Operator
import os

class TestPanel_3(bpy.types.Panel):
    bl_label = "Importar Modelos"
    bl_idname = "VIEW3D_PT_TestPanel_3"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Panel'
    
    words = {
        "Enter import path": {"en": "Enter import path:", "pt": "Insira o caminho da importação:"},
        "File format": {"en": "File format:", "pt": "Formato dos arquivos:"},
        "Import Models": {"en": "Import Models", "pt": "Importar Modelos"}
    }

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.label(text=self.words["Enter import path"][bpy.context.window_manager.language])
        layout.prop(scene, "model_path", text="")
        
        layout.label(text=self.words["File format"][bpy.context.window_manager.language])
        layout.prop(scene, "file_format", text="")
        
        layout.operator("import_models.button", text=self.words["Import Models"][bpy.context.window_manager.language])

class ImportModelsOperator(bpy.types.Operator):
    bl_idname = "import_models.button"
    bl_label = "Import Models"
    
    def execute(self, context):
        scene = context.scene
        model_path = scene.model_path
        file_format = scene.file_format.lower()
        
        if not os.path.exists(model_path):
            self.report({'ERROR'}, "Directory does not exist!")
            return {'CANCELLED'}
        
        collection = bpy.data.collections.get(context.scene['collection_for_import'])
        if not collection:
            collection = bpy.data.collections.new(coll_name)
            bpy.context.scene.collection.children.link(collection)
        
        for filename in os.listdir(model_path):
            if filename.lower().endswith(f".{file_format}") and os.path.isfile(os.path.join(model_path, filename)):
                filepath = os.path.join(model_path, filename)
                
                if file_format == "stl":
                    bpy.ops.import_mesh.stl(filepath=filepath, directory=model_path)
                elif file_format == "ply":
                    bpy.ops.import_mesh.ply(filepath=filepath, directory=model_path)
                elif file_format == "wrl":
                    bpy.ops.import_scene.x3d(filepath=filepath, directory=model_path)
                
                obj = context.selected_objects[0]
                obj_name = obj.name
                if obj_name not in collection.objects:
                    collection.objects.link(obj)
                else:
                    print(f"Object '{obj_name}' already in collection '{coll_name}'")
        
        context.scene.model_path = ""
        
        return {'FINISHED'}