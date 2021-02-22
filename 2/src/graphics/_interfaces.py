"""
Interfaces
"""
from typing import List
from PyQt5.QtGui import QColor

class IPoint:
    """
    2d point
    """
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


class ICanvas:
    """
    A canvas that can execute simple drawing operations(drawing polygon and filling it)
    """
    def draw_lines(self, points: List[IPoint], color: QColor):
        """draws lines between i-th and (i-1)-th points"""


    def fill(self, points: List[IPoint], color: QColor):
        """fills all pixels in space closed by lines between i-th and (i-1)-th points"""


class IDrawable:
    """
    Graphics item that can be drawn on ICanvas
    """
    @property
    def points(self) -> List[IPoint]:
        """returns points to draw on canvas"""


    @property
    def color(self) -> QColor:
        """color"""


    def paint(self, canvas: ICanvas):
        """paints this item onto canvas"""



class IAffineTransformable:
    """
    Graphics item that can be moved/scaled/rotated
    """
    def move(self, delta: IPoint):
        """moves the item point by delta"""


    def rotate(self, about: IPoint, rad: float):
        """rotates the item about given point by given amount of radians"""


    def scale(self, about: IPoint, w: float, h: float):
        """scales the item about given point by given scale"""
