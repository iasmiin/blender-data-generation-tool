import bpy
from bpy.types import Operator
import math
import time

class TestPanel_6(bpy.types.Panel):
    bl_label = "Renderizar Classes"
    bl_idname = "VIEW3D_PT_TestPanel_6"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Panel'
    
    words = {
        "Set Frames Angle": {"en": "Set Frames Angle:", "pt": "Definir Ângulo dos Quadros:"},
        "Set Frames": {"en": "Set Frames", "pt": "Definir Quadros"},
        "Render Collections": {"en": "Render Collections", "pt": "Renderizar Coleção"}
    }
    
    names_list = []
    output_list = []

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text=self.words["Set Frames Angle"][bpy.context.window_manager.language])
        row = layout.row()
        row.prop(context.scene, "frames_angle", text="")
        row.operator("render.set_frames_angle", text=self.words["Set Frames"][bpy.context.window_manager.language])
        
        row = layout.row()
        row.operator("render.render_collections", text=self.words["Render Collections"][bpy.context.window_manager.language])
        

class RENDER_OT_set_frames_per_rotation(bpy.types.Operator):
    bl_idname = "render.set_frames_angle"
    bl_label = "Set Frames per Rotation"
    bl_description = "Set the number of frames to be rendered per 360 degrees of the bezier circle path"

    def execute(self, context):
        angle = int(context.scene.frames_angle)
        frame_angles = [str(angle * i) for i in range(1, int(360 / angle) + 1)]
        context.scene.frames_angle = ','.join(frame_angles)
        return {'FINISHED'}


class RENDER_OT_render_collections(bpy.types.Operator):
    bl_idname = "render.render_collections"
    bl_label = "Render Collections"

    def execute(self, context):
        world = bpy.context.scene.world
        world.color = (1, 1, 1)
        
        data_coll = bpy.data.collections['Data Collection']
        scene_coll = bpy.context.scene.collection.objects

        frame_angles = context.scene.frames_angle.split(',')

        for obj in bpy.context.scene.objects:
            if not obj.hide_render:
                obj.hide_render = True

        for i, coll_name in enumerate(TestPanel_6.names_list):
            coll = bpy.data.collections.get(coll_name)
            
            start_time = time.time()
            
            if coll is not None:
                output_path = TestPanel_6.output_list[i % len(TestPanel_6.output_list)]
                for obj in coll.objects:
                    smooth_modifier = obj.modifiers.new(name='Smooth', type='LAPLACIANSMOOTH')
                    smooth_modifier.lambda_factor = 0.0078125
                    smooth_modifier.iterations = 1
                    bpy.ops.object.modifier_apply({"object": obj}, modifier=smooth_modifier.name)
                    
                    obj.select_set(True)
                    bpy.context.view_layer.objects.active = obj
                    bpy.ops.object.shade_smooth()

                    for other_obj in coll.objects:
                        if other_obj == obj:
                            other_obj.hide_render = False
                        else:
                            other_obj.hide_render = True

                    elemento = 5 * max(obj.dimensions.x, obj.dimensions.y, obj.dimensions.z)

                    bpy.ops.curve.primitive_bezier_circle_add(radius=elemento, enter_editmode=False,
                                                              align='WORLD', location=(0, 0, 0))
                    bezier_circle = bpy.context.object
                    try:
                        data_coll.objects.link(bpy.data.objects['BezierCircle'])
                    except RuntimeError:
                        pass

                    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0),
                                              rotation=(1.5708, 0, -1.5708), scale=(1, 1, 1))
                    camera = bpy.context.object

                    follow_path = camera.constraints.new('FOLLOW_PATH')
                    follow_path.target = bezier_circle
                    follow_path.use_curve_follow = True
                    bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner='OBJECT')

                    try:
                        data_coll.objects.link(bpy.data.objects['Camera'])
                    except RuntimeError:
                        pass

                    camera = bpy.data.objects.get("Camera")
                    circle = bpy.data.objects.get("BezierCircle")
                    camera.constraints[0].target = circle
                    camera.constraints[0].use_curve_follow = True

                    for frame_angle in frame_angles:
                        bezier_circle.rotation_euler[2] = math.radians(int(frame_angle))
                        bpy.ops.render.render(animation=True)
                        obj_name = obj.name
                        bpy.data.images["Render Result"].save_render(filepath=f"{output_path}/{coll_name}_Frame_{frame_angle}.png")

                    camera.constraints[0].target = None
                    camera.constraints[0].use_curve_follow = False

                    bpy.data.objects.remove(camera, do_unlink=True)
                    bpy.data.objects.remove(bezier_circle, do_unlink=True)

                    obj.hide_render = True
                    
            end_time = time.time()
            elapsed_time = end_time - start_time

            print(f"Tempo decorrido: {elapsed_time}s")
                    
        context.scene.frames_angle = ""

        return {'FINISHED'}