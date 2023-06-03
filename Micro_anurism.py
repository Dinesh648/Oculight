#MOST ACCURATE CODE CELL-------------------------------------------------------------------------------------------
import cv2
import numpy as np
import sys
import os

# Load the image
image_path = sys.argv[1]
output_path = sys.argv[2]
img = cv2.imread(image_path)

# 1. Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Resize the image for faster processing
resized_img = cv2.resize(gray_img, (0,0), fx=0.5, fy=0.5)

# 3. Detect blob-like structures using the Hessian feature detector
hessian = cv2.ORB_create()
kp = hessian.detect(resized_img, None)

# 4. Draw keypoints on the image
img_kp = cv2.drawKeypoints(resized_img, kp, None, color=(0,255,0), flags=0)

# 5. Apply a color filter to distinguish soft exudates
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
yellow_min = np.array([20, 100, 100], np.uint8)
yellow_max = np.array([30, 255, 255], np.uint8)
mask = cv2.inRange(hsv_img, yellow_min, yellow_max)
yellow_filtered_img = cv2.bitwise_and(img, img, mask=mask)

# 6. Calculate the diameter of the fundus image
diameter = np.max(np.sum(np.sum(np.abs(np.diff(gray_img, axis=0)), axis=1) > 0, axis=0))

# 7. Search for the optical disc
disc_location = "unknown"
bright_area = np.where(gray_img > np.mean(gray_img) + np.std(gray_img))
if len(bright_area[0]) > 0:
    disc_location = "right" if np.mean(bright_area[1]) > diameter/2 else "left"

cv2.namedWindow('Yellow filtered image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Yellow filtered image', img.shape[1], img.shape[0])

# Display the results
# cv2.imshow('Hessian keypoints', img_kp)
# cv2.imshow('Yellow filtered image', yellow_filtered_img)
print(f"Fundus image diameter: {diameter}")
print(f"Optical disc location: {disc_location}")

image_name = os.path.basename(image_path)
image_without_extension = os.path.splitext(image_name)[0]
extension = os.path.splitext(image_name)[1].lstrip('.')
img_kp_image = image_without_extension + "_kp." +str(extension)
img_yellow_image = image_without_extension + "_yel." + str(extension)
processed_kp_image_path = os.path.join(output_path,img_kp_image)
processed_yel_image_path = os.path.join(output_path,img_yellow_image)

cv2.imwrite(processed_kp_image_path,img_kp)
cv2.imwrite(processed_yel_image_path,yellow_filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()