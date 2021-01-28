import pygame
import pygame_gui
from numpy import arange
from math import cos
from enum import Enum, auto
from plot import Plot
from factories import ButtonHandledFactory, ColourPickerHandledFactory


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
        self.init_new_fun(initSize)

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
        bhf = ButtonHandledFactory(self.buttonSize, self.ui)

        self.buttons = [
            bhf.make(
                pos = (0, 0),
                text = "Plot new function",
                handle = lambda event: self.setState(PlotUI.State.NEW_FUN)
            ),
            bhf.make(
                (0, self.buttonSize[1]),
                text = "Clear",
                handle = lambda event: self.plot.clear()

            ),
            bhf.make(
                (0, self.buttonSize[1] * 2),
                text = "Settings",
                handle = lambda event: self.setState(PlotUI.State.SETTINGS)

            )
        ]


    def init_settings(self, initSize):
        self.uiSettings = pygame_gui.UIManager(initSize)
        bhf = ButtonHandledFactory(self.buttonSize, self.uiSettings)
        cphf = ColourPickerHandledFactory(
            pygame.Rect(100 ,50, 420, 400),
            "Choose colour",
            self.uiSettings
        )

        self.settings = [
            bhf.make(
                (0, 0),
                text = "Background Color",
                handle = lambda event: self.setColourPicker(
                    cphf.make(
                        pygame.Color(self.plot.bgColor),
                        lambda event: self.plot.set_bg_color(event.colour)
                    )
                )
            ),
            bhf.make(
                (0, self.buttonSize[1]),
                text = "Axes Color",
                handle = lambda event: self.setColourPicker(
                    cphf.make(
                        pygame.Color(self.plot.axesColor),
                        handle = lambda event: self.plot.set_axes_color(event.colour)
                    )
                )
            ),
            bhf.make(
                (0, self.buttonSize[1] * 2),
                text = "Text Color",
                handle = lambda event: self.setColourPicker(
                    cphf.make(
                        pygame.Color(self.plot.textColor),
                        handle = lambda event: self.plot.set_text_color(event.colour)
                    )
                )

            ),
            bhf.make(
                (0, self.buttonSize[1] * 3),
                text = "Return",
                handle = lambda event: self.setState(PlotUI.State.DEF)
            )
        ] 


    def init_new_fun(self, initSize):
        self.uiFun = pygame_gui.UIManager(initSize)
        bhf = ButtonHandledFactory(self.buttonSize, self.uiFun)
        cphf = ColourPickerHandledFactory(
            pygame.Rect(100, 50, 420, 400),
            "Choose colour",
            self.uiFun
        )

        def plot_with(start, end, step, f, color, width):
            xs = arange(start, end, step)
            return lambda event: self.plot.plot(
                xs = xs,
                ys = list(map(f, xs)),
                color = color,
                width = width
            )


        def fun(a, b):
            return lambda x: abs(x) + a * cos(b * x)

        self.funButtons = [
            bhf.make(
                pos = (0, 0),
                text = "f1",
                handle = plot_with(
                    start = -3,
                    end = 3,
                    step = 0.01,
                    f = fun(2, -1),
                    color = (0, 0, 255),
                    width = 4
                )
            ),
            bhf.make(
                pos = (0, self.buttonSize[1] * 1),
                text = "f2",
                handle = plot_with(
                    start = -6,
                    end = 0,
                    step = 0.01,
                    f = fun(1, -2),
                    color = (255, 255, 0),
                    width = 2
                )
            ),
            bhf.make(
                pos = (0, self.buttonSize[1] * 2),
                text = "Return",
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
                for bh in self.funButtons:
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
        elif self.state == PlotUI.State.NEW_FUN:
            self.uiFun.process_events(event)


    def update(self, delta):
        self.plot.update(self.canvas.get_size())
        self.canvas.blit(self.plot.surface, (0, 0))
            
        if self.state == PlotUI.State.DEF:
            self.ui.update(delta)
            self.ui.draw_ui(self.canvas)
        elif self.state == PlotUI.State.SETTINGS:
            self.uiSettings.update(delta)
            self.uiSettings.draw_ui(self.canvas)
        elif self.state == PlotUI.State.NEW_FUN:
            self.uiFun.update(delta)
            self.uiFun.draw_ui(self.canvas)
            
        pygame.display.update()


    def run(self):
        clock = pygame.time.Clock()
        self.isRunning = True
        while self.isRunning:
            for event in pygame.event.get():
                self.process_events(event)
            self.update(clock.tick(60) / 1000.0)
            
