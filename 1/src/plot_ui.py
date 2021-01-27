import pygame
import pygame_gui
from numpy import arange
from math import sin
from pygame_gui.windows import UIColourPickerDialog
from enum import Enum, auto
from plot import Plot


class ButtonHandled:
    def __init__(self, relative_rect, text, manager, handle):
        self.button = pygame_gui.elements.UIButton(
            relative_rect = relative_rect,
            text = text,
            manager = manager
        )

        self.handle = handle


class PlotUI:
    class State(Enum):
        DEF = auto()
        NEW_FUN = auto()
        SETTINGS = auto()


    class ColorState(Enum):
        DEF = auto()
        AXES = auto()
        TEXT = auto()
        BG = auto()


    def __init__(self):
        pygame.init()

        initSize = (800, 600)

        self.canvas = pygame.display.set_mode(initSize)
        pygame.display.set_caption("diit_pz1921_cg1_safonov")

        self.plot = Plot(
            bgColor = (255, 255, 255),
            axesColor = (0, 255, 0),
            axesWidth = 4,
            textColor = (255, 0, 0),
            fontSize = 16
        )
        self.ui = pygame_gui.UIManager(initSize)

        self.buttonSize = (200, 60)
        
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
                    UIColourPickerDialog(
                        pygame.Rect(160, 50, 420, 400),
                        self.uiSettings,
                        window_title = "Choose colour",
                        initial_colour = pygame.Color(self.plot.bgColor)
                    ),
                    PlotUI.ColorState.BG
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
                    UIColourPickerDialog(
                        pygame.Rect(160, 50, 420, 400),
                        self.uiSettings,
                        window_title = "Choose colour",
                        initial_colour = pygame.Color(self.plot.axesColor)
                    ),
                    PlotUI.ColorState.AXES
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
        
        self.state = PlotUI.State.DEF
        self.colourState = PlotUI.ColorState.DEF


    def setState(self, state):
        self.state = state

    
    def setColourPicker(self, cp, state):
        self.colourPicker = cp
        self.colourState = state


    def disable_buttons(self):
        pass

    
    def enable_buttons(self):
        pass


    def run(self):
        clock = pygame.time.Clock()
        isRunning = True
        while isRunning:
            delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                isRunning = event.type != pygame.QUIT
                
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        for bh in self.buttons:
                            if event.ui_element == bh.button:
                                bh.handle(event)
                        for bh in self.settings:
                            if event.ui_element == bh.button:
                                bh.handle(event)
                    if event.user_type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                        if self.colourState == PlotUI.ColorState.AXES:
                            self.plot.axesColor = event.colour
                        if self.colourState == PlotUI.ColorState.BG:
                            self.plot.bgColor = event.colour
                    if (event.user_type == pygame_gui.UI_WINDOW_CLOSE and
                            event.ui_element == self.colourPicker):
                        self.colourPicker = None
                        self.colourState = PlotUI.ColorState.DEF

                if self.state == PlotUI.State.DEF:
                    self.ui.process_events(event)
                elif self.state == PlotUI.State.SETTINGS:
                    self.uiSettings.process_events(event)
                
            self.plot.update(self.canvas.get_size())
            self.canvas.blit(self.plot.surface, (0, 0))
            
            if self.state == PlotUI.State.DEF:
                self.ui.update(delta)
                self.ui.draw_ui(self.canvas)
            elif self.state == PlotUI.State.SETTINGS:
                self.uiSettings.update(delta)
                self.uiSettings.draw_ui(self.canvas)
            
            pygame.display.update()
