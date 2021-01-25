import pygame
from numpy import arange
from functools import reduce


def linear_map(x, from_, to):
    return to[0] + (to[1] - to[0]) * ((x - from_[0]) / (from_[1] - from_[0]))

def virtual_map(height):
    return lambda point: (point[0], height - point[1])


class Plot:
    def __init__(self, displaySize, bgColor, axisesColor, funColor, range_, f):
        self.displaySize = displaySize
        self.bgColor = bgColor
        self.axisesColor = axisesColor
        self.funColor = funColor
        self.range_ = range_
        self.f = f


    def plot(self):
        pygame.init()
        self.surface = pygame.display.set_mode(self.displaySize)
        pygame.display.set_caption("diit_pz1911_y2_cg1_safonov")

        while True:
            self.surface.fill(self.bgColor)
            self.axises()
            self.function()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

        
    def axises(self):
        points = [(x, self.f(x)) for x in arange(self.range_[0], self.range_[1], (self.range_[1] - self.range_[0]) / self.surface.get_width())]
        rangeY = reduce(
                lambda old, point: (min(old[0], point[0]), max(old[1], point[1])),
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


    def function(self):
        pygame.draw.lines(
                self.surface,
                self.axisesColor,
                False,
                (
                    (0, 0),
                    (0, self.surface.get_height()),
                    self.surface.get_size()
                    ),
                10
                )


def main():
    plot_ = Plot(
                (800, 600),
                (255, 255, 255),
                (0, 0, 0),
                (0, 0, 0),
                (-10, 10),
                lambda x: x
            )
    plot_.plot() 


if __name__ == "__main__":
    main()
