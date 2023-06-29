import open3d as o3d
from PIL import Image
from generateRGBD import generateRGBD
import numpy as np

# Get the RGBD image generated from Omniverse data
displayAll = False
rgbd1 = generateRGBD(camera=0, image=1, display=displayAll)
rgbd2 = generateRGBD(camera=1, image=1, display=displayAll)

# Set camera intrinsic values
intrinsic = o3d.camera.PinholeCameraIntrinsic(1280, 720, 1500, 1500, 640, 360)

# Create point clouds
pcd1 = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd1, intrinsic)
pcd2 = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd2, intrinsic)

# Compute odometry between RGBD images (not strictly necessary for Omniverse cameras with known translations, but
# probably is necessary for real world cameras)
option = o3d.pipelines.odometry.OdometryOption() # TODO maybe set options
success, trans, info = o3d.pipelines.odometry.compute_rgbd_odometry(rgbd1, rgbd2, intrinsic, option=option)

if success:
    print("Transformation success")
    pcd1.transform(trans)

# Translate right side up, and display right side up
pcd = pcd1 + pcd2
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
o3d.visualization.draw_geometries([pcd])
