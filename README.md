# YOLO-Custom-object-detection
In this project I used YOLOv5 model to train and predict custom objects such as malt seeds. Image dataset was splitted into two classes (acceptable and not acceptable) 
- Link to YOLOv5 official website [YOLOv5](https://github.com/ultralytics/yolov5)

### Used libraries
- Python
- OpenCV
- All libraries included in the YOLOv5 documentation


### Project stages
1. At this stage it was necessary to collect the right images. The images come from personal database.
2. Labeling objects in images. In this I used [LabelImg](https://github.com/HumanSignal/labelImg)
3. Extracting data from XML files ---> **Jupyter Notebook**
4. Conver labels information into DataFrame format ---> **Jupyter Notebook**
5. Split data into train and test sets ---> **Jupyter Notebook**
6. Create YAML file ---> **Jupyter Notebook**
7. Training model ---> **Google Colaboratory**
8. Get predictions from YOLO model ---> **Jupyter Notebook**


<p align="center">
Examples
</p>

![malt_detector](https://github.com/k-malicki/ComputerVision-YOLO-custom-object-detection/assets/141445691/196375ec-23c0-4a60-b447-455f89174bb6)

![output2](https://github.com/k-malicki/ComputerVision-YOLO-custom-object-detection/assets/141445691/87e0919c-41dd-4e7c-b284-e3148153302d)




