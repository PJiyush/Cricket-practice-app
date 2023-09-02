print("Importing Libraries...")
import cv2
import mediapipe as mp
import Global
import ball
import Stumps
import Hands

print("Importing Libraries...Done")

print("Initializing...")
hands = mp.solutions.hands
hand = hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
drawFunc = mp.solutions.drawing_utils

print("Initializing...Done")



cap = cv2.VideoCapture(0)
cap.set(3, Global.Xdirection)
cap.set(4, Global.Ydirection)
score = 0
point = 0
OnOff = Global.OnOff
radiusImcrement = Global.radiusImcrement
color = Global.color

print("Game Started")
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    resultsHand = hand.process(imgRGB) 
    if resultsHand.multi_hand_landmarks:
        for handLms in resultsHand.multi_hand_landmarks:
            try:
                xVal , yVal = Hands.averageOfHand(handLms,img)
                catch = True 
            except:
                catch = False
            
            if catch==False:
                xVal, yVal = 0,0
            if(ball.checkForBall((xVal,yVal),OnOff,Global.pos,Global.rad)): 
                print(score)
                color = (0,255,0)
                Global.rad = 8
                OnOff = -1
                point = 48
            else:
                color = (0,255,255)
                
            if(point>3):
                point = point -4
            
            cv2.putText(img,'Score '+ str(score), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.putText(img,'Time '+ str(point), (10, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
            if(point>0):
                if(Stumps.checkInStumps((xVal,yVal),OnOff,Global.stumpsTopLeft,Global.stumpsBottomRight)):
                        score = score + 1
                        # print("HIT")
                        point = 0

            drawFunc.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)

    Global.rad = Global.rad + radiusImcrement
    if OnOff==1:
        ball.drawBall(img,(Global.pos[0],Global.pos[1]),int(Global.rad),color)
    if Global.rad>35:
        radiusImcrement = -1*(radiusImcrement)
    if Global.rad<5:
        radiusImcrement = -1*(radiusImcrement)
        OnOff = (-1)*(OnOff)
        ball.reset(onOff=OnOff,rad=Global.rad,pos=Global.pos)

    Stumps.drawStumps(img,Global.stumpsTopLeft,Global.stumpsBottomRight)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()