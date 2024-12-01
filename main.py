import cv2

haar_cascade_path = "./detection-model/haar_face.xml"

haar_face = cv2.CascadeClassifier(haar_cascade_path)

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_rect = haar_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    rectangle_x1 = 700
    rectangle_y1 = 200
    rectangle_x2 = 1300
    rectangle_y2 = 900

    cv2.rectangle(frame, (rectangle_x1, rectangle_y1), (rectangle_x2, rectangle_y2), (0, 255, 0), thickness=2)

    if len(faces_rect) == 0:
        cv2.putText(frame, "Can't detect any faces", (800, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    for (x1, y1, x2, y2) in faces_rect:
        print(f"""
        x1: {x1} rectangle_x1 = 700
        y1: {y1} rectangle_y1 = 200
        x2: {x2} rectangle_x2 = 1300
        y2: {y2} rectangle_y2 = 900
        """)

        cv2.rectangle(frame, (x1, y1), (x1+x2, y1+y2), (0, 255, 0), thickness=2)
        if x1 < rectangle_x1 or y1 < rectangle_y1 or x1 > rectangle_y2 or y1 > 500:
            cv2.putText(frame, "Please put your face inside the rectangle", (660, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Hold your head still", (800, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()