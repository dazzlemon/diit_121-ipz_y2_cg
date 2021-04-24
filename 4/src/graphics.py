from PyQt5.QtGui import QVector3D, QColor
from OpenGL.GL       import *
from OpenGL.GLU      import *
from OpenGL.GLUT     import *
from PyQt5.QtOpenGL  import *
import numpy as np

def gl_color(color: QColor):
    """wrapper to use with QColor"""
    glColor3f(
        color.red() / 255,
        color.green() / 255,
        color.blue() / 255
    )


def gl_translate(point: QVector3D):
    """wrapper to use with QVector3D"""
    glTranslatef(
        point.x(),
        point.y(),
        point.z()
    )


def gl_scale(scale: QVector3D):
    """wrapper to use with QVector3D"""
    glScalef(
        scale.x(),
        scale.y(),
        scale.z()
    )


class Ellipsoid:
    def __init__(self, origin: QVector3D, radiuses: QVector3D, color: QColor):
        """
        radiuses = (radX, radY, radZ)
        origin is the center
        """
        self.origin = origin
        self.radiuses = radiuses
        self.color  = color


    def paint(self):
        max_rad = max(
            self.radiuses.x(),
            self.radiuses.y(),
            self.radiuses.z()
        )

        scales = QVector3D(
            self.radiuses.x() / max_rad,
            self.radiuses.y() / max_rad,
            self.radiuses.z() / max_rad
        )

        sphere = gluNewQuadric()
        gl_color(self.color)

        gl_translate(self.origin)
        gl_scale(scales)
        gluSphere(sphere, max_rad, 50, 50)
        gl_scale(QVector3D(1, 1, 1) / scales)
        gl_translate(-self.origin)


class Sphere(Ellipsoid):
    def __init__(self, origin: QVector3D, radius: float, color: QColor):
        """origin is the center"""
        Ellipsoid.__init__(self,
            origin, QVector3D(radius, radius, radius), color)


class RectangularPrism:
    def __init__(self, origin: QVector3D, size: QVector3D, color: QColor):
        """size = (xLength, yHeight, zWidth)"""
        self.origin = origin
        self.size   = size
        self.color  = color


    def paint(self):
        gl_translate(self.origin)
        gl_scale(self.size)
        gl_color(self.color)
        # glutSolidCube(self.size)
        glBegin(GL_QUADS)
        # top
        glNormal3f( 0.0, 1.0,  0.0)
        glVertex3f(-0.5, 0.5,  0.5)
        glVertex3f( 0.5, 0.5,  0.5)
        glVertex3f( 0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)

        # front
        glNormal3f( 0.0,  0.0, 1.0)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f( 0.5, -0.5, 0.5)
        glVertex3f( 0.5,  0.5, 0.5)
        glVertex3f(-0.5,  0.5, 0.5)

        # right
        glNormal3f(1.0,  0.0,  0.0)
        glVertex3f(0.5, -0.5,  0.5)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5,  0.5, -0.5)
        glVertex3f(0.5,  0.5,  0.5)

        # left
        glNormal3f(-1.0,  0.0,  0.0)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)

        # bottom
        glNormal3f( 0.0, -1.0,  0.0)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)

        # back
        glNormal3f( 0.0,  0.0, -1.0)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        
        glEnd()

        gl_scale(QVector3D(1, 1, 1) / self.size)
        gl_translate(-self.origin)


class Cube:
    def __init__(self, origin: QVector3D, size: float, color: QColor):
        """origin is the point to which size are added, size > 0"""
        self.origin = origin
        self.size   = size
        self.color  = color


    def paint(self):
        gl_translate(self.origin)
        glScalef(self.size, self.size, self.size)
        gl_color(self.color)
        # glutSolidCube(self.size)
        glBegin(GL_QUADS)
        # top
        glNormal3f( 0.0, 1.0,  0.0)
        glVertex3f(-0.5, 0.5,  0.5)
        glVertex3f( 0.5, 0.5,  0.5)
        glVertex3f( 0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)

        # front
        glNormal3f( 0.0,  0.0, 1.0)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f( 0.5, -0.5, 0.5)
        glVertex3f( 0.5,  0.5, 0.5)
        glVertex3f(-0.5,  0.5, 0.5)

        # right
        glNormal3f(1.0,  0.0,  0.0)
        glVertex3f(0.5, -0.5,  0.5)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5,  0.5, -0.5)
        glVertex3f(0.5,  0.5,  0.5)

        # left
        glNormal3f(-1.0,  0.0,  0.0)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)

        # bottom
        glNormal3f( 0.0, -1.0,  0.0)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)

        # back
        glNormal3f( 0.0,  0.0, -1.0)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        
        glEnd()

        glScalef(1 / self.size, 1 / self.size, 1 / self.size)
        gl_translate(-self.origin)


class Line3D:
    def __init__(self, start: QVector3D, end: QVector3D, color: QColor):
        self.start = start
        self.end   = end
        self.color = color


    def paint(self):
        gl_color(self.color)
        glBegin(GL_LINES)
        glVertex3f(self.start.x(), self.start.y(), self.start.z())
        glVertex3f(self.end.x(), self.end.y(), self.end.z())
        glEnd()
