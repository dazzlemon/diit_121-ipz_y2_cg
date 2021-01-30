from PyQt5 import QtCore

class Plotter:
    def __init__(self):
        pass


    def plot(self, scene):
        scene.clear()

        x = scene.width()
        y = scene.height()

        scene.addLine(QtCore.QLineF(0, 0, x, y))
        scene.addLine(QtCore.QLineF(0, y, x, 0))
        
        scene.update()
