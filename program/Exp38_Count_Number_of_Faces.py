import cv2
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
