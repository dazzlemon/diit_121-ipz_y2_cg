from functools import reduce
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPen, QBrush
from .plottable_function import PlottableFunction
from .math_2d import linear_map_2d, points_frame, widest_frame


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


    def plot(self, scene, funcs):
        scene.clear()

        self._w = int(scene.width())
        self._h = int(scene.height())

        self._fill_bg(scene)
        if len(funcs) > 0:
            self._calculate_frame(funcs)
            self._draw_funcs(scene, funcs)
            self._draw_axes(scene)
            self._draw_intersections(scene)
            self._draw_markup(scene)

        scene.update()

    
    def _calculate_frame(self, funcs):
        funcs_points = [func.points(self._w) for func in funcs]# [[(x, y)]]
        frames = map(points_frame, funcs_points)# [(minX, minY, maxX, minY)]
        self._frame = reduce(widest_frame, frames)# (minX, minY, maxX, maxY)


    def _fill_bg(self, scene):
        scene.addRect(0, 0, self._w, self._h, QtGui.QPen(), QtGui.QBrush(self.bgColor))


    def _draw_funcs(self, scene, funcs):
        for func in funcs:
            points = list(map(
                lambda point: self._map_to_frame(point),
                func.points(self._w)
            ))
            brush = QtGui.QBrush(func.color)
            
            if func.style == PlottableFunction.Style.NORMAL:
                for i in range(len(points) - 1):
                    scene.addLine(QtCore.QLineF(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1]), QPen(brush, func.width))
            elif func.style == PlottableFunction.Style.DOTTED:
                for i in range(0, len(points), 10):
                    point = points[i]
                    scene.addEllipse(point[0], point[1], func.width, func.width, QPen(QtGui.QColorConstants.Transparent), brush)


    def _draw_axes(self, scene):
        zero = self._map_to_frame((0, 0))
        scene.addLine(QtCore.QLineF(0, zero[1], self._w, zero[1]), QPen(QBrush(self.axesColor), self.axesWidth))
        scene.addLine(QtCore.QLineF(zero[0], 0, zero[0], self._h), QPen(QBrush(self.axesColor), self.axesWidth))


    def _map_to_frame(self, point):
        return linear_map_2d(point, self._frame, (0, self._h, self._w, 0))


    def _draw_intersections(self, scene):
        pass


    def _draw_markup(self, scene):
        pass 
