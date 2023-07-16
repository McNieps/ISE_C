import pygame

from ise.app.app import App


App.init(None, default_only=True)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
