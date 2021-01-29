import pygame
from ui_handled import ButtonHandled, ColourPickerHandled

class ButtonHandledFactory:
    def __init__(self, size, manager):
        self.manager = manager
        self.size = size


    def make(self, pos, text, handle):
        return ButtonHandled(
            relative_rect = pygame.Rect(pos, self.size),
            text = text,
            manager = self.manager,
            handle = handle
        )


class ColourPickerHandledFactory:
    def __init__(self, size, text, manager):
        self.size = size
        self.text = text
        self.manager = manager


    def make(self, colour, handle):
        return ColourPickerHandled(
            self.size,
            self.manager,
            self.text,
            colour,
            handle
        )
