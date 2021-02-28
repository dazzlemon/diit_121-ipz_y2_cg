"""
Cg3 Main
"""

from more_itertools import pairwise
from math import sqrt
import numpy as np
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from graphics_point3d import Point3d, GraphicsPoint3d
from forms_py import Ui_MainWindow

t_right_angle_dimetric = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, -1, 0],
])

class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def from3dto2d(x, y, z):
    #p4 = np.array([x, y, z, 1])
    #p4_ = t_right_angle_dimetric @ p4
    x_ = (x - z) / sqrt(2)#p4_[0]
    y_ = (x + 2*y + z) / sqrt(6)#p4_[1]
    return Point2d(x_, y_)


class Cg3(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._main_window = QMainWindow()
        self._main_ui     = Ui_MainWindow()
        self._main_ui.setupUi(self._main_window)
        self._init_canvas()
        self._init_signals()


    def _init_canvas(self):
        self._scene = QGraphicsScene()
#       self._scene.setSceneRect(0, 0, 800, 600)
        self._main_ui.gview.setScene(self._scene)
#       self._main_ui.gview.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.parallelepiped = Parallelepiped(
            GraphicsPoint3d(0, 0,   0),
            GraphicsPoint3d(100, 200, 0),
            100,
            100
        )
        self._update()


    def _init_signals(self):
        pass


    def _update(self):
        self._scene.clear()

        zero = GraphicsPoint3d(0, 0, 0)

        unit_vecs = [
            GraphicsPoint3d(1, 0, 0),
            GraphicsPoint3d(0, 1, 0),
            GraphicsPoint3d(0, 0, 1),
        ]

        zero = from3dto2d(zero.x, zero.y, zero.z)

        for p in unit_vecs:
            p_ = from3dto2d(p.x, p.y, p.z)
            self._scene.addLine(zero.x, zero.y, 1000 * p_.x, 1000 * p_.y)

        self.parallelepiped.paint(self._scene)


    def exec_(self):
        self._main_window.show()
        QApplication.exec_()


class Parallelepiped:
    """parallelepiped"""
    def __init__(self, start1: Point3d, start2: Point3d, w: float, h: float):
        """
        start1 & start2 - starting points for bases (that are connected by single edge)
        w, h - size of base
        w -> O_x
        h -> O_z
        """

        self.start1 = start1
        self.start2 = start2
        self.w = w
        self.h = h


    def paint(self, canvas: QGraphicsScene):
        face1 = [
            self.start1,
            GraphicsPoint3d(self.start1.x + self.w, self.start1.y,          self.start1.z),
            GraphicsPoint3d(self.start1.x + self.w, self.start1.y, self.start1.z + self.h),
            GraphicsPoint3d(self.start1.x,          self.start1.y, self.start1.z + self.h),
        ]
        face2 = [
            self.start2,
            GraphicsPoint3d(self.start2.x + self.w, self.start2.y,          self.start2.z),
            GraphicsPoint3d(self.start2.x + self.w, self.start2.y, self.start2.z + self.h),
            GraphicsPoint3d(self.start2.x,          self.start2.y, self.start2.z + self.h),
        ]

        for p in face1 + face2:
            p_ = from3dto2d(p.x, p.y, p.z)
            p.x = p_.x
            p.y = p_.y

        for p1, p2 in pairwise([*face1, face1[0]]):
            canvas.addLine(p1.x, p1.y, p2.x, p2.y)

        for p1, p2 in pairwise([*face2, face2[0]]):
            canvas.addLine(p1.x, p1.y, p2.x, p2.y)

        for p1, p2 in zip(face1, face2):
            canvas.addLine(p1.x, p1.y, p2.x, p2.y)

def main():
    """main"""
    import sys
    app = Cg3(sys.argv)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
