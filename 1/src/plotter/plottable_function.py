from numpy import linspace

class PlottableFunction:
    def __init__(self, color, width, rangeX, f):
        self.color = color
        self.width = width
        self.rangeX = rangeX
        self.f = f


    def points(self, num):
        xs = linspace(self.rangeX[0], self.rangeX[1], num = num)
        ys = map(self.f, xs)
        return zip(xs, ys)
