"""class BezierSurface"""
from typing import final
import numpy as np
from more_itertools   import pairwise
from PyQt5.QtWidgets  import QGraphicsScene
from PyQt5.QtGui      import QPen, QColor
from graphics_point3d import GraphicsPoint3d

MATRIX_BEZIER: final = np.array([
    [-1,  3, -3, 1],
    [ 3, -6,  3, 0],
    [-3,  3,  0, 0],
    [ 1,  0,  0, 0]
])

class BezierSurface:
    """Bezier surface estimated by 16 points in p_matrix"""


    def __init__(self, p_x, p_y, p_z):
        """p_x, p_y, p_z -> 4x4 real matrices, np.arrays!"""
        self.p_x = p_x
        self.p_y = p_y
        self.p_z = p_z
        self.s_steps = 20
        self.t_steps = 20
        self.rot_x = 0
        self.rot_y = 0
        self.rot_z = 0
        self.scale = 1
        self.delta = GraphicsPoint3d(0, 0, 0)

    def paint(self, canvas: QGraphicsScene, world3d_to_view):
        """paints this surface to <canvas> using world3d_to_view to project 2d to 3d"""
        def apply_transforms(p):
            p.move(self.delta)
            p.scale(GraphicsPoint3d(self.scale, self.scale, self.scale))
            p.rotate_x(self.rot_x)
            p.rotate_y(self.rot_y)
            p.rotate_z(self.rot_z)
            return world3d_to_view(p)
        m = []
        for s in np.linspace(0, 1, num=self.s_steps):
            row = []
            for t in np.linspace(0, 1, num=self.t_steps):
                s_ = np.array([s**3, s**2, s, 1])
                t_ = np.array([t**3, t**2, t, 1])

                x = s_ @ MATRIX_BEZIER @ self.p_x.T @ MATRIX_BEZIER.T @ t_.T
                y = s_ @ MATRIX_BEZIER @ self.p_y.T @ MATRIX_BEZIER.T @ t_.T
                z = s_ @ MATRIX_BEZIER @ self.p_z.T @ MATRIX_BEZIER.T @ t_.T

                p = apply_transforms(GraphicsPoint3d(x, y, z))
                row.append(p)
            m.append(row)

        for row in m:
            for p1, p2 in pairwise(row):
                canvas.addLine(p1.x, p1.y, p2.x, p2.y)
        for r1, r2 in pairwise(m):
            for p1, p2 in zip(r1, r2):
                canvas.addLine(p1.x, p1.y, p2.x, p2.y)
        m = []
        for i in range(4):
            row = []
            for j in range(4):
                p = apply_transforms(
                    GraphicsPoint3d(
                        self.p_x[i][j],
                        self.p_y[i][j],
                        self.p_z[i][j]
                    )
                )
                row.append(p)
            m.append(row)
        
        for row in m:
            for p1, p2 in pairwise(row):
                canvas.addLine(p1.x, p1.y, p2.x, p2.y, QPen(QColor(255, 0, 0)))
        for r1, r2 in pairwise(m):
            for p1, p2 in zip(r1, r2):
                canvas.addLine(p1.x, p1.y, p2.x, p2.y, QPen(QColor(255, 0, 0)))
                


def main():
    """main"""
    bs = BezierSurface(
        np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]),
        np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]),
        np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ])
    )
    bs.paint(None, None)


if __name__ == "__main__":
    main()
