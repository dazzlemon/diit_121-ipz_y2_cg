"""
IGraphicsItem to use with ICanvas, and its extensions
"""
from ._interfaces import ICanvas, IPoint

class IGraphicsItem:
    """
    Graphics item that can draw itself onto ICanvas
    """
    def paint(self, canvas: ICanvas):
        """paints this item onto canvas"""


    def move(self, delta: IPoint):
        """moves the item point by delta"""


    def rotate(self, about: IPoint, rad: float):
        """rotates the item about given point by given amount of radians"""


    def scale(self, about: IPoint, mul: float):
        """scales the item about given point by given scale"""


class GraphicsPoint(IPoint, IGraphicsItem):
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


class GraphicsLine(IGraphicsItem):
    """
    Represents a 2D line
    """

    def __init__(self, x1, y1, x2, y2):
        self.start = GraphicsPoint(x1, y1)
        self.end   = GraphicsPoint(x2, y2)


    def paint(self, canvas: ICanvas):
        canvas.draw_lines([self.start, self.end])


class GraphicsRect(IGraphicsItem):
    """
    Represents a rectangle that can draw itself onto ICanvas
    """
    start: GraphicsPoint

    @property
    def size(self) -> GraphicsPoint:
        """.x -> width .y - height"""


    @size.setter
    def size(self, value):
        """sets size with new GraphicsPoint"""


class GraphicsEllipse(IGraphicsItem):
    """
    Represents an Ellipse enclosed in rect that can draw itself onto ICanvas
    """
    rect: GraphicsRect


class GraphicsSquare(GraphicsRect):
    """
    Represents a square that can draw itself onto ICanvas
    """
    @property
    def size(self) -> GraphicsPoint:
        """same as GraphicsRect.size but x and y actually have the same value"""


class GraphicsCircle(GraphicsEllipse):
    """
    Represents a a circle enclosed in square that can draw itself onto ICanvas
    """
    def __init__(self, rect: GraphicsSquare):
        self.rect = rect


class GraphicsPolygon(IGraphicsItem):
    """
    Represents a polygon that can draw itself onto ICanvas
    """
