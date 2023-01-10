import cv2 as cv

img = cv.imread('/home/esclimited/Python/Python4ComputerVision/ReadTextFromImage/sample2.jpg')

cv.imshow('test',img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
tresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21,7)
cv.imshow('tresh',tresh)
cv.waitKey(0)
cv.destroyAllWindows()