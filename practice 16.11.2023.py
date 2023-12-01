import cv2
import numpy as np

# def detect_watermark(image_path, threshold=50):
#     # Read the image
#     img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#     # Apply a simple thresholding to detect high-contrast regions
#     _, binary = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

#     # Find contours in the binary image
#     contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Check for regions with a small area (potential watermarks)
#     potential_watermarks = [cnt for cnt in contours if cv2.contourArea(cnt) < 1000]

#     # Draw rectangles around potential watermarks on the original image
#     img_with_rectangles = img.copy()
#     for cnt in potential_watermarks:
#         x, y, w, h = cv2.boundingRect(cnt)
#         cv2.rectangle(img_with_rectangles, (x, y), (x + w, y + h), 255, 2)

#     # Display the original image and the image with rectangles
#     cv2.imshow('Original Image', img)
#     cv2.imshow('Image with Rectangles', img_with_rectangles)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # Example usage
# image_path = " D:\\vedio_frame\\Komal\\frame_0012_1.png"
# detect_watermark(image_path)







def detect_watermark(image):
  # Convert the image to grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply a median blur to remove noise
  blurred = cv2.medianBlur(gray, 5)

  # Calculate the difference between the original image and the blurred image
  diff = cv2.subtract(gray, blurred)

  # Threshold the difference image to create a binary image
  thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

  # Find contours in the binary image
  contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Filter out small contours
  contours = [contour for contour in contours if cv2.contourArea(contour) > 1000]

  # If there are any contours, then the image has a watermark
  if len(contours) > 0:
    return True
  else:
    return False

# Load the image
image = cv2.imread("D:\\vedio_frame\\Komal\\frame_0012_1.png")

# Detect watermarks
if detect_watermark(image):
  print("The image has a watermark")
else:
  print("The image does not have a watermark")