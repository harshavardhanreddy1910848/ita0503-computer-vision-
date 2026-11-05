import cv2
import numpy as np
import os

# Experiment 21: Opening Morphological Operation (removes salt noise)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp21.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp21.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Opened Image", opened_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp21_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, opened_image]))
print(f"Exp 21 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
