import numpy as np
from PIL import Image
from scipy.ndimage import uniform_filter

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

# Function to add Gaussian noise to an image
def add_gaussian_noise(image, mean, sigma):
    noisy_image = np.array(image)
    gaussian_noise = np.random.normal(mean, sigma, noisy_image.shape)
    noisy_image = noisy_image + gaussian_noise
    noisy_image = np.clip(noisy_image, 0, 255)  # Clip values to be valid image pixel values
    return Image.fromarray(noisy_image.astype(np.uint8))

# Function to apply an averaging filter
def apply_averaging_filter(image, filter_size):
    image_array = np.array(image)
    filtered_image = uniform_filter(image_array, size=filter_size)
    return Image.fromarray(filtered_image)

# Load the image
image = Image.open('bird.png').convert('L')  # Convert to grayscale for simplicity

# Add salt-and-pepper noise
salt_prob = 0.02
pepper_prob = 0.02
sp_noisy_image = add_salt_and_pepper_noise(image, salt_prob, pepper_prob)

# Add Gaussian noise
mean = 0
sigma = 25
gaussian_noisy_image = add_gaussian_noise(image, mean, sigma)

# Apply averaging filter to salt-and-pepper noisy image
sp_filtered_image_3x3 = apply_averaging_filter(sp_noisy_image, 3)
sp_filtered_image_5x5 = apply_averaging_filter(sp_noisy_image, 5)

# Apply averaging filter to Gaussian noisy image
gaussian_filtered_image_3x3 = apply_averaging_filter(gaussian_noisy_image, 3)
gaussian_filtered_image_5x5 = apply_averaging_filter(gaussian_noisy_image, 5)

# Save or display results
sp_noisy_image.show(title="Salt and Pepper Noisy Image")
gaussian_noisy_image.show(title="Gaussian Noisy Image")
sp_filtered_image_3x3.show(title="Salt and Pepper Filtered 3x3")
sp_filtered_image_5x5.show(title="Salt and Pepper Filtered 5x5")
gaussian_filtered_image_3x3.show(title="Gaussian Filtered 3x3")
gaussian_filtered_image_5x5.show(title="Gaussian Filtered 5x5")
