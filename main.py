import pygame
import sys

import config.const
from src.video_element import VideoElement

from src.game_element import GameElement

if __name__ =="__main__":
    pygame.init()
    window=pygame.display.set_mode((config.const.SCREEN_WIDTH, config.const.SCREEN_HEIGHT))
    table= GameElement(config.const.TABLE_BASE_POS,config.const.TABLE, config.const.SCREEN_WIDTH,config.const.SCREEN_HEIGHT)

    video_file=config.const.VYDEO_FOLDER
    player=VideoElement(video_file)

should_continue=True
playing_video = False  # Flag to track if a video is playing
while should_continue:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             should_continue=False
            # pygame.quit()
            # sys.exit()

        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not playing_video:
                # If SPACE is pressed and no video is playing, play a random video
                playing_video = True  # Start video playback
                video_path = player.get_random_video()
                if video_path:
                    # Play video and check if we should continue
                   should_continue= player.play_video(window, video_path)
        
                playing_video = False  # Reset flag after playback

                

    if not playing_video:                
        table.draw(window, table.scaled_image())  # Redraw table if no video is playing

    # # Fill the screen with a color (e.g., white)
    # window.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

pygame.quit()