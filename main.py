import pygame
import sys

import config.const

from src.game_element import GameElement

if __name__ =="__main__":
    pygame.init()
    window=pygame.display.set_mode((config.const.SCREEN_WIDTH, config.const.SCREEN_HEIGHT))
    table= GameElement(config.const.TABLE_BASE_POS,config.const.TABLE, config.const.SCREEN_WIDTH,config.const.SCREEN_HEIGHT)

should_continue=True
while should_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    table.draw(window, table.scaled_image())

    """I have to fix table picture to right sides"""

    # # Fill the screen with a color (e.g., white)
    # window.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

pygame.quit()