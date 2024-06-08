import numpy as np
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def apply_convolution(image, kernel):
    # Convert the image to a numpy array
    image_np = np.asarray(image)
    
    # Apply convolution
    kernel_size = kernel.shape[0]
    convolved_image_np = np.zeros_like(image_np)
    
    # Padding the image to handle borders
    padded_image = np.pad(image_np, ((kernel_size//2, kernel_size//2), (kernel_size//2, kernel_size//2)), mode='constant', constant_values=0)
    
    for i in range(image_np.shape[0]):
        for j in range(image_np.shape[1]):
            region = padded_image[i:i+kernel_size, j:j+kernel_size]
            convolved_image_np[i, j] = np.sum(region * kernel)
    
    # Normalize the result to the range [0, 255]
    convolved_image_np = np.clip(convolved_image_np, 0, 255)
    
    # Convert the numpy array back to an image
    convolved_image = Image.fromarray(convolved_image_np.astype(np.uint8))
    
    return convolved_image

# Load the original image
try:
    image_path = 'bird.png'  # Replace with the path to your image
    original_image = Image.open(image_path).convert('L')  # Convert to grayscale
except Exception as e:
    print(f"Error loading image: {e}")
    raise

# Define the 3x3 averaging kernel
kernel_3x3 = np.ones((3, 3)) / 9.0

# Define the 5x5 averaging kernel
kernel_5x5 = np.ones((5, 5)) / 25.0

# Apply the convolution with the 3x3 kernel
convolved_image_3x3 = apply_convolution(original_image, kernel_3x3)

# Apply the convolution with the 5x5 kernel
convolved_image_5x5 = apply_convolution(original_image, kernel_5x5)

# Prepare the subplot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Display the original image
axes[0].imshow(original_image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

# Display the image convolved with the 3x3 kernel
axes[1].imshow(convolved_image_3x3, cmap='gray')
axes[1].set_title('Image with 3x3 Averaging Kernel')
axes[1].axis('off')

# Display the image convolved with the 5x5 kernel
axes[2].imshow(convolved_image_5x5, cmap='gray')
axes[2].set_title('Image with 5x5 Averaging Kernel')
axes[2].axis('off')

plt.tight_layout()
plt.show()
