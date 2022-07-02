import math
import bpy
import bmesh
from mathutils import Vector

def boolean_union(obj1, obj2, union_name="default_union"):
    bpy.context.view_layer.objects.active = obj1
    bool_one = obj1.modifiers.new(type="BOOLEAN", name=union_name)
    bool_one.object = obj2
    bool_one.operation = 'UNION'
    bool_one.use_self = True
    bpy.ops.object.modifier_apply(modifier=union_name)
    bpy.ops.object.select_all(action="DESELECT")
    obj2.select_set(True)
    bpy.ops.object.delete()

def create_arc(segments, magnitude, theta_start, theta_end, postition):
    theta = theta_start
    theta_inc = (theta_end - theta_start)/(segments)
    vertices = [ Vector(((magnitude)*math.cos(theta), (magnitude)*math.sin(theta), 0)) + Vector(postition)]
    for seg in range(segments-1):
        theta += theta_inc
        vertices.append( Vector(((magnitude)*math.cos(theta), (magnitude)*math.sin(theta), 0)) + Vector(postition))
    return vertices

def create_mesh(vertices, name="default_name"):
    bmesh_obj = bpy.data.meshes.new(name+"mesh")
    blender_obj = bpy.data.objects.new(name, bmesh_obj) 
    scene = bpy.context.scene
    scene.collection.objects.link(blender_obj)
    bm = bmesh.new()
    for i in vertices:
        bm.verts.new(i)
    return bm, bmesh_obj, blender_obj

def create_wire(cap_fill, vert_segs, cyl_segs, turns, radius, length, gap, name, theta_start):
    current_length = 0
    z_distance = 1/vert_segs
    segs = length / z_distance
    total_angle = 2*math.pi * turns
    delta = total_angle / segs
    mag = 2 * radius + gap
    theta = theta_start
    wire = []

    for i in range(int(segs)+1): # gather vertices
        x_pos = mag * math.cos(theta)
        y_pos = mag * math.sin(theta)

        if cap_fill == '0': # cap is triangle fan
            if i == 0:
                wire.append(Vector((x_pos, y_pos, current_length)))

        wire += create_arc(cyl_segs, 2 * radius, 0, 2*math.pi, Vector((x_pos, y_pos, current_length)))

        if cap_fill == '0':
            if i == int(segs):
                wire.append(Vector((x_pos, y_pos, current_length)))

        current_length += z_distance
        theta += delta

    bm, bmesh_obj, blender_obj = create_mesh(wire, name)

    # tesselate
    if hasattr(bm.verts, "ensure_lookup_table"):
        bm.verts.ensure_lookup_table()

        if cap_fill == '0':
            for v in range(cyl_segs): # bottom cap
                if v == (cyl_segs - 1):
                    bm.faces.new((  bm.verts[1],
                                    bm.verts[v + 1],
                                    bm.verts[0]))
                else:
                    bm.faces.new((  bm.verts[v + 2],
                                    bm.verts[v + 1],
                                    bm.verts[0]))

            wire_vert_count_center = int(segs + 1) * cyl_segs + 1
            wire_vert_count = int(segs) * cyl_segs + 1

            for v in range(cyl_segs): # top cap
                if v == (cyl_segs - 1):
                    bm.faces.new((  bm.verts[wire_vert_count_center],
                                    bm.verts[wire_vert_count + v],
                                    bm.verts[wire_vert_count]))
                else:
                    bm.faces.new((  bm.verts[wire_vert_count_center],
                                    bm.verts[wire_vert_count + v],
                                    bm.verts[wire_vert_count + v + 1]))

        elif cap_fill == '1': # cap is N-gon
            tmp_verts = [] # bottom cap
            for vert in range(cyl_segs, 0, -1):
                tmp_verts.append(bm.verts[vert])
            bm.faces.new(tmp_verts)

            end_v = (cyl_segs * (int(segs)+1)) # top cap
            start_v = end_v - cyl_segs
            bm.faces.new(bm.verts[start_v : end_v])

        for i in range(int(segs)): # spiral faces
            offset = i * cyl_segs

            if cap_fill == '0':
                offset += 1

            for v in range(cyl_segs):
                if v == cyl_segs-1:
                    bm.faces.new((  bm.verts[offset + v],
                                    bm.verts[offset],
                                    bm.verts[offset + cyl_segs],
                                    bm.verts[offset + cyl_segs + v]))
                else:
                    bm.faces.new((  bm.verts[offset + v],
                                    bm.verts[offset + v + 1],
                                    bm.verts[offset + cyl_segs + v + 1],
                                    bm.verts[offset + cyl_segs + v]))

        bm.to_mesh(bmesh_obj)
        bm.free()
        return(blender_obj)

def twisted_wire_set(cap_fill, vert_segs, cyl_segs, turns, wires, radii, length, gap, union, name):
    angle_delta = (2 * math.pi)/wires
    theta_start = 0
    b_objs = []

    for wire in range(wires):
        theta_start += angle_delta
        b_objs.append(create_wire(cap_fill, vert_segs, cyl_segs, turns, radii[wire], length, gap, name, theta_start))

    if union == '1': # blender object join
        bpy.context.view_layer.objects.active = b_objs[0]
        bpy.ops.object.select_all(action="DESELECT")
        for b_obj in b_objs:
            b_obj.select_set(True)
        bpy.ops.object.join()

    elif union == '2': # boolean union join
        for index, b_obj in enumerate(b_objs):
            if index:
                boolean_union(b_objs[0], b_obj)

class Twisted_Wire(bpy.types.Operator):
    bl_idname = 'twisted_wire.create_wire'
    bl_label = 'twisted wire op'
    bl_options = {'INTERNAL'}
    bl_description = "Create Twisted Wire"

    def execute(self, context):

        c = context.scene.twisted_wire
        radii = [obj.radius for obj in context.scene.custom_group]
        twisted_wire_set(   c.cap_fill, c.vert_segs, c.cyl_segs, c.turns,
                            c.wires, radii, c.length, c.gap, c.union, c.name)

        self.report({'INFO'}, "FINISHED")
        return {'FINISHED'}