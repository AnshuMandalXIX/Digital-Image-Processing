from PIL import Image, ImageOps
import matplotlib.pyplot as plt

def create_negative(image):
    try:
        if image.mode != 'RGB':
            image = image.convert('RGB')
        negative_image = ImageOps.invert(image)
        return negative_image
    except Exception as e:
        print(f"Error creating negative: {e}")
        return image

try:
    image_path = 'bird.png'
    original_image = Image.open(image_path)
except Exception as e:
    print(f"Error loading image: {e}")
    raise

negative_image = create_negative(original_image)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(original_image)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(negative_image)
axes[1].set_title('Negative Image')
axes[1].axis('off')

plt.tight_layout()
plt.show()