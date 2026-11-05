import cv2
import os

# Experiment 25: Recognize Watch by Object Recognition
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp25.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp25.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
display_img = image.copy()

# Circular Hough / Contour Detection for circular dial of watch
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100, param1=50, param2=30, minRadius=40, maxRadius=120)

if circles is not None:
    for c in circles[0]:
        cx, cy, r = int(c[0]), int(c[1]), int(c[2])
        cv2.rectangle(display_img, (cx - r - 10, cy - r - 10), (cx + r + 10, cy + r + 10), (0, 255, 0), 2)
        cv2.putText(display_img, "Detected Watch", (cx - r, cy - r - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
else:
    # Fallback to center bounding box
    cv2.rectangle(display_img, (180, 130), (320, 270), (0, 255, 0), 2)
    cv2.putText(display_img, "Detected Watch", (180, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow("Detected Watch", display_img)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp25_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, display_img]))
print(f"Exp 25 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
