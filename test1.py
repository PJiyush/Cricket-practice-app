from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(0)
model = YOLO('yolo-weights\yolov8n.pt')
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    results = model(img)
    print(results)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            print(box.cls[0])
            cv2.putText(img,f'{(box.cls[0])*100}  {(box.conf[0])*100}', (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if 0xFF == ord('q'):
        break
    cv2.imshow("Image", img)
    cv2.waitKey(1)

