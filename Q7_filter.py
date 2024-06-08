import numpy as np
from PIL import Image
from scipy.ndimage import uniform_filter, median_filter

# Function to add salt-and-pepper noise to an image
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.array(image)
    total_pixels = noisy_image.size
    num_salt = int(total_pixels * salt_prob)
    num_pepper = int(total_pixels * pepper_prob)
    
    # Add salt (white) noise
    coords = [np.random.randint(0, i, num_salt) for i in noisy_image.shape]
    noisy_image[tuple(coords)] = 255

    # Add pepper (black) noise
    coords = [np.random.randint(0, i, num_pepper) for i in noisy_image.shape]
    noisy_image[tuple(coords)] = 0
    
    return Image.fromarray(noisy_image)

# Function to apply an averaging (box) filter
def apply_box_filter(image, filter_size):
    image_array = np.array(image)
    filtered_image = uniform_filter(image_array, size=filter_size)
    return Image.fromarray(filtered_image)

# Function to apply a median filter
def apply_median_filter(image, filter_size):
    image_array = np.array(image)
    filtered_image = median_filter(image_array, size=filter_size)
    return Image.fromarray(filtered_image)

# Load the image
image = Image.open('bird.png').convert('L')  # Convert to grayscale for simplicity

# Add salt-and-pepper noise
salt_prob = 0.02
pepper_prob = 0.02
sp_noisy_image = add_salt_and_pepper_noise(image, salt_prob, pepper_prob)

# Apply 3x3 box filter
box_filtered_image_3x3 = apply_box_filter(sp_noisy_image, 3)

# Apply 5x5 box filter
box_filtered_image_5x5 = apply_box_filter(sp_noisy_image, 5)

# Apply median filter
median_filtered_image = apply_median_filter(sp_noisy_image, 3)

# Save or display results
sp_noisy_image.show(title="Salt and Pepper Noisy Image")
box_filtered_image_3x3.show(title="Box Filtered 3x3")
box_filtered_image_5x5.show(title="Box Filtered 5x5")
median_filtered_image.show(title="Median Filtered Image")
