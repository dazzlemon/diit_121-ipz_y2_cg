"""
CG4 Main
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from forms_py        import Ui_MainWindow
from peppe_frog      import PeppeFrog
from OpenGL.GL       import *
from OpenGL.GLU      import *
from OpenGL.GLUT     import *
from PyQt5.QtOpenGL  import *
from gl_widget       import *

class Cg4(QApplication):
    """Main class"""
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._main_window = QMainWindow()
        self._main_ui     = Ui_MainWindow()
        self._main_ui.setupUi(self._main_window)

        self.frog = PeppeFrog()
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0
        
        self._init_signals()

        def paint_gl():
            """TMP"""
            glClearColor(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()# identity matrix
            glTranslatef(3, 3, -3)# move (0, 0, 0)
            glScalef(0.01, 0.01, 0.01)
            
            glRotatef(self.x_angle, 1, 0, 0)
            glRotatef(self.y_angle, 0, 1, 0)
            glRotatef(self.z_angle, 0, 0, 1)

            self.frog.paint()

            glFlush()

        self._main_ui.openGLWidget.resizeGL = resize_gl
        self._main_ui.openGLWidget.paintGL = paint_gl
        self._main_ui.openGLWidget.initializeGL = initialize_gl
        self._main_ui.openGLWidget.setMinimumSize(640, 480)


    def _init_signals(self):
        def update_rot(axis):
            step = 5
            k = 0
            
            if getattr(self._main_ui, axis + "Clock").isChecked():
                k = -1
            elif getattr(self._main_ui, axis + "AntiClock").isChecked():
                k = 1

            new_val = getattr(self, axis + "_angle") + step * k
            if new_val > 360:
                new_val -= 360
            if new_val < 0:
                new_val += 360

            setattr(self, axis + "_angle", new_val)


        def rotate():
            update_rot("x")
            update_rot("y")
            update_rot("z")
            self._main_ui.openGLWidget.update()

        self._main_ui.rotateButton.pressed.connect(rotate)
        self._main_ui.rotateButton.setAutoRepeat(True)
            
            

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
