"""
CG3 GraphicsPoint3d
"""

from math import sin, cos, pi
import numpy as np


class Point2d:
    """(x, y) point in 2d space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Point3d:
    """x,y,z 3d point"""
    @property
    def x(self):
        """x component of this point"""
        return self._x


    @property
    def y(self):
        """y component of this point"""
        return self._y


    @property
    def z(self):
        """z component of this point"""
        return self._z


    @x.setter
    def x(self, value: float):
        self._x = value


    @y.setter
    def y(self, value: float):
        self._y = value


    @z.setter
    def z(self, value: float):
        self._z = value


class GraphicsPoint3d(Point3d):
    """Represents a point in 3d space"""
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z


    def move(self, delta: Point3d):
        """Moves this point by delta"""
        t = np.array([
            [1, 0, 0, delta.x],
            [0, 1, 0, delta.y],
            [0, 0, 1, delta.z],
            [0, 0, 0,       1],
        ])
        self.transform(t)


    def scale(self, scale: Point3d):
        """Scales this by <scale> about origin, if <scale> = (1, 1, 1) point doesnt change"""
        t = np.array([
            [scale.x, 0,       0,       0],
            [0,       scale.y, 0,       0],
            [0,       0,       scale.z, 0],
            [0,       0,       0,       1],
        ])
        self.transform(t)


    def rotate_x(self, rad: float):
        """Rotates by rad degrees around O_x"""
        t = np.array([
            [1,        0,         0, 0],
            [0, cos(rad), -sin(rad), 0],
            [0, sin(rad),  cos(rad), 0],
            [0,        0,         0, 1],
        ])
        self.transform(t)


    def rotate_y(self, rad: float):
        """Rotates by rad degrees around O_y"""
        t = np.array([
            [cos(rad), 0, -sin(rad), 0],
            [0,        1,         0, 0],
            [sin(rad), 0,  cos(rad), 0],
            [0,        0,         0, 1],
        ])
        self.transform(t)


    def rotate_z(self, rad: float):
        """Rotates by rad degrees around O_z"""
        t = np.array([
            [cos(rad), -sin(rad), 0, 0],
            [sin(rad),  cos(rad), 0, 0],
            [0,         0,        1, 0],
            [0,         0,        0, 1],
        ])
        self.transform(t)


    def transform(self, t_matrix):
        """applies t_matrix to this point"""
        vec4  = np.array([self.x, self.y, self.z, 1])
        vec4_ = t_matrix @ vec4
        self.x = vec4_[0]
        self.y = vec4_[1]
        self.z = vec4_[2]


    def __repr__(self):
        return "<Cg3::Point3d (x:%s, y:%s, z:%s)>" % (self.x, self.y, self.z)


    def __str__(self):
        return "(%s, %s, %s)" % (self.x, self.y, self.z)


def axonometric_proj(p: Point3d, rot_x, rot_y) -> Point2d:
    """Axonometric projection -> rot_y -> rot_x -> throw away z"""
    rot_x = np.deg2rad(rot_x)
    rot_y = np.deg2rad(rot_y)
    p.rotate_y(rot_y)
    p.rotate_x(rot_x)
    return Point2d(p.x, p.y)


def dimetric_proj(p: Point3d) -> Point2d:
    """Right angle dimetric projection from all positive octant(x, y, z >= 0)"""
    return axonometric_proj(p, 14, 21)# test numbers, but works about the same as matrix below
    # t = np.array([
    #     [  0.935, 0,     -0.354, 0],
    #     [ -0.118, 0.943, -0.312, 0],
    #     [  0,     0,      0,     0],
    #     [  0,     0,      0,     0],
    # ])
    # p4  = np.array([p.x, p.y, p.z, 1])
    # p4_ = t @ p4
    # x = p4_[0]
    # y = p4_[1]
    # return Point2d(x, y)


def isometric_proj(p: Point3d) -> Point2d:
    """Isometric Projection from all positive octant(x, y, z >= 0)"""
    return axonometric_proj(p, 35, 45)


def world2d_to_view(p: Point2d) -> Point2d:
    """Reverses y-compound of <p>"""
    return Point2d(p.x, -p.y)


def xy_proj(p: Point3d) -> Point2d:
    return Point2d(p.x, p.y)


def yz_proj(p: Point3d) -> Point2d:
    return Point2d(p.z, p.y)


def xz_proj(p: Point3d) -> Point2d:
    return Point2d(p.x, p.z)


def main():
    """main"""
    point = GraphicsPoint3d(1, 1, 1)
    print(point)

    point.scale(GraphicsPoint3d(0.5, 0.6, 0.7))
    print("after scale(0.5, 0.6, 0.7): %s" % point)
    point.scale(GraphicsPoint3d(1 / 0.5, 1 / 0.6, 1 / 0.7))

    point.rotate_x(pi)
    print("after rotate_x(pi): %s" % point)
    point.rotate_x(-pi)

    point.rotate_y(pi)
    print("after rotate_y(pi): %s" % point)
    point.rotate_y(-pi)

    point.rotate_z(pi)
    print("after rotate_z(pi): %s" % point)
    point.rotate_z(-pi)


if __name__ == "__main__":
    main()
