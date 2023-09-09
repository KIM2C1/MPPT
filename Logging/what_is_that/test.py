import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reverse String")

        self.input_label = QLabel("Input:", self)
        self.input_label.move(50, 50)

        self.input_edit = QLineEdit(self)
        self.input_edit.setGeometry(100, 50, 150, 30)

        self.reverse_button = QPushButton("Reverse", self)
        self.reverse_button.setGeometry(100, 100, 100, 30)
        self.reverse_button.clicked.connect(self.reverse)

        self.output_label = QLabel("Output:", self)
        self.output_label.move(50, 150)

        self.output_edit = QLineEdit(self)
        self.output_edit.setGeometry(100, 150, 150, 30)
        self.output_edit.setReadOnly(True)

    def reverse(self):
        input_text = self.input_edit.text()
        output_text = input_text[::-1]
        self.output_edit.setText(output_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    os.system('pasue')
