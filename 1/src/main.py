import pygame
import pygame_gui
from numpy import arange
from functools import reduce
from math import sin
from pygame_gui.windows import UIColourPickerDialog
from enum import Enum, auto


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


class PlotUI:
    class State(Enum):
        DEF = auto()
        CHOOSING_FUN = auto()
        CHOOSING_BG = auto()
        CHOOSING_TXT = auto()
        CHOOSING_MARKS = auto()


    def __init__(self):
        pygame.init()

        initSize = (800, 600)

        self.canvas = pygame.display.set_mode(initSize)
        pygame.display.set_caption("diit_pz1921_cg1_safonov")

        self.plot = Plot(
            bgColor = (255, 255, 255),
            axesColor = (0, 255, 0),
            funColor = (0, 0, 255),
            textColor = (255, 0, 0),
            range_ = (-10, 10),
            f = sin,
            lineWidth = 4,
            fontSize = 16
        )
        self.ui = pygame_gui.UIManager(initSize)

        self.buttonSize = (200, 60)

        self.buttonFunColour = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect(
                (0, 0), 
                self.buttonSize
            ),
            text = "Change function colour",
            manager = self.ui
        )

        self.buttonBgColour = pygame_gui.elements.UIButton(
            relative_rect = pygame.Rect(
                (0, self.buttonSize[1]),
                self.buttonSize
            ),
            text = "Change background colour",
            manager = self.ui
        )

        self.state = PlotUI.State.DEF


    def disable_buttons(self):
        self.buttonBgColour.disable()
        self.buttonFunColour.disable()

    
    def enable_buttons(self):
        self.buttonBgColour.enable()
        self.buttonFunColour.enable()


    def run(self):
        clock = pygame.time.Clock()
        isRunning = True
        while isRunning:
            delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                isRunning = event.type != pygame.QUIT
                
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.buttonFunColour:
                            self.colourPicker = UIColourPickerDialog(
                                pygame.Rect(160, 50, 420, 400),
                                self.ui,
                                window_title = "Choose colour",
                                initial_colour = pygame.Color(self.plot.funColor)
                            )
                            self.disable_buttons()
                            self.state = PlotUI.State.CHOOSING_FUN
                        if event.ui_element == self.buttonBgColour:
                            self.colourPicker = UIColourPickerDialog(
                                pygame.Rect(160, 50, 420, 400),
                                self.ui,
                                window_title = "Choose colour",
                                initial_colour = pygame.Color(self.plot.bgColor)
                            )
                            self.disable_buttons()
                            self.state = PlotUI.State.CHOOSING_BG
                        

                    if event.user_type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                        if self.state == PlotUI.State.CHOOSING_FUN:
                            self.plot.funColor = (event.colour.r, event.colour.g, event.colour.b)
                        if self.state == PlotUI.State.CHOOSING_BG:
                            self.plot.bgColor = event.colour
                        

                    if (event.user_type == pygame_gui.UI_WINDOW_CLOSE and
                            event.ui_element == self.colourPicker):
                        self.enable_buttons()
                        self.colourPicker = None
                        self.state = PlotUI.State.DEF

                self.ui.process_events(event)
                
            self.plot.update(self.canvas.get_size())
            self.ui.update(delta)
            self.canvas.blit(self.plot.surface, (0, 0))
            self.ui.draw_ui(self.canvas)
            pygame.display.update()


def main():
    plotUi = PlotUI()
    plotUi.run()

if __name__ == "__main__":
    main()
