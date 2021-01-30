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

        x = scene.width()
        y = scene.height()

        # tmp
        #scene.addRect(0, 0, x, y, QtGui.QPen(), QtGui.QBrush(QtGui.QColor(255, 255, 0)))
        #scene.addLine(QtCore.QLineF(0, 0, x, y))
        #scene.addLine(QtCore.QLineF(0, y, x, 0))
        # tmp

        # bg
        self.fillBg(scene)
        # funs
        # axes
        # intersections (x = 0, y = 0)
        # markup

        scene.update()


    def fillBg(self, scene):
        x = scene.width()
        y = scene.height()
        scene.addRect(0, 0, x, y, QtGui.QPen(), QtGui.QBrush(self.bgColor))
