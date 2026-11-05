import cv2
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
