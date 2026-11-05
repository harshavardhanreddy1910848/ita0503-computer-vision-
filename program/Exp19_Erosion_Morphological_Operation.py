import cv2
import numpy as np
import os

# Experiment 19: Erosion Morphological Operation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp19.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp19.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(gray, kernel, iterations=1)

cv2.imshow("Original Image", gray)
cv2.imshow("Eroded Morphological", eroded)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp19_output.png")
cv2.imwrite(out_path, cv2.hconcat([gray, eroded]))
print(f"Exp 19 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
