import cv2
import os

# Experiment 16: Sobel Filter
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp16.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp16.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv2.imshow("Original Image", image)
cv2.imshow("Sobel Combined", sobel_combined)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp16_output.png")
sobel_c_bgr = cv2.cvtColor(sobel_combined, cv2.COLOR_GRAY2BGR)
cv2.imwrite(out_path, cv2.hconcat([image, sobel_c_bgr]))
print(f"Exp 16 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
