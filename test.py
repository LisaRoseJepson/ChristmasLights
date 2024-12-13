import plasma
from plasma import plasma2040
import network
import time
import requests
from machine import Pin, ADC, I2C
from neopixel import NeoPixel
import random

# Total number of LEDs on our LED strip
num_leds = 50
GPIO_number = 15

# Define the LED pin number and number of LEDs
strand = NeoPixel(Pin(GPIO_number), num_leds)

# Colour list
# Define some GRB colour variables
white = 140,240,255 #White-ish!
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 175,255,150
orange = 223, 238, 105
pink = 150,150,200
purple = 100,40,255
iceblue = 25,150,200
unicorn = 150,175,255
bogey = 100, 215, 0
# our colours
iceiceblue = 20, 207, 160
rose = 185, 50, 21
boldiceblue = 35, 163, 219
limegreen = 41, 62, 12
lilac = 81, 0, 164
blueiceblue = 5, 100, 110
boldpink = 185, 25, 108
amber = 220, 142, 10
iceblueagain = 27, 133, 236
neonblue = 8, 200, 177
applegreen = 21, 100, 15
jadegreen = 27, 236, 66
neongreen = 42, 217, 6
neonpink = 106, 14, 39
gold = 255, 215, 0
silver = 192, 192, 192

speed = 0.5

num_colours = 17

def pattern1(colour1 = green, colour2 = red, speed = 0.5):
    # Two colour chasing    
    for led in range(num_leds):
        if led%2 == 0:
            strand[led] = (colour1)
            strand.write()
        else:
            strand[led] = (colour2)
            strand.write()
    
    time.sleep(speed)
    
    for led in range(num_leds):
        if led%2 != 0:
            strand[led] = (colour1)
            strand.write()
        else:
            strand[led] = (colour2)
            strand.write()
            
    time.sleep(speed)

def pattern2(speed):
    # random twinkles
    for led in range(num_leds):
        
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        
        strand[led] = (r, g, b)
        strand.write()
        
    time.sleep(speed)
    
def pattern3(speed):
    # pulse iceblue on blue
    strand.fill((blue)) # set all LEDs on strand to low intensity blue
    strand.write()
    time.sleep(speed)
    for led in range(num_leds):
        for i in range (255, 10, -1):
            strand[led] = (iceblue)
            strand.write()
        strand[led] = (blue)
        strand.write()
            
    for led in reversed(range(num_leds)):
        for i in range (255, 10, -1):
            strand[led] = (iceblue)
            strand.write()
        strand[led] = (blue)
        strand.write()
        
def pattern4(speed):
    
    strand.fill((0,0,5))
    strand.write()
    time.sleep(speed)
    for led in range(num_leds):
        for i in range (255, 10, -1):
            strand[led] = (0, i, 0)
            strand.write()
            
    for led in reversed(range(num_leds)):
        for i in range (255, 10, -1):
            strand[led] = (i, 0, 0)
            strand.write()

def pattern5(speed): # works good with LED strip
  
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Then iterate over 15 leds
    for led in range(num_leds):
        
        # Set each LED in the range to red
        strand[led] = (r, g, b)
        
        # Delay - the speed of the chaser
        time.sleep(0.1) # fixed speed as not controlling speed on the strip lights
        
        # Send the data to the strip
        strand.write()
    
while True:
    
    # Take potentiometer reading for colour selection
    pattern2(speed)
    
  
    
# while True:
#     
#     # Take potentiometer reading for colour selection
#     
#     colour = potentiometer.read_u16()/65535*num_colours
#     
#     if redbutton.value() == 1: #If the red button is pressed
#         speed += 0.25
#         print("Red")
#         print(f"Interval: {speed}")
#     if greenbutton.value() == 1: #If the green button is pressed
#         speed -= 0.25
#         print("Green")
#         print(f"Interval: {speed}")
#         
#     if speed > 2:
#         speed = 2
#     elif speed < 0.25:
#         speed = 0.25
#     else:
#         speed = speed
#         
#     if colour <= 1:
#         r1 = random.randint(0,255)
#         g1 = random.randint(0,255)
#         b1 = random.randint(0,255)
#         r2 = random.randint(0,255)
#         g2 = random.randint(0,255)
#         b2 = random.randint(0,255) 
#         pattern1((r1, b1, g1), (r2, b2, g2), speed)
#     elif colour <= 2:
#         pattern1(red, green, speed)
#     elif colour <= 3:
#         pattern1(blue, green, speed)
#     elif colour <= 4:
#         pattern1(red, gold, speed)
#     elif colour <= 5:
#         pattern1(green, gold, speed)
#     elif colour <= 6:
#         pattern1(blue, gold, speed)
#     elif colour <= 7:
#         pattern1(gold, silver, speed)
#     elif colour <= 8:
#         pattern1(green, silver, speed)
#     elif colour <= 9:
#         pattern1(blue, silver, speed)
#     elif colour <= 10:
#         pattern1(neongreen, neonblue, speed)
#     elif colour <= 11:
#         pattern1(neonpink, neonblue, speed)
#     elif colour <= 12:
#         pattern1(rose, lilac, speed)
#     elif colour <= 13:
#         pattern1(jadegreen, purple, speed)
#     elif colour <= 14:
#         pattern2(speed)
#     elif colour <= 15:
#         pattern5(speed)
#     elif colour <= 16:
#         pattern3(speed)
#     else:
#         pattern4(speed)

        
        
