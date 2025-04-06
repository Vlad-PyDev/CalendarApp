import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox
from ui import Ui_CalendarAppMainWindow


class CalendarAppMainWindow(QMainWindow, Ui_CalendarAppMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addEventButton.clicked.connect(self.add_event)
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #cfd9df, stop:1 #e2ebf0);
            }
            QPushButton, QCalendarWidget, QListWidget {
                font-size: 16px;
            }
        """)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_event(self):
        date = self.calendar.selectedDate().toString("dd.MM.yyyy")
        event_text, ok = QInputDialog.getText(self, "Добавить событие", "Введите событие:")
        if ok and event_text:
            self.eventList.addItem(f"{date}: {event_text}")
        elif ok:
            QMessageBox.warning(self, "Ошибка", "Событие не может быть пустым.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarAppMainWindow()
    window.show()
    sys.exit(app.exec_())
