import pygame as pg
import random

WIDTH = 400
HEIGHT = 600
FPS = 30

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255 ,0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)

# My Sprite

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
    def update(self):
        self.rect.x += 1
        if self.rect.left>WIDTH:
            self.rect.right = 0




pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Test Sprite")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
p1 = Player()
all_sprites.add(p1)

#Create Game Loop
running = True
while running:
    #Input (event)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
    #Update
    all_sprites.update()
    #Render
    screen.fill(GREEN)
    all_sprites.draw(screen)

    pg.display.flip()
pg.quit