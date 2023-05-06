from detection import detection
import cv2

def app(source):
    cap = cv2.VideoCapture(source)
    while cap.isOpened(): 
        frameName = "frame.jpg"
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(frameName,frame)
            detection("frame.jpg")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            return 0
    cap.release()
    cv2.destroyAllWindows()


