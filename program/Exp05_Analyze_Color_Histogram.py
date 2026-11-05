import cv2
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
