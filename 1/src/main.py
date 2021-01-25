import pygame
from numpy import arange
from functools import reduce
from math import sin


def linear_map(x, from_, to):
    return to[0] + (to[1] - to[0]) * ((x - from_[0]) / (from_[1] - from_[0]))

def virtual_map(height):
    return lambda point: (point[0], height - point[1])


class Plot:
    def __init__(self, displaySize, bgColor, axisesColor, funColor, textColor, range_, lineWidth, fontSize, f):
        self.displaySize = displaySize
        self.bgColor = bgColor
        self.axisesColor = axisesColor
        self.funColor = funColor
        self.textColor = textColor
        self.range_ = range_
        self.f = f
        self.lineWidth = lineWidth
        self.fontSize = fontSize


    def plot(self):
        pygame.init()
        self.font = pygame.font.Font("font.ttf", self.fontSize)
        self.surface = pygame.display.set_mode(self.displaySize)
        pygame.display.set_caption("diit_pz1911_y2_cg1_safonov")

        while True:
            self.surface.fill(self.bgColor)
            rangeY = self.function()
            self.axises(rangeY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

        
    def function(self):
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


    def axises(self, rangeY):
        zeroY = self.surface.get_height() - linear_map(0, rangeY, (0, self.surface.get_height()))
        zeroX = linear_map(0, self.range_, (0, self.surface.get_width()))
        pygame.draw.line(
                self.surface,
                self.axisesColor,
                (zeroX, 0),
                (zeroX, self.surface.get_height()),
                self.lineWidth
            )
        pygame.draw.line(
                self.surface,
                self.axisesColor,
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


def main():
    plot_ = Plot(
                displaySize = (800, 600),
                bgColor = (255, 255, 255),
                axisesColor = (0, 255, 0),
                funColor = (0, 0, 255),
                textColor = (255, 0, 0),
                range_ = (-10, 10),
                f = sin,
                lineWidth = 4,
                fontSize = 16
            )
    plot_.plot() 


if __name__ == "__main__":
    main()
