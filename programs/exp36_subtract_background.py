import cv2
import numpy as np
import os

# Experiment 36: Subtract background based on color levels (HSV)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp36.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp36.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Background color range (blueish sky/water background)
lower_bound = np.array([80, 30, 30], dtype=np.uint8)
upper_bound = np.array([140, 255, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_bound, upper_bound)
mask_inv = cv2.bitwise_not(mask)
foreground = cv2.bitwise_and(image, image, mask=mask_inv)

cv2.imshow("Original Image", image)
cv2.imshow("Background Subtracted Image", foreground)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp36_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, foreground]))
print(f"Exp 36 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
