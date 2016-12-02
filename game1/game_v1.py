import pygame

#Игра с ПРОСТЫМ объектом

#Создали окно
window  =  pygame.display.set_mode((700, 700))
pygame.display.set_caption('My first game')

#Создали игровой экран
screen = pygame.Surface((700, 700))

#Создание квадрата движущегося
square = pygame.Surface((40, 40))
x = 0
y = 0
square_go_right = True
square_go_down = True

#Запускаем основной цикл игры
done = True
while done:
    for e in pygame.event.get(): #Для выхода с игры через крестик
        if e.type == pygame.QUIT:
           done = False

    screen.fill((224, 238, 224)) #покрасили экран в формате rgba

#Перемещение элемента
    if square_go_right == True:
        x+=0.5
        if x > 660: #шриниа экрана - ширина объекта
          square_go_right = False
    else:
        x-=0.5
        if x  <  0:
            square_go_right = True
            
    if square_go_down == True:
        y+=0.5
        if x > 660: 
          square_go_down = False
    else:
        y-=0.5
        if y  <  0:
            square_go_down = True
    
    window.blit(screen, (0, 0)) #распологаем игровой экран в окне в нужных координатах
    window.blit(square, (x, y))
    pygame.display.flip() #показали окно
pygame.quit()
    
