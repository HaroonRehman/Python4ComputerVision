import numpy as np
import cv2 as cv
import imutils


# I am using my smartphone strema here you may use whatever stream you want.
url = 'http://test:test@192.168.0.101:4444/video'

cap = cv.VideoCapture(url)


while True:    
    ret, frame = cap.read()

    frame= cv.resize(frame,(460,720))
    
    cv.imshow('normal',frame)
    
    edge_initial = cv.Laplacian(frame,cv.CV_64F)
    edge_initial = np.uint8(edge_initial)
    cv.imshow('edged', edge_initial)

    # set the frame and trheshold according to your stream quality light etc.
    edge_final = cv.Canny(frame,660,1)
    cv.imshow('edge_final',edge_final)

    if cv.waitKey(1) == ord('x'):
        break
    
    
cap.release()
cv.destroyAllWindows()