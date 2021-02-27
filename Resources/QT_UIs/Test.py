# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/QT_UIs/Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from Hackathon.GoogleMap import GoogleMap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 590, 781, 81))
        self.frame.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 90, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 0, 90, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 0, 90, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 0, 90, 80))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 0, 90, 80))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 21))
        self.menubar.setObjectName("menubar")
        self.menuhi = QtWidgets.QMenu(self.menubar)
        self.menuhi.setObjectName("menuhi")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionwhy = QtWidgets.QAction(MainWindow)
        self.actionwhy.setObjectName("actionwhy")
        self.actiongo_away = QtWidgets.QAction(MainWindow)
        self.actiongo_away.setObjectName("actiongo_away")
        self.actionno_files = QtWidgets.QAction(MainWindow)
        self.actionno_files.setObjectName("actionno_files")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionnow = QtWidgets.QAction(MainWindow)
        self.actionnow.setObjectName("actionnow")
        self.actionfile_save = QtWidgets.QAction(MainWindow)
        self.actionfile_save.setObjectName("actionfile_save")
        self.actionfile_open = QtWidgets.QAction(MainWindow)
        self.actionfile_open.setObjectName("actionfile_open")
        self.actionfile = QtWidgets.QAction(MainWindow)
        self.actionfile.setObjectName("actionfile")


        self.menuhi.addAction(self.actionwhy)
        self.menuhi.addAction(self.actiongo_away)
        self.menuhi.addAction(self.actionno_files)
        self.menuhi.addAction(self.actionexit)
        self.menuhi.addAction(self.actionnow)
        self.menuhi.addSeparator()
        self.menuhi.addAction(self.actionfile_save)
        self.menuhi.addAction(self.actionfile_open)
        self.menuhi.addAction(self.actionfile)
        self.menubar.addAction(self.menuhi.menuAction())

        self.googleMap = GoogleMap(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.menuhi.setTitle(_translate("MainWindow", "hi"))
        self.actionwhy.setText(_translate("MainWindow", "why"))
        self.actiongo_away.setText(_translate("MainWindow", "go away"))
        self.actionno_files.setText(_translate("MainWindow", "no files"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionnow.setText(_translate("MainWindow", "now"))
        self.actionfile_save.setText(_translate("MainWindow", "file save"))
        self.actionfile_open.setText(_translate("MainWindow", "file open"))
        self.actionfile.setText(_translate("MainWindow", "file?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
