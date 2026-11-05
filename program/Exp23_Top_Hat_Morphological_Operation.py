import cv2
import numpy as np
import os

# Experiment 23: Top Hat Morphological Operation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp23.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp23.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((9, 9), np.uint8)
top_hat_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Image", top_hat_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp23_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, top_hat_image]))
print(f"Exp 23 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
