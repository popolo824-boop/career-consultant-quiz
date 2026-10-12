# Original voxel calico cat built from generic toy bricks, assembled brick-by-brick.
import bpy, bmesh, math, sys, os
from mathutils import Vector
OUT=sys.argv[sys.argv.index("--out")+1] if "--out" in sys.argv else "/tmp/frames/"
RES=float(sys.argv[sys.argv.index("--res")+1]) if "--res" in sys.argv else 1.0
FRAMES=sys.argv[sys.argv.index("--frames")+1] if "--frames" in sys.argv else None
SAMPLES=int(sys.argv[sys.argv.index("--samples")+1]) if "--samples" in sys.argv else 24

W,O,B,P,G,K="white","orange","black","pink","green","dark"
COL={W:(0.85,0.84,0.8,1),O:(0.9,0.32,0.03,1),B:(0.015,0.015,0.02,1),P:(0.95,0.32,0.42,1),G:(0.25,0.75,0.35,1),K:(0.15,0.15,0.17,1)}
vox={}
def put(x,y,z,c): vox[(x,y,z)]=c
# ---- body (z 1..6), x 3..10, y 2..7
for z in range(1,7):
    for x in range(3,11):
        for y in range(2,8):
            if (x in(3,10))+(y in(2,7))==2: continue
            put(x,y,z,W)
for z in range(3,7):
    for y in range(4,8):
        for x in range(3,6):
            if (x,y,z) in vox: put(x,y,z,O)
for z in range(1,4):
    for y in range(5,8):
        for x in range(8,11):
            if (x,y,z) in vox: put(x,y,z,B)
for x in (4,5,8,9): put(x,1,1,W); put(x,1,2,W)
# ---- head (z 7..15), x 0..13, y 1..8  (chibi: wider than body)
for z in range(7,16):
    for x in range(0,14):
        for y in range(1,9):
            if (x in(0,13))+(z in(7,15))+(y in(1,8))>=2: continue
            put(x,y,z,W)
for z in range(12,16):
    for x in range(0,6):
        for y in range(1,9):
            if (x,y,z) in vox: put(x,y,z,O)
for z in range(13,16):
    for x in range(9,14):
        for y in range(1,9):
            if (x,y,z) in vox: put(x,y,z,B)
# ears
for x in (1,2,3,4): put(x,4,16,O); put(x,5,16,O)
for x in (2,3): put(x,4,17,O); put(x,5,17,O)
for x in (9,10,11,12): put(x,4,16,B); put(x,5,16,B)
for x in (10,11): put(x,4,17,B); put(x,5,17,B)
put(2,4,16,P);put(3,4,16,P);put(10,4,16,P);put(11,4,16,P)
# face drawn on the front surface (y=1), flush
for (x,z) in [(3,10),(4,10),(3,11),(4,11),(9,10),(10,10),(9,11),(10,11)]: put(x,1,z,B)
for (x,z) in [(4,11),(10,11)]: put(x,1,z,W)
for (x,z) in [(6,9),(7,9)]: put(x,1,z,P)
for (x,z) in [(5,8),(8,8)]: put(x,1,z,B)
for (x,z) in [(2,9),(11,9)]: put(x,1,z,P)
# tail
for (x,y,z,c) in [(9,8,1,O),(10,8,1,O),(11,8,1,O),(11,8,2,O),(11,8,3,W),(11,8,4,O),(11,8,5,O),(11,8,6,B)]: put(x,y,z,c)
# grass base plate
base=[]
for x in range(-1,15):
    for y in range(-1,11): base.append((x,y))

# ---- merge rows into 1xN bricks along x (same z,y,color), max len 4
bricks=[]
for (x,y,z),c in sorted(vox.items(),key=lambda t:(t[0][2],t[0][1],t[0][0])):
    pass
seen=set()
for z in sorted({k[2] for k in vox}):
    for y in sorted({k[1] for k in vox if k[2]==z}):
        xs=sorted(k[0] for k in vox if k[2]==z and k[1]==y)
        i=0
        while i<len(xs):
            x0=xs[i]; c=vox[(x0,y,z)]; n=1
            while i+n<len(xs) and xs[i+n]==x0+n and vox[(x0+n,y,z)]==c and n<4: n+=1
            bricks.append((x0,y,z,n,c)); i+=n

# ---- scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o,do_unlink=True)
sc=bpy.context.scene
P_=1.0; H=1.2; GAP=0.03
def brick_mesh(n,name):
    bm=bmesh.new()
    bmesh.ops.create_cube(bm,size=1.0)
    for v in bm.verts:
        v.co.x=(v.co.x+0.5)*(n*P_-GAP)+GAP/2; v.co.y=(v.co.y+0.5)*(P_-GAP)+GAP/2; v.co.z=(v.co.z+0.5)*H
    bmesh.ops.bevel(bm,geom=list(bm.edges),offset=0.05,segments=2,affect='EDGES')
    for i in range(n):
        r=bmesh.ops.create_cone(bm,cap_ends=True,segments=16,radius1=0.3,radius2=0.3,depth=0.2)
        for v in r["verts"]: v.co+=Vector((i*P_+0.5,0.5,H+0.1))
    me=bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    for p in me.polygons: p.use_smooth=False
    return me
