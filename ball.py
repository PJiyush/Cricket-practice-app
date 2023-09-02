import cv2
import utils

def drawBall(img,centerTuple,radi, color)->None:
    cv2.circle(img,centerTuple,radi,color,cv2.FILLED)

def reset(onOff,rad,pos:list):
    pos[0],pos[1] = utils.generateRandomCordinates()
    onOff = (-1)*onOff
    pass

def checkForBall(handCenterTuple, onOff, ballCenter, ballRadius):
    if onOff == 1:
        if handCenterTuple[0] > ballCenter[0] - ballRadius and handCenterTuple[0] < ballCenter[0] + ballRadius:
            if handCenterTuple[1] > ballCenter[1] - ballRadius and handCenterTuple[1] < ballCenter[1] + ballRadius:
                return True
    return False
    
