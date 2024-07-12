import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image_path = "./hinhgoc.png"  # Replace with your image path
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    raise FileNotFoundError(f"Error: Unable to load image at {image_path}")

# Get the dimensions of the image
height, width, _ = image.shape

# Assuming the image is divided equally into 4 parts vertically
part_width = width // 4

# Split the image into 4 parts
parts = [image[:, i * part_width:(i + 1) * part_width] for i in range(4)]

# Create the stitcher object
stitcher = cv2.Stitcher_create()

# Stitch the images together
status, stitched = stitcher.stitch(parts)

if status == cv2.Stitcher_OK:
    # Display the stitched image
    stitched_rgb = cv2.cvtColor(stitched, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(15, 10))
    plt.imshow(stitched_rgb)
    plt.axis('off')
    plt.show()

    # Save the stitched image
    stitched_image_path = "/mnt/data/stitched_image.png"
    cv2.imwrite(stitched_image_path, stitched)
    print(f"Stitched image saved at: {stitched_image_path}")
else:
    print(f"Error during stitching: {status}")
