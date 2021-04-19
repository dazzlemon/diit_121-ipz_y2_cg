"""
CG4 Main
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from forms_py        import Ui_MainWindow
from gl_widget       import *
from peppe_frog      import PeppeFrog

from graphics.items  import GraphicsPoint
from PyQt5.QtGui     import QColor

class Cg4(QApplication):
    """Main class"""
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._main_window = QMainWindow()
        self._main_ui     = Ui_MainWindow()
        self._main_ui.setupUi(self._main_window)

        self.frog = PeppeFrog()
        self.gl_canvas = OpenGLCanvas()

        def paint_gl():
            """TMP"""
            glClearColor(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()# identity matrix
            glTranslatef(-2.5, 0.5, -6.0)# move (0, 0, 0)
            
            self.frog.paint(self.gl_canvas)# idk doesnt work

            glFlush()

        self._main_ui.openGLWidget.resizeGL = OpenGLCanvas.resize_gl
        self._main_ui.openGLWidget.paintGL = paint_gl
        self._main_ui.openGLWidget.initializeGL = OpenGLCanvas.initialize_gl
        self._main_ui.openGLWidget.setMinimumSize(640, 480)


    def exec_(self):
        """QApplication.exec_ override to show window before start"""
        self._main_window.show()
        QApplication.exec_()


def main():
    """main"""
    import sys# Actually absolutely OK, the same was in file mady by generator
    app = Cg4(sys.argv)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
