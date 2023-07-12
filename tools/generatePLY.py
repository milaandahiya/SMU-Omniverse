import open3d as o3d
from generateRGBD import generateRGBD
import math

# Get the RGBD image generated from Omniverse data
displayAll = False
rgbd1 = generateRGBD(camera=0, image=1, display=displayAll)
rgbd2 = generateRGBD(camera=1, image=1, display=displayAll)

# Set camera intrinsic values
intrinsic = o3d.camera.PinholeCameraIntrinsic(1280, 720, 1221, 941, 640, 360)

# Create point clouds
pcd1 = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd1, intrinsic)
pcd2 = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd2, intrinsic)

# rotate pcd2, attempt multiway registration
angle = -37.2 * math.pi / 180
pcd2.rotate([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
pcd2.translate([-0.035, 0, -0.026])

# Combine point clouds, and display right side up
pcd = pcd1 + pcd2
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
o3d.visualization.draw_geometries([pcd])
