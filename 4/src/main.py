"""
CG4 Main
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from OpenGL.GL       import *
from OpenGL.GLU      import *
from PyQt5.QtOpenGL  import *
from forms_py        import Ui_MainWindow

class Cg4(QApplication):
    """Main class"""
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._main_window = QMainWindow()
        self._main_ui     = Ui_MainWindow()
        self._main_ui.setupUi(self._main_window)

        def paintGL():
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslatef(-2.5, 0.5, -6.0)
            glColor3f( 1.0, 1.5, 0.0 )
            glPolygonMode(GL_FRONT, GL_FILL)
            glBegin(GL_TRIANGLES)
            glVertex3f(2.0,-1.2,0.0)
            glVertex3f(2.6,0.0,0.0)
            glVertex3f(2.9,-1.2,0.0)
            glEnd()
            glFlush()

        def initializeGL():
            glClearDepth(1.0)
            glDepthFunc(GL_LESS)
            glEnable(GL_DEPTH_TEST)
            glShadeModel(GL_SMOOTH)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(45.0,1.33,0.1, 100.0)
            glMatrixMode(GL_MODELVIEW)

        self._main_ui.openGLWidget.paintGL = paintGL
        self._main_ui.openGLWidget.initializeGL = initializeGL
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
