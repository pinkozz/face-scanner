import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

class VideoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Scanner")
        self.setGeometry(100, 100, 600, 900)

        # Layout and video display label
        self.layout = QVBoxLayout()
        self.video_label = QLabel()
        self.layout.addWidget(self.video_label)
        self.setLayout(self.layout)

        # Initialize OpenCV video capture
        self.capture = cv2.VideoCapture(1)

        # Timer to update the video feed
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame into RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Convert the frame to QImage
            height, width, _ = frame.shape
            qimage = QImage(frame.data, width, height, 3  * 1920, QImage.Format_RGB888)

            # Display the QImage on the QLabel
            self.video_label.setPixmap(QPixmap.fromImage(qimage))
    
    def closeEvent(self, event):
        # Release the video capture on close
        self.capture.release()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoApp()
    window.show()
    sys.exit(app.exec_())