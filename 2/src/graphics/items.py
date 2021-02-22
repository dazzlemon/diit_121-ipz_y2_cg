"""
IGraphicsItem to use with ICanvas, and its extensions
"""
from math import sqrt
from copy import deepcopy
import numpy as np
from ._interfaces import ICanvas, IPoint, IAffineTransformable, IDrawable
from PyQt5.QtGui import QColor


class GraphicsPoint(IPoint, IDrawable, IAffineTransformable):
    """
    Represents a 2D point that can draw itself onto ICanvas
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y


    @property
    def x(self):
        """returns x component of point"""
        return self._x


    @property
    def y(self):
        """returns y component of point"""
        return self._y


    @x.setter
    def x(self, value):
        """sets x component of point"""
        self._x = value


    @y.setter
    def y(self, value):
        """sets y component of point"""
        self._y = value


    def move(self, delta: IPoint):
        self.x += delta.x
        self.y += delta.y


class GraphicsLine(IDrawable, IAffineTransformable):
    """
    Represents a 2D line
    """

    def __init__(self, x1: float, y1: float, x2: float, y2: float, color: QColor):
        self.start = GraphicsPoint(x1, y1)
        self.end   = GraphicsPoint(x2, y2)
        self.color = color


    def paint(self, canvas: ICanvas):
        canvas.draw_lines([self.start, self.end], self.color)


    def move(self, delta: IPoint):
        self.start.move(delta)
        self.end.move(delta)


    @property
    def color(self) -> QColor:
        return self._color


    @color.setter
    def color(self, value):
        self._color = value


class GraphicsPolygon(IDrawable, IAffineTransformable):
    """
    Represents a polygon that can draw itself onto ICanvas
    """


class GraphicsRect(GraphicsPolygon):
    """
    Represents a rectangle that can draw itself onto ICanvas
    """
    def __init__(self, x1: float, y1: float, x2: float, y2: float, color: QColor):
        self.start = GraphicsPoint(x1, y1)
        self.size  = GraphicsPoint(x2, y2)
        self.color = color


    @property
    def size(self) -> GraphicsPoint:
        """.x -> width .y -> height"""
        return self._size


    @size.setter
    def size(self, value: GraphicsPoint):
        """sets size with new GraphicsPoint"""
        self._size = value


    def paint(self, canvas: ICanvas):
        x  = self.start.x
        y  = self.start.y
        dx = self.size.x
        dy = self.size.y
        points = [
            self.start,
            GraphicsPoint(x + dx, y),
            GraphicsPoint(x + dx, y + dy),
            GraphicsPoint(x     , y + dy),
            self.start
        ]
        canvas.draw_lines(points, self.color)
        canvas.fill(points, self.color)

    def move(self, delta: IPoint):
        self.start.move(delta)


    @property
    def color(self) -> QColor:
        return self._color


    @color.setter
    def color(self, value: QColor):
        self._color = value


class GraphicsSquare(GraphicsRect):
    """
    Represents a square that can draw itself onto ICanvas
    """
    def __init__(self, x: float, y: float, size: float, color: QColor):
        self.start = GraphicsPoint(x, y)
        self.size  = size
        self.color = color


    @property
    def size(self) -> GraphicsPoint:
        """same as GraphicsRect.size but x and y actually have the same value"""
        return GraphicsPoint(self._size, self._size)


    @size.setter
    def size(self, value: float):
        """value must be float"""
        self._size = value


class GraphicsEllipse(IDrawable, IAffineTransformable):
    """
    Represents an Ellipse enclosed in rect that can draw itself onto ICanvas
    """
    def __init__(self, x1: float, y1: float, x2: float, y2: float, color: QColor):
        self.rect  = GraphicsRect(x1, y1, x2, y2, color)


    def paint(self, canvas: ICanvas):
        orig_x = self.rect.start.x
        orig_y = self.rect.start.y

        a = self.rect.size.x / 2
        b = self.rect.size.y / 2
        flip = a < b
        if flip:
            a, b = b, a
            orig_x, orig_y = orig_y, orig_x

        f = lambda x: b / a * sqrt(a**2 - x**2)
        xs = np.linspace(-a, a, num = int(2 * a))

        points_top = [GraphicsPoint(x, f(x)) for x in xs]
        points_bot = list(map(
            lambda p: GraphicsPoint(p.x, -p.y),
            points_top
        ))
        points_bot.reverse()

        points = map(
            lambda p: GraphicsPoint(orig_x + p.x + a, orig_y + p.y + b),
            points_top + points_bot
        )

        if flip:
            points = map(
                lambda p: GraphicsPoint(p.y, p.x),
                points
            )

        canvas.draw_lines(deepcopy(points), self.color)
        canvas.fill(points, self.color)


    def move(self, delta: IPoint):
        self.rect.move(delta)


    @property
    def color(self) -> QColor:
        return self.rect.color


    @color.setter
    def color(self, value):
        self._color = value


class GraphicsCircle(GraphicsEllipse):
    """
    Represents a a circle enclosed in square that can draw itself onto ICanvas
    """
    def __init__(self, x1: float, y1: float, size: float, color: QColor):
        self.rect  = GraphicsSquare(x1, y1, size, color)
