import cv2
import numpy as np
import os

# Experiment 15: Harris Corner Detection
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp15.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp15.jpg")

original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
harris_corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
harris_corners = cv2.dilate(harris_corners, None)
image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

cv2.imshow("Original Image", original)
cv2.imshow("Harris Corner Detection", image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp15_output.png")
cv2.imwrite(out_path, cv2.hconcat([original, image]))
print(f"Exp 15 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
