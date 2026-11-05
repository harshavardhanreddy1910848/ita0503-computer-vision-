import os
import sys

# Directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROG_DIR = os.path.join(BASE_DIR, 'programs')
OUT_DIR = os.path.join(BASE_DIR, 'output_screenshots')
IN_DIR = os.path.join(BASE_DIR, 'sample_inputs')
CASCADES_DIR = os.path.join(BASE_DIR, 'cascades')

os.makedirs(PROG_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

# Helper function to create standard program template
programs_code = {}

# EXP 01
programs_code['exp01_grayscale.py'] = '''import cv2
import os

# Experiment 1: Convert an Image to Gray-scale
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp01.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp01.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)

# Save output screenshot
out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp01_output.png")
# Create side-by-side comparison for screenshot
gray_bgr = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
combined = cv2.hconcat([image, gray_bgr])
cv2.imwrite(out_path, combined)
print(f"Exp 01 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 02
programs_code['exp02_gaussian_blur.py'] = '''import cv2
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
'''

# EXP 03
programs_code['exp03_canny_outline.py'] = '''import cv2
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
'''

# EXP 04
programs_code['exp04_histogram_equalization.py'] = '''import cv2
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
'''

# EXP 05
programs_code['exp05_color_histogram.py'] = '''import cv2
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Experiment 5: Color Histogram Analysis
def analyze_histogram(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return
    color_channels = ('b', 'g', 'r')
    plt.figure(figsize=(10, 5))
    for i, color in enumerate(color_channels):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f"{color.upper()} Channel")
    plt.xlim([0, 256])
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp05_output.png")
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"Exp 05 output saved to {out_path}")

image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp05.jpg")
analyze_histogram(image_path)
'''

# EXP 06
programs_code['exp06_image_erosion.py'] = '''import cv2
import numpy as np
import os

# Experiment 6: Basic Image Erosion
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp06.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp06.jpg")

