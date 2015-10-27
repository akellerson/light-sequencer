#uncomment graphics to run in graphics.py
#from graphics import *
from random import randint
import time
import pygame
import os
import sys
import RPi.GPIO as GPIO

pin_map = [17,18,22,23,24,25]
GPIO.setmode(GPIO.BCM)
for i in pin_map:
    GPIO.setup(i, GPIO.OUT)

def onOff(pin, output):
    if output == '1':
        GPIO.output(pin_map[pin], 1)
    elif output == '0':
        GPIO.output(pin_map[pin], 0)



def play():
    
    #pygame.quit()
    # this works don't mess with it
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load('Jingle.mp3')
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.play(-1)
        while pygame.mixer.music.get_busy():
            #print "Playing..."
            clock.tick(1000)
            blinkyFile()
            time.sleep(2)
            break


def greenOrRed(value):

    if value == '1':
        return "red"
    elif value == '0':
        return "green"

def blinkyFile():
    
    ###########
    # uncomment this code if you want to run a graphics.py
    # graphical window
    # initialize graphics window
    #win = GraphWin('buttons',900,300)
    # number of buttons
    #numOfButtons = 6
    
    # create six buttons
    #buttonArray = ['button'+str(i) for i in range(numOfButtons)]
    # make buttons circles
    #for i in range(numOfButtons):
    #    buttonArray[i]=Circle(Point(((150*i)+75),150), 25)
    #    buttonArray[i].draw(win)
    ############

  
    start = time.time()

    f = open('testseq.txt')
    for line in f:
        i = line.split(',')
        beatTime = float(i[1].rstrip())
        while((time.time()-start) < beatTime):
            n = 0
        for y in range(len(i[0])):
            print "this should be single digit",y
            print "this should be single digit",i[0][y]
            #uncomment to run in graphics.py
            #buttonArray[y].setFill(greenOrRed(i[0][y]))
            onOff(y, i[0][y])
    f.close()


 
   
def main():
    #blinkyFile()
    play()
    GPIO.cleanup()

main()



