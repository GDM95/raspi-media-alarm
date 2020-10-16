#!/usr/bin/python


from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QLabel, QApplication, QHBoxLayout, QVBoxLayout, QDialogButtonBox, QDialog, QMainWindow, QTimeEdit)
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtCore import QTimer, QTime, Qt, QDateTime, QRect, QSize
from datetime import datetime
import sys



class AlarmSection(QWidget):

    def __init__(self, parent=None):
        super(AlarmSection, self).__init__(parent)
        self.parent = parent

        f = open("alarm.txt", "r")
        print(f.readline())

        self.hour = 7
        self.minute = 30
        self.ampm = "AM"
        self.initUI()


    def initUI(self):

        self.doneBtn = QLabel()
        self.doneBtn.setText("Done")
        self.doneBtn.setObjectName('doneBtn')
        self.doneBtn.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.doneBtn.mousePressEvent = self.handleDoneBtn #(self.hour, self.minute, self.ampm) actually construct date object and return
    

        self.monb = QPushButton('Mon', self)
        self.monb.setCheckable(True)
        self.monb.clicked[bool].connect(self.setColor)

        self.tuesb = QPushButton('Tue', self)
        self.tuesb.setCheckable(True)
        self.tuesb.clicked[bool].connect(self.setColor)

        self.wedb = QPushButton('Wed', self)
        self.wedb.setCheckable(True)
        self.wedb.clicked[bool].connect(self.setColor)

        self.thursb = QPushButton('Thur', self)
        self.thursb.setCheckable(True)
        self.thursb.clicked[bool].connect(self.setColor)

        self.frib = QPushButton('Fri', self)
        self.frib.setCheckable(True)
        self.frib.clicked[bool].connect(self.setColor)

        self.satb = QPushButton('Sat', self)
        self.satb.setCheckable(True)
        self.satb.clicked[bool].connect(self.setColor)

        self.sunb = QPushButton('Sun', self)
        self.sunb.setCheckable(True)
        self.sunb.clicked[bool].connect(self.setColor)

        daysOfWeekLayout = QHBoxLayout()
        daysOfWeekLayout.addWidget(self.monb)
        daysOfWeekLayout.addWidget(self.tuesb)
        daysOfWeekLayout.addWidget(self.wedb)
        daysOfWeekLayout.addWidget(self.thursb)
        daysOfWeekLayout.addWidget(self.frib)
        daysOfWeekLayout.addWidget(self.satb)
        daysOfWeekLayout.addWidget(self.sunb)



        testTime = QDateTime.currentDateTime().addSecs(50000).time()

        alarmTimeLayout = QHBoxLayout()
        alarmTimeLayout.addStretch(1)

        # VBox for editing hours
        hourLayout = QVBoxLayout()

        pixmap = QPixmap('up_arrow.png')
        pixmap = pixmap.scaled(QSize(60,60),  Qt.KeepAspectRatio);
        self.upArrowHour = QLabel()
        self.upArrowHour.setObjectName("upArrowHour")
        self.upArrowHour.setPixmap(pixmap)
        self.upArrowHour.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.upArrowHour.mousePressEvent = self.handleClickUpHour
        hourLayout.addWidget(self.upArrowHour)

        self.hourLabel = QLabel()
        #labelAlarmTime = testTime.toString('H:mm')
        #labelHour = testTime.toString('H')
        d = datetime.strptime(str(self.hour), "%H")
        labelHour = d.strftime("%-I")
        self.hourLabel.setText(labelHour)
        self.hourLabel.setObjectName('hourLabel')
        self.hourLabel.setAlignment(Qt.AlignCenter)
        hourLayout.addWidget(self.hourLabel)

        pixmap = QPixmap('down_arrow.png')
        pixmap = pixmap.scaled(QSize(60,60),  Qt.KeepAspectRatio);
        self.downArrowHour = QLabel()
        self.downArrowHour.setObjectName("downArrowHour")
        self.downArrowHour.setPixmap(pixmap)
        self.downArrowHour.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.downArrowHour.mousePressEvent = self.handleClickDownHour
        hourLayout.addWidget(self.downArrowHour)



        # VBox for editing minutes
        minuteLayout = QVBoxLayout()
        pixmap = QPixmap('up_arrow.png')
        pixmap = pixmap.scaled(QSize(60,60),  Qt.KeepAspectRatio);
        self.upArrowMinute = QLabel()
        self.upArrowMinute.setObjectName("upArrowMinute")
        self.upArrowMinute.setPixmap(pixmap)
        self.upArrowMinute.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.upArrowMinute.mousePressEvent = self.handleClickUpMinute
        minuteLayout.addWidget(self.upArrowMinute)

        self.minuteLabel = QLabel()
        #labelAlarmTime = testTime.toString('H:mm')
        #labelMinute = testTime.toString('mm')
        d = datetime.strptime(str(self.minute), "%M")
        labelMinute = d.strftime("%M")
        self.minuteLabel.setText(labelMinute.zfill(2))
        self.minuteLabel.setObjectName('minuteLabel')
        self.minuteLabel.setAlignment(Qt.AlignCenter)
        minuteLayout.addWidget(self.minuteLabel)

        pixmap = QPixmap('down_arrow.png')
        pixmap = pixmap.scaled(QSize(60,60),  Qt.KeepAspectRatio);
        self.downArrowMinute = QLabel()
        self.downArrowMinute.setObjectName("downArrowMinute")
        self.downArrowMinute.setPixmap(pixmap)
        self.downArrowMinute.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.downArrowMinute.mousePressEvent = self.handleClickDownMinute
        minuteLayout.addWidget(self.downArrowMinute)



        # QLabel for time colon (7:30)
        self.alarmColon = QLabel()
        self.alarmColon.setObjectName('alarmColon')
        self.alarmColon.setText(':')
        self.alarmColon.setAlignment(Qt.AlignCenter)


        # Alarm Info (AM/PM and On/Off)
        self.alarmAMPMLabel = QLabel()
        self.alarmAMPMLabel.setObjectName('AMPM')
        labelAlarmAMPM = testTime.toString('AP')
        self.alarmAMPMLabel.setText(self.ampm)
        self.alarmAMPMLabel.setAlignment(Qt.AlignCenter)
        self.alarmAMPMLabel.mousePressEvent = self.handleClickAMPM

        
        #clockTimeLayout.setAlignment(Qt.AlignHCenter)
        alarmTimeLayout.addLayout(hourLayout)
        alarmTimeLayout.addWidget(self.alarmColon)
        alarmTimeLayout.addLayout(minuteLayout)
        alarmTimeLayout.addWidget(self.alarmAMPMLabel)
        
        #clockTimeLayout.addLayout(alarmInfoLayout)
        alarmTimeLayout.addStretch(1)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.doneBtn)
        mainLayout.addLayout(alarmTimeLayout)
        mainLayout.addLayout(daysOfWeekLayout)
        

        self.setStyleSheet("""
            #hourLabel {
                color: lightgreen;
                font-size: 170px;
                font-family: "Lucida Console", Monaco, monospace;
            }

            #minuteLabel {
                color: lightgreen;
                font-size: 170px;
                font-family: "Lucida Console", Monaco, monospace;
            }

            #upArrowHour {
                margin-bottom: 20px;
            }

            #downArrowHour {
                margin: 0;
            }

            #upArrowMinute {
                margin-bottom: 20px;
            }

            #downArrowMinute {
                margin: 0;
            }

            #alarmColon {
                font-size: 100px;
                color: lightgreen;
                font-size: 170px;
                margin-bottom: 5px;
                font-family: "Lucida Console", Monaco, monospace;
            }

            #AMPM {
                color: lightgreen;
                font-family: "Lucida Console", Monaco, monospace;
                font-size: 75px;
                margin-bottom: 15px;
            }

            #alarmActive {
                color: lightgreen;
                font-size: 25px;
            }

            #edit {
                color: lightgreen;
                background-color: black;
            }

            #doneBtn {
                color: lightgreen;
                font-size: 25px;
                font-family: "Lucida Console", Monaco, monospace;
                max-height: 30px;
                max-width: 60px;
            }

            QHBoxLayout {
                background-color: red;
            }

            QPushButton {
                font-size: 20px;
                font-family: "Lucida Console", Monaco, monospace;
                padding: 5px;
                border: 1px solid silver;
                border-radius: 5px;
            }

            QPushButton:!checked { 
                color: lightgreen;
            }

            QPushButton:checked {
                background-color: lightgreen;
                color: black;
            }


            AlarmSection {
                background-color: black;
            }
        """)


        self.setLayout(mainLayout)
        self.setWindowTitle('Day Toggles')
        self.show()


    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = True
        else:
            val = False

        print(source.text())


    def handleClickAMPM(self, e):
        print(e)

        if(self.ampm == "AM"):
            self.ampm = "PM"
        else:
            self.ampm = "AM"
        self.alarmAMPMLabel.setText(self.ampm)

    def handleClickUpHour(self, e):
        print(e)

        if self.hour == 12:
            self.hour = 1
        else:
            self.hour += 1
        self.hourLabel.setText(str(self.hour))

    def handleClickDownHour(self, e):
        print(e)

        if self.hour == 1:
            self.hour = 12
        else:
            self.hour -= 1
        self.hourLabel.setText(str(self.hour))

    def handleClickUpMinute(self, e):
        print(e)

        if self.minute == 59:
            self.minute = 0
        else:
            self.minute += 1
        self.minuteLabel.setText(str(self.minute).zfill(2))
    
    def handleClickDownMinute(self, e):
        print(e)

        if self.minute == 0:
            self.minute = 59
        else:
            self.minute -= 1
        self.minuteLabel.setText(str(self.minute).zfill(2))

    def handleDoneBtn(self, e):

        x = datetime(2020, 9, 16, self.hour if self.ampm == "AM" else self.hour + 12, self.minute)
        print(x)

        # create date object and write to file -- also start cron job
        f = open("alarm.txt", "w")
        f.write(str(x))
        f.close()
        self.parent.startUIToolTab()




def main():
    app = QApplication(sys.argv)
    ex = AlarmSection()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()