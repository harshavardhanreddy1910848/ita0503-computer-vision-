import cv2
import numpy as np
import os

# Experiment 22: Closing Morphological Operation (closes pepper holes)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp22.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp22.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Closed Image", closed_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp22_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, closed_image]))
print(f"Exp 22 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
