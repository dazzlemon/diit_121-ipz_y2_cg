import pygame
from numpy import arange
from functools import reduce

def linear_map(x, from_, to):
    return to[0] + (to[1] - to[0]) * ((x - from_[0]) / (from_[1] - from_[0]))


def virtual_map(height):
    return lambda point: (point[0], height - point[1])


class Plot:
    def __init__(self, bgColor, axesColor, funColor, textColor, range_, lineWidth, fontSize, f):
        self.bgColor = bgColor
        self.axesColor = axesColor
        self.funColor = funColor
        self.textColor = textColor
        self.range_ = range_
        self.f = f
        self.lineWidth = lineWidth
        self.fontSize = fontSize
        self.font = pygame.font.Font("font.ttf", self.fontSize)


    def update(self, size):
        self.surface = pygame.Surface(size)
        self.surface.fill(self.bgColor)
        rangeY = self.draw_function()
        self.draw_axes(rangeY)


    def draw_function(self):
        points = [(x, self.f(x)) for x in arange(self.range_[0], self.range_[1], (self.range_[1] - self.range_[0]) / self.surface.get_width())]
        rangeY = reduce(
            lambda old, point: (min(old[0], point[1]), max(old[1], point[1])),
            points,
            (points[0][1], points[0][1])
        )

        points = map(
            lambda point: (
                int(linear_map(point[0], self.range_, (0, self.surface.get_width()))),
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
            self.funColor,
            False,
            list(points),
            self.lineWidth
        )

        return rangeY


    def draw_axes(self, rangeY):
        zeroY = self.surface.get_height() - linear_map(0, rangeY, (0, self.surface.get_height()))
        zeroX = linear_map(0, self.range_, (0, self.surface.get_width()))
        pygame.draw.line(
            self.surface,
            self.axesColor,
            (zeroX, 0),
            (zeroX, self.surface.get_height()),
            self.lineWidth
        )

        pygame.draw.line(
            self.surface,
            self.axesColor,
            (0, zeroY),
            (self.surface.get_width(), zeroY),
            self.lineWidth
        )

        textX = self.font.render("x", True, self.textColor)
        textY = self.font.render("y", True, self.textColor)
        textZero = self.font.render("0", True, self.textColor)
        textMaxY = self.font.render(str(round(rangeY[1], 3)), True, self.textColor)
        textMinY = self.font.render(str(round(rangeY[0], 3)), True, self.textColor)

        self.surface.blit(textY, (zeroX + self.lineWidth, 0))
        self.surface.blit(textX, (self.surface.get_width() - self.fontSize, zeroY - self.lineWidth - self.fontSize))
        self.surface.blit(textZero, (zeroX + self.lineWidth, zeroY - self.lineWidth - self.fontSize)) 
        self.surface.blit(textMaxY, (zeroX - self.lineWidth - self.fontSize * 3, 0))
        self.surface.blit(textMinY, (zeroX - self.lineWidth - self.fontSize * 3, self.surface.get_height() - self.fontSize))



















