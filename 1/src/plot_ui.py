import pygame
import pygame_gui
from numpy import arange
from math import sin
from pygame_gui.windows import UIColourPickerDialog
from enum import Enum, auto
from plot import Plot

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
