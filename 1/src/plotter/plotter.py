from functools import reduce
from more_itertools import pairwise
from PyQt5.QtGui import QPen, QBrush, QColorConstants
from PyQt5.QtCore import QLineF, QPointF
from .plottable_function import PlottableFunction
from .math_2d import linear_map_2d, points_frame, widest_frame, linear_map
import numpy as np

class Plotter:
    def __init__(self, bgColor, axesColor, axesWidth, marksColor, marksSize, marksStyle = None, textColor = None, textSize = None):
        self.bgColor = bgColor
        
        self.axesColor = axesColor
        self.axesWidth = axesWidth

        self.textColor = textColor
        self.textSize = textSize

        self.marksColor = marksColor
        self.marksStyle = marksStyle
        self.marksSize = marksSize


    def plot(self, scene, funcs):
        scene.clear()

        self._w = int(scene.width())
        self._h = int(scene.height())

        self._fill_bg(scene)
        if len(funcs) > 0:
            self._calculate_frame(funcs)
            self._draw_axes(scene)
            self._draw_funcs(scene, funcs)
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
            points = map(
                lambda point: self._map_to_frame(point),
                func.points(self._w)
            )
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


    def _draw_intersections(self, scene, func):
        points = func.points(self._w)
        intersection_idx = self._intersections_x(points)
        virtual_intersections = map(
            lambda point: self._map_to_frame_x(point[0]),
            np.array(points)[intersection_idx]
        )

        zeroY = self._map_to_frame_y(0)

        pen = QPen(QColorConstants.Transparent)
        brush = QBrush(self.marksColor)
        for x in virtual_intersections:
            self.add_circle(scene, (x, zeroY), self.marksSize, pen, brush)

        if func.rangeX[0] <= 0 <= func.rangeX[1]:
            point = self._map_to_frame((0, func.f(0)))
            self.add_circle(scene, point, self.marksSize, pen, brush)
            


    @staticmethod
    def _intersections_x(points):
        ys = list(map(lambda point: point[1], points))
        idx = np.argwhere(np.diff(np.sign(ys))).flatten()
        """
        1 - mapping values to -1, 0, 1 aka signs
        2 - inner difference(if two neighbours have -1, 1 or 1, -1 than function has value zero between them(so new array has idx around that val))
        3 - getting idx of 0s
        4 - one dimensional arrray
        """
        return idx


    def _draw_markup(self, scene):
        pass

    
    @staticmethod
    def add_circle(scene, center, size, pen, brush):
        origin = (
            center[0] - size / 2,
            center[1] - size / 2
        )
        scene.addEllipse(origin[0], origin[1], size, size, pen, brush)
