from numpy import arange

class PlottableFunction:
    def __init__(self):
        self.color = None
        self.rangeX = None
        self.f = None


    def points(self, step):
        xs = arange(x[0], x[1], step)
        ys = map(f, xs)
        return zip(xs, ys)
