import pygame as pg
import random as rd 
from collections import deque

pg.init()
width = 30
height = 30
size = 20
screen = pg.display.set_mode((width*size, height*size))
running = True
direction =(1,0)
snake = deque([(10, 15),(11, 15),(12, 15)])
pomme = (5,5)
clock = pg.time.Clock()

def draw_snake(snake):
    for z in snake:
        x=z[0]*size
        y=z[1]*size
        rect=pg.Rect(x, y, size, size)
        pg.draw.rect(screen, (0,255,0), rect)
    
def draw_apple(pomme):
    x=pomme[0]*size
    y=pomme[1]*size
    rect=pg.Rect(x, y, size, size)
    pg.draw.rect(screen, (255,0,0), rect)

def new_snake(snake, direction, pomme) : 
    if (snake[-1][0]+direction[0],snake[-1][1]+direction[1])==pomme : 
        snake.append((snake[-1][0]+direction[0],snake[-1][1]+direction[1]))
        snake.popleft()
        pomme=(rd.randint(0,29),rd.randint(0,29))
    else : 
        snake.append((snake[-1][0]+direction[0],snake[-1][1]+direction[1]))
        snake.popleft()
    for i in range (len(snake)):
        snake[i] = (snake[i][0]%30,snake[i][1]%30)
    return (snake, pomme)

while running:
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN :
            if event.key == pg.K_q :
                running = False
            elif event.key == pg.K_RIGHT and direction != (-1,0):
                direction = (1,0)
            elif event.key == pg.K_LEFT and direction != (1,0):
                direction = (-1,0)
            elif event.key == pg.K_UP and direction != (0,1):
                direction = (0,-1)
            elif event.key == pg.K_DOWN and direction != (0,-1):
                direction = (0,1)
        elif event.type == pg.QUIT:
            running = False
    screen.fill ((255,255,255))

    for i in range(width) :
        for j in range(height) :
            if (i+j)%2 ==1 :
                rect = pg.Rect(i*size,j*size,width,height)
                col = (0,0,0)
                pg.draw.rect(screen, col, rect)
            else :
                rect = pg.Rect(i*size,j*size,width,height)
                col = (255,255,255)
                pg.draw.rect(screen, col, rect)
    draw_snake(snake)
    draw_apple(pomme)
    snake, pomme = new_snake(snake, direction, pomme)
    print(pomme)
    pg.display.update() 
