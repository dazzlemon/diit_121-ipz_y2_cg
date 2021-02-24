from graphics._interfaces import IDrawable, IAffineTransformable, IPoint, ICanvas
from graphics.items import GraphicsEllipse, GraphicsCircle, GraphicsRect, GraphicsSquare, GraphicsLine
from PyQt5.QtGui import QColor


class CompoundGraphics(IDrawable, IAffineTransformable):
    def __init__(self):
        self._is_transformable = True


    def move(self, delta: IPoint):
        """IAffineTransformable override"""
        if self._is_transformable:
            for i in self._items:
                i.move(delta)


    def rotate(self, about: IPoint, rad: float):
        """IAffineTransformable override"""
        if self._is_transformable:
            for i in self._items:
                i.rotate(about, rad)


    def scale(self, about: IPoint, w: float, h: float):
        """IAffineTransformable override"""
        if self._is_transformable:
            for i in self._items:
                i.scale(about, w, h)


    def paint(self, canvas: ICanvas):
        for i in self._items:
            i.paint(canvas)


class PeppeFrog(CompoundGraphics):
    def __init__(self):
        CompoundGraphics.__init__(self)
        self._items = [
            PeppeBody(),
            PeppeEye(150),
            PeppeEye(0),
            PeppeMouth()
        ]


class PeppeEye(CompoundGraphics):
    def __init__(self, x: float):
        CompoundGraphics.__init__(self)
        self._items = [
            GraphicsCircle(450 + x, 350, 200, QColor(60, 150, 0)),#         eye body
            GraphicsEllipse(500 + x, 420, 120, 55, QColor(255, 255, 255)),# white
            GraphicsCircle(550 + x, 420, 50, QColor(0, 0, 0)),#             pupil
            GraphicsRect(560 + x, 430, 30, 20, QColor(255, 255, 255)),#     flare
            GraphicsSquare(560 + x, 430, 10, QColor(0, 0, 0)),#             flare shadow
        ]


class PeppeMouth(CompoundGraphics):
    def __init__(self):
        CompoundGraphics.__init__(self)
        self._items = [
            GraphicsEllipse(500, 550, 300, 55, QColor(30, 80, 0)),# lips
            GraphicsLine(500, 580, 300, QColor(0, 0, 0)),#          lip line
        ]


class PeppeBody(CompoundGraphics):
    def __init__(self):
        CompoundGraphics.__init__(self)
        self._items = [
            GraphicsEllipse(400, 400, 400, 300, QColor(60, 150, 0))
        ]
