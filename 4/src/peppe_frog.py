"""
peppe frog 3d
"""

from typing      import List
from PyQt5.QtGui import QColor, QVector3D
from graphics    import (Sphere, Ellipsoid, RectangularPrism, Cube, Line3D,
                        gl_translate)
from OpenGL.GL       import *


class CompoundGraphics:
    """Graphics elem from primitives"""
    def __init__(self, items: List, is_modifiable):
        self._items = items
        self.is_modifiable = is_modifiable

        self.rotations = QVector3D(0, 0, 0)
        self.delta = QVector3D(0, 0, 0)
        self.scale = 1


    def paint(self):
        """openGL"""
        for i in self._items:
            glRotatef(self.rotations.x(), 1, 0, 0)
            glRotatef(self.rotations.y(), 0, 1, 0)
            glRotatef(self.rotations.z(), 0, 0, 1)

            glScalef(self.scale, self.scale, self.scale)
            gl_translate(self.delta)

            i.paint()

            gl_translate(-self.delta)
            glScalef(1 / self.scale, 1 / self.scale, 1 / self.scale)

            glRotatef(-self.rotations.z(), 0, 0, 1)
            glRotatef(-self.rotations.y(), 0, 1, 0)
            glRotatef(-self.rotations.x(), 1, 0, 0)

    def move(self, ddelta):
        """TMP"""
        if self.is_modifiable:
            self.delta += ddelta


    def upd_scale(self, dscale):
        """TMP"""
        if self.is_modifiable:
            self.scale += dscale

            if self.scale <= 0:
                self.scale = 0.01
            if self.scale > 10:
                self.scale = 10


    def rotate(self, drot):
        """TMP"""
        if self.is_modifiable:
            self.rotations += drot

            if self.rotations.x() > 360:
                self.rotations.setX(self.rotations.x() - 360)
            if self.rotations.x() < 0:
                self.rotations.setX(self.rotations.x() + 360)

            if self.rotations.y() > 360:
                self.rotations.setY(self.rotations.y() - 360)
            if self.rotations.y() < 0:
                self.rotations.setY(self.rotations.y() + 360)

            if self.rotations.z() > 360:
                self.rotations.setZ(self.rotations.z() - 360)
            if self.rotations.z() < 0:
                self.rotations.setZ(self.rotations.z() + 360)


class PeppeFrog(CompoundGraphics):
    """Peppe frog 3d"""
    def __init__(self):
        CompoundGraphics.__init__(self, [
            PeppeBody(0, 0, 0),
            PeppeMouth(0, 0, 300),
            PeppeEye(-100, 200, 200),
            PeppeEye(100, 200, 200),
        ], True)


    def move(self, ddelta):
        """TMP"""
        for i in self._items:
            i.move(ddelta)


    def upd_scale(self, dscale):
        """TMP"""
        for i in self._items:
            i.upd_scale(dscale)


    def rotate(self, drot):
        """TMP"""
        for i in self._items:
            i.rotate(drot)


class PeppeEye(CompoundGraphics):
    """Peppe's eye"""
    def __init__(self, x, y, z):
        CompoundGraphics.__init__(self, [
            Sphere(
                QVector3D(x, y, z),
                100,
                QColor(60, 150, 0)
            ),# eye body
            Ellipsoid(
                QVector3D(x, y, z + 100),
                QVector3D(60, 30, 30),
                QColor(255, 255, 255)
            ),# white
            Sphere(
                QVector3D(x, y, z + 130),
                10,
                QColor(0, 0, 0)
            ),# pupil
            # RectangularPrism(
            #     QVector3D(560 + x, 430, 430),
            #     QVector3D(30, 20, 20),
            #     QColor(255, 255, 255)
            # ),# flare
            # Cube(
            #     QVector3D(560 + x, 430, 430),
            #     10,
            #     QColor(0, 0, 0)
            # ),# flare shadow
        ], True)


class PeppeMouth(CompoundGraphics):
    """Peppe's mouth"""
    def __init__(self, x, y, z):
        CompoundGraphics.__init__(self, [
            Ellipsoid(
                QVector3D(x, y, z),
                QVector3D(200, 25, 25),
                QColor(30, 80, 0)
            ),# lips
            Line3D(
                QVector3D(x - 160, y, z + 25),
                QVector3D(x + 160, y, z + 25),
                QColor(0, 0, 0)
            ),# lip line
        ], True)


class PeppeBody(CompoundGraphics):
    """Peppe's head(body of the head)"""
    def __init__(self, x, y, z):
        CompoundGraphics.__init__(self, [
            Ellipsoid(
                QVector3D(x, y, z),
                QVector3D(400, 300, 300),
                QColor(60, 150, 0)
            )
        ], True)
