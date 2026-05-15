# This is a stopwatch in python using PyQt5 library
import sys #sys helps Python interact with the system
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer, Qt

# QTimer library : runs code repeatedly after fixed interval

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        # add label to show text on screen
        self.time_label = QLabel("00:00:00",self)

        # timer object
        self.timer = QTimer(self)

        # start button object
        self.start_button = QPushButton("Start")

        # stop button object
        self.stop_button = QPushButton("Stop")
       # disable stop button initially
        self.stop_button.setEnabled(False)

        # reset button object
        self.reset_button = QPushButton("Reset")

        # add title and set window size
        self.setWindowTitle("Stopwatch")
        self.resize(400,300)

        # setting layout (it is important to center the label)
        vbox = QVBoxLayout() # for vertical layout
        vbox.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.time_label) # add time_label to layout

        hbox = QHBoxLayout() # for horizontal layout
        hbox.addWidget(self.start_button) # add start button to layout
        hbox.addWidget(self.stop_button) # add stop button to layout
        hbox.addWidget(self.reset_button) # add reset button to layout
        
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # centering label
        self.time_label.setAlignment(Qt.AlignCenter)

        # styling

        # setting stylesheet like fontsize and font weight
        self.time_label.setStyleSheet("font-weight: bold;"
                                      "font-size:140px;"
                                      "color:#defd28")

        self.setStyleSheet("background-color:#0b0b0b;")

        # style start_button
        self.start_button.setStyleSheet("QPushButton {"
                                         "font-size:24px;"
                                         "background-color:#ffffff;"
                                         "padding:10px;"
                                        "border-radius:15px;"
                                        "}"
                                         
                                        "QPushButton:hover{"
                                         "background-color:#48ef1e;"
                                         "font-weight: bold;"
                                        "}"

                                        "QPushButton:disabled{"
                                         "background-color:#7d7d7d;"
                                         "color:#dcdcdc;"
                                        "}"
                                        )
        

        self.stop_button.setStyleSheet( "QPushButton {"
                                         "font-size:24px;"
                                         "background-color:#ffffff;"
                                         "padding:10px;"
                                         "border-radius:15px;"
                                        "}"
                                         
                                        "QPushButton:hover{"
                                         "background-color:#f11818;"
                                         "color: white;"
                                         "font-weight: bold;"
                                        "}"
                                        
                                        "QPushButton:disabled{"
                                         "background-color:#7d7d7d;"
                                         "color:#dcdcdc;"
                                         "}"
                                        )
        

        self.reset_button.setStyleSheet( "QPushButton {"
                                        "font-size:24px;"
                                        "background-color:#ffffff;"
                                        "padding:10px;"
                                        "border-radius:15px;"
                                        "}"
                                         
                                        "QPushButton:hover{"
                                        "background-color:#5aecf3;"
                                        "font-weight: bold;"
                                        "}"
                                        )

        

        # connect timer to function
        self.timer.timeout.connect(self.update_time_display)
       

        # store seconds
        self.elapsed_seconds = 0


        # connect start button to start_stopwatch function
        self.start_button.clicked.connect(self.start_stopwatch)

        # connect stop button to stop_stopwatch function
        self.stop_button.clicked.connect(self.stop_stopwatch)

        # connect reset button to reset_stopwatch function
        self.reset_button.clicked.connect(self.reset_stopwatch)


    def update_time_display(self):
        self.elapsed_seconds += 1

        seconds = self.elapsed_seconds % 60
        
        # // is floor division
        minutes = (self.elapsed_seconds // 60) % 60

        hours  = self.elapsed_seconds // 3600

        time_text = f"{hours:02}:{minutes:02}:{seconds:02}"


        self.time_label.setText(time_text)

    def start_stopwatch(self):
        # stopwatch start due to this
        self.timer.start(1000)

        # enable stop button initially
        self.stop_button.setEnabled(True)

        # disable start button after timer start
        self.start_button.setEnabled(False)

    def stop_stopwatch(self):
        # stopwatch start due to this , stop emmitting timeout signal
        self.timer.stop()

        # enable start button after timer stop
        self.start_button.setEnabled(True)

        # disable stop button when timer stop
        self.stop_button.setEnabled(False)

    def reset_stopwatch(self):
        self.timer.stop()
        self.elapsed_seconds = 0
        self.time_label.setText("00:00:00")

        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv) # (sys.argv) It stores command line arguments.

    window = Stopwatch()
    window.show()

    sys.exit(app.exec_())
