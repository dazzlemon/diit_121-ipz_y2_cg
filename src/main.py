import pygame


class Plot:
    def __init__(self, displaySize, bgColor, range_):
        self.displaySize = displaySize
        self.bgColor = bgColor
        self.range_ = range_


    def plot(self):
        pygame.init()
        surface = pygame.display.set_mode(self.displaySize)
        pygame.display.set_caption("diit_pz1911_y2_cg1_safonov")

        while True:
            surface.fill(self.bgColor)
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
        return


def main():
    plot_ = Plot(
                (800, 600),
                (255, 255, 255),
                (-10, 10)
            )
    plot_.plot() 


if __name__ == "__main__":
    main()
