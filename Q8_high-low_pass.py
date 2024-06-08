import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to apply a Butterworth low-pass filter
def butterworth_lowpass_filter(d0, n, shape):
    P, Q = shape
    u = np.arange(P)
    v = np.arange(Q)
    u = u - P//2
    v = v - Q//2
    U, V = np.meshgrid(u, v, sparse=False, indexing='ij')
    D = np.sqrt(U**2 + V**2)
    H = 1 / (1 + (D / d0)**(2 * n))
    return H

# Function to apply a Butterworth high-pass filter
def butterworth_highpass_filter(d0, n, shape):
    P, Q = shape
    u = np.arange(P)
    v = np.arange(Q)
    u = u - P//2
    v = v - Q//2
    U, V = np.meshgrid(u, v, sparse=False, indexing='ij')
    D = np.sqrt(U**2 + V**2)
    H = 1 / (1 + (d0 / D)**(2 * n))
    return H

# Function to apply a filter in the frequency domain
def apply_filter(image, H):
    F = np.fft.fft2(image)
    F_shifted = np.fft.fftshift(F)
    G_shifted = F_shifted * H
    G = np.fft.ifftshift(G_shifted)
    g = np.fft.ifft2(G)
    return np.abs(g)

# Load the image
image_path = 'bird.png'
image = Image.open(image_path).convert('L')
image_array = np.array(image)

# Parameters
d0_low_1 = 30
d0_low_2 = 60
d0_high_1 = 30
d0_high_2 = 60
n = 2  # Butterworth filter order

# Shape of the image
shape = image_array.shape

# Create Butterworth filters
lowpass_filter_1 = butterworth_lowpass_filter(d0_low_1, n, shape)
lowpass_filter_2 = butterworth_lowpass_filter(d0_low_2, n, shape)
highpass_filter_1 = butterworth_highpass_filter(d0_high_1, n, shape)
highpass_filter_2 = butterworth_highpass_filter(d0_high_2, n, shape)

# Apply filters to the image
lowpass_image_1 = apply_filter(image_array, lowpass_filter_1)
lowpass_image_2 = apply_filter(image_array, lowpass_filter_2)
highpass_image_1 = apply_filter(image_array, highpass_filter_1)
highpass_image_2 = apply_filter(image_array, highpass_filter_2)

# Display results
plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.imshow(image_array, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.imshow(lowpass_image_1, cmap='gray')
plt.title(f'Butterworth Low-Pass (d0={d0_low_1})')
plt.axis('off')

plt.subplot(3, 2, 3)
plt.imshow(lowpass_image_2, cmap='gray')
plt.title(f'Butterworth Low-Pass (d0={d0_low_2})')
plt.axis('off')

plt.subplot(3, 2, 4)
plt.imshow(highpass_image_1, cmap='gray')
plt.title(f'Butterworth High-Pass (d0={d0_high_1})')
plt.axis('off')

plt.subplot(3, 2, 5)
plt.imshow(highpass_image_2, cmap='gray')
plt.title(f'Butterworth High-Pass (d0={d0_high_2})')
plt.axis('off')

plt.tight_layout()
plt.show()
