import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget
from alarm import AlarmSection
from date_time_display import DateTimeDisplay



class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.ToolsBTN = QPushButton('text', self)
        #self.ToolsBTN.move(50, 350)


class UIToolTab(QWidget):
    def __init__(self, parent=None):
        super(UIToolTab, self).__init__(parent)
        self.CPSBTN = QPushButton("text2", self)

        #self.CPSBTN.move(100, 350)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.showFullScreen()
        self.startUIToolTab()
        self.setStyleSheet("""
            MainWindow {
                background-color: black;
            }
        """)

    def startUIToolTab(self, event=None):
        #self.ToolTab = UIToolTab(self)
        self.ToolTab = DateTimeDisplay(self)
        self.setWindowTitle("Media Alarm")
        self.ToolTab.alarmCornerDisplay.alarmLabel.mousePressEvent = self.startUIWindow
        self.setCentralWidget(self.ToolTab)
        self.show()

    def startUIWindow(self, event):
        print("Second window clicked: ", event)
        #self.Window = UIWindow(self)
        self.Window = AlarmSection(self)
        self.setWindowTitle("Edit Alarm")
        self.setCentralWidget(self.Window)
        #self.Window.ToolsBTN.clicked.connect(self.startUIToolTab)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())