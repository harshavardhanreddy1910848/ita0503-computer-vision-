import cv2
import os
import numpy as np

# Experiment 9: Image scaling (bigger and smaller sizes)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp09.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp09.jpg")

bigger_image = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp09_output.png")

# Clean layout: pad smaller and original to match height of bigger_image for comparison
h_big, w_big = bigger_image.shape[:2]
orig_padded = np.zeros((h_big, image.shape[1], 3), dtype=np.uint8)
orig_padded[:image.shape[0], :image.shape[1]] = image

small_padded = np.zeros((h_big, smaller_image.shape[1], 3), dtype=np.uint8)
small_padded[:smaller_image.shape[0], :smaller_image.shape[1]] = smaller_image

cv2.putText(orig_padded, "Original (1x)", (20, h_big - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.putText(small_padded, "Small (0.5x)", (10, h_big - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
cv2.putText(bigger_image, "Enlarged (2.0x)", (20, h_big - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

combined = cv2.hconcat([orig_padded, small_padded, bigger_image])
cv2.imwrite(out_path, combined)
print(f"Exp 09 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
