# import plasma
# from plasma import plasma2040
# import network
# import requests
import time
from machine import Pin #, ADC, I2C
from neopixel import NeoPixel
import random

# Total number of LEDs on our LED strip
num_leds = 50 # leds 5m
# num_leds = 66 # stars 10m
LED_GPIO_number = 15

# Define the LED pin number and number of LEDs
strand = NeoPixel(Pin(LED_GPIO_number), num_leds)

# Configure the button pin
button_GPIO_number = 12
button = Pin(button_GPIO_number, Pin.IN, Pin.PULL_UP)  # Adjust to Pin.PULL_DOWN if needed

# Colour list
# Define some GRB colour variables
white = 240, 140, 255 #White-ish!
red = 0, 255, 0
green = 255, 0, 0
blue = 0, 0, 255
yellow = 255, 175, 150
orange = 238, 223, 105
pink = 150, 150, 200
purple = 40, 100, 255
iceblue = 150, 25, 200
unicorn = 175, 150,255
bogey = 215, 100, 0
# our colours
iceiceblue = 207, 20, 160
darkpurple = 0, 150, 150
rose = 50, 185, 21
boldiceblue = 163, 35, 219
limegreen = 62, 41, 12
lilac = 0, 81, 164
blueiceblue = 100, 5, 110
boldpink = 25, 185, 108
amber = 142, 220, 10
iceblueagain = 133, 27, 236
neonblue = 200, 8, 177
applegreen = 100, 21, 15
jadegreen = 236, 27, 66
neongreen = 217, 42, 6
neonpink = 14, 106, 39
gold = 215, 255, 0
silver = 192, 192, 192
turquoise = 236, 27, 236

pattern4List = [blue, turquoise, green, gold, red, darkpurple]
pattern5List = [blue, green, red, gold]
count = 0
ledBrightness = []

numPatterns = 19
patternSelected = 14
speed = 0.5

# Global flag to indicate button press
button_pressed = False
debounce_time = 200  # in milliseconds
last_press_time = 0  # tracks last valid press time

# Function to handle button press
def handle_button():
    global patternSelected
    if patternSelected < numPatterns:
        patternSelected += 1
    else:
        patternSelected = 1
#     print(patternSelected)

# Interrupt handler function
def on_button_press(_):
    global button_pressed, last_press_time
    
    current_time = time.ticks_ms()
    if time.ticks_diff(current_time, last_press_time) > debounce_time:
        button_pressed = True
        last_press_time = current_time
        
# Attach the interrupt to the button pin
button.irq(trigger=Pin.IRQ_FALLING, handler=on_button_press)

def pattern1(colour1 = green, colour2 = red): # Two colour chasing
        
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

def pattern2(speed): # random twinkles
    
    for led in range(num_leds):
        
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        
        strand[led] = (r, g, b)
        strand.write()
        
    time.sleep(speed)

def pattern3(): # random colour chaser
  
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Then iterate over 15 leds
    for led in range(num_leds):
        
        strand[led] = (r, g, b)
        
        # Delay - the speed of the chaser
        time.sleep(0.1) # fixed speed as not controlling speed on the strip lights
        
        # Send the data to the strip
        strand.write()
        
def pattern4(): # 6 colour block chaser
       
    if num_leds == 66:
        for led in range(num_leds):
            if led <11:
                strand[led] = (pattern4List[0])
            elif led <22:
                strand[led] = (pattern4List[1])
            elif led <33:
                strand[led] = (pattern4List[2])
            elif led <44:
                strand[led] = (pattern4List[3])
            elif led <55:
                strand[led] = (pattern4List[4])
            else:
                strand[led] = (pattern4List[5])
    else:
        for led in range(num_leds):
            if led <10:
                strand[led] = (pattern4List[0])
            elif led <20:
                strand[led] = (pattern4List[1])
            elif led <30:
                strand[led] = (pattern4List[2])
            elif led <40:
                strand[led] = (pattern4List[3])
            else:
                strand[led] = (pattern4List[4])
                
    strand.write()
    time.sleep(speed)
    
