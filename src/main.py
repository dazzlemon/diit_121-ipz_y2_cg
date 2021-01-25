import pygame


class Plot:
    range_ = (-10, 10)
    displaySize = (800, 600)
    bgColor = (255, 255, 255)
    #etc


    def plot(self):
        pygame.init()
        surface = pygame.display.set_mode(self.displaySize)
        pygame.display.set_caption("diit_pz1911_y2_cg1_safonov")

        while True:
            surface.fill(self.bgColor)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()


def main():
    plot_ = Plot()
    plot_.plot() 


if __name__ == "__main__":
    main()
