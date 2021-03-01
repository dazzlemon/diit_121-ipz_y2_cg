"""
Cg3 Point2d, from3dto2d, Parallelepiped
"""
from math import sqrt
from more_itertools import pairwise
import numpy as np
from PyQt5.QtWidgets import QGraphicsScene
from graphics_point3d import GraphicsPoint3d, Point3d

t_right_angle_dimetric = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, -1, 0],
])


class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def from3dto2d(x, y, z):
    #p4 = np.array([x, y, z, 1])
    #p4_ = t_right_angle_dimetric @ p4
    x_ = (x - z) / sqrt(2)#p4_[0]
    y_ = (x + 2*y + z) / sqrt(6)#p4_[1]
    return Point2d(x_, y_)


class Parallelepiped:
    """parallelepiped"""
    def __init__(self, start1: Point3d, start2: Point3d, w: float, h: float):
        """
        start1 & start2 - starting points for bases (that are connected by single edge)
        w, h - size of base
        w -> O_x
        h -> O_z
        """

        self.start1 = start1
        self.start2 = start2
        self.w = w
        self.h = h


    def paint(self, canvas: QGraphicsScene):
        face1 = [
            self.start1,
            GraphicsPoint3d(self.start1.x + self.w, self.start1.y,          self.start1.z),
            GraphicsPoint3d(self.start1.x + self.w, self.start1.y, self.start1.z + self.h),
            GraphicsPoint3d(self.start1.x,          self.start1.y, self.start1.z + self.h),
        ]
        face2 = [
            self.start2,
            GraphicsPoint3d(self.start2.x + self.w, self.start2.y,          self.start2.z),
            GraphicsPoint3d(self.start2.x + self.w, self.start2.y, self.start2.z + self.h),
            GraphicsPoint3d(self.start2.x,          self.start2.y, self.start2.z + self.h),
        ]

        for p in face1 + face2:
            p_ = from3dto2d(p.x, p.y, p.z)
            p.x = p_.x
            p.y = p_.y

        for p1, p2 in pairwise([*face1, face1[0]]):
            canvas.addLine(p1.x, p1.y, p2.x, p2.y)

        for p1, p2 in pairwise([*face2, face2[0]]):
            canvas.addLine(p1.x, p1.y, p2.x, p2.y)

        for p1, p2 in zip(face1, face2):
            canvas.addLine(p1.x, p1.y, p2.x, p2.y)


