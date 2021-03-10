"""class BezierSurface"""
from typing import final
import numpy as np
from more_itertools   import pairwise
from PyQt5.QtWidgets  import QGraphicsScene
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
        self.s_step = 0.05
        self.t_step = 0.05

    def paint(self, canvas: QGraphicsScene, world3d_to_view):
        """paints this surface to <canvas> using world3d_to_view to project 2d to 3d"""
        m = []
        for s in self._range(self.s_step):
            row = []
            for t in self._range(self.t_step):
                s_ = np.array([s**3, s**2, s, 1])
                t_ = np.array([t**3, t**2, t, 1])

                x = s_ @ MATRIX_BEZIER @ self.p_x.T @ t_.T
                y = s_ @ MATRIX_BEZIER @ self.p_y.T @ t_.T
                z = s_ @ MATRIX_BEZIER @ self.p_z.T @ t_.T

                p = world3d_to_view(GraphicsPoint3d(x, y, z))
                row.append(p)
            m.append(row)
                #print(f"(x = {x:.2f}, y = {y:.2f}, z = {z:.2f})", end="")
            #print()
        for row in m:
            for p1, p2 in pairwise(row):
                canvas.addLine(p1.x, p1.y, p2.x, p2.y)
        for r1, r2 in pairwise(m):
            for p1, p2 in zip(r1, r2):
                canvas.addLine(p1.x, p1.y, p2.x, p2.y)


    @staticmethod
    def _range(step):
        """[0, 1] linspace with <step>"""
        steps = int(1 / step) + 1
        return np.linspace(0, 1, num=steps)


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
