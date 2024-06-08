import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def reduce_gray_levels(image, levels):
    image_np = np.array(image)
    interval = 256 // levels
    image_reduced = (image_np // interval) * interval
    return Image.fromarray(image_reduced)

img = 'bird.png'
original_image = Image.open(img).convert('L')

gray_levels = [128, 64, 32, 16, 8]

fig, axes = plt.subplots(1, len(gray_levels) + 1, figsize=(20, 10))

axes[0].imshow(original_image, cmap='gray')
axes[0].set_title('Original Image (256 gray levels)')
axes[0].axis('off')

for i, levels in enumerate(gray_levels):
    reduced_image = reduce_gray_levels(original_image, levels)
    axes[i + 1].imshow(reduced_image, cmap='gray')
    axes[i + 1].set_title(f'{levels} gray levels')
    axes[i + 1].axis('off')

plt.tight_layout()
plt.show()