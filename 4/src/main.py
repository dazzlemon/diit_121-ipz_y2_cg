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

        def paint_shape():
            glColor3f(1.0, 1.5, 0.0)# color for next vertices
            glPolygonMode(GL_FRONT, GL_FILL)# polygon rasterization mode

            glBegin(GL_TRIANGLES)# next vertices will be grouped into triangles
            glVertex3f(2.0, -1.2, -1.0)
            glVertex3f(2.6,  0.0, 5.0)
            glVertex3f(2.9, -1.2, -4.0)
            glEnd()# end glBegin(GL_TRIANGLES)

        def paint_gl():
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()# identity matrix
            glTranslatef(-2.5, 0.5, -6.0)# move (0, 0, 0)
            paint_shape()
            glFlush()

        def init_gl(aspect):
            glClearDepth(1.0)# clear value for depth buffer [0, 1]
            #glDepthFunc(GL_LESS)# val for depth buffer comparisons, GL_LESS is def value
            glEnable(GL_DEPTH_TEST)# enable depth comparisons
            #glShadeModel(GL_SMOOTH)# smooth shading is default

            glMatrixMode(GL_PROJECTION)# load projection matrix
            glLoadIdentity()# make projection matrix := eye()
            #              angleY, aspect, zNear, zFar
            gluPerspective(90.0,   aspect, 0.1,   100.0)# perspective projection matrix
            glMatrixMode(GL_MODELVIEW)# load model view

        def initialize_gl():
            init_gl(1.33)

        def resize_gl(w, h):
            init_gl(w / h)

        self._main_ui.openGLWidget.resizeGL = resize_gl
        self._main_ui.openGLWidget.paintGL = paint_gl
        self._main_ui.openGLWidget.initializeGL = initialize_gl
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
