from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QGroupBox, QLabel
from PyQt5.QtCore import Qt

box1 = "dasd"
box2 = 2
box3 = 3
box4 = 4
box5 = 5
box6 = 6
box7 = 7
box8 = 8
box9 = 9
box10 = 10

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        self.setLayout(grid)

        for i in range(10):
            group_box = QGroupBox(f'Box {i+1}')
            group_box.setAlignment(Qt.AlignCenter)
            grid.addWidget(group_box, i // 2, i % 2)

            label = QLabel(str(globals()[f'box{i+1}']))
            label.setAlignment(Qt.AlignCenter)
            group_box.setLayout(QGridLayout())
            group_box.layout().addWidget(label)

            group_box.setStyleSheet('''
                QGroupBox {
                    border: 1px solid black;
                    border-radius: 5px;
                    font-size: 16px;
                    font-weight: bold;
                }
            ''')

        self.show()

app = QApplication([])
window = MainWindow()
app.exec_()

