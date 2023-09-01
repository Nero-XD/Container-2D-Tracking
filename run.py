import os
path = os.getcwd()
# for i in range(5):
#     os.system('python detect_or_track.py --device 0 --weights yolov7-e6e.pt --no-trace --show-track --exist-ok --track --source "testdata/%d.mp4" --project "testresult" --name ""'%(i+1))

# os.system('python detect_or_track.py --device 0 --weights yolov7-e6e.pt --no-trace --view-img --show-track --exist-ok --track --source "testdata/testdata.mp4" --project "testresult" --name ""')

# os.system('python detect_or_track.py --device 0 --weights yolov7-e6e.pt --no-trace --view-img --nosave --show-track --track --source "testdata/21.mp4" ')
# import torch
# torch.cuda.empty_cache()

# train
# os.system(('python train_aux.py --weights "runs/train/exp4/weights/best.pt" '
#            '--cfg "datasets/ContainersDetection/yolov7-e6e-container.yaml" '
#            '--data "datasets/ContainersDetection/data.yaml" '
#            '--cache-images '
#            '--device 0 --batch-size 16 --epoch 80 --workers 4'))

# predict video
os.system('python detect_or_track.py --weights "runs/train/exp6/weights/best.pt" --show-track --track --nosave --view-img --no-trace --source "D:/MyTool/VideoSplit/video/1.mp4" --conf-thres 0.85')
# os.system('python detect_or_track.py --weights "runs/train/exp6/weights/best.pt" --show-track --track --view-img --no-trace --source "D:/MyTool/VideoSplit/video/2.mp4" --conf-thres 0.85')

# predict picture
# os.system('python detect.py --weights "runs/train/exp3/weights/best.pt" --view-img --no-trace --source "D:/MyTool/VideoSplit/image/2_frame_0128.jpg" --conf-thres 0.75')