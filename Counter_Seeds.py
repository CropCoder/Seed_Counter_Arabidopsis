import cv2
import numpy as np

def count_green_seeds(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image from {image_path}")
        return 0

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range for green color
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([70, 255, 255])

    # Create a mask to isolate the green seeds
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw circles and numbers on the image
    for i, contour in enumerate(contours):
        # Get the center and radius of the circle to enclose the seed
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)

        # Draw the circle
        cv2.circle(image, center, radius, (0, 255, 0), 2)

        # Put a number next to the circle
        cv2.putText(image, str(i+1), (center[0] + radius, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Save the result image
    cv2.imwrite('result_image.jpg', image)

    return len(contours)

# Replace with your image path
image_path = r'D:\Projects\Github\Repos\Seed_counting\Test-Images\011724-1000#001.jpg'
count = count_green_seeds(image_path)
print(f"Number of green seeds: {count}")
