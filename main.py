import cv2
import time

haar_cascade_path = "./detection-model/haar_face.xml"

haar_face = cv2.CascadeClassifier(haar_cascade_path)

name = str(input("What is your name?: "))

cam = cv2.VideoCapture(0)

taken = False

while taken != True:
    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_rect = haar_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    rec_x1 = 700
    rec_y1 = 200
    rec_x2 = 1300
    rec_y2 = 900

    roi = frame[rec_y1+10:rec_y2-10, rec_x1+10:rec_x2-10]

    cv2.rectangle(frame, (rec_x1, rec_y1), (rec_x2, rec_y2), (0, 255, 0), thickness=2)

    if len(faces_rect) == 0:
        cv2.putText(frame, "Can't detect any faces", (800, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    for (x1, y1, x2, y2) in faces_rect:
        print(f"""
        x1: {x1} rec_x1 = 700
        y1: {y1} rec_y1 = 200
        x2: {x2} rec_x2 = 1300
        y2: {y2} rec_y2 = 900
        """)

        # cv2.rectangle(frame, (x1, y1), (x1+x2, y1+y2), (0, 255, 0), thickness=2)
        if x1 < rec_x1 or y1 < rec_y1 or x1 > rec_y2 or y1 > 500:
            cv2.putText(frame, "Please put your face inside the rectangle", (660, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Hold your head still. Precc 'c' to capture", (730, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                cv2.imwrite(f"./faces/{name}_face_{time.time()}.jpg", roi)
                taken = True


    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()