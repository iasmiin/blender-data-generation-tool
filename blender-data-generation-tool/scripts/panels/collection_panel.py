import bpy
from bpy.types import Operator

class TestPanel_2(bpy.types.Panel):
    bl_label = "Criar Coleção"
    bl_idname = "VIEW3D_PT_TestPanel_2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Panel'
    
    words = {
        "Enter collection name": {"en": "Enter collection name:", "pt": "Insira nome da coleção:"},
        "Add Collection Name": {"en": "Add Collection Name:", "pt": "Adicionar Nome da Coleção"},
        "Enter render output path": {"en": "Enter render output path:", "pt": "Insira o caminho de saída da renderização:"},
        "Add Render Output Path": {"en": "Add Render Output Path", "pt": "Adicionar o Caminho de Saída da Renderização"},
        "Create Collection": {"en": "Create Collection", "pt": "Criar Coleção"}
    }

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        row = layout.row()
        row.label(text=self.words["Enter collection name"][bpy.context.window_manager.language])
        row = layout.row()
        row.prop(context.scene, "coll_name", text="")
        row = layout.row()
        row.operator("render.add_collection_name", text=self.words["Add Collection Name"][bpy.context.window_manager.language])
        row = layout.row()
        row.label(text=self.words["Enter render output path"][bpy.context.window_manager.language])
        row = layout.row()
        row.prop(context.scene, "output_path", text="")
        row = layout.row()
        row.operator("render.add_output_path", text=self.words["Add Render Output Path"][bpy.context.window_manager.language])

        layout.operator("create_collection.button", text=self.words["Create Collection"][bpy.context.window_manager.language])

class RENDER_OT_add_collection_name(bpy.types.Operator):
    bl_idname = "render.add_collection_name"
    bl_label = "Add Collection Name"

    def execute(self, context):
        coll_name = context.scene.coll_name
        if coll_name not in TestPanel_6.names_list:
            TestPanel_6.names_list.append(coll_name)
        context.scene.coll_name = coll_name
        
        Create_Collection_Operator.names_list.append(coll_name)
        
        context.scene.coll_name = ""
        
        return {'FINISHED'}

class RENDER_OT_add_output_path(bpy.types.Operator):
    bl_idname = "render.add_output_path"
    bl_label = "Add Output Path"

    def execute(self, context):
        output_path = context.scene.output_path
        if output_path not in TestPanel_6.output_list:
            TestPanel_6.output_list.append(output_path)
        context.scene.output_path = output_path
        
        Create_Collection_Operator.output_list.append(output_path)
        
        context.scene.output_path = ""
        
        return {'FINISHED'}

class Create_Collection_Operator(bpy.types.Operator):
    bl_idname = "create_collection.button"
    bl_label = "Create Collection"
    
    output_list = []
    names_list = []
    
    def execute(self, context):
        scene = context.scene
        output_path = Create_Collection_Operator.output_list[0]
        coll_name = Create_Collection_Operator.names_list[0]

        if not coll_name:
            self.report({'ERROR'}, "Please enter a collection name!")
            return {'CANCELLED'}
        if not output_path:
            self.report({'ERROR'}, "Please enter an output filepath!")
            return {'CANCELLED'}

        collection = bpy.data.collections.get(coll_name)
        if not collection:
            collection = bpy.data.collections.new(coll_name)
            bpy.context.scene.collection.children.link(collection)
        else:
            self.report({'ERROR'}, f"Collection '{coll_name}' already exists!")
            return {'CANCELLED'}

        bpy.context.scene['collection_for_import'] = coll_name
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        
        Create_Collection_Operator.output_list.remove(output_path)
        Create_Collection_Operator.names_list.remove(coll_name)

        return {'FINISHED'}