import sys
import os
import time
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
import subprocess

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect the pushButton's click event to a custom function
        self.ui.pushButton.clicked.connect(self.on_buttonAdd1_click)
        self.ui.pushButton_5.clicked.connect(self.on_buttonDump_click)
        self.ui.pushButton_6.clicked.connect(self.on_buttonSearch_click)

    def on_buttonAdd1_click(self):
        print("Button Clicked!")

    def on_buttonDump_click(self):
        current_time = int(time.time())
        filename = f'dump_ecozona_{current_time}.mfd'
        command = f'mfoc -O {filename} -k KEYA'
        os.system(command)
    def on_buttonSearch_click(self):
        output = subprocess.check_output(["nfc-list"]).decode("utf-8")
        if "ISO14443A" in output:
            #enable all the buttons
            self.ui.label.setText("rilevato")
        else:
            self.ui.label.setText("")
            #disable all the buttons



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
