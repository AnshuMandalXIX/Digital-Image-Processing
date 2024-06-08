from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure

def histogram_equalization(image):
    image_np = np.asarray(image)
    equalized_image_np = exposure.equalize_hist(image_np)
    equalized_image = Image.fromarray((equalized_image_np * 255).astype(np.uint8))
    return equalized_image

def plot_histogram(image, ax, title):
    image_np = np.asarray(image)
    ax.hist(image_np.flatten(), bins=256, range=(0, 255), color='black', alpha=0.75)
    ax.set_title(title)
    ax.set_xlim(0, 255)

try:
    image_path = 'bird.png'
    original_image = Image.open(image_path).convert('L')
except Exception as e:
    print(f"Error loading image: {e}")
    raise

# Perform histogram equalization
equalized_image = histogram_equalization(original_image)

# Plot the original and equalized images with their histograms
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Display the original image and its histogram
axes[0, 0].imshow(original_image, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')
plot_histogram(original_image, axes[0, 1], 'Histogram of Original Image')

# Display the equalized image and its histogram
axes[1, 0].imshow(equalized_image, cmap='gray')
axes[1, 0].set_title('Equalized Image')
axes[1, 0].axis('off')
plot_histogram(equalized_image, axes[1, 1], 'Histogram of Equalized Image')

plt.tight_layout()
plt.show()