from numpy import linspace
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
        xs = linspace(self.rangeX[0], self.rangeX[1], num = num)
        ys = map(self.f, xs)
        return list(zip(xs, ys))
