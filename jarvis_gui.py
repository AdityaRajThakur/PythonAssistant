# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Jarvis_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import time
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 321, 301))
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("ezgif.com-gif-maker.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 321, 111))
        self.label_2.setText("")
        # self.label_2.setPixmap(QtGui.QPixmap("Jarvis_Loading_Screen.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 320, 151, 31))
        self.textBrowser.setStyleSheet("background:transparent;\n""border-radius: 2px solid balck;\n""color:white;\n")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("Listening....")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(160, 70, 151, 31))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:2p solid black;\n"
"color:white;\n")
        self.time = time.localtime()
        self.currenttime = time.strftime("%H:%M:%S",self.time)
        # self.textBrowser_2.setText(self.currenttime)
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.movie = QtGui.QMovie("ezgif.com-gif-maker.gif")
        self.label.setMovie(self.movie)
        self.movie2 = QtGui.QMovie("Jarvis_Loading_Screen.gif")
        self.label_2.setMovie(self.movie2)
        self.startanimation()
        
    def startanimation(self):
        self.movie.start()
        self.movie2.start()

