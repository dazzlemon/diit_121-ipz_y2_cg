from PyQt5 import QtCore

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

        self.funs = []


    def plot(self, scene):
        scene.clear()

        x = scene.width()
        y = scene.height()

        scene.addLine(QtCore.QLineF(0, 0, x, y))
        scene.addLine(QtCore.QLineF(0, y, x, 0))
        
        scene.update()
