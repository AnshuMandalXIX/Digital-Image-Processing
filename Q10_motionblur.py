import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

# Function to create a motion blur kernel
def motion_blur_kernel(size, angle):
    kernel = np.zeros((size, size), dtype=np.float32)
    k = int((size - 1) / 2)
    
    for i in range(size):
        kernel[i, int((i - k) * np.tan(angle) + k)] = 1
        
    kernel /= kernel.sum()
    return kernel

# Function to apply the motion blur to an image
def apply_motion_blur(image, kernel):
    blurred = cv2.filter2D(image, -1, kernel)
    return blurred

# Load the image
image_path = 'bird.png'
image = Image.open(image_path).convert('L')
image_array = np.array(image)

# Parameters
kernel_size = 15  # Size of the motion blur kernel
angle = 0  # Angle of the motion blur in radians

# Create motion blur kernel
motion_blur = motion_blur_kernel(kernel_size, angle)

# Apply motion blur to the image
blurred_image = apply_motion_blur(image_array, motion_blur)

# Display the original and blurred images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image_array, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(blurred_image, cmap='gray')
plt.title('Motion Blurred Image')
plt.axis('off')

plt.tight_layout()
plt.show()
