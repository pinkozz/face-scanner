import cv2
import time
import os

time.sleep(1)

haar_cascade_path = "./detection-model/haar_face.xml"

haar_face = cv2.CascadeClassifier(haar_cascade_path)

name = "serhii"
# name = str(input("What is your name?: "))

def putTextBG(img, text, org, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, text_color=(0, 0, 255), thickness=2, bg_color=(0,0,0)):
    cv2.rectangle(img, (0, 120), (1920, 155), bg_color, -1)
    cv2.putText(img, text, org, fontFace, fontScale, text_color, thickness)

cam = cv2.VideoCapture(1)

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

    cv2.rectangle(frame, (rec_x1, rec_y1), (rec_x2, rec_y2), (0, 0, 255), thickness=2)

    if len(faces_rect) == 0:
        putTextBG(frame, "Can't detect any faces", (810, 150))

    for (x1, y1, x2, y2) in faces_rect:
        print(f"""
        x1: {x1} rec_x1 = 700
        y1: {y1} rec_y1 = 200
        x2: {x2} rec_x2 = 1300
        y2: {y2} rec_y2 = 900
        """)

        # cv2.rectangle(frame, (x1, y1), (x1+x2, y1+y2), (0, 255, 0), thickness=2)
        if x1 < rec_x1 or y1 < rec_y1 or x1 > rec_y2 or y1 > 500:
            putTextBG(frame, "Please put your face inside the rectangle ", (660, 150))
        else:
            cv2.rectangle(frame, (rec_x1, rec_y1), (rec_x2, rec_y2), (0, 255, 0), thickness=2)

            putTextBG(frame, "Hold your head still. Precc 'c' to capture", (660, 150),  text_color=(0, 255, 0))
            if cv2.waitKey(1) & 0xFF == ord('c'):
                try:
                    os.mkdir(f"./faces/{name}")
                except FileExistsError:
                    pass
                cv2.imwrite(f"./faces/{name}/face_{time.time()}.jpg", roi)
                taken = True


    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()