from gpiozero import *
from time import sleep
import random

southRed = LED(17)
southYellow = LED(27)
southGreen = LED(22)

westRed = LED(23)
westYellow = LED(24)
westGreen = LED(25)

eastRed = LED(16)
eastYellow = LED(20)
eastGreen = LED(21)

northRed = LED(5)
northYellow = LED(6)
northGreen = LED(13)

buzzer = Buzzer(18)
button = Button(4)

all_lights = [southRed, southYellow, southGreen, northRed, northYellow, northGreen, westRed, westYellow, westGreen, eastRed, eastYellow, eastGreen]

def flash_all():
    for i in range(3):
            buzzer.on()
            for i in all_lights:
                i.on()
            sleep(0.1)
            buzzer.off()
            for i in all_lights:
                i.off()
            sleep(0.1)
            
def cycle_lights():
    for i in all_lights:
            print("Iterating through lights - presently on:" + str(i))
            i.on()
            sleep(0.2)
            i.off()
            sleep(0.2)

def accident():
    #All Green lights turn on, and buzzer beeps for
    #random intervals
    southGreen.on()
    northGreen.on()
    westGreen.on()
    eastGreen.on()
    for i in range(random.randint(5,10)):
        x = random.randint(1,10)
        buzzer.on()
        sleep(x/10)
        buzzer.off()
        sleep(x/10)
    southGreen.off()
    northGreen.off()
    westGreen.off()
    eastGreen.off()

def proper_traffic():
    for i in range(1,10):
        northRed.off()
        northGreen.on()
        southRed.off()
        southGreen.on()
        eastYellow.off()
        eastRed.on()
        westYellow.off()
        westRed.on()
        sleep(random.randint(5,10))
        northGreen.off()
        northYellow.on()
        southGreen.off()
        southYellow.on()
        sleep(2)
        northYellow.off()
        northRed.on()
        southYellow.off()
        southRed.on()
        westRed.off()
        westGreen.on()
        eastRed.off()
        eastGreen.on()
        sleep(random.randint(5,10))
        westGreen.off()
        westYellow.on()
        eastGreen.off()
        eastYellow.on()
        sleep(2)
    

while True:
    if button.is_pressed:
        proper_traffic()
        sleep(2)
        flash_all()
        sleep(2)
        cycle_lights()
        sleep(2)
        accident()