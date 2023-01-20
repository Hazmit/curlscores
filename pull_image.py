import cv2
import requests # to get image from the web
import shutil # to save it locally

imagesFolder = "./"
cap = cv2.VideoCapture("rtsp://admin:admin1admin@192.168.227.231:554")
frameRate = cap.get(5) #frame rate
count = 0

while cap.isOpened():
    frameId = cap.get(1)  # current frame number
    ret, frame = cap.read()

    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        # filename = imagesFolder + "/image_" + str(datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"))  + ".jpg"
        filename = imagesFolder + "snapshot.jpg"
        cv2.imwrite(filename, frame)

    cap.release()
    print ("Snapshot retrieved.")

cv2.destroyAllWindows()