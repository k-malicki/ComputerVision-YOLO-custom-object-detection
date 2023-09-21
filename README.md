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

![output1](https://github.com/k-malicki/YOLO-Custom-object-detection/assets/141445691/5dc95197-7231-47ab-b260-5080881162b2)

![output2](https://github.com/k-malicki/YOLO-Custom-object-detection/assets/141445691/07241088-c1fa-4b3d-90d7-d6a23453605f)



