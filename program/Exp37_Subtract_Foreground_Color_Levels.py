import cv2
import numpy as np
import os

# Experiment 37: Subtract foreground based on color levels (HSV)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp37.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp37.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Foreground color range (bright yellow/orange flower)
lower_bound = np.array([20, 100, 100], dtype=np.uint8)
upper_bound = np.array([40, 255, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_bound, upper_bound)
# Keep background only
background = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))

cv2.imshow("Original Image", image)
cv2.imshow("Foreground Subtracted Image", background)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp37_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, background]))
print(f"Exp 37 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
