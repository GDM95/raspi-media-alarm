import sys 
from alarm import AlarmSection
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialogButtonBox, QDialog, QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel 
from PyQt5.QtGui import QFont, QPainter 
from PyQt5.QtCore import QTimer, QTime, Qt, QDateTime, QRect
from datetime import datetime



class Window(QWidget):

    alarmSet = False
    clockTime = "7:30"
  
    def __init__(self): 
        super().__init__() 
  
        # setting geometry of main window 
        #self.setGeometry(100, 100, 800, 400)
        self.setStyleSheet("background-color: black;")
        self.showFullScreen()
  
        # creating a vertical layout 
        layout = QVBoxLayout() 
  
        # creating font object 
        stdFont = QFont('Arial', 100)
        timeFont = QFont('Arial', 250, QFont.Bold)



        ''' '''

        clockTimeLayout = QHBoxLayout()
        clockTimeLayout.addStretch(1)
        
        self.clockTimeLabel = QLabel()
        self.clockTimeLabel.setObjectName('clockTimeLabel')
        self.clockTimeLabel.mousePressEvent = self.editclockTime

        # Alarm Info (AM/PM and On/Off)
        self.clockAMPMLabel = QLabel()
        self.clockAMPMLabel.setObjectName('AMPM')
        self.clockAMPMLabel.setAlignment(Qt.AlignCenter)


        #alarmInfoLayout.addWidget(self.alarmActiveLabel)
        #alarmInfoLayout.addWidget(self.clockAMPMLabel)
        
        
        #clockTimeLayout.setAlignment(Qt.AlignHCenter)
        clockTimeLayout.addWidget(self.clockTimeLabel)
        clockTimeLayout.addWidget(self.clockAMPMLabel)
        
        #clockTimeLayout.addLayout(alarmInfoLayout)
        clockTimeLayout.addStretch(1)

        ''' '''
  
        # creating a label object 
        self.dateLabel = QLabel()
        self.dateLabel.setObjectName('date')
        self.dateLabel.setAlignment(Qt.AlignCenter)
        #self.dateLabel.setFont(stdFont)

        
        alarmSection = AlarmSection()
        alarmSection.mousePressEvent = self.editAlarmTime
        #alarmSection.mousePressEvent = lambda s : layout.setLayout


        # adding label to the layout 
        #layout.addWidget(self.dayOfWeekLabel)
        layout.addLayout(clockTimeLayout)
        layout.addWidget(self.dateLabel)
        layout.addWidget(alarmSection)


        # setting the layout to main window 
        self.setLayout(layout) 
  
        # creating a timer object 
        timer = QTimer(self) 
  
        # adding action to timer 
        timer.timeout.connect(self.showTime) 
  
        # update the timer every second 
        timer.start(1000)

        self.setStyleSheet("""
            #clockTimeLabel {
                color: lightgreen;
                font-size: 200px;
            }

            #AMPM {
                color: lightgreen;
                font-size: 25px;
            }

            #date {
                color: lightgreen;
                font-size: 50px;
            }

            Window {
                background-color: black;
            }

            QLabel {
                color: lightgreen;
                font-family: "Lucida Console", Monaco, monospace;
            }
        """)


    def editAlarmTime(self, s):
        print("click", s)
        window.setLayout(clockTimeLayout)


    def editclockTime(self, s):
        print("click", s)
        
        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")
  

    # method called by timer 
    def showTime(self): 
  
        # getting current time 
        #currentTime = QTime.currentTime() 
        now = QDateTime.currentDateTime()

        #print('Local datetime: ', now.toString(Qt.ISODate))
        print(now)
  
        # converting QTime object to string 
        labelTime = now.time().toString('H:mm')
        d = datetime.strptime(labelTime, "%H:%M")
        labelTime = d.strftime("%-I:%M")
        labelAMPM = now.time().toString('AP')
        labelDate = now.date().toString('ddd M/d/yy')
        #labelDayOfWeek = now.date().toString('dddd')
  
        # showing it to the label 
        print(labelTime)
        print(labelAMPM)
        self.clockTimeLabel.setText(labelTime)
        self.clockAMPMLabel.setText(labelAMPM)
        self.dateLabel.setText(labelDate)
        #self.dayOfWeekLabel.setText(labelDayOfWeek)

  
  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# showing all the widgets 
window.show() 
  
# start the app 
App.exit(App.exec_()) 
