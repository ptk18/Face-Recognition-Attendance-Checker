# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'attendancePJ.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(809, 591)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(10, 0, 411, 51))
        font = QFont()
        font.setPointSize(24)
        self.titleLabel.setFont(font)
        self.webcam = QWidget(self.centralwidget)
        self.webcam.setObjectName(u"webcam")
        self.webcam.setGeometry(QRect(20, 60, 521, 441))
        self.checkInBtn = QPushButton(self.centralwidget)
        self.checkInBtn.setObjectName(u"checkInBtn")
        self.checkInBtn.setGeometry(QRect(20, 530, 251, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.checkInBtn.setFont(font1)
        self.checkInBtn.setStyleSheet(u"background-color: rgb(0, 252, 0);\n"
"color: rgb(255, 255, 255);")
        self.checkOutBtn = QPushButton(self.centralwidget)
        self.checkOutBtn.setObjectName(u"checkOutBtn")
        self.checkOutBtn.setGeometry(QRect(280, 530, 261, 41))
        self.checkOutBtn.setFont(font1)
        self.checkOutBtn.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(560, 130, 241, 80))
        font2 = QFont()
        font2.setPointSize(12)
        self.gridLayoutWidget.setFont(font2)
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dateLabel = QLabel(self.gridLayoutWidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setFont(font2)

        self.horizontalLayout.addWidget(self.dateLabel)

        self.dateValue = QLabel(self.gridLayoutWidget)
        self.dateValue.setObjectName(u"dateValue")
        self.dateValue.setFont(font2)

        self.horizontalLayout.addWidget(self.dateValue)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timeLabel = QLabel(self.gridLayoutWidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setFont(font2)

        self.horizontalLayout_2.addWidget(self.timeLabel)

        self.timeValue = QLabel(self.gridLayoutWidget)
        self.timeValue.setObjectName(u"timeValue")
        self.timeValue.setFont(font2)

        self.horizontalLayout_2.addWidget(self.timeValue)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.detailsBox = QGroupBox(self.centralwidget)
        self.detailsBox.setObjectName(u"detailsBox")
        self.detailsBox.setGeometry(QRect(560, 250, 241, 221))
        self.detailsBox.setFont(font2)
        self.gridLayoutWidget_2 = QWidget(self.detailsBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 40, 221, 161))
        self.gridLayoutWidget_2.setFont(font2)
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.nameLabel = QLabel(self.gridLayoutWidget_2)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setFont(font2)

        self.horizontalLayout_3.addWidget(self.nameLabel)

        self.dateLabel_3 = QLabel(self.gridLayoutWidget_2)
        self.dateLabel_3.setObjectName(u"dateLabel_3")
        self.dateLabel_3.setFont(font2)

        self.horizontalLayout_3.addWidget(self.dateLabel_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.statusLabel = QLabel(self.gridLayoutWidget_2)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setFont(font2)

        self.horizontalLayout_4.addWidget(self.statusLabel)

        self.statusValue = QLabel(self.gridLayoutWidget_2)
        self.statusValue.setObjectName(u"statusValue")
        self.statusValue.setFont(font2)

        self.horizontalLayout_4.addWidget(self.statusValue)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.totalTimeLabel = QLabel(self.gridLayoutWidget_2)
        self.totalTimeLabel.setObjectName(u"totalTimeLabel")
        self.totalTimeLabel.setFont(font2)

        self.horizontalLayout_5.addWidget(self.totalTimeLabel)

        self.totalTimeValue = QLabel(self.gridLayoutWidget_2)
        self.totalTimeValue.setObjectName(u"totalTimeValue")
        self.totalTimeValue.setFont(font2)

        self.horizontalLayout_5.addWidget(self.totalTimeValue)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Attendance Checking...", None))
        self.checkInBtn.setText(QCoreApplication.translate("MainWindow", u"Check In", None))
        self.checkOutBtn.setText(QCoreApplication.translate("MainWindow", u"Check Out", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"Date: ", None))
        self.dateValue.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Time: ", None))
        self.timeValue.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.detailsBox.setTitle(QCoreApplication.translate("MainWindow", u"Details", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.dateLabel_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.statusValue.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.totalTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Total Time", None))
        self.totalTimeValue.setText(QCoreApplication.translate("MainWindow", u"-", None))
    # retranslateUi

