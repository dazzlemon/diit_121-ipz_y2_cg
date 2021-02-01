import numpy as np
from functools import reduce
from more_itertools import pairwise
from PyQt5.QtGui import QPen, QBrush, QColorConstants
from PyQt5.QtCore import QLineF, QPointF
from enum import Enum, auto
from .plottable_function import PlottableFunction
from .math_2d import linear_map_2d, points_frame, widest_frame, linear_map

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
            self._calculate_frame(funcs)
            self._draw_axes(scene)
            self._draw_funcs(scene, funcs)
            if self.markupOn:
                self._draw_markup(scene)

        scene.update()

    
    def _calculate_frame(self, funcs):
        funcs_points = [func.points(self._w) for func in funcs]# [[(x, y)]]
        frames = map(points_frame, funcs_points)# [(minX, minY, maxX, minY)]
        self._frame = reduce(widest_frame, frames)# (minX, minY, maxX, maxY)


    def _fill_bg(self, scene):
        scene.addRect(0, 0, self._w, self._h, QPen(), QBrush(self.bgColor))


    def _draw_funcs(self, scene, funcs):
        for func in funcs:
            points = list(map(
                lambda point: self._map_to_frame(point),
                func.points(self._w)
            ))
            brush = QBrush(func.color)
            
            if func.style == PlottableFunction.Style.NORMAL:
                pen = QPen(brush, func.width)
                for p0, p1 in pairwise(points):
                    point_i0 = QPointF(p0[0], p0[1])
                    point_i1 = QPointF(p1[0], p1[1])
                    line = QLineF(point_i0, point_i1)
                    scene.addLine(line, pen)
            elif func.style == PlottableFunction.Style.DOTTED:
                pen = QPen(QColorConstants.Transparent)
                for point in points[::10]:
                    self.add_circle(scene, point, func.width, pen, brush)
            
            self._draw_intersections(scene, func)


    def _draw_axes(self, scene):
        zero = self._map_to_frame((0, 0))
        pen = QPen(QBrush(self.axesColor), self.axesWidth)

        scene.addLine(QLineF(0, zero[1], self._w, zero[1]), pen)
        scene.addLine(QLineF(zero[0], 0, zero[0], self._h), pen)


    def _map_to_frame(self, point):
        return linear_map_2d(point, self._frame, (0, self._h, self._w, 0))


    def _map_to_frame_x(self, x):
        return linear_map(x, (self._frame[0], self._frame[2]), (0, self._w))


    def _map_to_frame_y(self, y):
        return linear_map(y, (self._frame[1], self._frame[3]), (self._h, 0))


    def _map_from_frame(self, point):
        return linear_map_2d(point, (0, self._h, self._w, 0), self._frame)


    def _map_from_frame_x(self, x):
        return linear_map(x, (0, self._w), (self._frame[0], self._frame[2]))


    def _map_from_frame_y(self, y):
        return linear_map(y, (self._h, 0), (self._frame[1], self._frame[3]))


    def _draw_intersections(self, scene, func):
        points = func.points(self._w)
        intersection_idx = self._intersections_x(points)
        virtual_intersections = map(
            lambda point: self._map_to_frame_x(point[0]),
            np.array(points)[intersection_idx]
        )

        zeroY = self._map_to_frame_y(0)
 
        for x in virtual_intersections:
            self._draw_mark(scene, (x, zeroY))

        if func.rangeX[0] <= 0 <= func.rangeX[1]:
            point = self._map_to_frame((0, func.f(0)))
            self._draw_mark(scene, point)


    def _draw_mark(self, scene, point):
        pen = QPen(QColorConstants.Transparent)
        brush = QBrush(self.marksColor)
        if self.marksStyle == Plotter.MarksStyle.CIRCLE:
            self.add_circle(scene, point, self.marksSize, pen, brush)
        elif self.marksStyle == Plotter.MarksStyle.SQUARE:
            self.add_rect(scene, point, self.marksSize, pen, brush)
    

    @staticmethod
    def _intersections_x(points):
        ys = list(map(lambda point: point[1], points))
        idx = np.flatnonzero(np.diff(np.sign(ys)))
        """
        1 - mapping values to -1, 0, 1 aka signs
        2 - inner difference(ith - i-1th, so if diff == 0 sign didnt change(1 - 1 or -1 - -1))
        3 - getting nonzero idxs
        """
        return idx


    def _draw_markup(self, scene):
        """
        SOME MAGIC NUMBERS HERE, I DIDNT FIND ANY OTHER WAY TO REPOSITION TEXT
        IT ACTUALLY SEEMS TO DO WITH UNSCALABLE FONT
        IF THE COMMENT IS STILL THERE I DIDNT FIND THE FIX(EITHER BECAUSE THERE IS NONE OR I DIDNT HAVE TIME)
        """
        n = 10
        width = 2

        brush = QBrush(self.markupColor)
        pen = QPen(brush, width)
        
        zero = self._map_to_frame((0, 0))
        zeroText = (
            zero[0] + max(self.axesWidth, self.markupSize) / 2,
            zero[1] - 2 * self.textSize - max(self.axesWidth, self.markupSize) / 2
        )
        step = (self._w / n, self._h / n)

        xs = self.linspace_range((0, self._w), zero[0], step[0])
        for x in xs:
            self.add_line(scene, (x, zero[1]), self.markupSize, 0, pen)
            
            text = scene.addText("{:.2e}".format(self._map_from_frame_x(x)))
            text.font().setPixelSize(self.textSize)
            text.font().setFamily("Arial")
            text.setDefaultTextColor(self.textColor)
            text.setPos(x - self.textSize * 3, zeroText[1])
        
        ys = self.linspace_range((0, self._h), zero[1], step[1])
        for y in ys:
            self.add_line(scene, (zero[0], y), self.markupSize, 1, pen)
            
            text = scene.addText("{:.2e}".format(self._map_from_frame_y(y)))
            text.font().setPixelSize(self.textSize)
            text.setDefaultTextColor(self.textColor)
            text.setPos(zeroText[0], y - 1.5 * self.textSize)


    @staticmethod
    def linspace_range(range_, from_, step):
        ps0 = np.arange(from_ + step, range_[1], step)
        ps1 = np.arange(from_ - step, range_[0], -step)
        return np.concatenate((ps0, ps1))


    @staticmethod
    def add_line(scene, center, length, orientation, pen):
        if orientation == 0:
            start = (center[0], center[1] - length / 2)
            end = (center[0], center[1] + length / 2)
        elif orientation == 1:
            start = (center[0] - length / 2, center[1])
            end = (center[0] + length / 2, center[1])
        scene.addLine(start[0], start[1], end[0], end[1], pen)


    @staticmethod
    def add_circle(scene, center, size, pen, brush):
        origin = (
            center[0] - size / 2,
            center[1] - size / 2
        )
        scene.addEllipse(origin[0], origin[1], size, size, pen, brush)


    @staticmethod
    def add_rect(scene, center, size, pen, brush):
        origin = (
            center[0] - size / 2,
            center[1] - size / 2
        )
        scene.addRect(origin[0], origin[1], size, size, pen, brush)
