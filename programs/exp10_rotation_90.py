import cv2
import os

# Experiment 10: 90-degree rotation clockwise
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp10.jpg")
img = cv2.imread(image_path)
if img is None:
    img = cv2.imread("input_exp10.jpg")

rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image 90 Clockwise", rotated_img)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp10_output.png")
# Pad to match heights for side-by-side display
h1, w1 = img.shape[:2]
h2, w2 = rotated_img.shape[:2]
max_h = max(h1, h2)
p1 = cv2.copyMakeBorder(img, 0, max_h - h1, 0, 0, cv2.BORDER_CONSTANT, value=[0,0,0])
p2 = cv2.copyMakeBorder(rotated_img, 0, max_h - h2, 0, 0, cv2.BORDER_CONSTANT, value=[0,0,0])
cv2.imwrite(out_path, cv2.hconcat([p1, p2]))
print(f"Exp 10 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
