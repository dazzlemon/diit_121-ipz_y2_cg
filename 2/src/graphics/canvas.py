"""
CG2
"""
from typing import List
from more_itertools import pairwise
from PyQt5.QtWidgets import QGraphicsScene
from ._interfaces import ICanvas, IPoint

class QCanvas(ICanvas):
    """
    QGraphicsScene wrapper(adapter) to use with IGraphicsItem
    """
    def __init__(self, canvas: QGraphicsScene):
        self.canvas = canvas

    def draw_lines(self, points: List[IPoint]):
        """draws lines between i-th and (i-1)-th points"""
        for p1, p2 in pairwise(points):
            self.canvas.addLine(p1.x, p1.y, p2.x, p2.y)


    def fill(self, points: List[IPoint]):
        """fills all pixels in space closed by lines between i-th and (i-1)-th points"""