meshes={n:brick_mesh(n,f"b{n}") for n in (1,2,3,4)}
mat=bpy.data.materials.new("plastic"); mat.use_nodes=True
nt=mat.node_tree; bsdf=nt.nodes["Principled BSDF"]
oi=nt.nodes.new("ShaderNodeObjectInfo"); nt.links.new(oi.outputs["Color"],bsdf.inputs["Base Color"])
bsdf.inputs["Roughness"].default_value=0.28
for m in meshes.values(): m.materials.append(mat)
# base plate (green, studs)
bpm=bpy.data.meshes.new("base"); bm=bmesh.new()
bmesh.ops.create_cube(bm,size=1.0)
for v in bm.verts: v.co.x=(v.co.x+0.5)*16-1; v.co.y=(v.co.y+0.5)*12-1; v.co.z=(v.co.z+0.5)*0.4+0.8
for x in range(-1,15):
    for y in range(-1,11):
        r=bmesh.ops.create_cone(bm,cap_ends=True,segments=12,radius1=0.3,radius2=0.3,depth=0.2)
        for v in r["verts"]: v.co+=Vector((x+0.5,y+0.5,1.3))
bm.to_mesh(bpm); bm.free(); bpm.materials.append(mat)
bo=bpy.data.objects.new("base",bpm); bo.color=(0.12,0.45,0.18,1); sc.collection.objects.link(bo)

STAGGER=1; DROP=10; START=12
objs=[]
for i,(x,y,z,n,c) in enumerate(bricks):
    o=bpy.data.objects.new(f"k{i}",meshes[n]); o.color=COL[c]; sc.collection.objects.link(o)
    tgt=Vector((x*P_,y*P_,1.2+(z-1)*H))
    f0=START+i*STAGGER
    o.location=tgt+Vector((0,0,14)); o.keyframe_insert("location",frame=f0)
    o.location=tgt; o.keyframe_insert("location",frame=f0+DROP)
    o.hide_render=True; o.keyframe_insert("hide_render",frame=f0-1)
    o.hide_render=False; o.keyframe_insert("hide_render",frame=f0)
    for fc in o.animation_data.action.fcurves if hasattr(o.animation_data.action,"fcurves") else []:
        pass
    objs.append(o)
# easing: set via keyframe interpolation (Blender 5 uses slotted actions; iterate generically)
def all_kps(o):
    a=o.animation_data.action
    try:
        for fc in a.fcurves: yield from fc.keyframe_points
    except AttributeError:
        for layer in a.layers:
            for strip in layer.strips:
                for cb in strip.channelbags:
                    for fc in cb.fcurves: yield from fc.keyframe_points
for o in objs:
    for kp in all_kps(o):
        kp.interpolation='BACK'; kp.easing='EASE_OUT'
END=START+len(bricks)*STAGGER+DROP+75
sc.frame_start=1; sc.frame_end=END; sc.render.fps=30

# camera on orbiting rig
center=Vector((7,4.5,10))
rig=bpy.data.objects.new("rig",None); rig.location=center; sc.collection.objects.link(rig)
cd=bpy.data.cameras.new("cam"); cd.lens=50
cam=bpy.data.objects.new("cam",cd); sc.collection.objects.link(cam); cam.parent=rig
cam.location=Vector((0,-44,10))
con=cam.constraints.new('TRACK_TO'); con.target=rig; con.track_axis='TRACK_NEGATIVE_Z'; con.up_axis='UP_Y'
sc.camera=cam
rig.rotation_euler=(0,0,math.radians(-30)); rig.keyframe_insert("rotation_euler",frame=1)
rig.rotation_euler=(0,0,math.radians(30)); rig.keyframe_insert("rotation_euler",frame=END)
# lights
def light(kind,loc,energy,size=5,rot=None):
    ld=bpy.data.lights.new(kind,kind); ld.energy=energy
    if kind=='AREA': ld.size=size
    lo=bpy.data.objects.new(kind,ld); lo.location=loc; sc.collection.objects.link(lo)
    c=lo.constraints.new('TRACK_TO'); c.target=rig; c.track_axis='TRACK_NEGATIVE_Z'; c.up_axis='UP_Y'
light('AREA',(-18,-22,30),9000,12)
light('AREA',(26,-10,14),2500,10)
light('AREA',(6,30,25),3000,10)
w=bpy.data.worlds.new("w"); sc.world=w; w.use_nodes=True
w.node_tree.nodes["Background"].inputs[0].default_value=(0.98,0.8,0.62,1); w.node_tree.nodes["Background"].inputs[1].default_value=0.75
# render
sc.render.engine='CYCLES'; sc.cycles.device='CPU'; sc.cycles.samples=SAMPLES; sc.cycles.use_denoising=True
sc.cycles.max_bounces=3; sc.cycles.diffuse_bounces=2; sc.cycles.glossy_bounces=2; sc.cycles.transmission_bounces=0; sc.cycles.transparent_max_bounces=2
sc.cycles.use_adaptive_sampling=True; sc.cycles.adaptive_threshold=0.05
sc.cycles.caustics_reflective=False; sc.cycles.caustics_refractive=False
sc.render.use_persistent_data=True
sc.cycles.denoiser='OPENIMAGEDENOISE'
sc.render.threads_mode='FIXED'; sc.render.threads=4
sc.render.resolution_x=int(1080*RES); sc.render.resolution_y=int(1920*RES); sc.render.resolution_percentage=100
sc.render.filepath=OUT; sc.render.image_settings.file_format='PNG'
sc.render.film_transparent=False
sc.view_settings.view_transform='Standard'
ENG=sys.argv[sys.argv.index('--engine')+1] if '--engine' in sys.argv else 'CYCLES'
sc.render.engine=ENG
print("BRICKS",len(bricks),"END",END,flush=True)
if FRAMES:
    for f in [int(x) for x in FRAMES.split(",")]:
        sc.frame_set(f); sc.render.filepath=f"{OUT}f{f:04d}.png"; bpy.ops.render.render(write_still=True)
else:
    bpy.ops.render.render(animation=True)
