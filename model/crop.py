import cv2
from PIL import Image

def cropFunc2(img, l):
    im = Image.open(img)
    left, upper, right, lower = l[0], l[1], l[2], l[3]
    left, upper, right, lower = int(left), int(upper), int(right)+1, int(lower)
    Cropped = im.crop((left, upper, right, lower))
    return Cropped



def drawFrame(l, u, r, b, frameName):
    img = cv2.imread(frameName)
    if type(img)!=None:
        img2 = img.copy()
        cv2.rectangle(img2, (l, u), (r, b), (255, 0, 0), 2)
        draw = "draw" + frameName.capitalize()
        cv2.imwrite(draw, img2)
    

