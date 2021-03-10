"""class BezierSurface"""
from typing import final
import numpy as np
from PyQt5.QtWidgets import QGraphicsScene

class BezierSurface:
    """Bezier surface estimated by 16 points in p_matrix"""
    MATRIX_BEZIER: final = np.array([
        [-1,  3, -3, 1],
        [ 3, -6,  3, 0],
        [-3,  3,  0, 0],
        [ 1,  0,  0, 0]
    ])


    def __init__(self, p_matrix):
        """p_matrix -> 4x4 array like of objects that have x, y, z attributes that return"""
        self.p_matrix = p_matrix
        self.s_step = 0.25
        self.v_step = 0.25

    def paint(self, canvas: QGraphicsScene, world3d_to_view):
        """paints this surface to <canvas> using world3d_to_view to project 2d to 3d"""
        for s in self._range(self.s_step):
            for v in self._range(self.v_step):
                print(f"(s = %.2f, v = %.2f)" % (s, v), end="")
            print()

    @staticmethod
    def _range(max_):
        steps = int(1 / max_) + 1
        return np.linspace(0, 1, num=steps)


def main():
    bs = BezierSurface(np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]))
    bs.paint(None, None)


if __name__ == "__main__":
    main()