import cv2
import os

# Experiment 4: Histogram Equalization
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp04.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp04.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
equalized_image = cv2.equalizeHist(gray_image)

cv2.imshow("Original Grayscale Image", gray_image)
cv2.imshow("Histogram Equalized Image", equalized_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp04_output.png")
combined = cv2.hconcat([gray_image, equalized_image])
cv2.imwrite(out_path, combined)
print(f"Exp 04 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
