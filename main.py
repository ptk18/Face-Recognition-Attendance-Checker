import cv2
import os
import numpy as np
import face_recognition
from PySide6.QtCore import Qt, QTimer, QDate
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox
from datetime import datetime
from attendancePJ import Ui_MainWindow

class FaceRecognitionApp(QMainWindow):
    def __init__(self):
        super(FaceRecognitionApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.webcam_label = QLabel(self.ui.webcam)
        self.webcam_label.setAlignment(Qt.AlignCenter)
        self.webcam_label.setFixedSize(640, 480)  

        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_webcam)
        self.timer.start(10)

        self.path = 'imagesAttendance'
        self.images = []
        self.classNames = []
        self.myList = os.listdir(self.path)
        for i in self.myList:
            currentImage = cv2.imread(f'{self.path}/{i}')
            self.images.append(currentImage)
            self.classNames.append(os.path.splitext(i)[0])

        self.encodeListKnown = self.find_encodings(self.images)

        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')
        current_time = datetime.now().strftime('%I:%M %p')
        self.ui.dateValue.setText(current_date)
        self.ui.timeValue.setText(current_time)

        self.TimeList1 = []
        self.TimeList2 = []
        self.username = " "

        self.connect_buttons()  # Connect buttons to functions

    def find_encodings(self, images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def update_webcam(self):
        success, frame = self.cap.read()
        if success:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces_in_frame = face_recognition.face_locations(frame)
            encodes_in_frame = face_recognition.face_encodings(frame, faces_in_frame)

            for encode_face, face_loc in zip(encodes_in_frame, faces_in_frame):
                matches = face_recognition.compare_faces(self.encodeListKnown, encode_face)
                print(matches)
                face_distance = face_recognition.face_distance(self.encodeListKnown, encode_face)
                print(face_distance)
                match_index = np.argmin(face_distance)
                print(face_loc)

                if matches[match_index]:
                    name = self.classNames[match_index]
                    self.username = name
                    y1, x2, y2, x1 = face_loc
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)
                    self.mark_attendance(name)

            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)
            self.webcam_label.setPixmap(pixmap)
        else:
            print("Failed to capture frame")
            
        if self.ui.checkInBtn.isChecked():
            self.check_in("dummy_name")
            self.ui.checkInBtn.setChecked(False)
        elif self.ui.checkOutBtn.isChecked():
            self.check_out("dummy_name")
            self.ui.checkOutBtn.setChecked(False)

    def mark_attendance(self, name):
        print("Inside mark_attendance function")
        print("CheckIn button state:", self.ui.checkInBtn.isChecked())
        print("CheckOut button state:", self.ui.checkOutBtn.isChecked())
        print(self.ui.checkInBtn.isChecked())
        if self.ui.checkInBtn.isChecked():
            self.check_in(name)
        elif self.ui.checkOutBtn.isChecked():
            self.check_out(name)
            
    def check_in(self, checked):
        print("Inside check_in function")
        if checked:
            name = self.ui.nameLabel.text()
            self.ui.checkInBtn.setEnabled(False)

            with open('attendance.csv', 'r+') as f:
                if (name != 'unknown'):
                    buttonReply = QMessageBox.question(self, 'Welcome ' + self.username, 'Are you checking in?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if buttonReply == QMessageBox.Yes:
                        date_time_string = datetime.now().strftime("%y/%m/%d %H:%M:%S")
                        f.writelines(f'\n{name},{date_time_string}')
                        self.ui.checkInBtn.setChecked(False)
                        self.ui.dateLabel_3.setText(self.username)
                        self.ui.statusValue.setText("Checked In")

                        self.TimeList1.append(datetime.now())
                        self.ui.checkInBtn.setEnabled(True)
                    else:
                        print("Not Clicked!")
                        self.ui.checkInBtn.setChecked(False)
                        self.ui.checkInBtn.setEnabled(True)

    def check_out(self, checked):
        print("Inside check_out function")
        if checked:
            name = self.ui.nameLabel.text()
            self.ui.checkOutBtn.setEnabled(False)

            with open('attendance.csv', 'r+') as f:
                if (name != 'unknown'):
                    buttonReply = QMessageBox.question(self, 'Welcome ' + self.username, 'Are you checking out?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if buttonReply == QMessageBox.Yes:
                        date_time_string = datetime.now().strftime("%y/%m/%d %H:%M:%S")
                        f.writelines(f'\n{name},{date_time_string}')
                        self.ui.checkOutBtn.setChecked(False)
                        self.ui.dateLabel_3.setText(self.username)
                        self.ui.statusValue.setText("Checked Out")

                        self.TimeList2.append(datetime.now())
                        self.ui.checkOutBtn.setEnabled(True)
                    else:
                        print("Not Clicked!")
                        self.ui.checkOutBtn.setChecked(False)
                        self.ui.checkOutBtn.setEnabled(True)

    def connect_buttons(self):
        self.ui.checkInBtn.clicked.connect(lambda: self.check_in("dummy_name"))
        self.ui.checkOutBtn.clicked.connect(lambda: self.check_out("dummy_name"))



if __name__ == "__main__":
    app = QApplication([])
    window = FaceRecognitionApp()
    window.connect_buttons()  # Connect buttons to functions
    window.show()
    app.exec()
