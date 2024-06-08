import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

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

def butterworth_bandpass_filter(d0, w, n, shape):
    P, Q = shape
    u = np.arange(P)
    v = np.arange(Q)
    u = u - P//2
    v = v - Q//2
    U, V = np.meshgrid(u, v, sparse=False, indexing='ij')
    D = np.sqrt(U**2 + V**2)
    H = 1 / (1 + ((D * w) / (D**2 - d0**2))**(2 * n))
    return H

def butterworth_bandstop_filter(d0, w, n, shape):
    P, Q = shape
    u = np.arange(P)
    v = np.arange(Q)
    u = u - P//2
    v = v - Q//2
    U, V = np.meshgrid(u, v, sparse=False, indexing='ij')
    D = np.sqrt(U**2 + V**2)
    H = 1 - 1 / (1 + ((D * w) / (D**2 - d0**2))**(2 * n))
    return H

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
d0 = 30  # Cutoff frequency
w = 10   # Bandwidth for band-pass and band-stop filters
n = 2    # Butterworth filter order

# Shape of the image
shape = image_array.shape

# Create filters
lowpass_filter = butterworth_lowpass_filter(d0, n, shape)
highpass_filter = butterworth_highpass_filter(d0, n, shape)
bandpass_filter = butterworth_bandpass_filter(d0, w, n, shape)
bandstop_filter = butterworth_bandstop_filter(d0, w, n, shape)

# Apply filters to the image
lowpass_image = apply_filter(image_array, lowpass_filter)
highpass_image = apply_filter(image_array, highpass_filter)
bandpass_image = apply_filter(image_array, bandpass_filter)
bandstop_image = apply_filter(image_array, bandstop_filter)

# Display results
plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.imshow(image_array, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.imshow(lowpass_image, cmap='gray')
plt.title('Butterworth Low-Pass Filtered')
plt.axis('off')

plt.subplot(3, 2, 3)
plt.imshow(highpass_image, cmap='gray')
plt.title('Butterworth High-Pass Filtered')
plt.axis('off')

plt.subplot(3, 2, 4)
plt.imshow(bandpass_image, cmap='gray')
plt.title('Butterworth Band-Pass Filtered')
plt.axis('off')

plt.subplot(3, 2, 5)
plt.imshow(bandstop_image, cmap='gray')
plt.title('Butterworth Band-Stop Filtered')
plt.axis('off')

plt.tight_layout()
plt.show()
