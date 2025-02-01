import bpy
from bpy.types import Operator

class TestPanel_4(bpy.types.Panel):
    bl_label = "Aparência dos Modelos"
    bl_idname = "VIEW3D_PT_TestPanel_4"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Panel'
    
    words = {
        "Select View": {"en": "Select View:", "pt": "Selecione a vista:"},
        "Select Material": {"en": "Select Material:", "pt": "Selecione o material:"},
        "Select Collection": {"en": "Select Collection:", "pt": "Selecione a coleção:"},
        "Apply Changes": {"en": "Apply Changes", "pt": "Aplicar Mudanças"}
    }
    
    bpy.types.Scene.selected_material = bpy.props.StringProperty()

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.label(text=self.words["Select View"][bpy.context.window_manager.language])
        layout.prop(scene, "selected_view", text="")
        
        layout.label(text=self.words["Select Material"][bpy.context.window_manager.language])
        layout.prop(scene, "selected_material", text="")
        
        row = layout.row()
        row.label(text=self.words["Select Collection"][bpy.context.window_manager.language])
        row = layout.row()
        row.prop_search(scene, "selected_collection", bpy.data, "collections")

        layout.operator("apply_changes.button", text=self.words["Apply Changes"][bpy.context.window_manager.language])
        
        
class Apply_Changes_Operator(bpy.types.Operator):
    bl_idname = "apply_changes.button"
    bl_label = "Apply Changes"

    def execute(self, context):
        scene = context.scene
        selected_collection = scene.selected_collection
        selected_material = scene.selected_material
        selected_view = scene.selected_view

        collection = bpy.data.collections.get(selected_collection)
        if collection:
            if selected_material == "STAINLESS_STEEL":
                diffuse_color = (0.75, 0.75, 0.75, 1)
                metallic = 1.0
                roughness = 0.2
            elif selected_material == "GALVANIZED_STEEL":
                diffuse_color = (0.85, 0.85, 0.85, 1)
                metallic = 0.8
                roughness = 0.4
            elif selected_material == "ZINC_PLATED_STEEL":
                diffuse_color = (0.8, 0.8, 0.8, 1)
                metallic = 0.7
                roughness = 0.3
            elif selected_material == "ALLOY_STEEL":
                diffuse_color = (0.6, 0.6, 0.6, 1)
                metallic = 1.0
                roughness = 0.5
            elif selected_material == "BRASS":
                diffuse_color = (0.9, 0.6, 0.2, 1)
                metallic = 1.0
                roughness = 0.1
            elif selected_material == "BRONZE":
                diffuse_color = (0.85, 0.5, 0.2, 1)
                metallic = 1.0
                roughness = 0.6
                
            for obj in collection.objects:
                if selected_view == "VISO":
                    obj.rotation_euler[0] = 2.0944
                    obj.rotation_euler[1] = 2.0944
                    obj.rotation_euler[2] = 2.0944
                elif selected_view == "VA":
                    obj.rotation_euler[0] = 0
                    obj.rotation_euler[1] = 0
                    obj.rotation_euler[2] = 0
                elif selected_view == "VP":
                    obj.rotation_euler[0] = 0
                    obj.rotation_euler[1] = 0
                    obj.rotation_euler[2] = 3.1416
                elif selected_view == "VS":
                    obj.rotation_euler[0] = -1.5708
                    obj.rotation_euler[1] = 0
                    obj.rotation_euler[2] = 0
                elif selected_view == "VI":
                    obj.rotation_euler[0] = 1.5708
                    obj.rotation_euler[1] = 0
                    obj.rotation_euler[2] = 0
                elif selected_view == "VLE":
                    obj.rotation_euler[0] = 0
                    obj.rotation_euler[1] = -1.5708
                    obj.rotation_euler[2] = 0
                elif selected_view == "VLD":
                    obj.rotation_euler[0] = 0
                    obj.rotation_euler[1] = 1.5708
                    obj.rotation_euler[2] = 0

            for obj in collection.objects:
                if not obj.data.materials:
                    obj.data.materials.append(bpy.data.materials.new(name=selected_material))
                material = obj.data.materials[0]
                material.diffuse_color = diffuse_color
                material.metallic = metallic
                material.roughness = roughness
                if material.node_tree is not None:
                    material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = diffuse_color
                    material.node_tree.nodes["Principled BSDF"].inputs[6].default_value = metallic
                    material.node_tree.nodes["Principled BSDF"].inputs[9].default_value = roughness

            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            region.tag_redraw()

        else:
            self.report({'ERROR'}, f"Collection '{selected_collection}' not found!")
            return {'CANCELLED'}

        return {'FINISHED'}