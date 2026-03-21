# --------------------------------------------------------------
# Import necessary libraries for:
# 1. Image processing (OpenCV)
# 2. Numerical operations (NumPy)
# 3. Displaying images (Matplotlib)
# --------------------------------------------------------------
import cv2
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------------------
# Define a utility function to display images using Matplotlib.
# 1. Set up the figure size.
# 2. Check if image is grayscale or color.
# 3. Convert color images from BGR to RGB for correct rendering.
# 4. Set the plot title and hide the axis.
# 5. Display the image on the screen.
# --------------------------------------------------------------
raw_image = cv2.imread("assets/example.jpg")
shape = raw_image.shape
print(f"Image Dimensions: {shape}")
raw_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2RGB)
plt.title("Image: ")
plt.imshow(raw_image)
plt.axis('off')
plt.show()
# --------------------------------------------------------------
# Define the main interactive function for edge detection.
# 1. Load an image from a specified path.
# 2. Convert it to grayscale.
# 3. Show the grayscale image to the user.
# 4. Present a menu of operations:
#    a) Sobel Edge Detection
#    b) Canny Edge Detection
#    c) Laplacian Edge Detection
#    d) Gaussian Smoothing
#    e) Median Filtering
#    f) Exit
# 5. Prompt the user to pick an option.
# 6. Perform the chosen operation and display the result.
# 7. Repeat until the user decides to exit.
# --------------------------------------------------------------
gray_image = cv2.cvtColor(raw_image, cv2.COLOR_RGB2GRAY)
plt.title("Grayscale Image")
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.show()
Menu = ["Sobel Edge Detection", "Canny Edge Detection", "Laplacian Edge Detection", "Gaussian Smoothing", "Median Filtering", "Exit"]
while True:
    print("Menu:")
    for i, option in enumerate(Menu, start=1):
        print(f"{i}) {option}")
    choice = int(input("Please select an option (1-6): ")) - 1
    if choice > 5 or choice < 0:
        print("Invalid choice. Please select a number between 1 and 6.")
        continue
    else: 
        break
# --------------------------------------------------------------
# Sobel Edge Detection:
# 1. Calculate Sobel filters along the x and y directions.
# 2. Convert both results to 8-bit images.
# 3. Combine them using bitwise OR.
# 4. Display the combined edge map.
# --------------------------------------------------------------
if choice == 0:
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
    plt.title("Sobel Edge Detection")
    plt.imshow(combined_sobel, cmap='gray')
    plt.axis('off')
    plt.show()
# --------------------------------------------------------------
# Canny Edge Detection:
# 1. Ask for lower and upper thresholds.
# 2. Apply Canny edge detection, which:
#    - Smooths the image with a Gaussian filter.
#    - Finds intensity gradients.
#    - Applies non-maximum suppression.
#    - Uses double-thresholding and edge tracking.
# 3. Display the detected edges.
# --------------------------------------------------------------
elif choice == 1:
    lower_threshold = int(input("Enter lower threshold for Canny edge detection: "))
    upper_threshold = int(input("Enter upper threshold for Canny edge detection: "))
    edges = cv2.Canny(gray_image, lower_threshold, upper_threshold)
    plt.title("Canny Edge Detection")
    plt.imshow(edges, cmap='gray')
    plt.axis('off')
    plt.show()
# --------------------------------------------------------------
# Laplacian Edge Detection:
# 1. Apply the Laplacian operator (second derivative).
# 2. Take the absolute value of the result to handle negative gradients.
# 3. Convert to 8-bit for display.
# 4. Show the resulting edges.
# --------------------------------------------------------------
elif choice == 2:
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
    laplacian_edges = cv2.convertScaleAbs(laplacian)
    plt.title("Laplacian Edge Detection")
    plt.imshow(laplacian_edges, cmap='gray')
    plt.axis('off')
    plt.show()
# --------------------------------------------------------------
# Gaussian Smoothing:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply GaussianBlur with the specified kernel.
# 3. Display the smoothed image, which helps reduce noise.
# --------------------------------------------------------------
elif choice == 3:
    kernel_size = int(input("Enter kernel size for Gaussian smoothing (odd number): "))
    if kernel_size % 2 == 0:
        print("Kernel size must be an odd number. Using default value of 3.")
        kernel_size = 3
    smoothed_image = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
    plt.title("Gaussian Smoothing")
    plt.imshow(smoothed_image, cmap='gray')
    plt.axis('off')
    plt.show()
# --------------------------------------------------------------
# Median Filtering:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply medianBlur, which replaces each pixel with the median of neighbors.
# 3. This helps remove salt-and-pepper noise while preserving edges.
# --------------------------------------------------------------
elif choice == 4:
    kernel_size = int(input("Enter kernel size for median filtering (odd number): "))
    if kernel_size % 2 == 0:
        print("Kernel size must be an odd number. Using default value of 3.")
        kernel_size = 3
    median_filtered_image = cv2.medianBlur(gray_image, kernel_size)
    plt.title("Median Filtering")
    plt.imshow(median_filtered_image, cmap='gray')
    plt.axis('off')
    plt.show()
# --------------------------------------------------------------
# Exit:
# 1. Print a message confirming exit.
# 2. Break out of the interactive loop.
# --------------------------------------------------------------
elif choice == 5:
    print("Exiting the program. Goodbye!")
    exit("So Long.")
# --------------------------------------------------------------
# Make a call to the interactive function with the path to an image.
# e.g., interactive_edge_detection("example.jpg")
# This is where the program starts running and awaits user input.
# --------------------------------------------------------------
