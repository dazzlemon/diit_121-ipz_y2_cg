"""
MAIN
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt5.QtCore import Qt
from forms_py import Ui_MainWindow
from graphics.items import GraphicsLine
from graphics.canvas import QCanvas

class Cg2(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._main_window = QMainWindow()
        self._main_ui = Ui_MainWindow()
        self._main_ui.setupUi(self._main_window)
        self._init_canvas()


    def _init_canvas(self):
        self._scene = QGraphicsScene()
        self._main_ui.gview.setScene(self._scene)
        self._main_ui.gview.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        self._canvas = QCanvas(self._scene)
        self._items = [GraphicsLine(0, 0, 500, 500)]

        for i in self._items:
            i.paint(self._canvas)

    def exec_(self):
        self._main_window.show()
        QApplication.exec_()


if __name__ == '__main__':
    import sys
    app = Cg2(sys.argv)
    sys.exit(app.exec_())
