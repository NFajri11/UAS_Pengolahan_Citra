import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from tkinter import Tk, Button
from tkinter.filedialog import askopenfilename

def median_filter(image, kernel_size):
    filtered_image = cv2.medianBlur(image, kernel_size)
    return filtered_image

def mse(original_image, processed_image):
    squared_diff = np.square(original_image.astype("float") - processed_image.astype("float"))
    mse_value = np.mean(squared_diff)
    return mse_value

def psnr(original_image, processed_image):
    mse_value = mse(original_image, processed_image)
    max_pixel = 255
    psnr_value = 20 * math.log10(max_pixel / math.sqrt(mse_value))
    return psnr_value

def select_and_process_image():
    # Select the image file using a file dialog
    Tk().withdraw()  # Hide the Tkinter root window
    filename = askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    # Load the selected image
    original_image = cv2.imread(filename)

    # Apply median filter
    kernel_size = 3  # Set the kernel size for the median filter
    filtered_image = median_filter(original_image, kernel_size)

    # Calculate MSE and PSNR
    mse_value = mse(original_image, filtered_image)
    psnr_value = psnr(original_image, filtered_image)

    # Convert BGR to RGB for displaying with matplotlib
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)

    # Create a new figure and display the images and metrics in a single window
    fig = plt.figure(figsize=(10, 5))  # Set the figure size to landscape orientation

    # Add the original image subplot
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title('Original Image')
    ax1.imshow(original_image)
    ax1.axis('off')

    # Add the filtered image subplot
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title(f'Median Filtered Image\nMSE: {mse_value:.2f}, PSNR: {psnr_value:.2f}')
    ax2.imshow(filtered_image)
    ax2.axis('off')

    plt.show()

# Create the tkinter window
window = Tk()

# Set the window title
window.title("Nurul Fajri _ 312110506")

# Set the window size
window.geometry("800x400")  # Set the width and height as desired (landscape orientation)

# Create the "Select Gambar" button
select_button = Button(window, text="Select Gambar", command=select_and_process_image)
select_button.pack()

# Start the tkinter event loop
window.mainloop()
