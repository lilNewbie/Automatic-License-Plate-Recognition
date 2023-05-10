from detection import detection
import cv2
import pafy
def app(source, option):
    if option=='YouTube':
        url = source
        vPafy = pafy.new(url)
        play = vPafy.getbest(preftype="webm")
        source = play
        return 0

    elif option=="image":
        detection(source)
        return 0
    
    else:
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


