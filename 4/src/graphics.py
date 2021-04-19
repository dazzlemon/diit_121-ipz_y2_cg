from PyQt5.QtGui import QVector3D, QColor
from OpenGL.GL       import *
from OpenGL.GLU      import *
from OpenGL.GLUT     import *
from PyQt5.QtOpenGL  import *

class Ellipsoid:
    def __init__(self, origin: QVector3D, params: QVector3D, color: QColor):
        """
        params = (a, b, c) > 0
        origin is the center
        """
        self.origin = origin
        self.params = params
        self.color  = color


    def paint(self):
        pass


class Sphere:
    def __init__(self, origin: QVector3D, radius: float, color: QColor):
        """origin is the center"""
        self.origin = origin
        self.radius = radius
        self.color  = color


    def paint(self):
        sphere = gluNewQuadric()
        glColor3f(
            self.color.red() / 255,
            self.color.green() / 255,
            self.color.blue() / 255
        )
        gluSphere(sphere, self.radius, 50, 50)


class RectangularPrism:
    def __init__(self, origin: QVector3D, size: QVector3D, color: QColor):
        """size = (xLength, yHeight, zWidth)"""
        self.origin = origin
        self.size   = size
        self.color  = color


    def paint(self):
        pass


class Cube:
    def __init__(self, origin: QVector3D, size: float, color: QColor):
        """origin is the point to which size are added, size > 0"""
        self.origin = origin
        self.size   = size
        self.color  = color


    def paint(self):
        pass


class Line3D:
    def __init__(self, start: QVector3D, end: QVector3D, color: QColor):
        self.start = start
        self.end   = end
        self.color = color


    def paint(self):
        pass
