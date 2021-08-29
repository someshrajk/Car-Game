import time
import pygame
import random 

pygame.init()
width=800
height=600

black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,255)

car_width=45
car_height=80

gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption("Car Game") 

icon=pygame.image.load('images.jpg') 
pygame.display.set_icon(icon)

clock=pygame.time.Clock() 

Car1Img= pygame.image.load("car1.png") 
Car2Img= pygame.image.load("car2.png")
bgImg= pygame.image.load("track.jpg")
crashImg= pygame.image.load("crash.png")
bgsImg=pygame.image.load("rd.jpg")



def highscore(count):
    font=pygame.font.Sysfont('None',50)
    test=font.render("SCORE BOARD :"+str(count),True,black)
    gameDisplay.blit(test,(30,30))

def dthings(thingx,thingy,thingz):
    gameDisplay.blit(thingz,(thingx,thingy))

def car(x,y):
    gameDisplay.blit(Car1Img,(x,y))

def object(test,font):
    testSurface=font.render(test,True,blue)
    return testSurface,testSurface.get.rect()

def message(test,size,x,y):
    font=pygame.font.Font("freesansbold.ttf",size)
    test_Surface,test_rectangle=object(test,font)
    test_rectangle.center=(x,y)
    gameDisplay.blit(test_Surface,test_rectangle)

def crash(x,y):
    gameDisplay.blit(crashImg,(x,y))
    message("YOU CRASHED THE CAR",64,width/2,height/2)

    pygame.display.update()
    time.sleep(2)
    loop()

def loop():
    bgx1=(width/2)-(360/2)
    bgx2=(width/2)-(360/2)
    bgy1=0
    bgy2=-600
    bgspeed=15
    speed_change=0
    car_x=((width/2)-(car_width/2))
    car_y=(height-car_height)
    carx_change=0
    road_start=(width/2)-130
    road_end=(width/2)+130

    thing_startx=random.randint(road_start,road_end-car_width)
    thing_starty=-600
    thingw=50
    thingh=100
    thing_speed=30
    count=0

    gameExit= False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True 
                pygame.quir()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_Left:
                    carx_change=-30
                elif event.key == pygame.K_Right:
                    carx_change= 30 

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_Left or event.key == pygame.K_Right:
                    carx_change= 0
                
        car_x +=carx_change 

        if car_x > road_end-car_width:
            crash(car_x-car_y)
        if car_x < road_start:
            crash(car_x-car_width,car_y)


        if car_y < thing_starty + thingh:
            if car_x >= thing_startx and car_x <=thing_startx + thingw:
                crash(car_x-25,car_y-car_height/2)
            if car_x+car_width >= thing_startx and car_x+car_width <= thing_startx + thingw:
                crash(car_x,car_y-car_height/2)


        gameDisplay.fill(green)
        gameDisplay.blit(bgsImg,(0,0))
        gameDisplay.blit(bgsImg,(440,0))

        gameDisplay.blit(bgImg,(bgx1,bgy1))
        gameDisplay.blit(bgImg,(bgx2,bgy2))

        car(car_x,car_y)
        dthings(thing_startx,thing_starty,Car2Img) 
        
        highscore(count)
        count+=1 

        thing_starty+= thing_speed

        if thing_starty > height:
            thing_startx = random.randrange(road_start,road_end-car_width)
            thing_starty = -200 

        bgy1 +=bgspeed 
        bgy2 +=bgspeed

        if bgy1 >= height:
            bgy1 = -600 

        if bgy2 >= height:
            bdy2 = -600


        pygame.display.update()
        clock.tick(60)

loop()                  



               





