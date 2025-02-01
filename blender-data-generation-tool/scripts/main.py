import bpy
from .panels.language_panel import TestPanel_1, SetLanguageOperator
from .panels.collection_panel import TestPanel_2, RENDER_OT_add_collection_name, RENDER_OT_add_output_path, Create_Collection_Operator
from .panels.import_panel import TestPanel_3, ImportModelsOperator
from .panels.material_panel import TestPanel_4, Apply_Changes_Operator
from .panels.render_panel import TestPanel_5, RENDER_OT_collection, TestPanel_6, RENDER_OT_set_frames_per_rotation, RENDER_OT_render_collections

def register():
    bpy.utils.register_class(TestPanel_1)
    bpy.utils.register_class(SetLanguageOperator)
    bpy.types.WindowManager.language = bpy.props.StringProperty(default="en")
    bpy.utils.register_class(TestPanel_2)
    bpy.utils.register_class(RENDER_OT_add_collection_name)
    bpy.utils.register_class(RENDER_OT_add_output_path)
    bpy.utils.register_class(Create_Collection_Operator)
    bpy.utils.register_class(TestPanel_3)
    bpy.utils.register_class(ImportModelsOperator)
    bpy.types.Scene.model_path = bpy.props.StringProperty(name="Model Path", default="")
    bpy.types.Scene.file_format = bpy.props.EnumProperty(name="File Format", items=[
        ("STL", ".stl", ""),
        ("PLY", ".ply", ""),
        ("WRL", ".wrl", ""),
    ], default="STL")
    bpy.utils.register_class(TestPanel_4)
    bpy.utils.register_class(Apply_Changes_Operator)
    bpy.types.Scene.selected_collection = bpy.props.StringProperty(name="")
    bpy.types.Scene.selected_material = bpy.props.EnumProperty(
        name="Selected Material",
        items=[("STAINLESS_STEEL", "Stainless Steel", ""),
               ("GALVANIZED_STEEL", "Galvanized Steel", ""),
               ("ZINC_PLATED_STEEL", "Zinc Plated Steel", ""),
               ("ALLOY_STEEL", "Alloy Steel", ""),
               ("BRASS", "Brass", ""),
               ("BRONZE", "Bronze", "")],
        description="Select Material",
        default="STAINLESS_STEEL"
    )
    bpy.utils.register_class(TestPanel_5)
    bpy.types.Scene.selected_view = bpy.props.EnumProperty(
        name="Selected View",
        items=[("VISO", "Isométrica: X=120° | Y=120° | Z=120°", ""),
               ("VA", "Vista frontal anterior: X=0° | Y=0° | Z=0°", ""),
               ("VP", "Vista frontal posterior: X=0° | Y=0° | Z=180°", ""),
               ("VS", "Vista superior: X=-90° | Y=0° | Z=0°", ""),
               ("VI", "Vista inferior: X=90° | Y=0° | Z=0°", ""),
               ("VLE", "Vista lateral esquerda: X=0° | Y=-90° | Z=0°", ""),
               ("VLD", "Vista lateral direita: X=0° | Y=90° | Z=0°", "")],
        description="Select View",
        default="VISO"
    )
    bpy.utils.register_class(TestPanel_6)
    bpy.types.Scene.coll_name = bpy.props.StringProperty(name="Collection Name")
    bpy.types.Scene.output_path = bpy.props.StringProperty(name="Output Path")
    bpy.types.Scene.frames_angle = bpy.props.StringProperty(name="Frames Angle")
    bpy.utils.register_class(RENDER_OT_set_frames_per_rotation)
    bpy.utils.register_class(RENDER_OT_render_collections)
    bpy.utils.register_class(RENDER_OT_collection)

def unregister():
    bpy.utils.unregister_class(TestPanel_1)
    bpy.utils.unregister_class(SetLanguageOperator)
    del bpy.types.WindowManager.language
    bpy.utils.unregister_class(TestPanel_2)
    bpy.utils.unregister_class(RENDER_OT_add_collection_name)
    bpy.utils.unregister_class(RENDER_OT_add_output_path)
    bpy.utils.unregister_class(Create_Collection_Operator)
    bpy.utils.unregister_class(TestPanel_3)
    bpy.utils.unregister_class(ImportModelsOperator)
    del bpy.types.Scene.model_path
    del bpy.types.Scene.file_format
    bpy.utils.unregister_class(TestPanel_4)
    bpy.utils.unregister_class(Apply_Changes_Operator)
    del bpy.types.Scene.selected_collection
    del bpy.types.Scene.selected_material
    bpy.utils.unregister_class(TestPanel_5)
    del bpy.types.Scene.selected_view
    bpy.utils.unregister_class(TestPanel_6)
    bpy.utils.unregister_class(RENDER_OT_set_frames_per_rotation)
    bpy.utils.unregister_class(RENDER_OT_render_collections)
    bpy.utils.unregister_class(RENDER_OT_collection)
    del bpy.types.Scene.coll_name
    del bpy.types.Scene.output_path
    del bpy.types.Scene.frames_angle

if __name__ == "__main__":
    register()