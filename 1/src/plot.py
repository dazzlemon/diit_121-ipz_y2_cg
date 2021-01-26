import pygame
from numpy import arange
from functools import reduce

def linear_map(x, from_, to):
    return to[0] + (to[1] - to[0]) * ((x - from_[0]) / (from_[1] - from_[0]))


def virtual_map(height):
    return lambda point: (point[0], height - point[1])


class Plot:
    def __init__(self, bgColor, axesColor, textColor, axesWidth, fontSize):
        self.bgColor = bgColor
        self.axesColor = axesColor
        self.axesWidth = axesWidth
        self.textColor = textColor
        self.fontSize = fontSize
        self.font = pygame.font.Font("font.ttf", self.fontSize)
        self.funs = []


    def plot(self, xs, ys, color, width):
        self.funs.append((xs, ys, color, width))

    
    def clear(self):
        self.funs.clear()


    def update(self, size):
        self.surface = pygame.Surface(size)
        self.surface.fill(self.bgColor)
        
        if len(self.funs) > 0:
            rangeX = self.range_x()
            rangeY = self.range_y()

            for f in self.funs:
                self.draw_func(f[0], f[1], rangeX, rangeY, f[2], f[3])

            self.draw_axes(rangeX, rangeY)


    def range_x(self):
        minmaxs = list(map(
            lambda points: (points[0][0], points[0][-1]),
            self.funs
        ))

        rangeX = reduce(
            lambda accum, minmax: (
                min(accum[0], minmax[0]),
                max(accum[1], minmax[1])
            ),
            minmaxs
        )

        return rangeX


    def range_y(self):
        yss = list(map(
            lambda points: list(points[1]),
            self.funs
        ))
 
        for ys in yss:
            ys.sort()

        minmaxs = list(map(
            lambda points: (points[0], points[-1]),
            yss
        ))

        rangeY = reduce(
            lambda accum, minmax: (
                min(accum[0], minmax[0]),
                max(accum[1], minmax[1])
            ),
            minmaxs
        )
        return rangeY



    def draw_func(self, xs, ys, rangeX, rangeY, color, width):
        points = zip(xs, ys)
        points = map(
            lambda point: (
                int(linear_map(point[0], rangeX, (0, self.surface.get_width()))),
                int(linear_map(point[1], rangeY, (0, self.surface.get_height())))
            ),
            points
        )

        points = map(
            virtual_map(self.surface.get_height()),
            points
        )

        pygame.draw.lines(
            self.surface,
            color,
            False,
            list(points),
            width
        )


    def draw_axes(self, rangeX, rangeY):
        zeroY = self.surface.get_height() - linear_map(0, rangeY, (0, self.surface.get_height()))
        zeroX = linear_map(0, rangeX, (0, self.surface.get_width()))
        pygame.draw.line(
            self.surface,
            self.axesColor,
            (zeroX, 0),
            (zeroX, self.surface.get_height()),
            self.axesWidth
        )

        pygame.draw.line(
            self.surface,
            self.axesColor,
            (0, zeroY),
            (self.surface.get_width(), zeroY),
            self.axesWidth
        )

        textX = self.font.render("x", True, self.textColor)
        textY = self.font.render("y", True, self.textColor)
        textZero = self.font.render("0", True, self.textColor)
        textMaxY = self.font.render(str(round(rangeY[1], 3)), True, self.textColor)
        textMinY = self.font.render(str(round(rangeY[0], 3)), True, self.textColor)

        self.surface.blit(textY, (zeroX + self.axesWidth, 0))
        self.surface.blit(textX, (self.surface.get_width() - self.fontSize, zeroY - self.axesWidth - self.fontSize))
        self.surface.blit(textZero, (zeroX + self.axesWidth, zeroY - self.axesWidth - self.fontSize)) 
        self.surface.blit(textMaxY, (zeroX - self.axesWidth - self.fontSize * 3, 0))
        self.surface.blit(textMinY, (zeroX - self.axesWidth - self.fontSize * 3, self.surface.get_height() - self.fontSize))
