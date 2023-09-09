from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

def on_button_click():
    alert = QMessageBox()
    alert.setText('Hello, World!')
    alert.exec_()

app = QApplication([])
window = QWidget()
button = QPushButton('Click me!', window)
button.clicked.connect(on_button_click)
window.show()
app.exec_()