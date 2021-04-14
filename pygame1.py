import pgzrun
import random

WIDTH = 500
HEIGHT = 400

ball= Actor('ball')
ball.pos = WIDTH/2, HEIGHT/2
ballMoveX = random.randint(-7,7)
ballMoveY = random.randint(-7,7)
screenColor = (random.randint(0,254), random.randint(0,254), random.randint(0,254))


def draw():
    screen.fill(screenColor)
    ball.draw()
    
def update():
    
    global ballMoveX
    global ballMoveY
    
    ball.x += ballMoveX
    ball.y += ballMoveY
    
    if (ball.y > HEIGHT or ball.y <0): 
        ball.y -= ballMoveY
        ballMoveY = -ballMoveY
    if (ball.x > WIDTH or ball.x <0): 
        ball.x -= ballMoveX
        ballMoveX = - ballMoveX
        
pgzrun.go()
