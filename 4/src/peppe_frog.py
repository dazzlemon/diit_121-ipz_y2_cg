"""
peppe frog 3d
"""

from typing      import List
from PyQt5.QtGui import QColor, QVector3D
from graphics    import Sphere, Ellipsoid, RectangularPrism, Cube, Line3D

class CompoundGraphics:
    """Graphics elem from primitives"""
    def __init__(self, items: List):
        self._items = items

    def paint(self):
        """openGL"""
        for i in self._items:
            i.paint()


class PeppeFrog(CompoundGraphics):
    """Peppe frog 3d"""
    def __init__(self):
        CompoundGraphics.__init__(self, [
            PeppeBody(),
            PeppeEye(150),
            PeppeEye(0),
            PeppeMouth()
        ])


class PeppeEye(CompoundGraphics):
    """Peppe's eye"""
    def __init__(self, x: float):
        CompoundGraphics.__init__(self, [
            Sphere(
                QVector3D(450 + x, 350, 350), 
                200,
                QColor(60, 150, 0)
            ),# eye body
            Ellipsoid(
                QVector3D(500 + x, 420, 420),
                QVector3D(120, 55, 55),
                QColor(255, 255, 255)
            ),# white
            Sphere(
                QVector3D(550 + x, 420, 420),
                50,
                QColor(0, 0, 0)
            ),# pupil
            RectangularPrism(
                QVector3D(560 + x, 430, 430),
                QVector3D(30, 20, 20),
                QColor(255, 255, 255)
            ),# flare
            Cube(
                QVector3D(560 + x, 430, 430),
                10,
                QColor(0, 0, 0)
            ),# flare shadow
        ])


class PeppeMouth(CompoundGraphics):
    """Peppe's mouth"""
    def __init__(self):
        CompoundGraphics.__init__(self, [
            Ellipsoid(
                QVector3D(500, 550, 550),
                QVector3D(300, 55, 55),
                QColor(30, 80, 0)
            ),# lips
            Line3D(
                QVector3D(500, 580, 580),
                QVector3D(300, 580, 580),
                QColor(0, 0, 0)
            ),# lip line
        ])


class PeppeBody(CompoundGraphics):
    """Peppe's head(body of the head)"""
    def __init__(self):
        CompoundGraphics.__init__(self, [
            Ellipsoid(
                QVector3D(400, 400, 400),
                QVector3D(400, 300, 300),
                QColor(60, 150, 0)
            )
        ])
