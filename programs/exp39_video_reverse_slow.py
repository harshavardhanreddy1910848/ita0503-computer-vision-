import cv2
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
