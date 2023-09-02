import cv2
import Global

def averageOfHand(handLms, img, landmarkList:list = [5,9,13,17,0] )->tuple:
    sumX = 0
    sumY = 0
    for i in landmarkList:
        sumX = sumX + handLms.landmark[i].x
        sumY = sumY + handLms.landmark[i].y
    sumX = sumX/5
    sumY = sumY/5
    cv2.circle(img,(int(sumX*Global.Xdirection),int(sumY*Global.Ydirection)),5,(0,0,255),cv2.FILLED)
    return (int(sumX*Global.Xdirection),int(sumY*Global.Ydirection))

