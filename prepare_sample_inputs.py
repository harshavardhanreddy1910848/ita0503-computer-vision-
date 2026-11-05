import os
import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import shutil

INPUT_DIR = os.path.abspath('sample_inputs')
PROG_DIR = os.path.abspath('programs')
OUT_DIR = os.path.abspath('output_screenshots')

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(PROG_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# STEP 1: PREPARE ALL 40 UNIQUE INPUTS
# -------------------------------------------------------------
print("Preparing unique inputs for all 40 experiments...")

# 1. Grayscale input
img1 = np.zeros((400, 600, 3), dtype=np.uint8)
for i in range(400):
    img1[i, :] = [int(120 + 80 * np.sin(i / 30.0)), int(140 + 60 * np.cos(i / 40.0)), 220]
cv2.circle(img1, (300, 200), 80, (40, 180, 240), -1)
cv2.rectangle(img1, (100, 250), (220, 380), (80, 120, 60), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp01.jpg'), img1)

# 2. Gaussian Blur input
img2 = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.rectangle(img2, (0, 0), (600, 400), (230, 240, 245), -1)
for x in range(50, 550, 40):
    cv2.line(img2, (x, 50), (x, 350), (20, 20, 180), 3)
    cv2.circle(img2, (x, 200), 15, (0, 140, 0), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp02.jpg'), img2)

# 3. Canny input
img3 = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.putText(img3, "EDGE DETECT", (80, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 4)
cv2.rectangle(img3, (60, 60), (540, 340), (0, 255, 255), 3)
cv2.circle(img3, (450, 250), 60, (200, 100, 255), 4)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp03.jpg'), img3)

# 4. Histogram Equalization input (low-contrast dark image)
img4 = np.full((400, 600), 90, dtype=np.uint8)
for r in range(400):
    for c in range(600):
        img4[r, c] = int(85 + 25 * np.sin(r/20) * np.cos(c/20))
cv2.circle(img4, (300, 200), 70, 115, -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp04.jpg'), img4)

# 5. Color Histogram input (rich 3-channel distribution)
img5 = np.zeros((400, 600, 3), dtype=np.uint8)
img5[:, :200] = [220, 50, 50]    # Blueish
img5[:, 200:400] = [40, 200, 40] # Greenish
img5[:, 400:] = [30, 30, 230]    # Reddish
cv2.circle(img5, (300, 200), 100, (200, 240, 50), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp05.jpg'), img5)

# 6. Erode function input
img6 = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.putText(img6, "EROSION", (100, 220), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 8)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp06.jpg'), img6)

# 7. Video slow/fast motion
vid7_path = os.path.join(INPUT_DIR, 'input_exp07.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
vw7 = cv2.VideoWriter(vid7_path, fourcc, 20.0, (400, 300))
for f in range(40):
    f_img = np.zeros((300, 400, 3), dtype=np.uint8)
    cx = int(50 + f * 7.5)
    cy = int(150 + 60 * np.sin(f / 3.0))
    cv2.circle(f_img, (cx, cy), 25, (0, 220, 255), -1)
    cv2.putText(f_img, f"Frame {f+1}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    vw7.write(f_img)
vw7.release()

# 8. Dilate function input (thin lines/dots)
img8 = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.putText(img8, "DILATE", (120, 220), cv2.FONT_HERSHEY_SIMPLEX, 2.2, (255, 255, 255), 2)
for pt in [(100, 80), (250, 90), (450, 100), (200, 320), (400, 310)]:
    cv2.circle(img8, pt, 3, (255, 255, 255), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp08.jpg'), img8)

# 9. Image scaling input
img9 = np.zeros((300, 400, 3), dtype=np.uint8)
cv2.rectangle(img9, (0, 0), (400, 300), (180, 200, 160), -1)
cv2.rectangle(img9, (80, 60), (320, 240), (40, 60, 220), -1)
cv2.circle(img9, (200, 150), 50, (255, 255, 255), -1)
cv2.putText(img9, "SCALE", (140, 160), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 2)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp09.jpg'), img9)

# 10. 90-degree rotation input
img10 = np.zeros((400, 500, 3), dtype=np.uint8)
cv2.rectangle(img10, (0, 0), (500, 400), (240, 230, 210), -1)
cv2.arrowedLine(img10, (100, 200), (400, 200), (0, 0, 220), 8, tipLength=0.2)
cv2.putText(img10, "UP", (220, 140), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 120, 0), 3)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp10.jpg'), img10)

# 11. 180-degree rotation input
img11 = np.zeros((400, 500, 3), dtype=np.uint8)
cv2.rectangle(img11, (0, 0), (500, 200), (240, 180, 100), -1) # Sky
cv2.rectangle(img11, (0, 200), (500, 400), (100, 200, 100), -1) # Ground
cv2.circle(img11, (380, 100), 40, (0, 240, 255), -1) # Sun
cv2.rectangle(img11, (120, 160), (200, 280), (50, 50, 180), -1) # House
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp11.jpg'), img11)

# 12. 270-degree rotation input
img12 = np.zeros((400, 500, 3), dtype=np.uint8)
cv2.rectangle(img12, (0, 0), (500, 400), (190, 190, 240), -1)
cv2.putText(img12, "TOP-LEFT", (40, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (180, 0, 0), 3)
cv2.rectangle(img12, (200, 150), (450, 350), (0, 140, 140), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp12.jpg'), img12)

# 13. Affine transformation input
img13 = np.zeros((400, 500, 3), dtype=np.uint8)
for i in range(0, 500, 50):
    cv2.line(img13, (i, 0), (i, 400), (80, 80, 80), 1)
for j in range(0, 400, 50):
    cv2.line(img13, (0, j), (500, j), (80, 80, 80), 1)
cv2.rectangle(img13, (100, 100), (300, 250), (0, 200, 255), -1)
cv2.circle(img13, (380, 280), 40, (255, 100, 100), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp13.jpg'), img13)

# 14. Perspective transformation input
img14 = np.zeros((500, 500, 3), dtype=np.uint8)
pts = np.array([[120, 80], [380, 60], [440, 420], [80, 380]], np.int32)
cv2.fillPoly(img14, [pts], (220, 220, 220))
cv2.polylines(img14, [pts], True, (0, 0, 255), 3)
cv2.putText(img14, "CARD", (190, 240), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (20, 20, 20), 3)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp14.jpg'), img14)

# 15. Harris Corner detection input (checkerboard/geometric corners)
img15 = np.zeros((400, 400, 3), dtype=np.uint8)
for r in range(8):
    for c in range(8):
        if (r + c) % 2 == 0:
            cv2.rectangle(img15, (c*50, r*50), ((c+1)*50, (r+1)*50), (255, 255, 255), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp15.jpg'), img15)

# 16. Sobel algorithm input
img16 = np.zeros((400, 500, 3), dtype=np.uint8)
cv2.rectangle(img16, (80, 80), (420, 320), (180, 180, 180), -1)
cv2.circle(img16, (250, 200), 70, (255, 255, 255), -1)
cv2.line(img16, (50, 350), (450, 50), (0, 0, 255), 5)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp16.jpg'), img16)

# 17. Watermark insertion input
img17 = np.zeros((400, 600, 3), dtype=np.uint8)
for y in range(400):
    img17[y, :] = [int(180 - y*0.2), int(210 - y*0.3), int(250 - y*0.4)]
cv2.circle(img17, (480, 100), 50, (255, 255, 220), -1)
cv2.rectangle(img17, (0, 280), (600, 400), (30, 140, 60), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp17.jpg'), img17)

# 18. ROI cropping, copying and pasting input
img18 = np.zeros((400, 600, 3), dtype=np.uint8)
cv2.rectangle(img18, (0, 0), (600, 400), (220, 230, 235), -1)
# Draw distinct target object at top-left
cv2.rectangle(img18, (50, 50), (180, 180), (240, 120, 50), -1)
cv2.circle(img18, (115, 115), 35, (50, 220, 240), -1)
cv2.putText(img18, "ROI", (80, 125), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp18.jpg'), img18)

# 19. Erosion morphological operation input
img19 = np.zeros((350, 500, 3), dtype=np.uint8)
cv2.putText(img19, "OPENCV", (60, 200), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 8)
cv2.circle(img19, (420, 180), 40, (255, 255, 255), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp19.jpg'), img19)

# 20. Dilation morphological operation input
img20 = np.zeros((350, 500, 3), dtype=np.uint8)
cv2.putText(img20, "VISION", (80, 200), cv2.FONT_HERSHEY_SIMPLEX, 2.2, (255, 255, 255), 2)
cv2.rectangle(img20, (50, 50), (450, 300), (255, 255, 255), 2)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp20.jpg'), img20)

# 21. Opening morphological operation input (circles with salt noise)
img21 = np.zeros((350, 500), dtype=np.uint8)
cv2.circle(img21, (150, 175), 60, 255, -1)
cv2.circle(img21, (350, 175), 60, 255, -1)
# Add salt noise (small dots)
np.random.seed(42)
noise_pts = np.random.randint(0, 350, (150, 2))
for y, x in noise_pts:
    img21[y, min(x, 499)] = 255
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp21.jpg'), img21)

# 22. Closing morphological operation input (circles with pepper holes)
img22 = np.zeros((350, 500), dtype=np.uint8)
cv2.circle(img22, (150, 175), 70, 255, -1)
cv2.circle(img22, (350, 175), 70, 255, -1)
# Add pepper noise (small black holes inside)
for pt in [(130, 160), (160, 180), (140, 195), (340, 160), (360, 180), (330, 170)]:
    cv2.circle(img22, pt, 4, 0, -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp22.jpg'), img22)

# 23. Top Hat input (bright spots on non-uniform gradient background)
img23 = np.zeros((350, 500), dtype=np.uint8)
for c in range(500):
    img23[:, c] = int(30 + 100 * (c / 500.0))
# Add small bright spots
for pt in [(100, 100), (250, 150), (400, 200), (150, 260), (320, 280)]:
    cv2.circle(img23, pt, 8, 255, -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp23.jpg'), img23)

# 24. Black Hat input (dark spots on bright background)
img24 = np.full((350, 500), 200, dtype=np.uint8)
for c in range(500):
    img24[:, c] = int(220 - 80 * (c / 500.0))
# Add small dark spots
for pt in [(100, 120), (220, 160), (380, 140), (180, 250), (340, 270)]:
    cv2.circle(img24, pt, 8, 30, -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp24.jpg'), img24)

# 25. Watch recognition input
img25 = np.zeros((400, 500, 3), dtype=np.uint8)
cv2.rectangle(img25, (0, 0), (500, 400), (220, 215, 205), -1) # Desk
# Draw watch strap
cv2.rectangle(img25, (220, 40), (280, 360), (40, 40, 40), -1)
# Draw watch dial
cv2.circle(img25, (250, 200), 65, (200, 200, 200), -1)
cv2.circle(img25, (250, 200), 60, (255, 255, 255), -1)
# Draw dial hour marks & hands
for ang in range(0, 360, 30):
    rad = np.deg2rad(ang)
    x1 = int(250 + 50 * np.cos(rad))
    y1 = int(200 + 50 * np.sin(rad))
    x2 = int(250 + 58 * np.cos(rad))
    y2 = int(200 + 58 * np.sin(rad))
    cv2.line(img25, (x1, y1), (x2, y2), (20, 20, 20), 2)
# Hour and minute hands
cv2.line(img25, (250, 200), (250, 160), (20, 20, 20), 3)
cv2.line(img25, (250, 200), (280, 200), (20, 20, 20), 2)
cv2.circle(img25, (250, 200), 4, (0, 0, 200), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp25.jpg'), img25)

# 26. Video reverse input
vid26_path = os.path.join(INPUT_DIR, 'input_exp26.mp4')
vw26 = cv2.VideoWriter(vid26_path, fourcc, 15.0, (400, 300))
for f in range(30):
    f_img = np.zeros((300, 400, 3), dtype=np.uint8)
    cv2.rectangle(f_img, (0, 0), (400, 300), (60, 50, 40), -1)
    y_pos = int(50 + f * 7)
    cv2.circle(f_img, (200, y_pos), 20, (0, 255, 120), -1)
    cv2.putText(f_img, f"Frame {f+1}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    vw26.write(f_img)
vw26.release()

# 27. Face detection input (realistic human face portrait with eyes/smile features)
def draw_face(canvas, cx, cy, scale=1.0):
    # Skin tone
    skin = (170, 200, 235)
    r = int(55 * scale)
    cv2.ellipse(canvas, (cx, cy), (int(r*0.85), r), 0, 0, 360, skin, -1)
    # Hair
    cv2.ellipse(canvas, (cx, cy - int(r*0.5)), (int(r*0.9), int(r*0.6)), 0, 180, 360, (30, 30, 40), -1)
    # Eyebrows
    cv2.line(canvas, (cx - int(25*scale), cy - int(20*scale)), (cx - int(8*scale), cy - int(22*scale)), (30, 30, 40), 2)
    cv2.line(canvas, (cx + int(8*scale), cy - int(22*scale)), (cx + int(25*scale), cy - int(20*scale)), (30, 30, 40), 2)
    # Eyes
    cv2.circle(canvas, (cx - int(16*scale), cy - int(10*scale)), int(5*scale), (255, 255, 255), -1)
    cv2.circle(canvas, (cx - int(16*scale), cy - int(10*scale)), int(3*scale), (40, 30, 20), -1)
    cv2.circle(canvas, (cx + int(16*scale), cy - int(10*scale)), int(5*scale), (255, 255, 255), -1)
    cv2.circle(canvas, (cx + int(16*scale), cy - int(10*scale)), int(3*scale), (40, 30, 20), -1)
    # Nose
    cv2.line(canvas, (cx, cy - int(5*scale)), (cx - int(3*scale), cy + int(10*scale)), (140, 170, 200), 2)
    cv2.line(canvas, (cx - int(3*scale), cy + int(10*scale)), (cx + int(3*scale), cy + int(10*scale)), (140, 170, 200), 2)
    # Smile / Mouth
    cv2.ellipse(canvas, (cx, cy + int(22*scale)), (int(16*scale), int(8*scale)), 0, 0, 180, (50, 50, 180), 2)

img27 = np.zeros((450, 450, 3), dtype=np.uint8)
cv2.rectangle(img27, (0, 0), (450, 450), (220, 220, 225), -1)
# If lena or downloaded face exists, we use authentic image
if os.path.exists('sample_inputs/sample_exp27.jpg'):
    img27 = cv2.imread('sample_inputs/sample_exp27.jpg')
else:
    draw_face(img27, 225, 220, scale=1.8)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp27.jpg'), img27)

# 28. Vehicle detection video (Car traffic video!)
# We downloaded traffic_video.mp4 earlier; let's copy it or link it
if os.path.exists('traffic_video.mp4'):
    shutil.copy('traffic_video.mp4', os.path.join(INPUT_DIR, 'input_exp28_traffic.mp4'))
    print("Copied authentic traffic_video.mp4 for Exp 28 vehicle detection.")
else:
    # Create traffic video with moving cars
    vid28_path = os.path.join(INPUT_DIR, 'input_exp28_traffic.mp4')
    vw28 = cv2.VideoWriter(vid28_path, fourcc, 20.0, (640, 360))
    for f in range(60):
        f_img = np.zeros((360, 640, 3), dtype=np.uint8)
        # Road
        cv2.rectangle(f_img, (0, 100), (640, 360), (70, 70, 70), -1)
        # Road lane lines
        for lx in range(0, 640, 60):
            cv2.line(f_img, (lx, 230), (lx+30, 230), (255, 255, 255), 3)
        # Car 1 moving right
        c1x = int((f * 8) % 700) - 60
        cv2.rectangle(f_img, (c1x, 140), (c1x+100, 190), (0, 0, 200), -1)
        cv2.rectangle(f_img, (c1x+20, 120), (c1x+70, 140), (0, 0, 160), -1)
        cv2.circle(f_img, (c1x+25, 190), 12, (20, 20, 20), -1)
        cv2.circle(f_img, (c1x+75, 190), 12, (20, 20, 20), -1)
        # Car 2 moving right (lane 2)
        c2x = int((f * 12 + 200) % 700) - 60
        cv2.rectangle(f_img, (c2x, 260), (c2x+110, 315), (200, 150, 0), -1)
        cv2.rectangle(f_img, (c2x+25, 240), (c2x+80, 260), (160, 120, 0), -1)
        cv2.circle(f_img, (c2x+30, 315), 14, (20, 20, 20), -1)
        cv2.circle(f_img, (c2x+85, 315), 14, (20, 20, 20), -1)
        vw28.write(f_img)
    vw28.release()

# 29. Eye detection input (Clear face portrait showing eyes)
if os.path.exists('sample_inputs/sample_exp29.jpg'):
    img29 = cv2.imread('sample_inputs/sample_exp29.jpg')
else:
    img29 = np.zeros((450, 450, 3), dtype=np.uint8)
    cv2.rectangle(img29, (0, 0), (450, 450), (230, 230, 230), -1)
    draw_face(img29, 225, 220, scale=1.8)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp29.jpg'), img29)

# 30. Smile detection input (Portrait of smiling face)
if os.path.exists('sample_inputs/sample_exp30.jpg'):
    img30 = cv2.imread('sample_inputs/sample_exp30.jpg')
else:
    img30 = np.zeros((450, 450, 3), dtype=np.uint8)
    cv2.rectangle(img30, (0, 0), (450, 450), (235, 230, 225), -1)
    draw_face(img30, 225, 215, scale=1.8)
    # Bright smiling mouth with visible teeth
    cv2.ellipse(img30, (225, 255), (32, 16), 0, 0, 180, (255, 255, 255), -1)
    cv2.ellipse(img30, (225, 255), (32, 16), 0, 0, 180, (40, 40, 180), 2)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp30.jpg'), img30)

# 31. Image segmentation input (distinct fruit / coin foreground on light background)
img31 = np.full((400, 500, 3), 210, dtype=np.uint8)
# Add some dark foreground objects
cv2.circle(img31, (180, 200), 70, (40, 50, 180), -1)
cv2.rectangle(img31, (300, 140), (420, 260), (30, 120, 40), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp31.jpg'), img31)

# 32 to 35 are generated dynamically or take dimensions/parameters in the code!
# Let's also provide default sample config inputs for them.

# 36. Background subtraction input based on color levels (e.g. object with dark background or specific color)
img36 = np.zeros((400, 500, 3), dtype=np.uint8)
# Background: blueish gradient
for r in range(400):
    img36[r, :] = [180, 80, 40]
# Foreground: Bright red/orange object
cv2.circle(img36, (250, 200), 80, (20, 40, 230), -1)
cv2.rectangle(img36, (220, 160), (280, 240), (255, 255, 255), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp36.jpg'), img36)

# 37. Foreground subtraction input
img37 = np.zeros((400, 500, 3), dtype=np.uint8)
# Background: Nature green
img37[:, :] = [50, 160, 50]
# Foreground: Bright yellow flower
cv2.circle(img37, (250, 200), 75, (30, 220, 240), -1)
cv2.circle(img37, (250, 200), 25, (10, 80, 150), -1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp37.jpg'), img37)

# 38. Count faces input (Group with multiple faces)
img38 = np.zeros((400, 650, 3), dtype=np.uint8)
cv2.rectangle(img38, (0, 0), (650, 400), (220, 220, 220), -1)
# Draw 4 distinct faces
draw_face(img38, 110, 200, scale=1.1)
draw_face(img38, 240, 190, scale=1.15)
draw_face(img38, 380, 210, scale=1.05)
draw_face(img38, 510, 195, scale=1.1)
cv2.imwrite(os.path.join(INPUT_DIR, 'input_exp38.jpg'), img38)

# 39. Reverse video in slow motion input
vid39_path = os.path.join(INPUT_DIR, 'input_exp39.mp4')
vw39 = cv2.VideoWriter(vid39_path, fourcc, 20.0, (400, 300))
for f in range(35):
    f_img = np.zeros((300, 400, 3), dtype=np.uint8)
    cv2.rectangle(f_img, (0, 0), (400, 300), (40, 40, 60), -1)
    x = int(50 + f * 9)
    y = int(220 - 140 * np.sin(f * np.pi / 34))
    cv2.circle(f_img, (x, y), 22, (0, 200, 255), -1)
    cv2.putText(f_img, f"Slow Motion Frame {f+1}", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    vw39.write(f_img)
vw39.release()

# 40. Video with text to extract
vid40_path = os.path.join(INPUT_DIR, 'input_exp40.mp4')
vw40 = cv2.VideoWriter(vid40_path, fourcc, 15.0, (500, 300))
for f in range(25):
    f_img = np.zeros((300, 500, 3), dtype=np.uint8)
    cv2.rectangle(f_img, (0, 0), (500, 300), (240, 240, 240), -1)
    cv2.putText(f_img, "COMPUTER VISION", (60, 130), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3)
    cv2.putText(f_img, "LABORATORY 2025", (70, 190), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (180, 0, 0), 3)
    vw40.write(f_img)
vw40.release()

print("All 40 distinct sample inputs ready!")

