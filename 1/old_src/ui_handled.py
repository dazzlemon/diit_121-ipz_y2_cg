import pygame_gui
from pygame_gui.windows import UIColourPickerDialog

class ButtonHandled:
    def __init__(self, relative_rect, text, manager, handle):
        self.button = pygame_gui.elements.UIButton(
            relative_rect = relative_rect,
            text = text,
            manager = manager
        )
        self.handle = handle


class ColourPickerHandled:
    def __init__(self, relative_rect, manager, title, colour, handle):
        self.colourPicker = UIColourPickerDialog(
            relative_rect,
            manager,
            window_title = title,
            initial_colour = colour
        )

        self.handle = handle
