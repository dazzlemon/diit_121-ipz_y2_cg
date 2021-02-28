"""
Cg3 Main
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from graphics_point3d import Point3d, GraphicsPoint3d
from forms_py import Ui_MainWindow

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
        self._scene.setSceneRect(0, 0, 800, 600)
        self._main_ui.gview.setScene(self._scene)
        self._main_ui.gview.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self.parallelepiped = Parallelepiped(
            GraphicsPoint3d(0, 0, 0),
            GraphicsPoint3d(0, 0, 1),
            1,
            1
        )
        self._update()

    def _init_signals(self):
        pass


    def _update(self):
        self._scene.clear()
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
        """

        self.start1 = start1
        self.start2 = start2
        self.w = w
        self.h = h


    def paint(self, canvas: QGraphicsScene):
        pass


def main():
    """main"""
    import sys
    app = Cg3(sys.argv)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
