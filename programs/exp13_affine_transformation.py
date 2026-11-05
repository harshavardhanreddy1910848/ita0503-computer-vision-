import cv2
import numpy as np
import os

# Experiment 13: Affine Transformation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp13.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp13.jpg")

rows, cols, ch = image.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
matrix = cv2.getAffineTransform(pts1, pts2)
transformed_image = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", transformed_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp13_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, transformed_image]))
print(f"Exp 13 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
