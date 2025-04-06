from PyQt5 import QtCore, QtWidgets


class Ui_CalendarAppMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("CalendarAppMainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(20, 20, 300, 250))
        self.calendar.setObjectName("calendar")

        self.eventList = QtWidgets.QListWidget(self.centralwidget)
        self.eventList.setGeometry(QtCore.QRect(340, 20, 240, 250))
        self.eventList.setObjectName("eventList")

        self.addEventButton = QtWidgets.QPushButton(self.centralwidget)
        self.addEventButton.setGeometry(QtCore.QRect(20, 290, 560, 40))
        self.addEventButton.setObjectName("addEventButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtWidgets.QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Календарь"))
        self.addEventButton.setText(_translate("MainWindow", "Добавить событие"))
