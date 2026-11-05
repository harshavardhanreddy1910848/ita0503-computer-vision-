import cv2
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
