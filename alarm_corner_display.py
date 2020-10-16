#!/usr/bin/python


from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QLabel, QApplication, QHBoxLayout, QVBoxLayout, QDialogButtonBox, QDialog, QMainWindow, QTimeEdit)
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtCore import QTimer, QTime, Qt, QDateTime, QRect, QSize
from datetime import datetime
import sys



class AlarmCornerDisplay(QWidget):

    def __init__(self, parent=None):
        super(AlarmCornerDisplay, self).__init__(parent)
        self.initUI()


    def initUI(self):
        self.isAlarmActive = False        
  
        alarmCornerLayout = QHBoxLayout() 
        alarmCornerLayout.addStretch(0)

        pixmap = QPixmap('ios_alarm_inactive.png')
        pixmap = pixmap.scaled(QSize(33,33),  Qt.KeepAspectRatio);
        self.lbl = QLabel()
        self.lbl.setObjectName("alarmIcon")
        self.lbl.setPixmap(pixmap)
        self.lbl.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        self.lbl.mousePressEvent = self.clickAlarmActive
        alarmCornerLayout.addWidget(self.lbl)

        self.alarmLabel = QLabel()
        self.alarmLabel.setText("7:30 AM")
        self.alarmLabel.setObjectName('alarmText')
        self.alarmLabel.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        alarmCornerLayout.addWidget(self.alarmLabel)
        

        # setting the layout to main window 
        self.setLayout(alarmCornerLayout) 
        

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
                font-size: 32px;
            }

            #alarmIcon {
                margin-right: 10px;
            }

            
            QLabel {
                color: lightgreen;
                font-family: "Lucida Console", Monaco, monospace;
            }
        """)



    def clickAlarmActive(self, s):
        print("click", s)

        if(self.isAlarmActive == False):
            resStr = 'ios_alarm_active.png'
        else:
            resStr = 'ios_alarm_inactive.png'

        self.isAlarmActive = not self.isAlarmActive

        pixmap = QPixmap(resStr)
        pixmap = pixmap.scaled(QSize(33,33),  Qt.KeepAspectRatio);
        self.lbl.setPixmap(pixmap)



    def editAlarmTime(self, s):
        print("click", s)
        #window.setLayout(clockTimeLayout)