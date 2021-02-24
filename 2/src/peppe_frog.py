from graphics._interfaces import IDrawable, IAffineTransformable, IPoint, ICanvas
from graphics.items import GraphicsEllipse, GraphicsCircle, GraphicsRect, GraphicsSquare, GraphicsLine
from PyQt5.QtGui import QColor

class PeppeFrog(IDrawable, IAffineTransformable):
    def __init__(self):
        self._items = [
            GraphicsEllipse(400, 400, 400, 300, QColor(60, 150, 0)),#   head body
            GraphicsCircle(450, 350, 200, QColor(60, 150, 0)),#         left eye body
            GraphicsCircle(580, 350, 200, QColor(60, 150, 0)),#         right eye body
            GraphicsEllipse(500, 420, 120, 55, QColor(255, 255, 255)),# left white
            GraphicsEllipse(650, 420, 120, 55, QColor(255, 255, 255)),# right white
            GraphicsCircle(550, 420, 50, QColor(0, 0, 0)),#             left pupil
            GraphicsCircle(700, 420, 50, QColor(0, 0, 0)),#             right pupil
            GraphicsRect(560, 430, 30, 20, QColor(255, 255, 255)),#     left flare
            GraphicsRect(710, 430, 30, 20, QColor(255, 255, 255)),#     right flare
            GraphicsSquare(560, 430, 10, QColor(0, 0, 0)),#             left flare shadow
            GraphicsSquare(710, 430, 10, QColor(0, 0, 0)),#             right flare shadow
            GraphicsEllipse(500, 550, 300, 55, QColor(30, 80, 0)),#     mouth
            GraphicsLine(500, 580, 300, QColor(0, 0, 0))#               lip line
        ]


    def move(self, delta: IPoint):
        """IAffineTransformable override"""
        for i in self._items:
            i.move(delta)


    def rotate(self, about: IPoint, rad: float):
        """IAffineTransformable override"""
        for i in self._items:
            i.rotate(about, rad)


    def scale(self, about: IPoint, w: float, h: float):
        """IAffineTransformable override"""
        for i in self._items:
            i.scale(about, w, h)


    def paint(self, canvas: ICanvas):
        for i in self._items:
            i.paint(canvas)
