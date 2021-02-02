import numpy as np
from enum import Enum, auto

class PlottableFunction:
    class Style(Enum):
        DOTTED = auto()
        NORMAL = auto()

    def __init__(self, color, width, rangeX, f, style = Style.NORMAL):
        self.color = color
        self.width = width
        self.rangeX = rangeX
        self.f = f
        self.style = style


    def points(self, num):
        _f = np.vectorize(self.f)
        xs = np.linspace(self.rangeX[0], self.rangeX[1], num = num)
        ys = _f(xs)
        return np.array((xs, ys))
