import cv2
import os

# Experiment 3: Canny Edge Detection
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp03.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp03.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)

cv2.imshow("Original Image", image)
cv2.imshow("Edge Detected Image", edges)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp03_output.png")
edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
combined = cv2.hconcat([image, edges_bgr])
cv2.imwrite(out_path, combined)
print(f"Exp 03 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
