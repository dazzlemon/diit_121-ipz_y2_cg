"""
CG2
"""
from typing import List
from more_itertools import pairwise
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtGui import QPolygonF, QPen, QBrush, QColor
from PyQt5.QtCore import QPointF
from ._interfaces import ICanvas, IPoint

class QCanvas(ICanvas):
    """
    QGraphicsScene wrapper(adapter) to use with IGraphicsItem
    """
    def __init__(self, canvas: QGraphicsScene):
        self.canvas = canvas


    def draw_lines(self, points: List[IPoint], color: QColor):
        """draws lines between i-th and (i-1)-th points"""
        for p1, p2 in pairwise(points):
            self.canvas.addLine(p1.x, p1.y, p2.x, p2.y, QPen(color))


    def fill(self, points: List[IPoint], color: QColor):
        """fills all pixels in space closed by lines between i-th and (i-1)-th points"""
        self.canvas.addPolygon(QPolygonF(map(
            lambda ip: QPointF(ip.x, ip.y),
            points
        )), QPen(color), QBrush(color))
