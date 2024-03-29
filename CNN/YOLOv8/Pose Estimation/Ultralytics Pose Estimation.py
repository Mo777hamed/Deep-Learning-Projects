# -*- coding: utf-8 -*-
"""Ultralytics Pose Estimation .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yjlk0_W_yXpJaMeARafVTR7OJnBuxc16
"""

#pip install ultralytics

from ultralytics import YOLO

# Load the pre-trained YOLOv8 model
model = YOLO('yolov8n-pose.pt')

results = model(source="/content/yoga_pose1.jpeg", show=True, conf=0.4, save=True)

# Print the outputs
for output in results:
    print(output)