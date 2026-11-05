import cv2
import numpy as np
import os

# Experiment 8: Dilate an Image using Dilate function
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp08.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp08.jpg")

kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(image, kernel, iterations=2)

cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp08_output.png")
combined = cv2.hconcat([image, dilated_image])
cv2.imwrite(out_path, combined)
print(f"Exp 08 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
