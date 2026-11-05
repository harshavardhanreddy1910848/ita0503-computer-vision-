import cv2
import os

# Experiment 31: Image Segmentation using Thresholding
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp31.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp31.jpg", cv2.IMREAD_GRAYSCALE)

threshold_value = 127
_, segmented_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp31_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, segmented_image]))
print(f"Exp 31 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
