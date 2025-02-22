import pygame

class GameElement:
    def __init__(self, pos, image_path, screen_width, screen_height):
        self.pos=pos
        self.image=pygame.image.load(image_path)
        self.screen_width=screen_width
        self.screen_height=screen_height
     

    """transofrm picture to resulution of monitor where is programn running"""
    def scaled_image(self):
        return pygame.transform.scale(self.image,(self.screen_width,self.screen_height))
        


    #draw image
    def draw(self, dest, scaled_image):
        dest.blit(scaled_image, self.pos)


