import cv2
import numpy as np
import os

# Experiment 14: Perspective Transformation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp14.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp14.jpg")

rows, cols, ch = image.shape
pts1 = np.float32([[120, 80], [380, 60], [80, 380], [440, 420]])
pts2 = np.float32([[50, 50], [450, 50], [50, 450], [450, 450]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
transformed_image = cv2.warpPerspective(image, matrix, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", transformed_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp14_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, transformed_image]))
print(f"Exp 14 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
