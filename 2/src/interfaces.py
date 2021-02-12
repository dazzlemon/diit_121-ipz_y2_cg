"""
CG2
"""
from typing import List
from PyQt5.QtWidgets import QGraphicsScene

class ICanvas:
    """
    A canvas that can execute simple drawing operations(drawing polygon and filling it)
    """
    def draw_lines(self, lines: List[GraphicsPoint]):
        """draws lines between i-th and (i-1)-th points"""


    def fill(self, lines: List[GraphicsPoint]):
        """fills all pixels in space closed by lines between i-th and (i-1)-th points"""


class IGraphicsItem:
    """
    Graphics item that can draw itself onto ICanvas
    """
    def paint(self, canvas: ICanvas):
        """paints this item onto canvas"""


    def move(self, delta: GraphicsPoint):
        """moves the item point by delta"""


    def rotate(self, about: GraphicsPoint, rad: float):
        """rotates the item about given point by given amount of radians"""


    def scale(self, about: GraphicsPoint, mul: float):
        """scales the item about given point by given scale"""


class GraphicsLine(IGraphicsItem):
    """
    Represents a 2D line
    """
    start: GraphicsPoint
    end: GraphicsPoint


class GraphicsPoint(IGraphicsItem):
    """
    Represents a 2D point that can draw itself onto ICanvas
    """
    x: int
    y: int


class GraphicsRect(IGraphicsItem):
    """
    Represents a rectangle that can draw itself onto ICanvas
    """
    start: GraphicsPoint
    size: GraphicsPoint


class GraphicsEllipse(IGraphicsItem):
    """
    Represents an Ellipse enclosed in rect that can draw itself onto ICanvas
    """
    rect: GraphicsRect


class GraphicsSquare(GraphicsRect):
    """
    Represents a square that can draw itself onto ICanvas
    """


class GraphicsCircle(GraphicsEllipse):
    """
    Represents a a circle enclosed in square that can draw itself onto ICanvas
    """


class GraphicsPolygon(IGraphicsItem):
    """
    Represents a polygon that can draw itself onto ICanvas
    """


class QCanvas(ICanvas):
    """
    QGraphicsScene wrapper(adapter) to use with IGraphicsItem
    """
    canvas: QGraphicsScene
