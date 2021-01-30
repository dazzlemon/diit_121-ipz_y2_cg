from PyQt5 import QtCore, QtGui

class Plotter:
    def __init__(self):
        self.bgColor = None
        
        self.axesColor = None
        self.axesWidth = None

        self.textColor = None
        self.textSize = None

        self.marksColor = None
        self.marksStyle = None
        self.marksSize = None

        self.funcs = []


    def add_func(self, func):
        self.funcs.append(func)


    def clear(self):
        self.funcs.clear()


    def plot(self, scene):
        scene.clear()

        x = scene.width()
        y = scene.height()

        scene.addRect(0, 0, x, y, QtGui.QPen(), QtGui.QBrush(QtGui.QColor(255, 255, 0)))

        scene.addLine(QtCore.QLineF(0, 0, x, y))
        scene.addLine(QtCore.QLineF(0, y, x, 0))
        
        scene.update()
