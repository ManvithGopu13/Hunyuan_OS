import trimesh
import pyrender

# Load the GLB model as a trimesh Scene or Mesh
tm_obj = trimesh.load('301_2.glb')

# Convert to pyrender.Scene, no matter input type
if isinstance(tm_obj, trimesh.Scene):
    scene = pyrender.Scene.from_trimesh_scene(tm_obj)
else:
    scene = pyrender.Scene()
    mesh = pyrender.Mesh.from_trimesh(tm_obj)
    scene.add(mesh)

# Display with pyrender.Viewer
v = pyrender.Viewer(scene, use_raymond_lighting=True)
