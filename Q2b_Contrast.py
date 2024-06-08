from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

def adjust_contrast(image, factor):
    try:
        if image.mode != 'RGB':
            image = image.convert('RGB')
        enhancer = ImageEnhance.Contrast(image)
        adjusted_image = enhancer.enhance(factor)
        return adjusted_image
    except Exception as e:
        print(f"Error adjusting contrast: {e}")
        return image

try:
    image_path = 'bird.png'
    original_image = Image.open(image_path)
except Exception as e:
    print(f"Error loading image: {e}")
    raise

contrast_factors = [0.4, 1.0, 1.8]  # 0.5 for decrease, 1.5 for increase

fig, axes = plt.subplots(1, len(contrast_factors), figsize=(15, 5))

for i, factor in enumerate(contrast_factors):
    try:
        adjusted_image = adjust_contrast(original_image, factor)
        axes[i].imshow(adjusted_image)
        axes[i].set_title(f'Contrast factor: {factor}')
        axes[i].axis('off')
    except Exception as e:
        print(f"Error displaying image: {e}")

plt.tight_layout()
plt.show()