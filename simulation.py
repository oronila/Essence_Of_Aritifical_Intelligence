import pygame
from bots import *
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("A literal moving block")

generation = 1

population = 1000



vel = 5
run = True

movenum = 0
moves = 400
dots = []


font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('Generation: ' + str(generation), True, (255,255,255))
text2 = font.render('Moves: ' + str(moves), True, (255,255,255))
textRect = text.get_rect()
textRect2 = text.get_rect()
textRect.center = (70, 25)
textRect2.center = (430, 25)


for i in range(0,population): #intialize the population of dots
    dots.append(dot()) #intialize moves in dot class



while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    window.fill((0,0,0))

    text = font.render('Generation: ' + str(generation), True, (255,255,255))
    window.blit(text, textRect)
    text2 = font.render('Moves: ' + str(moves), True, (255,255,255))
    window.blit(text2, textRect2)

    pygame.draw.circle(window, (0,255,0), (250,20), 10, 20)

    for i in range(len(dots)): # range(dots.__len__()) also works
        if(dots[i].x<=255 and dots[i].x>=245 and dots[i].y>=15 and dots[i].y<=25 and dots[i].won==False):
            dots[i].botWin(movenum)
            #print(movenum)

        if(movenum<moves and dots[i].won==False):
            if(dots[i].movement[movenum] == 0): # W
                dots[i].y += vel
            if(dots[i].movement[movenum] == 1): # S
                dots[i].y -= vel
            if(dots[i].movement[movenum] == 2): # A
                dots[i].x -= vel
            if(dots[i].movement[movenum] == 3): # D
                dots[i].x += vel
        pygame.draw.rect(window, (255,0,0), (dots[i].x, dots[i].y, dots[i].width, dots[i].height))
    movenum+=1
    
    if(movenum>=moves):
        newdots = []
        for i in range(len(dots)):
            dots[i].calculateScore()
        for i in range(0,population): 
            newdots.append(dot())
            #print(dots[i].score)

        dots.sort(key=lambda x: x.score)
        #for i in range(len(dots)):
        #    print(dots[i].score)
        
        for i in range(0,round(population*0.4)):
            newdots[i].setMovement(dots[random.randint(round(population*0.8),population-1)].movement)
        for i in range(round(population*0.4),round(population*0.9)):
            newdots[i].setMovement(dots[random.randint(round(population*0.4),round(population*0.8))].movement)
        for i in range(round(population*0.9),population):
            newdots[i].setMovement(dots[random.randint(0,round(population*0.4)-1)].movement)
        #for i in range(0,100):
            #newdots[i].mutate()
        #    newdots.append(dots)
        newdots[0].setMovement(dots[population-1].movement)
        if(dots[population-1].score>1000 and moves>60):
            moves-=10
            moveTotal-=10
        dots = newdots
        for i in range(1,population):
            dots[i].mutate()
            #print(newdots[i].movement)
        
        
        movenum = 0
        generation+=1


    
    #pygame.draw.rect(window, (255,0,0), (x, y, width, height))
    #pygame.draw.circle(window, (0,255,0), (240, 30, 0, 5))

    pygame.display.update() 
    



pygame.quit()