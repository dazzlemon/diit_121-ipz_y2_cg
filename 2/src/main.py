"""
MAIN
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen, QBrush
from forms_py import Ui_MainWindow
from graphics.items import GraphicsPoint
from graphics.canvas import QCanvas
from peppe_frog import PeppeFrog

class Cg2(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._main_window = QMainWindow()
        self._main_ui = Ui_MainWindow()
        self._main_ui.setupUi(self._main_window)
        self._init_canvas()
        self._init_signals()


    def _init_canvas(self):
        self._scene = QGraphicsScene()
        self._scene.setSceneRect(0, 0, 800, 600)
        self._main_ui.gview.setScene(self._scene)
        self._main_ui.gview.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self._canvas = QCanvas(self._scene)
        self.frog    = PeppeFrog()
        self._about_point = GraphicsPoint(600, 600)
        self._update()


    def _init_signals(self):
        def move(dx, dy):
            def move_():
                self.frog.move(GraphicsPoint(dx, dy))
                self._update()
            return move_
        self._main_ui.moveRightButton.pressed.connect(move(10, 0))
        self._main_ui.moveLeftButton.pressed.connect(move(-10, 0))
        self._main_ui.moveUpButton.pressed.connect(move(0, -10))
        self._main_ui.moveDownButton.pressed.connect(move(0, 10))
        self._main_ui.moveRightUpButton.pressed.connect(move(10, -10))
        self._main_ui.moveRightDownButton.pressed.connect(move(10, 10))
        self._main_ui.moveLeftDownButton.pressed.connect(move(-10, 10))
        self._main_ui.moveLeftUpButton.pressed.connect(move(-10, -10))

        self._main_ui.moveRightButton.setAutoRepeat(True)
        self._main_ui.moveLeftButton.setAutoRepeat(True)
        self._main_ui.moveUpButton.setAutoRepeat(True)
        self._main_ui.moveDownButton.setAutoRepeat(True)
        self._main_ui.moveRightUpButton.setAutoRepeat(True)
        self._main_ui.moveRightDownButton.setAutoRepeat(True)
        self._main_ui.moveLeftDownButton.setAutoRepeat(True)
        self._main_ui.moveLeftUpButton.setAutoRepeat(True)

        def rotate(rad):
            def rot():
                self.frog.rotate(self._about_point, rad)
                self._update()
            return rot
        self._main_ui.rotateClockwiseButton.pressed.connect(rotate(0.1))
        self._main_ui.rotateAnticlockwiseButton.pressed.connect(rotate(-0.1))

        self._main_ui.rotateClockwiseButton.setAutoRepeat(True)
        self._main_ui.rotateAnticlockwiseButton.setAutoRepeat(True)

        def scale(mul):
            def scale_():
                self.frog.scale(self._about_point, mul, mul)
                self._update()
            return scale_
        self._main_ui.scaleUpButton.pressed.connect(scale(1.2))
        self._main_ui.scaleDownButton.pressed.connect(scale(0.8))

        self._main_ui.scaleUpButton.setAutoRepeat(True)
        self._main_ui.scaleDownButton.setAutoRepeat(True)

        def scene_click(event):
            self._about_point.x = event.scenePos().x()
            self._about_point.y = event.scenePos().y()
            self._update()
        self._scene.mouseReleaseEvent = scene_click

        def checkbox_toggled(ref):
            def toggle(val):
                ref._is_transformable = val
            return toggle
        self._main_ui.bodyCheck.stateChanged.connect(checkbox_toggled(self.frog._items[0]))
        self._main_ui.rightEyeCheck.stateChanged.connect(checkbox_toggled(self.frog._items[1]))
        self._main_ui.leftEyeCheck.stateChanged.connect(checkbox_toggled(self.frog._items[2]))
        self._main_ui.mouthCheck.stateChanged.connect(checkbox_toggled(self.frog._items[3]))

        self._main_ui.bodyCheck.setChecked(self.frog._items[0]._is_transformable)
        self._main_ui.rightEyeCheck.setChecked(self.frog._items[1]._is_transformable)
        self._main_ui.leftEyeCheck.setChecked(self.frog._items[2]._is_transformable)
        self._main_ui.mouthCheck.setChecked(self.frog._items[3]._is_transformable)


    def _update(self):
        self._scene.clear()
        self.frog.paint(self._canvas)
        self._scene.addEllipse(self._about_point.x, self._about_point.y,
                               4, 4,
                               QPen(QColor(255, 0, 0)), QBrush(QColor(255, 0, 0)))
        self._scene.update()

    def exec_(self):
        self._main_window.show()
        QApplication.exec_()


if __name__ == '__main__':
    import sys
    app = Cg2(sys.argv)
    sys.exit(app.exec_())
