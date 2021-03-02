"""
Cg3 Point2d, from3dto2d, Parallelepiped
"""
from copy             import deepcopy
from more_itertools   import pairwise
from PyQt5.QtWidgets  import QGraphicsScene
from graphics_point3d import GraphicsPoint3d, Point3d, world3d_to_view

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
        self.rot_x = 0
        self.rot_y = 0
        self.rot_z = 0
        self.scale = 1


    def paint(self, canvas: QGraphicsScene):
        """
        Paints this Parallelepiped onto canvas
        """
        def apply_transforms(p):
            p.rotate_x(self.rot_x)
            p.rotate_y(self.rot_y)
            p.rotate_z(self.rot_z)
            p.scale(GraphicsPoint3d(self.scale, self.scale, self.scale))
            return world3d_to_view(p)

        face1 = deepcopy([
            self.start1,
            GraphicsPoint3d(self.start1.x + self.w, self.start1.y,          self.start1.z),
            GraphicsPoint3d(self.start1.x + self.w, self.start1.y, self.start1.z + self.h),
            GraphicsPoint3d(self.start1.x,          self.start1.y, self.start1.z + self.h),
        ])


        face1 = map(apply_transforms, face1)

        face2 = deepcopy([
            self.start2,
            GraphicsPoint3d(self.start2.x + self.w, self.start2.y,          self.start2.z),
            GraphicsPoint3d(self.start2.x + self.w, self.start2.y, self.start2.z + self.h),
            GraphicsPoint3d(self.start2.x,          self.start2.y, self.start2.z + self.h),
        ])
        face2 = map(apply_transforms, face2)

        def pairwise_lf(gen):
            """
            same as pairwise, but last pair is (last, first),
            and not generator but raw list
            doesnt ruin input generator
            """
            l = list(deepcopy(gen))
            l.append(l[0])
            return pairwise(l)

        for p1, p2 in pairwise_lf(face1):
            canvas.addLine(p1.x, p1.y, p2.x, p2.y)

        for p1, p2 in pairwise_lf(face2):
            canvas.addLine(p1.x, p1.y, p2.x, p2.y)

        for p1, p2 in zip(face1, face2):
            canvas.addLine(p1.x, p1.y, p2.x, p2.y)


