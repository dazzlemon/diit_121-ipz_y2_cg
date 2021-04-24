"""
CG4 Main
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from forms_py        import Ui_MainWindow
from peppe_frog      import PeppeFrog
from OpenGL.GL       import *
from OpenGL.GLU      import *
from PyQt5.QtOpenGL  import *
from gl_widget       import *
from PyQt5.QtGui     import QVector3D, QColor
from graphics        import Line3D

class Cg4(QApplication):
    """Main class"""
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._main_window = QMainWindow()
        self._main_ui     = Ui_MainWindow()
        self._main_ui.setupUi(self._main_window)

        self.frog = PeppeFrog()

        self._init_signals()

        def draw_lines():
            zero = QVector3D(0, 0, 0)

            x = Line3D(
                zero,
                QVector3D(1000, 0, 0),
                QColor(255, 0, 0)
            )

            y = Line3D(
                zero,
                QVector3D(0, 1000, 0),
                QColor(0, 255, 0)
            )

            z = Line3D(
                zero,
                QVector3D(0, 0, 1000),
                QColor(0, 0, 255)
            )

            x.paint()
            y.paint()
            z.paint()


        def paint_gl():
            glClearColor(0.85, 0.85, 0.85, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()# identity matrix
            glTranslatef(-1, -1, -6)# move (0, 0, 0)
            glScalef(0.01, 0.01, 0.01)

            if self._main_ui.axesCheckBox.isChecked():
                draw_lines()
            self.frog.paint()

            glFlush()

        self._main_ui.openGLWidget.resizeGL = resize_gl
        self._main_ui.openGLWidget.paintGL = paint_gl
        self._main_ui.openGLWidget.initializeGL = initialize_gl
        self._main_ui.openGLWidget.setMinimumSize(640, 480)

        # glutInit(argv)
        # glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        # glutCreateWindow(b"Safonov CG4")


    def _init_signals(self):
        def rotate():
            step = 5
            k = QVector3D(0, 0, 0)

            for axis in ["x", "y", "z"]:
                if getattr(self._main_ui, axis + "Clock").isChecked():
                    getattr(k, "set" + axis.upper())(-1)
                elif getattr(self._main_ui, axis + "AntiClock").isChecked():
                    getattr(k, "set" + axis.upper())(1)

            self.frog.rotate(k * step)
            self._main_ui.openGLWidget.update()

        self._main_ui.rotateButton.pressed.connect(rotate)

        def move():
            step = 3
            k = QVector3D(0, 0, 0)

            if self._main_ui.xPos.isChecked():
                k.setX(1)
            elif self._main_ui.xNeg.isChecked():
                k.setX(-1)

            if self._main_ui.yPos.isChecked():
                k.setY(1)
            elif self._main_ui.yNeg.isChecked():
                k.setY(-1)

            if self._main_ui.zPos.isChecked():
                k.setZ(1)
            elif self._main_ui.zNeg.isChecked():
                k.setZ(-1)

            self.frog.move(k * step)
            self._main_ui.openGLWidget.update()

        self._main_ui.moveButton.pressed.connect(move)

        def scale(up):
            def s():
                step = 0.01

                delta = step * (1 if up else -1)

                self.frog.upd_scale(delta)
                self._main_ui.openGLWidget.update()
            return s

        self._main_ui.scaleDownButton.pressed.connect(scale(False))
        self._main_ui.scaleUpButton.pressed.connect(scale(True))

        def modifiable_update(what):
            def upd(val):
                self.frog._items[what].is_modifiable = val == 2
                print("what: %d, val: %s" % (what, val == 2))
            return upd

        self._main_ui.bodyCheckBox.stateChanged.connect(modifiable_update(0))
        self._main_ui.mouthCheckBox.stateChanged.connect(modifiable_update(1))
        self._main_ui.lEyeCheckBox.stateChanged.connect(modifiable_update(2))
        self._main_ui.rEyeCheckBox.stateChanged.connect(modifiable_update(3))

        self._main_ui.axesCheckBox.stateChanged.connect(self._main_ui.openGLWidget.update)

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
