import cv2
import os

# Experiment 17: Watermark Insertion
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp17.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp17.jpg")

watermarked = image.copy()
overlay = image.copy()
cv2.putText(overlay, "COPYRIGHT (C) 2025", (50, 220), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (255, 255, 255), 3, cv2.LINE_AA)
alpha = 0.6
cv2.addWeighted(overlay, alpha, watermarked, 1 - alpha, 0, watermarked)

cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", watermarked)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp17_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, watermarked]))
print(f"Exp 17 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
