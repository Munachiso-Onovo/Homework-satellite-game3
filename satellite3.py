import random 
import pgzrun
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []
start_time = 0
end_time = 0
total_time = 0
next_satellite = 0
number_satellite = 8

def create_satellite():
    global start_time
    for i in range(0,number_satellite):
        satellite = Actor("car2.png")
        satellite.pos = random.randint(40,750),random.randint(40,550)
        satellites.append(satellite)
    start_time = time()

def draw():
    screen.blit("starry.jpg",(0,0))
    number = 1
    for i in satellites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20)) #The +20 puts the number beside the satellite
        i.draw()
        number += 1 #number +=1 is another way of saying number = number + 1
    global total_time
    
    for i in lines:
        screen.draw.line(i[0],i[1],"yellow")

    if next_satellite < number_satellite:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)),[10,10],fontsize = 40)
    
    else:
        screen.draw.text(str(round(total_time,1)),[10,10],fontsize = 40)
    
    def update():
        pass

def on_mouse_down(pos):
    global next_satellite
    global lines
    if next_satellite < number_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite - 1].pos,satellites[next_satellite].pos))
            next_satellite += 1
        else:
            lines = []
            next_satellite = 0




create_satellite()




pgzrun.go()


