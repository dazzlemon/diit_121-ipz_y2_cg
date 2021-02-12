"""
CG2
"""
from typing import List
from PyQt5.QtWidgets import QGraphicsScene
from graphics_item import IPoint

class ICanvas:
    """
    A canvas that can execute simple drawing operations(drawing polygon and filling it)
    """
    def draw_lines(self, lines: List[IPoint]):
        """draws lines between i-th and (i-1)-th points"""


    def fill(self, lines: List[IPoint]):
        """fills all pixels in space closed by lines between i-th and (i-1)-th points"""



class QCanvas(ICanvas):
    """
    QGraphicsScene wrapper(adapter) to use with IGraphicsItem
    """
    canvas: QGraphicsScene
