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


class GraphicsPolygon(IGraphicsItem):
    """
    Represents a polygon that can draw itself onto ICanvas
    """


class GraphicsRect(GraphicsPolygon):
    """
    Represents a rectangle that can draw itself onto ICanvas
    """
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.start = GraphicsPoint(x1, y1)
        self.size  = GraphicsPoint(x2, y2)


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
        canvas.draw_lines(points)


class GraphicsSquare(GraphicsRect):
    """
    Represents a square that can draw itself onto ICanvas
    """
    def __init__(self, x: float, y: float, size: float):
        self.start = GraphicsPoint(x, y)
        self.size = size


    @property
    def size(self) -> GraphicsPoint:
        """same as GraphicsRect.size but x and y actually have the same value"""
        return GraphicsPoint(self._size, self._size)


    @size.setter
    def size(self, value: float):
        """value must be float"""
        self._size = value

class GraphicsEllipse(IGraphicsItem):
    """
    Represents an Ellipse enclosed in rect that can draw itself onto ICanvas
    """
    rect: GraphicsRect


class GraphicsCircle(GraphicsEllipse):
    """
    Represents a a circle enclosed in square that can draw itself onto ICanvas
    """
    def __init__(self, rect: GraphicsSquare):
        self.rect = rect
