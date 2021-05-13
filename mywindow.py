from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setEnabled(True)
        MainWindow.resize(1204, 923)
        MainWindow.setGeometry(500, 200, 400, 500)
        MainWindow.setWindowTitle("MainWindow")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        qss_file = open('style_window.qss').read()

        self.textBrowser = QtWidgets.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(50, 70, 300, 400))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFontPointSize(10)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 25, 189, 30))
        self.pushButton.setObjectName("pushButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(350, 2, 21, 19))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(375, 2, 21, 19))
        self.toolButton_2.setObjectName("toolButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "ЗАПУСК"))
        self.toolButton.setText(_translate("MainWindow", "_"))
        self.toolButton_2.setText(_translate("MainWindow", "X"))





