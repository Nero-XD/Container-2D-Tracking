# Container-2D-Tracking

以[YOLOv7](https://github.com/WongKinYiu/yolov7)为基础，使用YOLOv7-E6E预训练模型进行训练，加入了[SORT](https://github.com/haroonshakeel/yolov7-object-tracking)模块进行多目标轨迹跟踪。

Tested with：Python3.9.17，Pytorch1.11.0+cu113

# Dataset

[Containers Detection Computer Vision Project](https://universe.roboflow.com/one14-intelligence/containers-detection-db0c2)

# Demo

### Container

![test1](https://github.com/Nero-XD/Container-2D-Tracking/blob/main/assets/test1.gif)

### MS COCO

![test2](https://github.com/Nero-XD/Container-2D-Tracking/blob/main/assets/test2.gif)



# Official Model（MS COCO）

| Model                                                        | Test Size | AP<sup>test</sup> | AP<sub>50</sub><sup>test</sup> | AP<sub>75</sub><sup>test</sup> | batch 1 fps | batch 32 average time |
| :----------------------------------------------------------- | :-------: | :---------------: | :----------------------------: | :----------------------------: | :---------: | :-------------------: |
| [**YOLOv7**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt) |    640    |     **51.4%**     |           **69.7%**            |           **55.9%**            |  161 *fps*  |       2.8 *ms*        |
| [**YOLOv7-X**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x.pt) |    640    |     **53.1%**     |           **71.2%**            |           **57.8%**            |  114 *fps*  |       4.3 *ms*        |
| [**YOLOv7-W6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6.pt) |   1280    |     **54.9%**     |           **72.6%**            |           **60.1%**            |  84 *fps*   |       7.6 *ms*        |
| [**YOLOv7-E6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6.pt) |   1280    |     **56.0%**     |           **73.5%**            |           **61.2%**            |  56 *fps*   |       12.3 *ms*       |
| [**YOLOv7-D6**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-d6.pt) |   1280    |     **56.6%**     |           **74.0%**            |           **61.8%**            |  44 *fps*   |       15.0 *ms*       |
| [**YOLOv7-E6E**](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e.pt) |   1280    |     **56.8%**     |           **74.4%**            |           **62.1%**            |  36 *fps*   |       18.7 *ms*       |

# Trained Model（Based On YOLOv7-E6E）

| Images | Labels |   P   |   R   | mAP@.5 | mAP@.5:.95:100% | per 640x640 image at batch-size 16 |
| :----: | :----: | :---: | :---: | :----: | :-------------: | :--------------------------------: |
|  132   |  2388  | 0.853 | 0.732 |  0.8   |      0.459      |              15.6 ms               |

链接：https://pan.baidu.com/s/1MGQuDrCjQbpaSiux0SaOSA?pwd=twz5 
提取码：twz5

# Installation

```shell
conda create MyEnv python=3.9
conda activate MyEnv
pip install -r requirements.txt
```

# Inference

On video:

```
python detect_or_track.py --weights Container_best.pt --conf 0.25 --img-size 640 --source yourvideo.mp4
```

