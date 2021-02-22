"""
IGraphicsItem to use with ICanvas, and its extensions
"""
from typing import List
from math import sqrt, cos, sin
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
        # no matrices required
        self.x += delta.x
        self.y += delta.y


    def rotate(self, about: IPoint, rad: float):
        move = np.array([
            [1, 0, about.x],
            [0, 1, about.y],
            [0, 0, 1      ],
        ])
        rotate = np.array([
            [cos(rad), -sin(rad), 0],
            [sin(rad),  cos(rad), 0],
            [0,         0,        1],
        ])
        move_ = np.array([
            [1, 0, -about.x],
            [0, 1, -about.y],
            [0, 0, 1       ],
        ])
        xy1 = np.array([self.x, self.y, 1])
        new = move_ @ rotate @ move @ xy1 # x @ y -> np.matmul(x, y)
        self.x = new[0]
        self.y = new[1]


    def transform(self, matrix: np.ndarray):
        """
        applies transformation matrix to this point,
        needed to be able to apply affine transformations
        as well as normal like changing width/size/radius etc
        """
        #TODO: add check for matrix' dimensions
        xy1 = np.array([self.x, self.y, 1])
        new = matrix @ xy1
        self.x = new[0]
        self.y = new[1]


class GraphicsLine(IDrawable, IAffineTransformable):
    """
    Represents a 2D line
    """

    def __init__(self, x1: float, y1: float, length: float, color: QColor):
        self.start  = GraphicsPoint(x1, y1)
        self.length = length
        self.color  = color
        self.transformations = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ])


    def paint(self, canvas: ICanvas):
        points = deepcopy([self.start, GraphicsPoint(self.start.x + self.length, self.start.y)])
        for i in points:
            i.transform(self.transformations)
        canvas.draw_lines(points, self.color)


    def move(self, delta: IPoint):
        move = np.array([
            [1, 0, delta.x],
            [0, 1, delta.y],
            [0, 0, 1      ],
        ])
        self.transformations = move @ self.transformations



    @property
    def color(self) -> QColor:
        return self._color


    @color.setter
    def color(self, value):
        self._color = value


    def rotate(self, about: IPoint, rad: float):
        move = np.array([
            [1, 0, about.x],
            [0, 1, about.y],
            [0, 0, 1      ],
        ])
        rotate = np.array([
            [cos(rad), -sin(rad), 0],
            [sin(rad),  cos(rad), 0],
            [0,         0,        1],
        ])
        move_ = np.array([
            [1, 0, -about.x],
            [0, 1, -about.y],
            [0, 0, 1       ],
        ])
        matrix = move_ @ rotate @ move
        self.transformations = matrix @ self.transformations



class GraphicsPolygonLike(IDrawable, IAffineTransformable):
    """
    Represents a polygon that can draw itself onto ICanvas
    """
    def paint(self, canvas: ICanvas):
        canvas.draw_lines(self.points, self.color)
        canvas.fill(self.points, self.color)


    @property
    def points(self) -> List[IPoint]:
        """Returns anchor points to draw a figure on ICanvas"""


class GraphicsRect(GraphicsPolygonLike):
    """
    Represents a rectangle that can draw itself onto ICanvas
    """
    def __init__(self, x1: float, y1: float, x2: float, y2: float, color: QColor):
        self._points = [
            GraphicsPoint(x1, y1),
            GraphicsPoint(x1 + x2, y1),
            GraphicsPoint(x1 + x2, y1 + y2),
            GraphicsPoint(x1     , y1 + y2),
            GraphicsPoint(x1, y1),
        ]
        self.color = color


    @property
    def size(self) -> GraphicsPoint:
        """.x -> width .y -> height"""
        return self._size


    @size.setter
    def size(self, value: GraphicsPoint):
        """sets size with new GraphicsPoint"""
        self._size = value


    @property
    def points(self) -> List[IPoint]:
        return self._points


    def move(self, delta: IPoint):
        for i in self._points:
            i.move(delta)


    @property
    def color(self) -> QColor:
        return self._color


    @color.setter
    def color(self, value: QColor):
        self._color = value


    def rotate(self, about: IPoint, rad: float):
        for i in self._points:
            i.rotate(about, rad)


class GraphicsSquare(GraphicsRect):
    """
    Represents a square that can draw itself onto ICanvas
    """
    def __init__(self, x: float, y: float, size: float, color: QColor):
        GraphicsRect.__init__(self, x, y, size, size, color)


class GraphicsEllipse(IDrawable, IAffineTransformable):
    """
    Represents an Ellipse enclosed in rect that can draw itself onto ICanvas
    """
    def __init__(self, x1: float, y1: float, x2: float, y2: float, color: QColor):
        self.start = GraphicsPoint(x1, y1)
        self.size  = GraphicsPoint(x2, y2)
        self.color = color
        self.transformations = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ])

    def paint(self, canvas: ICanvas):
        orig_x = self.start.x
        orig_y = self.start.y

        a = self.size.x / 2
        b = self.size.y / 2
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
            points = list(map(
                lambda p: GraphicsPoint(p.y, p.x),
                points
            ))

        for i in points:
            i.transform(self.transformations)

        canvas.draw_lines(points, self.color)
        canvas.fill(points, self.color)


    @property
    def color(self) -> QColor:
        return self._color


    @color.setter
    def color(self, value):
        self._color = value


    def rotate(self, about: IPoint, rad: float):
        move = np.array([
            [1, 0, about.x],
            [0, 1, about.y],
            [0, 0, 1      ],
        ])
        rotate = np.array([
            [cos(rad), -sin(rad), 0],
            [sin(rad),  cos(rad), 0],
            [0,         0,        1],
        ])
        move_ = np.array([
            [1, 0, -about.x],
            [0, 1, -about.y],
            [0, 0, 1       ],
        ])
        matrix = move_ @ rotate @ move
        self.transformations = matrix @ self.transformations


class GraphicsCircle(GraphicsEllipse):
    """
    Represents a a circle enclosed in square that can draw itself onto ICanvas
    """
    def __init__(self, x1: float, y1: float, size: float, color: QColor):
        GraphicsEllipse.__init__(self, x1, y1, size, size, color)