def pattern5(): # RGBY chaser
    
    for led in range(num_leds):

        if led%4 == 0:
            strand[led] = (pattern5List[0])
        elif led%2 == 0:
            strand[led] = (pattern5List[2])
        elif (led+1)%4 == 0:
            strand[led] = (pattern5List[1])
        else:
            strand[led] = (pattern5List[3])
                
    strand.write()
    time.sleep(speed)
    
def pattern6(): # RGBY twinkles
    
    brightnessChoices = [0.1, 1] # 10% or 100% brightness
    
    for led in range(num_leds):

        if led%4 == 0:
            base_colour = pattern5List[0]
        elif led%2 == 0:
            base_colour = pattern5List[2]
        elif (led+1)%4 == 0:
            base_colour = pattern5List[1]
        else:
            base_colour = pattern5List[3]

        # Randomly chooose brightness
        brightness = brightnessChoices[random.randint(0, 1)] 
        r = int(base_colour[0] * brightness)
        g = int(base_colour[1] * brightness)
        b = int(base_colour[2] * brightness)

        strand[led] = (r, g, b)

    strand.write()
    time.sleep(speed*2)
    
def pattern7(count): # RGBY twinkles - prevents being bright or dim more than two times running
       
    brightnessChoices = [0.1, 1] # 10% or 100% brightness
    global ledBrightness
    
    # Update brightness values based on count
    if count%2 == 0:
        ledBrightness = [brightnessChoices[random.randint(0, 1)] for _ in range(num_leds)]
    else:
        ledBrightness = [0.1 if item == 1 else 1 for item in ledBrightness]

    for led in range(num_leds):
        if led%4 == 0:
            base_colour = pattern5List[0]
        elif led%2 == 0:
            base_colour = pattern5List[2]
        elif (led+1)%4 == 0:
            base_colour = pattern5List[1]
        else:
            base_colour = pattern5List[3]

        r = int(base_colour[0] * ledBrightness[led])
        g = int(base_colour[1] * ledBrightness[led])
        b = int(base_colour[2] * ledBrightness[led])

        strand[led] = (r, g, b)

    strand.write()
    time.sleep(speed*2)
    
     
while True:
    
    if button_pressed:
        handle_button()
        button_pressed = False  # Reset the flag
        
    if patternSelected <= 1:
        r1 = random.randint(0,255)
        g1 = random.randint(0,255)
        b1 = random.randint(0,255)
        r2 = random.randint(0,255)
        g2 = random.randint(0,255)
        b2 = random.randint(0,255) 
        pattern1((r1, b1, g1), (r2, b2, g2))
    elif patternSelected <= 2:
        pattern1(red, green)
    elif patternSelected <= 3:
        pattern1(blue, green)
    elif patternSelected <= 4:
        pattern1(red, gold)
    elif patternSelected <= 5:
        pattern1(green, gold)
    elif patternSelected <= 6:
        pattern1(blue, gold)
    elif patternSelected <= 7:
        pattern1(gold, silver)
    elif patternSelected <= 8:
        pattern1(green, silver)
    elif patternSelected <= 9:
        pattern1(blue, silver)
    elif patternSelected <= 10:
        pattern1(neongreen, neonblue)
    elif patternSelected <= 11:
        pattern1(neonpink, neonblue)
    elif patternSelected <= 12:
        pattern1(rose, lilac)
    elif patternSelected <= 13:
        pattern1(jadegreen, purple)
    elif patternSelected <= 14:
        pattern2(speed)
    elif patternSelected <= 15:
        pattern4()
        pattern4List.insert(0, pattern4List.pop(-1))
    elif patternSelected <= 16:
        pattern5()
        pattern5List.insert(0, pattern5List.pop(-1))
    elif patternSelected <= 17:
        pattern6()
    elif patternSelected <= 18:
        pattern7(count)
        if count == 0 or count == 2:
            count = 1
        else:
            count = 2
    else:
        pattern3()
        


        
