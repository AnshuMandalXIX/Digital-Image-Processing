from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def apply_threshold(image, threshold):
    image_np = np.asarray(image)
    binary_image_np = (image_np > threshold) * 255
    binary_image = Image.fromarray(binary_image_np.astype(np.uint8))
    return binary_image

try:
    image_path = 'bird.png'  # Replace with the path to your image
    original_image = Image.open(image_path).convert('L')  # Convert to grayscale
except Exception as e:
    print(f"Error loading image: {e}")
    raise

# Define threshold values
#threshold_values = [50, 100, 150, 200]  # User-defined thresholds
values = input("Enter Threshold value separated by space:")
threshold_values = list(map(int, values.split()))  

fig, axes = plt.subplots(len(threshold_values) + 1, 2, figsize=(10, 10))

# Display the original grayscale image
axes[0, 0].imshow(original_image, cmap='gray')
axes[0, 0].set_title('Original Grayscale Image')
axes[0, 0].axis('off')

# Plot histogram of the original grayscale image
axes[0, 1].hist(np.asarray(original_image).flatten(), bins=256, range=(0, 255), color='black', alpha=0.75)
axes[0, 1].set_title('Histogram of Grayscale Image')

# Process and display images with different thresholds
for i, threshold in enumerate(threshold_values):
    binary_image = apply_threshold(original_image, threshold)
    axes[i + 1, 0].imshow(binary_image, cmap='gray')
    axes[i + 1, 0].set_title(f'Binary Image with Threshold {threshold}')
    axes[i + 1, 0].axis('off')
    axes[i + 1, 1].hist(np.asarray(binary_image).flatten(), bins=256, range=(0, 255), color='black', alpha=0.75)
    axes[i + 1, 1].set_title(f'Histogram with Threshold {threshold}')

plt.tight_layout()
plt.show()