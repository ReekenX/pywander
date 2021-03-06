import pygame
from pygame.locals import KEYDOWN
from pywander.boards.base import BoardBase
from pywander.boards.switch import SwitchBoard
from pywander.boards.how_to import HowToBoard
from pywander.objects.label import LabelObject
from pywander.objects.image import ImageObject


class StartupBoard(BoardBase):
    switch_board = False
    labels = []

    def __init__(self, *args, **kwargs):
        self.background = ImageObject('background.png')

    def process_draw_on_surface(self, surface):
        self.background.draw_on_surface(surface)

        if self.labels == []:
            label = LabelObject('PYWANDER', 37)
            label.rect.left = 90
            label.rect.top = 90
            self.labels.append(label)

            label = LabelObject('IS A GAME...', 15)
            label.rect.left = 329
            label.rect.top = 109
            self.labels.append(label)

            label = LabelObject('WHERE YOU MUST SAVE THE WORLD IN', 15)
            label.rect.left = 60
            label.rect.top = 170
            self.labels.append(label)

            label = LabelObject('LESS THAN...', 25)
            label.rect.left = 410
            label.rect.top = 170
            self.labels.append(label)

            label = LabelObject('9 TIMES', 121)
            label.rect.left = 31
            label.rect.top = 184
            self.labels.append(label)

        for label in self.labels:
            label.draw_on_surface(surface)

        buffer = pygame.image.tostring(surface, 'RGB')
        self.buffer = buffer
        self.buffer_size = surface.get_size()

    def process_inputs(self, events):
        for event in events:
            if event.type == KEYDOWN:
                self.switch_board = True

    def is_time_to_switch_board(self):
        return self.switch_board

    def get_next_board(self):
        return SwitchBoard(self.buffer, self.buffer_size, HowToBoard())
