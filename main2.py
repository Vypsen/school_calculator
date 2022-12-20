import pygame as pg

pg.init()

pg.display.set_caption('snake')
WIDTH = 600
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))

class Body():
    def __init__(self, size):
        self.x = WIDTH/2 - WIDTH/2%size
        self.y = WIDTH/2 - WIDTH/2%size
        self.size = size
        self.length = 4
        self.is_life = True
        self.pause = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.list_of_body = [[self.x, self.y+size],
                            [self.x, self.y+size*2],
                            [self.x, self.y+size*3],
                            [self.x, self.y+size*4]]


size = 10
is_run = True
snake = Body(size)
screen.fill((255, 255, 255))

while is_run:

    keys = pg.key.get_pressed()

    if keys[pg.K_PAUSE]:
        snake.pause = not snake.pause

    if snake.pause == False:
        if keys[pg.K_LEFT] and snake.right == False:
            snake.left = True
            snake.up = False
            snake.down = False
        if keys[pg.K_RIGHT] and snake.left == False:
            snake.right = True
            snake.up = False
            snake.down = False
        if keys[pg.K_UP] and snake.down == False:
            snake.up = True
            snake.left = False
            snake.right = False
        if keys[pg.K_DOWN] and snake.up == False:
            snake.down = True
            snake.left = False
            snake.right = False


    pg.time.delay(70)

    pg.draw.rect(screen, (0,0,0), (snake.x, snake.y, size, size))

    for i in snake.list_of_body:
        pg.draw.rect(screen, (0,0,0), (i[0], i[1], size, size))

    if snake.left or snake.right or snake.down or snake.up:
        snake.list_of_body.insert(0, [snake.x, snake.y])
        snake.list_of_body.pop()


    pg.display.update()

pg.quit()

