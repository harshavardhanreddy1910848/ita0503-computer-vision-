import cv2
import os

# Experiment 2: Convert an Image to Blur using Gaussian Blur
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp02.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp02.jpg")

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp02_output.png")
combined = cv2.hconcat([image, blurred_image])
cv2.imwrite(out_path, combined)
print(f"Exp 02 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
