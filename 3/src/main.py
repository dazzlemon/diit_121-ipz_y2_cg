"""
Cg3 Main
"""

from PyQt5.QtGui      import QPen, QBrush
from PyQt5.QtCore     import Qt
from PyQt5.QtWidgets  import QApplication, QMainWindow, QGraphicsScene
from forms_py         import Ui_MainWindow
from graphics_point3d import GraphicsPoint3d
from parallelepiped   import Parallelepiped
from graphics_point3d import from3dto2d

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


def main():
    """main"""
    import sys
    app = Cg3(sys.argv)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
