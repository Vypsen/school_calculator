import pygame as pg 

pg.display.set_caption('snake')
WIDTH = 600
HEIGTH = 600

screen = pg.display.set_mode((WIDTH, HEIGTH))

class Body():
    def __init__(self, size):
        self.x = WIDTH/2 
        self.y = HEIGTH/2
        self.len = 4
        self.size = size
        self.is_life = True
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        
        self.list_of_body = [[self.x, self.y + size],
                             [self.x, self.y + size*2],
                             [self.x, self.y + size*3],
                             [self.x, self.y + size*4]]

        def is_dead(self):
            if ([self.x, self.y] in self.list_of_body) or self.x == WIDTH or self.x == 0 or self.y == HEIGTH or self.y == 0:
                self.is_life = False
        
            
            

size = 10
snake = Body(size)

is_run = True

while is_run:

    screen.fill((219, 24, 110))

    pg.draw.rect(screen, (0, 0, 0), (snake.x, snake.y, size, size))
    
    for i in snake.list_of_body:
        pg.draw.rect(screen, (0, 0, 0), (i[0], i[1], size, size))


    pg.display.update()


pg.quit()
