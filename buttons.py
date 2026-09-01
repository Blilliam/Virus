from multiprocessing import Value

import pygame
import sys


class Button:
    def __init__(self, x, y, w, h, txt):
        self.txt = pygame.font.SysFont("Arial", 45).render(txt, True, (0, 0, 255))
        self.bottom = pygame.Rect(x, y, w, h)
        self.top = pygame.Rect(x + w/20, y + h/20, w * 18/20, h * 18/20)
        self.value = False
        self.hovering = False
        self.topRadius = int(self.top.width/2)
        self.bottomRadius = int(self.bottom.width/2)

    def draw(self, screen):
        c = None
        if self.value:
            c = (50, 200, 50)
        else:
            c = (200, 50, 50)
        if self.hovering:
            pygame.draw.rect(screen, (142, 142, 142), self.bottom, border_radius=self.bottomRadius)
        pygame.draw.rect(screen, c, self.top, border_radius=self.topRadius)
        screen.blit(self.txt, (self.bottom.x + self.bottom.width/2 - self.txt.get_width()/2, self.bottom.y + self.bottom.height/2 - self.txt.get_height()/2))

    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.button == 1:
                if self.bottom.collidepoint(event.pos):
                    self.value  = not self.value
    def update(self, dt):
        self.hovering = self.bottom.collidepoint(pygame.mouse.get_pos())

class Slider:
    def __init__(self, x, y, w, h, v1, v2):
        ...

    def update(self):
        ...


