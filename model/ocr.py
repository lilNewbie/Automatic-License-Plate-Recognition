from paddleocr import PaddleOCR
from log import LogNumber
import numpy as np
from PIL import Image
import cv2

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def recogFunc(img2):
    img_normal = cv2.imread(img2)
    img_normal = cv2.cvtColor(img_normal, cv2.COLOR_BGR2GRAY)
    img_normal = normal(img_normal)
    img3 = "scaledLP.jpg"

    cv2.imwrite(img3, img_normal)
    
    img_scaled = setImgDPI(img3)
    result = ocr.ocr(img_scaled, cls=True)
    print(result)
    if result != [[]]:
        LogNumber(result[0][0][1][0])


def normal(img):
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    return img


def setImgDPI(img):
    im = Image.open(img)
    length_x, width_y = im.size
    factor = min(1, float(1024.0 / length_x))
    size = int(factor * length_x), int(factor * width_y)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_filename = "scaledLP.jpg"
    im_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename

