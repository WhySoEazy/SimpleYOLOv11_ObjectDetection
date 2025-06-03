from ultralytics import YOLO

model = YOLO('yolo11x.pt')

result = model('Cats.mp4' , save=True)