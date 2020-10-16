#!/usr/bin/python


from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QLabel, QApplication, QHBoxLayout, QVBoxLayout, QDialogButtonBox, QDialog, QMainWindow, QTimeEdit)
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtCore import QTimer, QTime, Qt, QDateTime, QRect, QSize
from datetime import datetime
from alarm_corner_display import AlarmCornerDisplay

import sys



class DateTimeDisplay(QWidget):

    def __init__(self, parent=None):
        super(DateTimeDisplay, self).__init__(parent)
        self.initUI()


    def initUI(self):
        # creating a vertical layout 
        layout = QVBoxLayout()
  
        clockTimeLayout = QHBoxLayout()
        clockTimeLayout.addStretch(1)
        
        self.clockTimeLabel = QLabel()
        self.clockTimeLabel.setObjectName('clockTimeLabel')
        self.clockTimeLabel.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        

        #self.clockTimeLabel.mousePressEvent = self.editclockTime

        # Alarm Info (AM/PM and On/Off)
        self.clockAMPMLabel = QLabel()
        self.clockAMPMLabel.setObjectName('AMPM')
        self.clockAMPMLabel.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

         
        #clockTimeLayout.setAlignment(Qt.AlignHCenter)
        clockTimeLayout.addWidget(self.clockTimeLabel)
        clockTimeLayout.addWidget(self.clockAMPMLabel)
        
        #clockTimeLayout.addLayout(alarmInfoLayout)
        clockTimeLayout.addStretch(1)

  
        # creating a label object 
        self.dateLabel = QLabel()
        self.dateLabel.setObjectName('date')
        self.dateLabel.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        
        #alarmSection = AlarmSection()
        #alarmSection.mousePressEvent = self.editAlarmTime
        #alarmSection.mousePressEvent = lambda s : layout.setLayout


        # adding label to the layout 
        #layout.addWidget(self.dayOfWeekLabel)
        layout.addLayout(clockTimeLayout)
        layout.addWidget(self.dateLabel)
        #layout.addWidget(alarmSection)

        self.alarmCornerDisplay = AlarmCornerDisplay()
        layout.addWidget(self.alarmCornerDisplay)


        # setting the layout to main window 
        self.setLayout(layout) 

        self.showTime() 

  
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
                font-size: 50px;
                margin-bottom: 15px;
            }

            #date {
                color: lightgreen;
                font-size: 50px;
            }

            #alarmText {
                font-size: 30px;
            }

            
            QLabel {
                color: lightgreen;
                font-family: "Lucida Console", Monaco, monospace;
            }
        """)




    def editAlarmTime(self, s):
        print("click", s)
        #window.setLayout(clockTimeLayout)



    # method called by timer 
    def showTime(self): 
  
        # getting current time 
        #currentTime = QTime.currentTime() 
        now = QDateTime.currentDateTime()

        #print('Local datetime: ', now.toString(Qt.ISODate))
  
        # converting QTime object to string 
        labelTime = now.time().toString('H:mm')
        d = datetime.strptime(labelTime, "%H:%M")
        labelTime = d.strftime("%-I:%M")
        labelAMPM = now.time().toString('AP')
        labelDate = now.date().toString('ddd M/d/yy')
        #labelDayOfWeek = now.date().toString('dddd')
  
        # showing it to the label 
        self.clockTimeLabel.setText(labelTime)
        self.clockAMPMLabel.setText(labelAMPM)
        self.dateLabel.setText(labelDate)
        #self.dayOfWeekLabel.setText(labelDayOfWeek)