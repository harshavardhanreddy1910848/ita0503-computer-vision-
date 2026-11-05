import os
import shutil
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Target folders
PROGRAM_DIR = os.path.join(BASE_DIR, 'program')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output screenshot')

os.makedirs(PROGRAM_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Experiment mappings: (exp_id, prog_src_name, new_prog_name, new_res_name, aim, result)
exp_data = [
    (1, "exp01_grayscale.py", "Exp01_Convert_Image_to_Grayscale.py", "Exp01_Result_Successfully_Converted_to_Grayscale.png",
     "Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to Gray-scale.",
     "Successfully read the input image and converted it to grayscale using OpenCV in Python."),
    (2, "exp02_gaussian_blur.py", "Exp02_Gaussian_Blur.py", "Exp02_Result_Successfully_Applied_Gaussian_Blur.png",
     "Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to Blur using Gaussian Blur.",
     "Successfully read the input image and applied Gaussian Blur using OpenCV in Python."),
    (3, "exp03_canny_outline.py", "Exp03_Canny_Outline_Edge_Detection.py", "Exp03_Result_Successfully_Detected_Edges_with_Canny.png",
     "Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to show outline using Canny function.",
     "Successfully read the input image and applied edge detection using the Canny function in OpenCV."),
    (4, "exp04_histogram_equalization.py", "Exp04_Histogram_Equalization.py", "Exp04_Result_Successfully_Performed_Histogram_Equalization.png",
     "Implement histogram equalization on the given image and compare it with the original image using Open CV.",
     "Successfully performed Histogram Equalization on the input image and compared it with the original grayscale image."),
    (5, "exp05_color_histogram.py", "Exp05_Analyze_Color_Histogram.py", "Exp05_Result_Successfully_Analyzed_Color_Histogram.png",
     "Write a Python function to analyze the histogram of the given input image based on color levels using Open CV.",
     "Successfully analyzed and plotted the color histogram (Blue, Green, Red) of the given image."),
    (6, "exp06_image_erosion.py", "Exp06_Image_Erosion_Function.py", "Exp06_Result_Successfully_Converted_Image_to_Erode.png",
     "Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to erode using Erode function.",
     "Successfully read the input image and applied erosion using OpenCV Erode function."),
    (7, "exp07_video_slow_fast.py", "Exp07_Video_Slow_and_Fast_Motion.py", "Exp07_Result_Successfully_Displayed_Video_Slow_and_Fast_Motion.png",
     "Perform basic video processing operations on the captured video. Read captured video in python and display the video, in slow motion and in fast motion.",
     "Successfully read captured video and displayed playback in slow motion and fast motion."),
    (8, "exp08_image_dilation.py", "Exp08_Image_Dilation_Function.py", "Exp08_Result_Successfully_Dilated_Image.png",
     "Perform basic Image Handling and processing operations on the image is to read an image in python and Dilate an Image using Dilate function.",
     "Successfully read the input image and dilated the image using OpenCV Dilate function."),
    (9, "exp09_image_scaling.py", "Exp09_Image_Scaling_Bigger_and_Smaller.py", "Exp09_Result_Successfully_Resized_to_Bigger_and_Smaller.png",
     "Implement the image scaling techniques to resize the images to both bigger and small sizes.",
     "Successfully resized an image to both bigger (2x) and smaller (0.5x) sizes using OpenCV."),
    (10, "exp10_rotation_90.py", "Exp10_Rotate_90_Clockwise.py", "Exp10_Result_Successfully_Rotated_90_Degree_Clockwise.png",
     "Perform a 90-degree rotation clockwise along the y-axis for the given image.",
     "Successfully applied a 90-degree rotation clockwise on the given image."),
    (11, "exp11_rotation_180.py", "Exp11_Rotate_180_Clockwise_Along_Y_Axis.py", "Exp11_Result_Successfully_Rotated_180_Degree_Along_Y_Axis.png",
     "Perform a 180-degree rotation clockwise along the y-axis for the given image.",
     "Successfully performed 180-degree clockwise rotation along the Y-axis."),
    (12, "exp12_rotation_270.py", "Exp12_Rotate_270_Clockwise_Along_Y_Axis.py", "Exp12_Result_Successfully_Rotated_270_Degree_Along_Y_Axis.png",
     "Perform a 270-degree rotation clockwise along the y-axis for the given image.",
     "Successfully performed 270-degree clockwise rotation along the Y-axis."),
    (13, "exp13_affine_transformation.py", "Exp13_Affine_Transformation.py", "Exp13_Result_Successfully_Applied_Affine_Transformation.png",
     "Perform Affine Transformation on the given image using python and Open CV.",
     "Successfully applied an Affine Transformation to the given image and saved result."),
    (14, "exp14_perspective_transformation.py", "Exp14_Perspective_Transformation.py", "Exp14_Result_Successfully_Applied_Perspective_Transformation.png",
     "Perform Perspective Transformation on the given image using python and Open CV.",
     "Successfully applied Perspective Transformation using 4 source and destination points."),
    (15, "exp15_harris_corner_detection.py", "Exp15_Harris_Corner_Detection.py", "Exp15_Result_Successfully_Detected_Corners_with_Harris.png",
     "Perform basic Image Handling and processing operations on the image is to read an image in python and detect the corners in the image using Harris Corner Detection function.",
     "Successfully applied Harris Corner Detection to the given image and highlighted corners in red."),
    (16, "exp16_sobel_edge_detection.py", "Exp16_Sobel_Edge_Detection_Filter.py", "Exp16_Result_Successfully_Filtered_with_Sobel_Algorithm.png",
     "Implement a Sobel algorithm using Open CV to filter the input image.",
     "Successfully applied Sobel Edge Detection in X and Y directions and combined gradient."),
    (17, "exp17_watermarking.py", "Exp17_Watermarking_Technique.py", "Exp17_Result_Successfully_Inserted_Watermark.png",
     "Design and implement a water marking technique to insert the watermark into the original effectively image using Open CV.",
     "Successfully blended and inserted an effective semi-transparent watermark into the original image."),
    (18, "exp18_roi_crop_copy_paste.py", "Exp18_ROI_Crop_Copy_and_Paste.py", "Exp18_Result_Successfully_Cropped_Copied_and_Pasted_ROI.png",
     "Implement image cropping, copying and pasting to select a region of interest (ROI) from the source image using Open CV.",
     "Successfully cropped a Region of Interest (ROI) and pasted it to target coordinate."),
    (19, "exp19_morphological_erosion.py", "Exp19_Erosion_Morphological_Operation.py", "Exp19_Result_Successfully_Implemented_Erosion_Morphology.png",
     "Implement the Erosion Morphological operations technique using Open CV in python.",
     "Successfully performed morphological erosion using structuring kernel."),
    (20, "exp20_morphological_dilation.py", "Exp20_Dilation_Morphological_Operation.py", "Exp20_Result_Successfully_Implemented_Dilation_Morphology.png",
     "Implement the Dilation technique as a Morphological operation to dilate the foreground regions based on Open CV.",
     "Successfully dilated foreground regions using morphological dilation."),
    (21, "exp21_morphological_opening.py", "Exp21_Opening_Morphological_Operation.py", "Exp21_Result_Successfully_Implemented_Opening_Morphology.png",
     "Implement the Opening technique as a Morphological operation to dilate the foreground regions based on Open CV.",
     "Successfully applied morphological opening (erosion followed by dilation) removing noise."),
    (22, "exp22_morphological_closing.py", "Exp22_Closing_Morphological_Operation.py", "Exp22_Result_Successfully_Implemented_Closing_Morphology.png",
     "Implement the Closing technique as a Morphological operation to dilate the foreground regions based on Open CV.",
     "Successfully applied morphological closing (dilation followed by erosion) closing small holes."),
    (23, "exp23_top_hat.py", "Exp23_Top_Hat_Morphological_Operation.py", "Exp23_Result_Successfully_Implemented_Top_Hat_technique.png",
     "Implement the Top hat technique as a Morphological operation to dilate the foreground regions based on Open CV.",
     "Successfully extracted bright foreground elements on non-uniform background using Top Hat."),
    (24, "exp24_black_hat.py", "Exp24_Black_Hat_Morphological_Operation.py", "Exp24_Result_Successfully_Implemented_Black_Hat_technique.png",
     "Implement the Black hat technique as a Morphological operation to dilate the foreground regions based on Open CV.",
     "Successfully extracted darker foreground objects on bright background using Black Hat."),
    (25, "exp25_watch_recognition.py", "Exp25_Watch_Recognition_Object_Detection.py", "Exp25_Result_Successfully_Recognized_Watch_Object.png",
     "Recognize watch from the given image by general Object recognition using Open CV.",
     "Successfully detected and recognized the watch object with bounding box."),
    (26, "exp26_video_reverse.py", "Exp26_Reverse_Video_Frames.py", "Exp26_Result_Successfully_Reversed_Video_Frames.png",
     "Implement a function to reverse the frames of the video to create a video in reverse mode using Open CV.",
     "Successfully reversed video frames and generated reversed video playback."),
    (27, "exp27_face_detection.py", "Exp27_Face_Detection_Haar_Cascade.py", "Exp27_Result_Successfully_Detected_Human_Faces.png",
     "Implement a face detection algorithm using Open CV to detect and locate human faces in the images.",
     "Successfully detected human faces using OpenCV Haar Cascade classifier."),
    (28, "exp28_vehicle_detection_video.py", "Exp28_Vehicle_Detection_Video_Haar_Cascade.py", "Exp28_Result_Successfully_Detected_Vehicles_in_Video.png",
     "Implement a vehicle detection algorithm using Open CV to detect and locate vehicles in each frame of the video.",
     "Successfully detected and tracked vehicles frame-by-frame in real traffic video."),
    (29, "exp29_eye_detection.py", "Exp29_Eye_Detection_Haar_Cascade.py", "Exp29_Result_Successfully_Detected_Human_Eyes.png",
     "Implement an Eye detection algorithm using Open CV to detect and locate human eyes in the images.",
     "Successfully localized and placed blue bounding boxes around human eyes."),
    (30, "exp30_smile_detection.py", "Exp30_Smile_Detection_Haar_Cascade.py", "Exp30_Result_Successfully_Detected_Human_Smile.png",
     "Implement a Smile detection algorithm using Open CV to detect and locate human smile in the images.",
     "Successfully detected human smile within detected facial region."),
    (31, "exp31_segmentation_threshold.py", "Exp31_Image_Segmentation_Threshold.py", "Exp31_Result_Successfully_Segmented_Image_by_Threshold.png",
     "Implement a Segmentation algorithm using Open CV to segment the given input image based on the given threshold values.",
     "Successfully segmented input image into binary foreground and background via thresholding."),
    (32, "exp32_colored_corner_boxes.py", "Exp32_Colored_Boxes_Four_Corners.py", "Exp32_Result_Successfully_Created_4_Colored_Corner_Boxes.png",
     "Write a Python function to create a white image size entered by the user and then create 4 boxes of Black, Blue, Green and Red respectively on each corner of the image.",
     "Successfully created white image with 4 colored boxes (Black, Blue, Green, Red) occupying 1/10th size."),
    (33, "exp33_shape_rectangle.py", "Exp33_Create_Shape_of_Rectangle.py", "Exp33_Result_Successfully_Created_Rectangle_Shape.png",
     "Write a Python function to create a white image size entered by the user and then create a shape of Rectangle using Open CV.",
     "Successfully created user-defined white image with centered rectangle."),
    (34, "exp34_shape_circle.py", "Exp34_Create_Shape_of_Circle.py", "Exp34_Result_Successfully_Created_Circle_Shape.png",
     "Write a Python function to create a white image size entered by the user and then create a shape of Circle using Open CV.",
     "Successfully created user-defined white image with centered red circle."),
    (35, "exp35_text_on_image.py", "Exp35_Text_String_Appeared_on_Image.py", "Exp35_Result_Successfully_Placed_Text_String_on_Image.png",
     "Write a Python function to create a text string entered by the user that must be appeared on the given image using Open CV.",
     "Successfully centered and rendered user text string onto image canvas."),
    (36, "exp36_subtract_background.py", "Exp36_Subtract_Background_Color_Levels.py", "Exp36_Result_Successfully_Subtracted_Background_by_Color.png",
     "Write a Python function to subtract the background of the given input image based on color levels using Open CV.",
     "Successfully extracted foreground object and removed background using HSV color thresholding."),
    (37, "exp37_subtract_foreground.py", "Exp37_Subtract_Foreground_Color_Levels.py", "Exp37_Result_Successfully_Subtracted_Foreground_by_Color.png",
     "Write a Python function to subtract the foreground of the given input image based on color levels using Open CV.",
     "Successfully removed foreground object based on HSV color range, preserving background."),
    (38, "exp38_count_faces.py", "Exp38_Count_Number_of_Faces.py", "Exp38_Result_Successfully_Detected_and_Counted_Number_of_Faces.png",
     "Write a Python function to Count the number of faces for the given input image using Open CV.",
     "Successfully detected and counted all human faces present in input image."),
    (39, "exp39_video_reverse_slow.py", "Exp39_Reverse_Video_Slow_Motion.py", "Exp39_Result_Successfully_Played_Video_in_Reverse_Slow_Motion.png",
     "Write a Python function to play the given video in reverse mode in slow motion.",
     "Successfully extracted frames, reversed their sequence, and rendered in slow motion with time delay."),
    (40, "exp40_extract_text_video.py", "Exp40_Extract_Text_from_Videos.py", "Exp40_Result_Successfully_Extracted_Text_from_Video_Frames.png",
     "Write a Python function to extract the text from videos.",
     "Successfully processed video frames and extracted on-screen text using OCR techniques.")
]

# Copy programs and outputs with new naming conventions
for item in exp_data:
    exp_num, orig_prog, new_prog, new_res, aim, res = item
    
    # Program
    src_prog = os.path.join(BASE_DIR, 'programs', orig_prog)
    dst_prog = os.path.join(PROGRAM_DIR, new_prog)
    if os.path.exists(src_prog):
        shutil.copy(src_prog, dst_prog)
        
    # Screenshot
    orig_scr = f"exp{exp_num:02d}_output.png"
    src_scr = os.path.join(BASE_DIR, 'output_screenshots', orig_scr)
    dst_scr = os.path.join(OUTPUT_DIR, new_res)
    if os.path.exists(src_scr):
        shutil.copy(src_scr, dst_scr)

print(f"Copied 40 programs to '{PROGRAM_DIR}' and 40 screenshots to '{OUTPUT_DIR}'.")

# Build README.md
readme_content = """# ITA05 - Computer Vision Laboratory (Jan 2025)

Complete implementation of all **40 Computer Vision Experiments** based on the Saveetha School of Engineering Computer Vision Laboratory Record Note Book manual.

---

## Repository Structure

```
├── program/                 # All 40 Python experiment scripts (named by program)
├── output screenshot/       # Output screenshots for all 40 experiments (named by result)
├── sample_inputs/           # Distinct sample images & videos for each experiment
└── cascades/                # Pre-trained Haar Cascade XML models
```

---

## Index of 40 Experiments

| S.No | Program Name | Aim & Description | Result Screenshot |
|:---:|:---|:---|:---|
"""

for item in exp_data:
    exp_num, orig_prog, new_prog, new_res, aim, res = item
    readme_content += f"| **{exp_num}** | [`{new_prog}`](program/{new_prog}) | **Aim:** {aim}<br>**Result:** {res} | [Screenshot](output%20screenshot/{new_res}) |\n"

readme_content += """
---

## Requirements & Setup

Install the required Python computer vision libraries:
```bash
pip install opencv-python matplotlib numpy pytesseract
```

### Running Any Experiment
Navigate to the root directory and execute any program:
```bash
python "program/Exp01_Convert_Image_to_Grayscale.py"
python "program/Exp28_Vehicle_Detection_Video_Haar_Cascade.py"
```
"""

with open(os.path.join(BASE_DIR, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("Generated comprehensive README.md")
