import pygame
import pygame_gui
from numpy import arange
from math import sin
from pygame_gui.windows import UIColourPickerDialog
from enum import Enum, auto
from plot import Plot
from ui_handled import ButtonHandled, ColourPickerHandled


class PlotUI:
    class State(Enum):
        DEF = auto()
        NEW_FUN = auto()
        SETTINGS = auto()


    def __init__(self):
        pygame.init()
        initSize = (800, 600)
        self.canvas = pygame.display.set_mode(initSize)
        pygame.display.set_caption("diit_pz1921_cg1_safonov")
        
        self.buttonSize = (200, 60)
        self.init_menu(initSize)
        self.init_settings(initSize)

        self.plot = Plot(
            bgColor = (255, 255, 255),
            axesColor = (0, 255, 0),
            axesWidth = 4,
            textColor = (255, 0, 0),
            fontSize = 16
        )
        self.state = PlotUI.State.DEF

    
    def init_menu(self, initSize):
        self.ui = pygame_gui.UIManager(initSize)

        def plot_two(event):
            self.plot.plot(
                xs = arange(-10, 10, 0.1),
                ys = list(map(
                    lambda x: sin(x),
                    arange(-10, 10, 0.1)
                )),
                color = (0, 0, 255),
                width = 4
            )
            self.plot.plot(
                xs = arange(0, 20, 0.1),
                ys = list(map(
                    lambda x: 2*x,
                    arange(0, 20, 0.1)
                )),
                color = (0, 255, 255),
                width = 2
            )


        self.buttons = [
            ButtonHandled(
                relative_rect = pygame.Rect(
                    (0, 0),
                    self.buttonSize
                ),
                text = "Plot new function",
                manager = self.ui,
                handle = plot_two
            ),
            ButtonHandled(
                relative_rect = pygame.Rect(
                    (0, self.buttonSize[1]),
                    self.buttonSize
                ),
                text = "Clear",
                manager = self.ui,
                handle = lambda event: self.plot.clear()

            ),
            ButtonHandled(
                relative_rect = pygame.Rect(
                    (0, self.buttonSize[1] * 2),
                    self.buttonSize
                ),
                text = "Settings",
                manager = self.ui,
                handle = lambda event: self.setState(PlotUI.State.SETTINGS)

            )
        ]


    def init_settings(self, initSize):
        cpSize = pygame.Rect(100, 50, 420, 400)
        self.uiSettings = pygame_gui.UIManager(initSize)
        self.settings = [
            ButtonHandled(
                relative_rect = pygame.Rect(
                    (0, 0),
                    self.buttonSize
                ),
                text = "Background Color",
                manager = self.uiSettings,
                handle = lambda event: self.setColourPicker(
                    ColourPickerHandled(
                        cpSize,
                        self.uiSettings,
                        "Choose colour",
                        pygame.Color(self.plot.bgColor),
                        handle = lambda event: self.plot.set_bg_color(event.colour)
                    )
                )
            ),
            ButtonHandled(
                relative_rect = pygame.Rect(
                    (0, self.buttonSize[1]),
                    self.buttonSize
                ),
                text = "Axes Color",
                manager = self.uiSettings,
                handle = lambda event: self.setColourPicker(
                    ColourPickerHandled(
                        cpSize,
                        self.uiSettings,
                        "Choose colour",
                        pygame.Color(self.plot.axesColor),
                        handle = lambda event: self.plot.set_axes_color(event.colour)
                    )
                )
            ),
            ButtonHandled(
                relative_rect = pygame.Rect(
                    (0, self.buttonSize[1] * 2),
                    self.buttonSize
                ),
                text = "Axes Width",
                manager = self.uiSettings,
                handle = lambda event: 0

            ),
            ButtonHandled(
                relative_rect = pygame.Rect(
                    (0, self.buttonSize[1] * 3),
                    self.buttonSize
                ),
                text = "Return",
                manager = self.uiSettings,
                handle = lambda event: self.setState(PlotUI.State.DEF)
            )
        ] 


    def setState(self, state):
        self.state = state

    
    def setColourPicker(self, cp):
        self.colourPicker = cp


    def disable_buttons(self):
        pass

    
    def enable_buttons(self):
        pass


    def process_events(self, event):
        self.isRunning = event.type != pygame.QUIT
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                for bh in self.buttons:
                    if event.ui_element == bh.button:
                        bh.handle(event)
                for bh in self.settings:
                    if event.ui_element == bh.button:
                        bh.handle(event)
            if event.user_type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                self.colourPicker.handle(event)
            if (event.user_type == pygame_gui.UI_WINDOW_CLOSE and
                    event.ui_element == self.colourPicker):
                self.colourPicker = None

        if self.state == PlotUI.State.DEF:
            self.ui.process_events(event)
        elif self.state == PlotUI.State.SETTINGS:
            self.uiSettings.process_events(event)


    def run(self):
        clock = pygame.time.Clock()
        self.isRunning = True
        while self.isRunning:
            delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                self.process_events(event)
            self.plot.update(self.canvas.get_size())
            self.canvas.blit(self.plot.surface, (0, 0))
            
            if self.state == PlotUI.State.DEF:
                self.ui.update(delta)
                self.ui.draw_ui(self.canvas)
            elif self.state == PlotUI.State.SETTINGS:
                self.uiSettings.update(delta)
                self.uiSettings.draw_ui(self.canvas)
            
            pygame.display.update()
