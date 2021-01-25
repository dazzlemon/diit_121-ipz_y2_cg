import pygame


class Plot:
    def __init__(self, displaySize, bgColor, axisesColor, range_):
        self.displaySize = displaySize
        self.bgColor = bgColor
        self.axisesColor = axisesColor
        self.range_ = range_


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
        return


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
                (-10, 10)
            )
    plot_.plot() 


if __name__ == "__main__":
    main()
