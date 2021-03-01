"""
CG3 GraphicsPoint3d
"""

from math import sin, cos, pi, sqrt
import numpy as np

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


def world3d_to_2d(x, y, z):
    #p4 = np.array([x, y, z, 1])
    #p4_ = t_right_angle_dimetric @ p4
    x_ = (x - z) / sqrt(2)#p4_[0]
    y_ = -(x - 2*y + z) / sqrt(6)#p4_[1]
    return Point2d(x_, y_)


def world2d_to_view(p: Point2d):
    return Point2d(p.x, -p.y)


def world3d_to_view(x, y, z):
    return world2d_to_view(world3d_to_2d(x, y, z))


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