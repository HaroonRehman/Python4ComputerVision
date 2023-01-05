import cv2 as cv

# You can upload a video or Use your Camera than do the stuff live.



# You will provide arugment like (0) if you have one camera and (1) if you have two cameras and so on. The value depends which camera you wanna use .

# You will provide argument ('filename.mp4') or ('PathToFile/filename.mp4') for a video file. It support most of the video formats , you may search for your particual vidoe format on google for that.
video = cv.VideoCapture('movement.mp4')
background_subtractor = cv.createBackgroundSubtractorMOG2(900,900)

while True:
    ret, frame = video.read()
    if ret:
        mask = background_subtractor.apply(frame)
        cv.imshow('Mask',mask)

        # This will end the loop
        if cv.waitKey(5) == ord('x'):
            break 
    else:
        vidoe = cv.VideoCapture('movement.mp4')

cv.destroyAllWindows()
video.release()