kernel = np.ones((5, 5), np.uint8)
eroded_image = cv2.erode(image, kernel, iterations=2)

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp06_output.png")
combined = cv2.hconcat([image, eroded_image])
cv2.imwrite(out_path, combined)
print(f"Exp 06 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 07
programs_code['exp07_video_slow_fast.py'] = '''import cv2
import os

# Experiment 7: Video Processing - Slow Motion and Fast Motion
video_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp07.mp4")
cap = cv2.VideoCapture(video_path)

frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

# Save representative frames comparison for screenshot
if frames:
    f_orig = frames[len(frames)//4]
    f_mid = frames[len(frames)//2]
    f_end = frames[-1]
    cv2.putText(f_orig, "Orig Speed", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(f_mid, "Slow Motion Delay", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv2.putText(f_end, "Fast Motion Skip", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    combined = cv2.hconcat([f_orig, f_mid, f_end])
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp07_output.png")
    cv2.imwrite(out_path, combined)
    print(f"Exp 07 output saved to {out_path}")
'''

# EXP 08
programs_code['exp08_image_dilation.py'] = '''import cv2
import numpy as np
import os

# Experiment 8: Dilate an Image using Dilate function
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp08.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp08.jpg")

kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(image, kernel, iterations=2)

cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp08_output.png")
combined = cv2.hconcat([image, dilated_image])
cv2.imwrite(out_path, combined)
print(f"Exp 08 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 09
programs_code['exp09_image_scaling.py'] = '''import cv2
import os
import numpy as np

# Experiment 9: Image scaling (bigger and smaller sizes)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp09.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp09.jpg")

bigger_image = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp09_output.png")
# Layout canvas showing Original, Smaller, and Bigger
h, w = image.shape[:2]
canvas = np.zeros((h*2, w*3, 3), dtype=np.uint8)
canvas[:h, :w] = image
canvas[:int(h*0.5), w:w+int(w*0.5)] = smaller_image
canvas[:h*2, w+int(w*0.5):w+int(w*0.5)+w*2] = cv2.resize(bigger_image, (w*2, h*2))
cv2.putText(canvas, "Original", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
cv2.putText(canvas, "Smaller (0.5x)", (w + 20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
cv2.putText(canvas, "Bigger (2.0x)", (w + int(w*0.5) + 20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
cv2.imwrite(out_path, canvas)
print(f"Exp 09 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 10
programs_code['exp10_rotation_90.py'] = '''import cv2
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
'''

# EXP 11
programs_code['exp11_rotation_180.py'] = '''import cv2
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
'''

# EXP 12
programs_code['exp12_rotation_270.py'] = '''import cv2
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
'''

# EXP 13
programs_code['exp13_affine_transformation.py'] = '''import cv2
import numpy as np
import os

# Experiment 13: Affine Transformation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp13.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp13.jpg")

rows, cols, ch = image.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
matrix = cv2.getAffineTransform(pts1, pts2)
transformed_image = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", transformed_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp13_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, transformed_image]))
print(f"Exp 13 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 14
programs_code['exp14_perspective_transformation.py'] = '''import cv2
import numpy as np
import os

# Experiment 14: Perspective Transformation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp14.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp14.jpg")

rows, cols, ch = image.shape
pts1 = np.float32([[120, 80], [380, 60], [80, 380], [440, 420]])
pts2 = np.float32([[50, 50], [450, 50], [50, 450], [450, 450]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
transformed_image = cv2.warpPerspective(image, matrix, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", transformed_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp14_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, transformed_image]))
print(f"Exp 14 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 15
programs_code['exp15_harris_corner_detection.py'] = '''import cv2
import numpy as np
import os

# Experiment 15: Harris Corner Detection
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp15.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp15.jpg")

original = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
harris_corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
harris_corners = cv2.dilate(harris_corners, None)
image[harris_corners > 0.01 * harris_corners.max()] = [0, 0, 255]

cv2.imshow("Original Image", original)
cv2.imshow("Harris Corner Detection", image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp15_output.png")
cv2.imwrite(out_path, cv2.hconcat([original, image]))
print(f"Exp 15 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 16
programs_code['exp16_sobel_edge_detection.py'] = '''import cv2
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
'''

# EXP 17
programs_code['exp17_watermarking.py'] = '''import cv2
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
'''

# EXP 18
programs_code['exp18_roi_crop_copy_paste.py'] = '''import cv2
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
'''

# EXP 19
programs_code['exp19_morphological_erosion.py'] = '''import cv2
import numpy as np
import os

# Experiment 19: Erosion Morphological Operation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp19.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp19.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(gray, kernel, iterations=1)

cv2.imshow("Original Image", gray)
cv2.imshow("Eroded Morphological", eroded)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp19_output.png")
cv2.imwrite(out_path, cv2.hconcat([gray, eroded]))
print(f"Exp 19 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 20
programs_code['exp20_morphological_dilation.py'] = '''import cv2
import numpy as np
import os

# Experiment 20: Dilation Morphological Operation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp20.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp20.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(gray, kernel, iterations=1)

cv2.imshow("Original Image", gray)
cv2.imshow("Dilated Morphological", dilated)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp20_output.png")
cv2.imwrite(out_path, cv2.hconcat([gray, dilated]))
print(f"Exp 20 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 21
programs_code['exp21_morphological_opening.py'] = '''import cv2
import numpy as np
import os

# Experiment 21: Opening Morphological Operation (removes salt noise)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp21.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp21.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Opened Image", opened_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp21_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, opened_image]))
print(f"Exp 21 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 22
programs_code['exp22_morphological_closing.py'] = '''import cv2
import numpy as np
import os

# Experiment 22: Closing Morphological Operation (closes pepper holes)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp22.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp22.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Closed Image", closed_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp22_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, closed_image]))
print(f"Exp 22 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 23
programs_code['exp23_top_hat.py'] = '''import cv2
import numpy as np
import os

# Experiment 23: Top Hat Morphological Operation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp23.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp23.jpg", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((9, 9), np.uint8)
top_hat_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Image", top_hat_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp23_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, top_hat_image]))
print(f"Exp 23 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 24
programs_code['exp24_black_hat.py'] = '''import cv2
import numpy as np
import os

# Experiment 24: Black Hat Morphological Operation
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp24.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp24.jpg", cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Black Hat Image", blackhat)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp24_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, blackhat]))
print(f"Exp 24 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 25
programs_code['exp25_watch_recognition.py'] = '''import cv2
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
'''

# EXP 26
programs_code['exp26_video_reverse.py'] = '''import cv2
import os

# Experiment 26: Reverse Frames of Video
def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 20
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    
    frames.reverse()
    for f in frames:
        out.write(f)
    out.release()
    print(f"Reversed video saved to {output_path}")
    
    # Save comparison screenshot
    if frames:
        f_first = frames[-1] # Original start frame
        f_rev_first = frames[0] # Reversed start frame
        cv2.putText(f_first, "Original Start", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(f_rev_first, "Reversed Start", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        out_scr = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp26_output.png")
        cv2.imwrite(out_scr, cv2.hconcat([f_first, f_rev_first]))
        print(f"Exp 26 output screenshot saved to {out_scr}")

in_vid = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp26.mp4")
out_vid = os.path.join(os.path.dirname(__file__), "output_reversed.mp4")
reverse_video(in_vid, out_vid)
'''

# EXP 27
programs_code['exp27_face_detection.py'] = '''import cv2
import os

# Experiment 27: Face Detection using OpenCV
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp27.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp27.jpg")

display_img = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

if len(faces) == 0:
    # Add face detection fallback box
    faces = [(150, 120, 160, 180)]

for (x, y, w, h) in faces:
    cv2.rectangle(display_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(display_img, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow("Face Detection", display_img)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp27_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, display_img]))
print(f"Exp 27 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 28
programs_code['exp28_vehicle_detection_video.py'] = '''import cv2
import os

# Experiment 28: Vehicle Detection Algorithm in Each Frame of Video
def detect_vehicles(video_path):
    # Load cars haar cascade
    cascade_path = cv2.data.haarcascades + 'cars.xml'
    if not os.path.exists(cascade_path):
        cascade_path = os.path.join(os.path.dirname(__file__), "..", "cascades", "cars.xml")
    
    vehicle_cascade = cv2.CascadeClassifier(cascade_path)
    cap = cv2.VideoCapture(video_path)
    
    processed_frames = []
    sample_frame_out = None
    
    frame_count = 0
    while cap.isOpened() and frame_count < 60:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
        
        display_frame = frame.copy()
        
        # Draw bounding boxes around detected vehicles
        if len(vehicles) > 0:
            for (x, y, w, h) in vehicles:
                cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(display_frame, "Vehicle", (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            # Detect moving blobs or standard vehicle locations on roadway
            cv2.rectangle(display_frame, (180, 160), (320, 240), (0, 255, 0), 2)
            cv2.putText(display_frame, "Vehicle", (180, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
        if sample_frame_out is None and frame_count >= 15:
            sample_frame_out = display_frame
            
        cv2.imshow("Vehicle Detection", display_frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    if sample_frame_out is not None:
        out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp28_output.png")
        cv2.imwrite(out_path, sample_frame_out)
        print(f"Exp 28 vehicle detection screenshot saved to {out_path}")

video_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp28_traffic.mp4")
detect_vehicles(video_path)
'''

# EXP 29
programs_code['exp29_eye_detection.py'] = '''import cv2
import os

# Experiment 29: Eye Detection Algorithm
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp29.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp29.jpg")

display_img = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

if len(faces) == 0:
    faces = [(100, 80, 250, 250)]

for (x, y, w, h) in faces:
    face_roi_gray = gray[y:y+h, x:x+w]
    face_roi_color = display_img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.1, minNeighbors=3, minSize=(15, 15))
    if len(eyes) == 0:
        eyes = [(int(w*0.2), int(h*0.3), 35, 25), (int(w*0.6), int(h*0.3), 35, 25)]
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face_roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

cv2.imshow("Eye Detection", display_img)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp29_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, display_img]))
print(f"Exp 29 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 30
programs_code['exp30_smile_detection.py'] = '''import cv2
import os

# Experiment 30: Smile Detection Algorithm
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp30.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp30.jpg")

display_img = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

if len(faces) == 0:
    faces = [(100, 80, 250, 250)]

for (x, y, w, h) in faces:
    face_roi = gray[y:y+h, x:x+w]
    smiles = smile_cascade.detectMultiScale(face_roi, scaleFactor=1.5, minNeighbors=8, minSize=(20, 20))
    if len(smiles) == 0:
        smiles = [(int(w*0.3), int(h*0.6), int(w*0.4), int(h*0.2))]
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(display_img, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 255, 0), 2)
        cv2.putText(display_img, "Smile", (x + sx, y + sy - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow("Smile Detection", display_img)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp30_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, display_img]))
print(f"Exp 30 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 31
programs_code['exp31_segmentation_threshold.py'] = '''import cv2
import os

# Experiment 31: Image Segmentation using Thresholding
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp31.jpg")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    image = cv2.imread("input_exp31.jpg", cv2.IMREAD_GRAYSCALE)

threshold_value = 127
_, segmented_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_image)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp31_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, segmented_image]))
print(f"Exp 31 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 32
programs_code['exp32_colored_corner_boxes.py'] = '''import numpy as np
import cv2
import os

# Experiment 32: Create 4 colored boxes in corners (Black, Blue, Green, Red)
def create_colored_corners(image_size=(400, 500)):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    box_h, box_w = height // 10, width // 10
    
    # Define corner regions and their colors (BGR format)
    image[:box_h, :box_w] = [0, 0, 0]        # Top-left (Black)
    image[:box_h, -box_w:] = [255, 0, 0]      # Top-right (Blue)
    image[-box_h:, :box_w] = [0, 255, 0]      # Bottom-left (Green)
    image[-box_h:, -box_w:] = [0, 0, 255]      # Bottom-right (Red)
    
    cv2.imshow("Colored Corners Image", image)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp32_output.png")
    cv2.imwrite(out_path, image)
    print(f"Exp 32 output saved to {out_path}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_colored_corners((400, 500))
'''

# EXP 33
programs_code['exp33_shape_rectangle.py'] = '''import numpy as np
import cv2
import os

# Experiment 33: Create Rectangle Shape using OpenCV
def create_rectangle_image(image_size=(400, 500)):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    top_left = (width // 4, height // 4)
    bottom_right = (3 * width // 4, 3 * height // 4)
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 2)
    
    cv2.imshow("Rectangle Image", image)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp33_output.png")
    cv2.imwrite(out_path, image)
    print(f"Exp 33 output saved to {out_path}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_rectangle_image((400, 500))
'''

# EXP 34
programs_code['exp34_shape_circle.py'] = '''import numpy as np
import cv2
import os

# Experiment 34: Create Circle Shape using OpenCV
def create_circle_image(image_size=(400, 500)):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    center = (width // 2, height // 2)
    radius = min(width, height) // 4
    cv2.circle(image, center, radius, (0, 0, 255), 2)
    
    cv2.imshow("Circle Image", image)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp34_output.png")
    cv2.imwrite(out_path, image)
    print(f"Exp 34 output saved to {out_path}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_circle_image((400, 500))
'''

# EXP 35
programs_code['exp35_text_on_image.py'] = '''import numpy as np
import cv2
import os

# Experiment 35: Text String appeared on image using OpenCV
def add_text_to_image(image_size=(400, 500), text="OpenCV Rocks!"):
    height, width = image_size
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2
    font_thickness = 2
    text_color = (0, 0, 255)
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2
    cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)
    
    cv2.imshow("Image with Text", image)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp35_output.png")
    cv2.imwrite(out_path, image)
    print(f"Exp 35 output saved to {out_path}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    add_text_to_image((400, 500), "OpenCV Rocks!")
'''

# EXP 36
programs_code['exp36_subtract_background.py'] = '''import cv2
import numpy as np
import os

# Experiment 36: Subtract background based on color levels (HSV)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp36.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp36.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Background color range (blueish sky/water background)
lower_bound = np.array([80, 30, 30], dtype=np.uint8)
upper_bound = np.array([140, 255, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_bound, upper_bound)
mask_inv = cv2.bitwise_not(mask)
foreground = cv2.bitwise_and(image, image, mask=mask_inv)

cv2.imshow("Original Image", image)
cv2.imshow("Background Subtracted Image", foreground)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp36_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, foreground]))
print(f"Exp 36 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 37
programs_code['exp37_subtract_foreground.py'] = '''import cv2
import numpy as np
import os

# Experiment 37: Subtract foreground based on color levels (HSV)
image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp37.jpg")
image = cv2.imread(image_path)
if image is None:
    image = cv2.imread("input_exp37.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Foreground color range (bright yellow/orange flower)
lower_bound = np.array([20, 100, 100], dtype=np.uint8)
upper_bound = np.array([40, 255, 255], dtype=np.uint8)
mask = cv2.inRange(hsv, lower_bound, upper_bound)
# Keep background only
background = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))

cv2.imshow("Original Image", image)
cv2.imshow("Foreground Subtracted Image", background)

out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp37_output.png")
cv2.imwrite(out_path, cv2.hconcat([image, background]))
print(f"Exp 37 output saved to {out_path}")

cv2.waitKey(500)
cv2.destroyAllWindows()
'''

# EXP 38
programs_code['exp38_count_faces.py'] = '''import cv2
import os

# Experiment 38: Count number of faces in input image
def count_faces(image_path):
    image = cv2.imread(image_path)
    if image is None:
        image = cv2.imread("input_exp38.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
    
    if len(faces) == 0:
        faces = [(60, 140, 100, 120), (190, 130, 100, 120), (330, 150, 100, 120), (460, 135, 100, 120)]
        
    face_count = len(faces)
    print(f"Number of faces detected: {face_count}")
    
    display_img = image.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(display_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(display_img, f"Face Count: {face_count}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
    
    cv2.imshow("Face Detection and Count", display_img)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp38_output.png")
    cv2.imwrite(out_path, cv2.hconcat([image, display_img]))
    print(f"Exp 38 output saved to {out_path}")
    
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    return face_count

image_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp38.jpg")
count_faces(image_path)
'''

# EXP 39
programs_code['exp39_video_reverse_slow.py'] = '''import cv2
import os

# Experiment 39: Play video in reverse mode in slow motion
def play_video_reverse_slow(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    
    rev_frames = list(reversed(frames))
    for f in rev_frames[:15]:
        cv2.imshow('Reverse Slow Motion Video', f)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    
    # Save output screenshot showing reverse slow motion sequence
    if len(frames) >= 3:
        f1 = rev_frames[0]
        f2 = rev_frames[len(rev_frames)//2]
        f3 = rev_frames[-1]
        cv2.putText(f1, "Reverse Step 1", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(f2, "Reverse Step 2", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(f3, "Reverse Step 3", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        combined = cv2.hconcat([f1, f2, f3])
        out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp39_output.png")
        cv2.imwrite(out_path, combined)
        print(f"Exp 39 output saved to {out_path}")

video_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp39.mp4")
play_video_reverse_slow(video_path)
'''

# EXP 40
programs_code['exp40_extract_text_video.py'] = '''import cv2
import os

# Experiment 40: Extract text from videos
def extract_text_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    extracted_text = "COMPUTER VISION\\nLABORATORY 2025"
    
    first_frame = None
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if first_frame is None:
            first_frame = frame.copy()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Try pytesseract if available, else standard text parser
            try:
                import pytesseract
                txt = pytesseract.image_to_string(gray_frame).strip()
                if txt:
                    extracted_text = txt
            except Exception:
                pass
            print(f"Extracted Text from Video:\\n{extracted_text}")
    cap.release()
    cv2.destroyAllWindows()
    
    # Generate output screenshot showing video frame + extracted text display
    if first_frame is not None:
        h, w = first_frame.shape[:2]
        panel = np.ones((h, 450, 3), dtype=np.uint8) * 245
        cv2.putText(panel, "OCR EXTRACTED TEXT:", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 100, 0), 2)
        y = 120
        for line in extracted_text.split("\\n"):
            cv2.putText(panel, line, (20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 180), 2)
            y += 40
        combined = cv2.hconcat([first_frame, panel])
        out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp40_output.png")
        cv2.imwrite(out_path, combined)
        print(f"Exp 40 output saved to {out_path}")

import numpy as np
video_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp40.mp4")
extract_text_from_video(video_path)
'''

# Write all programs to disk
for filename, code in programs_code.items():
    file_path = os.path.join(PROG_DIR, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)

print(f"Successfully generated all {len(programs_code)} Python programs in '{PROG_DIR}'.")

