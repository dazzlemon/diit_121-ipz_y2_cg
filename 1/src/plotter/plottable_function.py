from numpy import linspace

class PlottableFunction:
    def __init__(self):
        self.color = None
        self.rangeX = None
        self.f = None


    def points(self, num):
        xs = linspace(x[0], x[1], num = num)
        ys = map(f, xs)
        return zip(xs, ys)
