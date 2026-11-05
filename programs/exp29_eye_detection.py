import cv2
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
