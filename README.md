🚦 Traffic Detection and Signalling System

<br><br>  

📌 Overview

This project implements an AI-powered traffic detection and automatic signal control system to reduce congestion and improve road safety.
It uses YOLOv5 object detection to count vehicles in real-time and dynamically adjust traffic light timings based on density.

<br><br>  

✨ Features

Real-time Vehicle Detection using YOLOv5

Traffic Density Estimation per lane

Dynamic Signal Control → Green light assigned to the lane with the highest density

Live GUI Interface built with Tkinter to visualize traffic lights and switching

Scalable System that can be adapted to real-world traffic junctions

<br><br>  

🛠️ Tech Stack

Programming Language: Python

Libraries & Tools:

    OpenCV → Video capture & frame processing

    YOLOv5 → Object detection for vehicles

    Tracker Module → Continuous tracking across frames
  
    Tkinter → GUI for traffic lights and signals

IDE: Jupyter Notebook / PyCharm

<br><br>  

📂 Project Workflow

Input Module → CCTV/Video input of traffic junction

Vehicle Detection & Counting → YOLOv5 identifies and counts vehicles per lane

Traffic Control Logic → Algorithm assigns green signal to lane with max density

GUI Visualization → Tkinter-based interface shows real-time signal switching

<br><br>  

📷 Demo Flow

🎥 Input: Real-time CCTV/video feed

🧮 Processing: YOLOv5 detects + counts vehicles

🚦 Output: Traffic lights dynamically updated in GUI

<br><br>  

📑 Future Enhancements

Integrate YOLOv8 for improved accuracy and real-time performance

Deploy on edge devices for real-time smart city applications

Cloud integration for large-scale traffic data analytics


<br><br>  

👍 CODE IMPLEMENTATION AND WORING 

![Traffic Demo 1](Screenshot%202025-08-30%20114019.png)  
![Traffic Demo 2](Screenshot%202025-08-30%20114035.png)


