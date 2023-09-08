import sys
import os
import time
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
import subprocess
import re

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Connect the pushButton's click event to a custom function
        self.ui.pushButton.clicked.connect(self.on_buttonAdd1_click)
        self.ui.pushButton_4.clicked.connect(self.on_buttonZero_click)
        self.ui.pushButton_5.clicked.connect(self.on_buttonDump_click)
        self.ui.pushButton_6.clicked.connect(self.on_buttonSearch_click)

    def on_buttonAdd1_click(self):
        fileBin = dumpCard()
        with open(fileBin, 'rb') as file:
            byte_sequence = file.read()
        start_index = 0x20
        section = byte_sequence[start_index:]
        hex_string = binascii.hexlify(section).decode()
        first_8_characters = hex_string[:8]
        print(first_8_characters)
        result = first_8_characters.replace("0", "")
        if len(result) == 0:
            new_balance = "64 00 00 00"
            with open(fileBin, 'rb+') as file:
                file.seek(32)
                file.write(bytes.fromhex(new_balance))
                file.seek(40)
                file.write(bytes.fromhex(new_balance))
        else:
            result_int = int(result, 16)
            result_int += 100
            result = hex(result_int)[2:]
            new_balance = result
            for i in range(8 - len(result)):
                new_balance = new_balance + "0"
            print(new_balance)
            with open(fileBin, 'rb+') as file:
                file.seek(32)
                file.write(bytes.fromhex(new_balance))
                file.seek(40)
                file.write(bytes.fromhex(new_balance))
        command = f'nfc-mfclassic w a u {fileBin} {fileBin}'
        os.system(command)


    def on_buttonDump_click(self):
        current_time = int(time.time())
        filename = f'dump_ecozona_{current_time}.mfd'
        command = f'mfoc -O {filename} -k KEYA'
        os.system(command)

    def dumpCard():
        current_time = int(time.time())
        filename = f'dump_ecozona_{current_time}.mfd'
        command = f'mfoc -O {filename} -k KEYA'
        os.system(command)
        return filename

    #search
    def on_buttonSearch_click(self):
        output = subprocess.check_output(["nfc-list"]).decode("utf-8")
        if "ISO14443A" in output:
            #enable all the buttons
            uid_match = re.search(r"UID \(NFCID1\): (\w+ \w+ \w+ \w+)", output)
            uid_value = uid_match.group(1)
            self.ui.label.setText("rilevato")
            self.ui.label_2.setText("UID: " + uid_value)
            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
        else:
            self.ui.label.setText("")
            self.ui.label_2.setText("")
            #disable all the buttons
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton_5.setEnabled(False)
            self.ui.pushButton_6.setEnabled(False)

    def on_buttonZero_click(self):
        fileBin = dumpCard()
        with open(fileBin, 'rb+') as file:
            file.seek(32)
            file.write(bytes.fromhex("00 00 00 00"))
            file.seek(36)
            file.write(bytes.fromhex("FF FF FF FF"))
            file.seek(40)
            file.write(bytes.fromhex("00 00 00 00"))
        command = f'nfc-mfclassic w a u {fileBin} {fileBin}'
        os.system(command)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
