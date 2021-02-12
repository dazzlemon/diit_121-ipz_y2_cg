"""
Interfaces
"""
from typing import List

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


class ICanvas:
    """
    A canvas that can execute simple drawing operations(drawing polygon and filling it)
    """
    def draw_lines(self, points: List[IPoint]):
        """draws lines between i-th and (i-1)-th points"""


    def fill(self, points: List[IPoint]):
        """fills all pixels in space closed by lines between i-th and (i-1)-th points"""
