import cv2
import torch
import numpy as np
from tracker import *
import tkinter as tk
import time
import random
import threading
from tkinter import ttk

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

cap=cv2.VideoCapture('highway.mp4')

count=0
tracker = Tracker()

def POINTS(event,x,y,flags,param):
    if event==cv2.EVENT_MOUSEMOVE:
        mp=[x,y]
        print(mp)

cv2.namedWindow('DETECTION')
cv2.setMouseCallback('DETECTION',POINTS)

veh=[]
area1=[(448,445),(428,472),(526,482),(524,449)]
area2=[(699,430),(774,430),(837,468),(732,468)]
area3=[(298,496),(418,496),(373,546),(205,546)]
area4=[(584,407),(663,407),(686,425),(588,425)]
a1=set()
a2=set()
a3=set()
a4=set()
while True:
    ret,frame=cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,600))
    results=model(frame)
    l=[]
    for index,rows in results.pandas().xyxy[0].iterrows():
        x=int(rows.iloc[0])
        y=int(rows.iloc[1])
        x1=int(rows.iloc[2])
        y1=int(rows.iloc[3])
        b=str(rows['name'])
        
        l.append([x,y,x1,y1])
    box=tracker.update(l)
    for i in box:
        x2,y2,x3,y3,id=i
        cv2.rectangle(frame,(x2,y2),(x3,y3),(0,0,255),2)
        cv2.circle(frame,(x3,y3),4,(0,255,0),-1)
        result1=cv2.pointPolygonTest(np.array(area1,np.int32),(x3,y3),False)
        result2=cv2.pointPolygonTest(np.array(area2,np.int32),(x3,y3),False)
        result3=cv2.pointPolygonTest(np.array(area3,np.int32),(x3,y3),False)
        result4=cv2.pointPolygonTest(np.array(area4,np.int32),(x3,y3),False)
        if result1>0:
            a1.add(id)
        if result2>0:
            a2.add(id)
        if result3>0:
            a3.add(id)
        if result4>0:
            a4 .add(id)
        
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(255,255,0),3)
    cv2.polylines(frame,[np.array(area2,np.int32)],True,(255,255,0),3)
    cv2.polylines(frame,[np.array(area3,np.int32)],True,(255,255,0),3)
    cv2.polylines(frame,[np.array(area4,np.int32)],True,(255,255,0),3)
    l1=len(a1)
    veh.append(l1)
    cv2.putText(frame,str(l1),(549,465),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)
    l2=len(a2)
    cv2.putText(frame,str(l2),(804,411),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)
    l3=len(a3)
    cv2.putText(frame,str(l3),(216,518),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)
    l4=len(a4)
    cv2.putText(frame,str(l4),(562,403),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)
    cv2.imshow("DETECTION",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()

class TrafficLightControlSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Control System")
        
        self.lanes = ['Lane 1', 'Lane 2', 'Lane 3', 'Lane 4']
        self.green_lane = None
        self.traffic_lights = {}
        self.traffic_density_labels = {}
        self.signal_switching_label = None

        self.create_gui()
        self.start_traffic_light_system()

    def create_gui(self):
        for i, lane in enumerate(self.lanes):
            label_frame = tk.Frame(self.root, bg="white", highlightbackground="black", highlightthickness=2, bd=0)
            label_frame.grid(row=0, column=i, padx=15, pady=15)  

            label = tk.Label(label_frame, text=lane, font=("Arial", 16), bg="white")  
            label.pack(padx=10, pady=5) 

            light_label = tk.Label(label_frame, bg="gray", width=15, height=7)  
            light_label.pack(padx=10, pady=5)  
            self.traffic_lights[lane] = light_label

            density_label = tk.Label(label_frame, text="Density: ", bg="white")
            density_label.pack(padx=10, pady=5)
            self.traffic_density_labels[lane] = density_label

        self.signal_switching_label = tk.Label(self.root, text="", font=("Arial", 12), bg="white")
        self.signal_switching_label.grid(row=1, columnspan=len(self.lanes), padx=15, pady=5)

    def measure_traffic_density(self):
        return {lane: random.randint(0, 50) for lane in self.lanes}

    def switch_to_next_lane(self):
        current_index = self.lanes.index(self.green_lane)
        next_index = (current_index + 1) % len(self.lanes)
        self.green_lane = self.lanes[next_index]

    def run_traffic_light_system(self):
        count=0
        while count<=10:
            traffic_density = self.measure_traffic_density()
            max_density_lane = max(traffic_density, key=traffic_density.get)

            if self.green_lane != max_density_lane:
                self.green_lane = max_density_lane
                signal_switching_message = f"Switching green light to {self.green_lane}"
                self.signal_switching_label.config(text=signal_switching_message)

                for lane, light_label in self.traffic_lights.items():
                    if lane == self.green_lane:
                        light_label.config(bg="green")
                    else:
                        light_label.config(bg="red")

            for lane, density_label in self.traffic_density_labels.items():
                density_label.config(text=f"Density: {traffic_density[lane]}")

            time.sleep(random.randint(5, 10))
            self.switch_to_next_lane()
            count+=1

    def start_traffic_light_system(self):
        t = threading.Thread(target=self.run_traffic_light_system)
        t.daemon = True
        t.start()

def main():
    root = tk.Tk()
    app = TrafficLightControlSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()


