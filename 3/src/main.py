"""
Cg3 Main
"""
import numpy as np
from PyQt5.QtWidgets  import QApplication, QMainWindow, QGraphicsScene
from forms_py         import Ui_MainWindow
from graphics_point3d import GraphicsPoint3d, isometric_proj, dimetric_proj, world2d_to_view
from parallelepiped   import Parallelepiped
from bezier_surface   import BezierSurface

class Cg3(QApplication):
    """Main class"""
    def __init__(self, argv):
        QApplication.__init__(self, argv)

        self._main_window = QMainWindow()
        self._main_ui     = Ui_MainWindow()
        self._main_ui.setupUi(self._main_window)
        self._proj = isometric_proj
        self._is_parallelepiped = True
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
        self.bezier_surface = BezierSurface(
            np.array([# xs
                [100, 200, 300, 400],
                [100, 200, 300, 400],
                [100, 200, 300, 400],
                [100, 200, 300, 400],
            ]),
            np.array([# ys
                [200, 100, 100, 100],
                [100, 200, 100, 100],
                [100, 100, 200, 100],
                [100, 100, 100, 200],
            ]),
            np.array([# zs
                [100, 200, 300, 400],
                [100, 200, 300, 400],
                [100, 200, 300, 400],
                [100, 200, 300, 400],
            ])
        )
        self._update()


    def _init_signals(self):
        def rotate(axis):
            def rot(val):
                setattr(self.parallelepiped, "rot_" + axis, np.deg2rad(val))
                self._update()
            return rot
        self._main_ui.xDial.valueChanged.connect(rotate("x"))
        self._main_ui.yDial.valueChanged.connect(rotate("y"))
        self._main_ui.zDial.valueChanged.connect(rotate("z"))

        def scale(val):
            self.parallelepiped.scale = val
            self._update()
        self._main_ui.scaleSpinBox.valueChanged.connect(scale)

        def move(axis):
            def m(val):
                setattr(self.parallelepiped.delta, axis, val)
                self._update()
            return m
        self._main_ui.xSpinBox.valueChanged.connect(move("x"))
        self._main_ui.ySpinBox.valueChanged.connect(move("y"))
        self._main_ui.zSpinBox.valueChanged.connect(move("z"))

        def iso(var):
            if var:
                self._proj = isometric_proj
                self._update()
        def dim(var):
            if var:
                self._proj = dimetric_proj
                self._update()
        self._main_ui.isoRadio.toggled.connect(iso)
        self._main_ui.dimRadio.toggled.connect(dim)
        self._main_ui.isoRadio.setChecked(True)

        def g_elem_toggle(is_parallelepiped):
            def toggle(var):
                self._is_parallelepiped = is_parallelepiped and var
                self._main_ui.pMatrixGroup.setEnabled(not self._is_parallelepiped)
                self._update()
            return toggle
        self._main_ui.parallelepipedRadio.toggled.connect(g_elem_toggle(True))
        self._main_ui.surfaceRadio.toggled.connect(g_elem_toggle(False))
        self._main_ui.parallelepipedRadio.setChecked(True)

        self._main_ui.sStepsSpinBox.setValue(self.bezier_surface.s_steps)
        self._main_ui.tStepsSpinBox.setValue(self.bezier_surface.t_steps)
        def s_steps_changed(val):
            self.bezier_surface.s_steps = val
            self._update()
        self._main_ui.sStepsSpinBox.valueChanged.connect(s_steps_changed)
        def t_steps_changed(val):
            self.bezier_surface.t_steps = val
            self._update()
        self._main_ui.tStepsSpinBox.valueChanged.connect(t_steps_changed)

        def p_mat_changed(axis, i, j):
            def pij_changed(val):
                getattr(self.bezier_surface, "p_" + axis)[i][j] = val
                self._update()
            return pij_changed
        for axis in ["x", "y", "z"]:
            for i in range(4):
                for j in range(4):
                    getattr(self._main_ui, "%s%d%dSpinBox" % (axis, i, j)).valueChanged.connect(p_mat_changed(axis, i, j))



    def _update(self):
        def world3d_to_view(p):
            return world2d_to_view(self._proj(p))
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
        if self._is_parallelepiped:
            self.parallelepiped.paint(self._scene, world3d_to_view)
        else:
            self.bezier_surface.paint(self._scene, world3d_to_view)

    def exec_(self):
        """QApplication.exec_ overload to show window before start"""
        self._main_window.show()
        QApplication.exec_()


def main():
    """main"""
    import sys# Actually absolutely OK, the same way as in files made by generator
    app = Cg3(sys.argv)
    sys.exit(app.exec_())# Non zero return when everything is actually OK, idk


if __name__ == "__main__":
    main()
