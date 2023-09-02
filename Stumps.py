import cv2

def drawStumps(img, topLeft, bottomRight, color=(0,255,0)):
    cv2.rectangle(img,topLeft,bottomRight, color, 5)

def checkInStumps(centreTuple, onOff, topLeft, bottomRight):
    if onOff == -1:
        if centreTuple[0] > topLeft[0] and centreTuple[0] < bottomRight[0]:
            if centreTuple[1] > topLeft[1] and centreTuple[1] < bottomRight[1]:
                return True
    return False
