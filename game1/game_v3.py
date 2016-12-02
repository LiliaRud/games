import pygame

#Игра с взаимодействием игровых объектов между собой

window  =  pygame.display.set_mode((700, 700))
pygame.display.set_caption('My first game')
screen = pygame.Surface((700, 700))

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

def Intersect(x1, x2, y1, y2):
    if(x1>x2-256)and(x1<x2+256)and(y1>y2-256)and(y1<y2+256):
        return 1
    else:
        return 0

hero = Sprite(300, 400, 'lion.ico')
hero.up = True
goal = Sprite(300, 10, 'android.png')
goal.up = False

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
           done = False

    screen.fill((205, 145, 158))

    if hero.up == True:
        hero.y -= 1
        if hero.y == 0:
            hero.up = False
    else:
        hero.y += 1
        if hero.y == 444:
            hero.up = True

    if goal.up == True:
        goal.y -= 1
        if goal.y == 0:
            goal.up = False
    else:
        goal.y += 1
        if goal.y == 400:
            goal.up = True


    if Intersect(goal.x, hero.x, goal.y, hero.y) == True:
        hero.up = False
        goal.up = True


    hero.render()
    goal.render()
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5)
pygame.quit()
