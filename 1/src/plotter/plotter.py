from PyQt5 import QtCore, QtGui

class Plotter:
    def __init__(self, bgColor, axesColor = None, axesWidth = None, textColor = None, textSize = None, marksColor = None, marksStyle = None, marksSize = None):
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
        self._rangeX = (-3, 3)# tmp val
        self._rangeY = (-1, 5)# tmp val

        self._fill_bg(scene)
        self._draw_funcs(scene)
        self._draw_axes(scene)
        self._draw_intersections(scene)
        self._draw_markup(scene)

        scene.update()


    def _fill_bg(self, scene):
        scene.addRect(0, 0, self._w, self._h, QtGui.QPen(), QtGui.QBrush(self.bgColor))


    def _draw_funcs(self, scene):
        for func in self.funcs:
            points = map(
                lambda point: (
                    self.linear_map(point[0], self._rangeX, (0, self._w)),
                    self.linear_map(point[1], self._rangeY, (self._h, 0))
                ),
                func.points(self._w)
            )

            for point in points:
                scene.addEllipse(point[0], point[1], func.width, func.width, QtGui.QPen(), QtGui.QBrush(func.color))


    def _draw_axes(self, scene):
        pass


    def _draw_intersections(self, scene):
        pass


    def _draw_markup(self, scene):
        pass

    
    @staticmethod
    def linear_map(x, from_, to):
        return to[0] + (to[1] - to[0]) * ((x - from_[0]) / (from_[1] - from_[0]))
