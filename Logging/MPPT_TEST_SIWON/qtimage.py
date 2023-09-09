import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QTransform

class ImageViewer(QGraphicsView):
    def __init__(self):
        super().__init__()

        # QGraphicsScene 생성
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        # 이미지 로드
        self.image = QPixmap("one.png")

        # 이미지 회전 각도 초기화
        self.rotation_angle = 0

        # 타이머 설정
        self.timer = QTimer()
        self.timer.timeout.connect(self.rotateImage)
        self.timer.start(100)  # 100ms마다 회전

    def rotateImage(self):
        # 이미지 회전 각도 업데이트
        self.rotation_angle += 1
        if self.rotation_angle >= 360:
            self.rotation_angle = 0

        # QGraphicsScene 초기화
        self.scene.clear()

        # 회전된 이미지를 그래픽 항목으로 추가
        item = self.scene.addPixmap(self.image)
        item.setTransformOriginPoint(item.boundingRect().center())
        item.setPos(0, 0)
        item.setRotation(self.rotation_angle)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    exit(app.exec_())
