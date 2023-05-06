from ocr import recogFunc
from ultralytics import YOLO
from crop import cropFunc2
from crop import drawFrame
model = YOLO("model\lpd.pt")
model2 = YOLO(r"model\vehicle.pt")

def detection(img):
    res = model2(img, conf=0.4)
    crops = res[0].boxes.numpy()
    
    for j in range(len(crops)):
        l = list(crops.boxes[j])
        frame = cropFunc2(img, l)
        drawFrame(int(l[0]), int(l[1]), int(l[2]), int(l[3]), img)
        if frame!=[]:
            img2 = "res.jpg"
            frame.save(img2)
            extractInfo(img2)
            


def extractInfo(img):
    res = model(img, conf=0.7)
    crops = res[0].boxes.numpy()

    for j in range(len(crops)):
        l = list(crops.boxes[j])
        frame = cropFunc2(img, l)
        if frame != []:
            img2 = "lp.jpg"
            frame.save(img2)
            recogFunc(img2)

