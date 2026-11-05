import cv2
import numpy as np
import os

# Experiment 24: Black Hat Morphological Operation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp24.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp24.jpg", cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Black Hat Image", blackhat)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp24_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, blackhat]))
print(f"Exp 24 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
