from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPen, QBrush
from functools import reduce
from .plottable_function import PlottableFunction

class Plotter:
    def __init__(self, bgColor, axesColor, axesWidth, textColor = None, textSize = None, marksColor = None, marksStyle = None, marksSize = None):
        self.bgColor = bgColor
        
        self.axesColor = axesColor
        self.axesWidth = axesWidth

        self.textColor = textColor
        self.textSize = textSize

        self.marksColor = marksColor
        self.marksStyle = marksStyle
        self.marksSize = marksSize

        self.funcs = []


    def add_func(self, func):
        self.funcs.append(func)


    def clear(self):
        self.funcs.clear()


    def plot(self, scene):
        scene.clear()

        self._w = int(scene.width())
        self._h = int(scene.height())

        self._fill_bg(scene)
        if len(self.funcs) > 0:
            self._calculate_frame()
            self._draw_funcs(scene)
            self._draw_axes(scene)
            self._draw_intersections(scene)
            self._draw_markup(scene)

        scene.update()

    
    def _calculate_frame(self):
        funcs_points = [func.points(self._w) for func in self.funcs]# [[(x, y)]]
        frames = map(self.points_frame, funcs_points)# [(minX, minY, maxX, minY)]
        self._frame = reduce(self.widest_frame, frames)# (minX, minY, maxX, maxY)


    def _fill_bg(self, scene):
        scene.addRect(0, 0, self._w, self._h, QtGui.QPen(), QtGui.QBrush(self.bgColor))


    def _draw_funcs(self, scene):
        for func in self.funcs:
            points = list(map(
                lambda point: self.linear_map_2d(point, self._frame, (0, self._h, self._w, 0)),
                func.points(self._w)
            ))
            if func.style == PlottableFunction.Style.NORMAL:
                for i in range(len(points) - 1):
                    scene.addLine(QtCore.QLineF(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1]), QtGui.QPen(QtGui.QBrush(func.color), func.width))
            elif func.style == PlottableFunction.Style.DOTTED:
                for i in range(0, len(points), 10):
                    point = points[i]
                    scene.addEllipse(point[0], point[1], func.width, func.width, QtGui.QPen(QtGui.QColorConstants.Transparent), QtGui.QBrush(func.color))


    def _draw_axes(self, scene):
        zero = (
            self.linear_map(0, (self._frame[0], self._frame[2]), (0, self._w)),
            self.linear_map(0, (self._frame[1], self._frame[3]), (self._h, 0))
        )

        scene.addLine(QtCore.QLineF(0, zero[1], self._w, zero[1]), QPen(QBrush(self.axesColor), self.axesWidth))
        scene.addLine(QtCore.QLineF(zero[0], 0, zero[0], self._h), QPen(QBrush(self.axesColor), self.axesWidth))


    def _draw_intersections(self, scene):
        pass


    def _draw_markup(self, scene):
        pass

    
    @staticmethod
    def linear_map_2d(point, from_frame, to_frame):
        return (
            Plotter.linear_map(point[0], (from_frame[0], from_frame[2]), (to_frame[0], to_frame[2])),
            Plotter.linear_map(point[1], (from_frame[1], from_frame[3]), (to_frame[1], to_frame[3]))
        )


    @staticmethod
    def linear_map(x, from_, to):
        return to[0] + (to[1] - to[0]) * ((x - from_[0]) / (from_[1] - from_[0]))


    @staticmethod
    def points_frame(points):
        """
        in: [(x, y)]
        out: (minX, minY, maxX. maxY)
        """
        return reduce(
            lambda frame, point: (
                min(frame[0], point[0]),
                min(frame[1], point[1]),
                max(frame[2], point[0]),
                max(frame[3], point[1])
            ),
            points,
            (points[0][0], points[0][1], points[0][0], points[0][1])
        )


    @staticmethod
    def widest_frame(r1, r2):
        return (
            min(r1[0], r2[0]),# minX
            min(r1[1], r2[1]),# minY
            max(r1[2], r2[2]),# maxX
            max(r1[3], r2[3]) # maxY
        )

