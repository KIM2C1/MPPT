import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import QTimer, QPoint

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("image_qt.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.angle = 0
        self.rotation_center = QPoint(43, 14)  # 회전 중심점 좌표 설정

        # QTimer를 사용하여 일정 간격으로 이미지 회전
        self.timer = QTimer()
        self.timer.timeout.connect(self.rotate_image)
        self.timer.start(1000)  # 1초마다 타이머가 작동하도록 설정

    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)

    def rotate_image(self):
        self.angle += 5
        transform = QTransform().translate(self.rotation_center.x(), self.rotation_center.y()).rotate(self.angle).translate(-self.rotation_center.x(), -self.rotation_center.y())
        rotated_pixmap = self.pixmap.transformed(transform)
        self.label.setPixmap(rotated_pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    # 이미지 로드 및 표시
    image_path = "pngwing.com.png"
    myWindow.pixmap = QPixmap(image_path)
    myWindow.load_image(image_path)

    myWindow.show()

    app.exec_()

