import pygame
from numpy import arange
from functools import reduce
from math import sin


def linear_map(x, from_, to):
    return to[0] + (to[1] - to[0]) * ((x - from_[0]) / (from_[1] - from_[0]))

def virtual_map(height):
    return lambda point: (point[0], height - point[1])


class Plot:
    def __init__(self, displaySize, bgColor, axisesColor, funColor, textColor, range_, f):
        self.displaySize = displaySize
        self.bgColor = bgColor
        self.axisesColor = axisesColor
        self.funColor = funColor
        self.textColor = textColor
        self.range_ = range_
        self.f = f


    def plot(self):
        pygame.init()
        self.font = pygame.font.Font("font.ttf", 32)
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
                10
                )
        #print("rangeY( " + str(rangeY[0]) + " , " + str(rangeY[1]) + " )")
        return rangeY


    def axises(self, rangeY):
        zeroY = self.surface.get_height() - linear_map(0, rangeY, (0, self.surface.get_height()))
        zeroX = linear_map(0, self.range_, (0, self.surface.get_width()))
        pygame.draw.line(
                self.surface,
                self.axisesColor,
                (zeroX, 0),
                (zeroX, self.surface.get_height()),
                10
            )
        pygame.draw.line(
                self.surface,
                self.axisesColor,
                (0, zeroY),
                (self.surface.get_width(), zeroY),
                10
            )

        textX = self.font.render("x", True, self.textColor)
        textY = self.font.render("y", True, self.textColor)
        textZero = self.font.render("0", True, self.textColor)

        self.surface.blit(textY, (zeroX + 10, 0))
        self.surface.blit(textX, (self.surface.get_width() - 32, zeroY - 10 - 32))
        self.surface.blit(textZero, (zeroX + 10, zeroY - 10 - 32))


def main():
    plot_ = Plot(
                displaySize = (800, 600),
                bgColor = (255, 255, 255),
                axisesColor = (0, 255, 0),
                funColor = (0, 0, 255),
                textColor = (255, 0, 0),
                range_ = (-10, 10),
                f = sin
            )
    plot_.plot() 


if __name__ == "__main__":
    main()
