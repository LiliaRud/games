import pygame

#Игра с ИГРОВЫМ объектом

window  =  pygame.display.set_mode((700, 700))
pygame.display.set_caption('My first game')
screen = pygame.Surface((700, 700))

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        #self.bitmap.set_colorkey((0, 0, 0)) #Какой цвет у изображения сделать прозрачным
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y)) #Отображает оъект на игровой экран

#Создаем героя и цель, порядок отображения зависит от того, кто прописан сначала
hero = Sprite(0, 0, 'lion.ico')
hero.go_right = True
hero.go_down = True
goal = Sprite(200, 400, 'love_cloud.png')

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
           done = False

    screen.fill((205, 145, 158))

    if hero.go_right == True:
        hero.x += 1
        if hero.x > 444:
            hero.go_right = False
    else:
        hero.x -= 1
        if hero.x < 0:
            hero.go_right = True

    if hero.go_down == True:
        hero.y += 1
        if hero.y > 444:
            hero.go_down = False
    else:
        hero.y -= 1
        if hero.y < 0:
            hero.go_down = True

    #Отображаем объекты
    hero.render()
    goal.render()
    
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5) #Замедление скорости с использованием задржки времени
pygame.quit()
