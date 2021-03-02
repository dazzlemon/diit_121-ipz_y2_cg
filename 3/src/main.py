"""
Cg3 Main
"""
import numpy as np
from PyQt5.QtGui      import QPen, QBrush
from PyQt5.QtCore     import Qt
from PyQt5.QtWidgets  import QApplication, QMainWindow, QGraphicsScene
from forms_py         import Ui_MainWindow
from graphics_point3d import GraphicsPoint3d, world3d_to_view
from parallelepiped   import Parallelepiped

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
            GraphicsPoint3d(10, 0, 10),
            GraphicsPoint3d(110, 210, 0),
            100,
            100
        )
        self._update()


    def _init_signals(self):
        def rot_x(x):
            self.parallelepiped.rot_x = np.deg2rad(x)
            self._update()

        def rot_y(y):
            self.parallelepiped.rot_y = np.deg2rad(y)
            self._update()

        def rot_z(z):
            self.parallelepiped.rot_z = np.deg2rad(z)
            self._update()

        self._main_ui.xDial.valueChanged.connect(rot_x)
        self._main_ui.yDial.valueChanged.connect(rot_y)
        self._main_ui.zDial.valueChanged.connect(rot_z)

        def scale(val):
            self.parallelepiped.scale = val
            self._update()
        self._main_ui.scaleSpinBox.valueChanged.connect(scale)

    def _update(self):
        self._scene.clear()

        zero = world3d_to_view(GraphicsPoint3d(0, 0, 0))

        unit_vecs = [
            (GraphicsPoint3d(1, 0, 0), "x"),
            (GraphicsPoint3d(0, 1, 0), "y"),
            (GraphicsPoint3d(0, 0, 1), "z"),
        ]

        axes_len = 1000
        for p, name in unit_vecs:
            p_ = world3d_to_view(p)
            self._scene.addLine(zero.x, zero.y, axes_len * p_.x, axes_len * p_.y)
            text = self._scene.addText(name)
            text.setPos(p_.x * axes_len, p_.y * axes_len)

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
