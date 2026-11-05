import cv2
import os

# Experiment 1: Convert an Image to Gray-scale
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp01.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp01.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)

# Save output screenshot
out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp01_output.png")
# Create side-by-side comparison for screenshot
gray_bgr = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
combined = cv2.hconcat([image, gray_bgr])
cv2.imwrite(out_path, combined)
print(f"Exp 01 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
