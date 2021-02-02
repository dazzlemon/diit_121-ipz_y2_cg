import numpy as np
from functools import reduce
from more_itertools import pairwise
from PyQt5.QtGui import QPen, QBrush, QColorConstants, QFont
from PyQt5.QtCore import QLineF, QPointF, QRectF
from enum import Enum, auto
from .plottable_function import PlottableFunction
from .private.plotter_math import *

class Plotter:
    class MarksStyle(Enum):
        CIRCLE = auto()
        SQUARE = auto()


    def __init__(self, bgColor, axesColor, axesWidth, marksColor, marksSize, marksStyle, textColor, textSize, markupSize, markupColor, markupOn = False):
        self.bgColor = bgColor
        
        self.axesColor = axesColor
        self.axesWidth = axesWidth

        self.textColor = textColor
        self.textSize = textSize

        self.marksColor = marksColor
        self.marksStyle = marksStyle
        self.marksSize = marksSize

        self.markupSize = markupSize
        self.markupColor = markupColor
        self.markupOn = markupOn


    def plot(self, scene, funcs):
        scene.clear()

        self._w = int(scene.width())
        self._h = int(scene.height())

        self._fill_bg(scene)
        if len(funcs) > 0:
            self._frame = frame(np.array([f.points(self._w) for f in funcs]))
            self._draw_axes(scene)
            self._draw_funcs(scene, funcs)
            if self.markupOn:
                self._draw_markup(scene)

        scene.update()


    def _fill_bg(self, scene):
        scene.addRect(0, 0, self._w, self._h, QPen(), QBrush(self.bgColor))


    def _draw_funcs(self, scene, funcs):
        for func in funcs:
            points = list(map(
                lambda point: self._to_frame(point),
                func.points(self._w).transpose()
            ))
            brush = QBrush(func.color)
            
            if func.style == PlottableFunction.Style.NORMAL:
                pen = QPen(brush, func.width)
                for p0, p1 in pairwise(points):
                    line = QLineF(p0[0], p0[1], p1[0], p1[1])
                    scene.addLine(line, pen)
            elif func.style == PlottableFunction.Style.DOTTED:
                pen = QPen(QColorConstants.Transparent)
                for point in points[::10]:
                    o = sqr_origin(point, func.width)
                    scene.addEllipse(o[0], o[1], func.width, func.width, pen, brush)
            
            self._draw_intersections(scene, func) 


    def _draw_axes(self, scene):
        zero = self._to_frame((0, 0))
        pen = QPen(QBrush(self.axesColor), self.axesWidth)

        scene.addLine(QLineF(0, zero[1], self._w, zero[1]), pen)
        scene.addLine(QLineF(zero[0], 0, zero[0], self._h), pen)


    def _to_frame(self, point):
        return linear_map_2d(point, self._frame, (0, self._h, self._w, 0))


    def _to_frame_x(self, x):
        return linear_map(x, (self._frame[0], self._frame[2]), (0, self._w))


    def _to_frame_y(self, y):
        return linear_map(y, (self._frame[1], self._frame[3]), (self._h, 0))


    def _from_frame(self, point):
        return linear_map_2d(point, (0, self._h, self._w, 0), self._frame)


    def _from_frame_x(self, x):
        return linear_map(x, (0, self._w), (self._frame[0], self._frame[2]))


    def _from_frame_y(self, y):
        return linear_map(y, (self._h, 0), (self._frame[1], self._frame[3]))


    def _draw_intersections(self, scene, func):
        points = func.points(self._w)
        intersection_idx = intersections(points[1])
        virtual_intersections = map(
            lambda point: self._to_frame_x(point),
            points[0][intersection_idx]
        )

        zeroY = self._to_frame_y(0)
 
        for x in virtual_intersections:
            self._draw_mark(scene, (x, zeroY))

        if func.rangeX[0] <= 0 <= func.rangeX[1]:
            point = self._to_frame((0, func.f(0)))
            self._draw_mark(scene, point)


    def _draw_mark(self, scene, point):
        pen = QPen(QColorConstants.Transparent)
        brush = QBrush(self.marksColor)
        o = sqr_origin(point, self.marksSize)
        r = QRectF(o[0], o[1], self.marksSize, self.marksSize)
        if self.marksStyle == Plotter.MarksStyle.CIRCLE:
            scene.addEllipse(r, pen, brush)
        elif self.marksStyle == Plotter.MarksStyle.SQUARE:
            scene.addRect(r, pen, brush)


    def _draw_markup(self, scene):
        width = 2
        pen = QPen(QBrush(self.markupColor), width)
        font = QFont("Sans Serif")
        font.setPixelSize(self.textSize)
        
        zero = self._to_frame((0, 0))
        n = 10
        step = (self._w / n, self._h / n)

        xs = linspace_range((0, self._w), zero[0], step[0])
        for x in xs:
            l = line((x, zero[1]), self.markupSize, 0)
            scene.addLine(l[0], l[1], l[2], l[3], pen)
            point = (x - self.textSize * 3, zero[1] - self.textSize - max(self.markupSize, self.axesWidth) / 2 - 10)
            #                            3 - halfbody back                                                       10 - margin to axis / markup line
            num = self._from_frame_x(x)
            self.add_axis_subscript(scene, point, num, font, self.textColor)
        
        ys = linspace_range((0, self._h), zero[1], step[1])
        for y in ys:
            l = line((zero[0], y), self.markupSize, 1)
            scene.addLine(l[0], l[1], l[2], l[3], pen)
            point = (zero[0] + max(self.markupSize, self.axesWidth) / 2, y - self.textSize)
            num = self._from_frame_y(y)
            self.add_axis_subscript(scene, point, num, font, self.textColor)


    @staticmethod
    def add_axis_subscript(scene, pos, num, font, color):
        text = scene.addText("{:.2e}".format(num))
        text.setFont(font)
        text.setDefaultTextColor(color)
        text.setPos(pos[0], pos[1])
