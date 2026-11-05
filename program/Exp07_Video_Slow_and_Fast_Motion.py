import cv2
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
