import cv2
import os

# Experiment 12: 270-degree rotation clockwise along Y-axis
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp12.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp12.jpg")

flipped_image = cv2.flip(image, 1)
rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original Image", image)
cv2.imshow("Rotated 270-degree Along Y-axis", rotated_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp12_output.png")
h1, w1 = image.shape[:2]
h2, w2 = rotated_image.shape[:2]
max_h = max(h1, h2)
p1 = cv2.copyMakeBorder(image, 0, max_h - h1, 0, 0, cv2.BORDER_CONSTANT, value=[0,0,0])
p2 = cv2.copyMakeBorder(rotated_image, 0, max_h - h2, 0, 0, cv2.BORDER_CONSTANT, value=[0,0,0])
cv2.imwrite(out_path, cv2.hconcat([p1, p2]))
print(f"Exp 12 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
