import cv2
import os

# Experiment 11: 180-degree rotation clockwise along Y-axis (flip + rotate)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp11.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp11.jpg")

flipped_image = cv2.flip(image, 1)
rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_180)

cv2.imshow("Original Image", image)
cv2.imshow("Rotated 180-degree Along Y-axis", rotated_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp11_output.png")
combined = cv2.hconcat([image, rotated_image])
cv2.imwrite(out_path, combined)
print(f"Exp 11 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
