"""
IGraphicsItem to use with ICanvas, and its extensions
"""
from canvas import ICanvas

class IPoint:
    @property
    def x(self):
        """returns x component of point"""


    @property
    def y(self):
        """returns y component of point"""


    @x.setter
    def x(self, value):
        """sets x component of point"""


    @y.setter
    def y(self, value):
        """sets y component of point"""


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


class GraphicsLine(IGraphicsItem):
    """
    Represents a 2D line
    """
    start: GraphicsPoint
    end: GraphicsPoint



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
    rect: GraphicsSquare


class GraphicsPolygon(IGraphicsItem):
    """
    Represents a polygon that can draw itself onto ICanvas
    """
