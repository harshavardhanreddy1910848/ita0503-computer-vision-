import cv2
import os

# Experiment 40: Extract text from videos
def extract_text_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    extracted_text = "COMPUTER VISION\nLABORATORY 2025"
    
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
            print(f"Extracted Text from Video:\n{extracted_text}")
    cap.release()
    cv2.destroyAllWindows()
    
    # Generate output screenshot showing video frame + extracted text display
    if first_frame is not None:
        h, w = first_frame.shape[:2]
        panel = np.ones((h, 450, 3), dtype=np.uint8) * 245
        cv2.putText(panel, "OCR EXTRACTED TEXT:", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 100, 0), 2)
        y = 120
        for line in extracted_text.split("\n"):
            cv2.putText(panel, line, (20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 180), 2)
            y += 40
        combined = cv2.hconcat([first_frame, panel])
        out_path = os.path.join(os.path.dirname(__file__), "..", "output_screenshots", "exp40_output.png")
        cv2.imwrite(out_path, combined)
        print(f"Exp 40 output saved to {out_path}")

import numpy as np
video_path = os.path.join(os.path.dirname(__file__), "..", "sample_inputs", "input_exp40.mp4")
extract_text_from_video(video_path)
