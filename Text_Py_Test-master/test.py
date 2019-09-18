# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 772)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(51, 51, 51);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.upperFrame = QtWidgets.QFrame(self.centralwidget)
        self.upperFrame.setGeometry(QtCore.QRect(-40, 0, 1221, 51))
        self.upperFrame.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.upperFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upperFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upperFrame.setObjectName("upperFrame")
        self.layoutWidget = QtWidgets.QWidget(self.upperFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 10, 1001, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(235, 150, 111);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(235, 150, 111);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(640, 80, 461, 561))
        self.textEdit.setStyleSheet("background-color: rgb(85, 85, 85);\n"
"font: 75 9pt \"Consolas\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.input = QtWidgets.QLabel(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(20, 80, 481, 561))
        self.input.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.input.setLineWidth(3)
        self.input.setText("")
        self.input.setScaledContents(False)
        self.input.setAlignment(QtCore.Qt.AlignCenter)
        self.input.setObjectName("input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label.setObjectName("label")
        self.AddPic = QtWidgets.QLabel(self.centralwidget)
        self.AddPic.setGeometry(QtCore.QRect(210, 290, 101, 101))
        self.AddPic.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.AddPic.setText("")
        self.AddPic.setPixmap(QtGui.QPixmap("res/addPicIcon.png"))
        self.AddPic.setScaledContents(True)
        self.AddPic.setAlignment(QtCore.Qt.AlignCenter)
        self.AddPic.setObjectName("AddPic")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 60, 55, 16))
        self.label_3.setObjectName("label_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(510, 70, 123, 571))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(253, 181, 143);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(235, 150, 111);\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(235,150,111);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(253, 181, 143);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(235, 150, 111);\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(253, 181, 143);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(235, 150, 111);\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(253, 181, 143);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(235, 150, 111);\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(253, 181, 143);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(235, 150, 111);\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(253, 181, 143);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(235, 150, 111);\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(253, 181, 143);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(235, 150, 111);\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(253, 181, 143);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(235, 150, 111);\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout.addWidget(self.pushButton_10)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(680, 690, 181, 31))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(235, 150, 111);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(870, 690, 181, 31))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(235, 150, 111);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 680, 95, 20))
        self.radioButton.setStyleSheet("QRadioButton{\n"
"color:white\n"
"}")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 720, 95, 20))
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
"    color:white\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(770, 300, 191, 101))
        font = QtGui.QFont()
        font.setFamily("HP Simplified")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 650, 141, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(1040, 650, 61, 21))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setMinimum(12)
        self.spinBox.setMaximum(30)
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(930, 650, 101, 20))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(340, 660, 451, 23))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(235,150,111);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}\n"
"\"\"\"\n"
"\n"
"COMPLETED_STYLE = \"\"\"\n"
"QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: red;\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSingle_Image = QtWidgets.QAction(MainWindow)
        self.actionSingle_Image.setObjectName("actionSingle_Image")
        self.actionPNG = QtWidgets.QAction(MainWindow)
        self.actionPNG.setObjectName("actionPNG")
        self.actionJPEG = QtWidgets.QAction(MainWindow)
        self.actionJPEG.setObjectName("actionJPEG")
        self.actionTIF = QtWidgets.QAction(MainWindow)
        self.actionTIF.setObjectName("actionTIF")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Text Recognition Test"))
        self.pushButton_3.setText(_translate("MainWindow", "Open Image/Rotate/Histogram"))
        self.pushButton_7.setText(_translate("MainWindow", "Save Text To File"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#dfdace;\">Input Image</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#dfdace;\">Output</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Convert Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Edge Detect"))
        self.pushButton_9.setText(_translate("MainWindow", "Sharpen"))
        self.pushButton_8.setText(_translate("MainWindow", "Blur"))
        self.pushButton_11.setText(_translate("MainWindow", "GrayScale"))
        self.pushButton_12.setText(_translate("MainWindow", "Segmentation"))
        self.pushButton_4.setText(_translate("MainWindow", "Contrast Test"))
        self.pushButton_10.setText(_translate("MainWindow", "Noise Reduction"))
        self.pushButton_6.setText(_translate("MainWindow", "Clear"))
        self.pushButton_5.setText(_translate("MainWindow", "Save Text Test"))
        self.radioButton.setText(_translate("MainWindow", "Latvian"))
        self.radioButton_2.setText(_translate("MainWindow", "English"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Text</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#dfdace;\">Language selection:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Output Font Size:"))
        self.actionSingle_Image.setText(_translate("MainWindow", "Single Image"))
        self.actionPNG.setText(_translate("MainWindow", "PNG"))
        self.actionJPEG.setText(_translate("MainWindow", "JPEG"))
        self.actionTIF.setText(_translate("MainWindow", "TIF"))
