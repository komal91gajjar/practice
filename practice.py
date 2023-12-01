# import cv2
# import numpy as np
# from sklearn.cluster import KMeans

# # Load the image
# image = cv2.imread('Left_center\frame_0000_3.png')

# # Reshape the image to a 2D array of pixels
# pixels = image.reshape((-1, 3))

# # Apply k-means clustering
# kmeans = KMeans(n_clusters=K)
# kmeans.fit(pixels)

# # Get cluster assignments for each pixel
# labels = kmeans.labels_

# # Reshape the labels to the shape of the original image
# segmented_image = labels.reshape(image.shape[:2])

# # Display the segmented image
# cv2.imshow('Segmented Image', segmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# from sklearn.cluster import KMeans

# # Load the image
# image_path = 'Left_center/frame_0000_3.png'
# image = cv2.imread(image_path)

# # Check if the image is successfully loaded
# if image is None:
#     print(f"Error: Unable to read the image at path: {image_path}")
#     exit()

# # Reshape the image to a 2D array of pixels
# pixels = image.reshape((-1, 3))

# # Apply k-means clustering
# K = 3  # Set the number of clusters
# kmeans = KMeans(n_clusters=K, n_init=10)  # Explicitly set n_init to suppress the warning
# kmeans.fit(pixels)

# # Get cluster assignments for each pixel
# labels = kmeans.labels_

# # Reshape the labels to the shape of the original image
# segmented_image = labels.reshape(image.shape[:2])

# # Convert the data type to np.uint8
# segmented_image = np.uint8(segmented_image)

# # Display the segmented image
# cv2.imshow('Segmented Image', segmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
# from sklearn.cluster import KMeans

# # Load the image
# image_path = 'your_image_path.jpg'
# image = cv2.imread(image_path)

# # Check if the image is successfully loaded
# if image is None:
#     print(f"Error: Unable to read the image at path: {image_path}")
#     exit()

# Reshape the image to a 2D array of pixels
# pixels = image.reshape((-1, 3))

# # Apply k-means clustering
# K = 3  # Set the number of clusters
# kmeans = KMeans(n_clusters=K)
# kmeans.fit(pixels)

# # Get cluster assignments for each pixel
# labels = kmeans.labels_

# # Reshape the labels to the shape of the original image
# segmented_image = labels.reshape(image.shape[:2])

# Convert the data type to np.uint8
# segmented_image = np.uint8(segmented_image)

# # Display the segmented image
# cv2.imshow('Segmented Image', segmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
from sklearn.cluster import KMeans

# Load the image
image_path = 'Left_center/frame_0000_3.png'
image = cv2.imread(image_path)

# Check if the image is successfully loaded
if image is None:
    print(f"Error: Unable to read the image at path: {image_path}")
    exit()

# Reshape the image to a 2D array of pixels
pixels = image.reshape((-1, 3))

# Apply k-means clustering
K = 3  # Set the number of clusters
kmeans = KMeans(n_clusters=K, n_init=10, random_state=42)  # Set random_state for reproducibility
kmeans.fit(pixels)

# Get cluster assignments for each pixel
labels = kmeans.labels_

# Reshape the labels to the shape of the original image
segmented_image = labels.reshape(image.shape[:2])

# Assign colors to clusters
cluster_colors = np.random.randint(0, 255, size=(K, 3), dtype=np.uint8)

# Map cluster labels to colors
colored_segmentation = cluster_colors[segmented_image]

# Display the segmented image
cv2.imshow('Colored Segmented Image', colored_segmentation)
cv2.waitKey(0)
cv2.destroyAllWindows()

