import cv2
import numpy as np
import os

# Experiment 6: Basic Image Erosion
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp06.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp06.jpg")

kernel = np.ones((5, 5), np.uint8)
eroded_image = cv2.erode(image, kernel, iterations=2)

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp06_output.png")
combined = cv2.hconcat([image, eroded_image])
cv2.imwrite(out_path, combined)
print(f"Exp 06 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
