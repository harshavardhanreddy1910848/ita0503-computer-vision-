import cv2
import os

# Experiment 18: ROI Cropping, Copying and Pasting
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp18.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp18.jpg")

result_image = image.copy()
# Select ROI (top-left region)
roi = image[50:180, 50:180]
# Paste into new location (bottom-right region)
result_image[200:330, 380:510] = roi
cv2.rectangle(result_image, (380, 200), (510, 330), (0, 255, 0), 2)

cv2.imshow("Original Image", image)
cv2.imshow("ROI Cropped and Pasted", result_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp18_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, result_image]))
print(f"Exp 18 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
