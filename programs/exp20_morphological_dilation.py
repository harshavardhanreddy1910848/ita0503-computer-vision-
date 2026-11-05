import cv2
import numpy as np
import os

# Experiment 20: Dilation Morphological Operation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp20.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp20.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(gray, kernel, iterations=1)

cv2.imshow("Original Image", gray)
cv2.imshow("Dilated Morphological", dilated)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp20_output.png")
cv2.imwrite(out_path, cv2.hconcat([gray, dilated]))
print(f"Exp 20 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
