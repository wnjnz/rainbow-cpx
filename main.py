import time
from adafruit_circuitplayground.express import cpx
import simpleio


# blink red LED
# while True:
#    cpx.red_led = True
#    time.sleep(0.5)
#    cpx.red_led = False
#    time.sleep(0.5)


# Print Switch Status
#while True:
#    print("Slide switch:", cpx.switch)
#    time.sleep(0.5)


# Blinky Switch
# Note that we don't have to say if cpx.switch = True: . The True is implied in the if statement.
#while True:
#    if cpx.switch:
#        cpx.red_led = True
#    else:
#        cpx.red_led = False


# Blinky Switch 
#while True:
#    cpx.red_led = cpx.switch


# Tap Detection
#cpx.detect_taps = 1
#while True:
#    if cpx.tapped:
#        print("Tapped!")


# Tap twice to turn on
#cpx.detect_taps = 2
#while True:
#    if cpx.tapped:
#        print("Tapped!")
#        cpx.red_led = True
#        time.sleep(0.1)
#    else:
#        cpx.red_led = False

# Tap twice to toggle
#cpx.detect_taps = 2
#while True:
#    if cpx.tapped:
#        print("Tapped!")
#        if cpx.red_led:
#            cpx.red_led = False
#        else: 
#            cpx.red_led = True
#    time.sleep(0.1)


# The following code detects a shake 
#while True:
#    if cpx.shake():
#        print("Shake detected!")


# Shake to turn on light
#while True:
#    if cpx.shake(shake_threshold=20): #default fault for shake threshold is 30. lower number means detects easier.
#        print("Shake detected!")
#        cpx.red_led = True
#    else:
#        cpx.red_led = False


# make all neopixels red 
#while True: 
#    cpx.pixels.fill((50, 0, 0))


# turn on all pixels one by one. 
#numlights = 10
#while True:
#    for i in range(0, numlights):
#        cpx.pixels[i] = (255, 0, 0)
#        time.sleep (1)


# a variable is a conatiner that holds onto information
#purple = (50, 0, 50)
#blue = (0, 0, 50)

#slowly dim all red neopixels with loop and variable 
#redval = 100
#while redval > 0:
#    print ("red value is " + str(redvval))
#    cpx.pixels.fill((redval, 0, 0))
#    redval = redval - 1
#    time.sleep(0.001)


#light sensor + Plotter 
#while True:
#    print("Light:", cpx.light) 
#    print((cpx.light,))
#    time.sleep(1)


#light sensor indicator
#cpx.pixels.auto_write = False 
#cpx.pixels.brightness = 0.3
#while True:
    # light value remapped to pixel position
#    peak = simpleio.map_range(cpx.light, 0, 320, 0, 10) 
#    print(cpx.light)
#    print(int(peak))    
#    for i in range(0, 10, 1):
#        if i <= peak:
#            cpx.pixels[i] = (0, 255, 255) 
#        else:
#            cpx.pixels[i] = (0, 0, 0)
#    cpx.pixels.show()
#    time.sleep(0.05)


#print and plot accelerometer value
#while True:
#    x, y, z = cpx.acceleration
#    print((x, y, z))    
#    time.sleep(0.5)


# Main loop gets x, y and z axis acceleration, prints the values, and turns on # red, green and blue, at levels related to the x, y and z values.
# Color Glow Acclerometer 
#while True:
#    if cpx.switch:
#        print("Slide switch off!") 
#        cpx.pixels.fill((0, 0, 0)) 
#        continue
#    else: 
#        R=0
#        G=0
#        B=0
#    x, y, z = cpx.acceleration 
#    print((x, y, z))
#    if x:
#        R = int(simpleio.map_range(R + abs(int(x)), 0, 10, 0, 255))
#    if y:
#        G = int(simpleio.map_range(G + abs(int(y)), 0, 10, 0, 255))
#    if z:
#        B = int(simpleio.map_range(B + abs(int(z)), 0, 10, 0, 255))
#    cpx.pixels.fill((R, G, B))
#    print ("red: " + str(R) + " green: " + str(G) + " blue: " + str(B))


#using buttons a and b 
#while True:
#    if cpx.button_a:
#        print("Button A pressed!") 
#        cpx.pixels.fill((0, 50, 50))
#    if cpx.button_b:
#        print("Button B pressed!") 
#        cpx.pixels.fill((0, 0, 0))


#the following code uses python list slicing to light up LEDs in halves. 
#while True:
#    if cpx.button_a:
#        cpx.pixels[0:5] = [(255, 0, 0)] * 5
#    if cpx.button_b:
#        cpx.pixels[5:10] = [(0, 255, 0)] * 5 
#    else:
#        cpx.pixels.fill((0, 0, 0))
#while True:
#    print("Temperature C:", cpx.temperature) 
#    print ((cpx.temperature,))
#    time.sleep(1)


#using touchpad 
#while True:
#    if cpx.touch_A1:
#        print("Touched A1!")
#    time.sleep(0.1)


#touch the rainbow 
#while True:
#    if cpx.touch_A1:
#        print("Touched A1!")
#        cpx.pixels[6] = (255, 0, 0)
#    if cpx.touch_A2:
#        print("Touched A2!")
#        cpx.pixels[8] = (210, 45, 0)
#    if cpx.touch_A3:
#        print("Touched A3!")
#        cpx.pixels[9] = (155, 100, 0)
#    if cpx.touch_A4:
#        print("Touched A4!")
#        cpx.pixels[0] = (0, 255, 0)
#    if cpx.touch_A5:
#        print("Touched A5!")
#        cpx.pixels[1] = (0, 135, 125)
#    if cpx.touch_A6:
#        print("Touched A6!")
#        cpx.pixels[3] = (0, 0, 255)
#    if cpx.touch_A7:
#        print("Touched A7!")
#        cpx.pixels[4] = (100, 0, 155)
#    time.sleep(0.1)

#Play tone cpx.play_tone(frequency, seconds)
#while True:
#    if cpx.button_a:
#        cpx.play_tone(262, 1)
#    if cpx.button_b:
#        cpx.play_tone(294, 1)

#play the tone only when you provide an input
#while True:
#    if cpx.button_a:
#        cpx.start_tone(262)
#    elif cpx.button_b:
#        cpx.start_tone(294)
#    else:
#        cpx.stop_tone()

#play .wav file 
cpx.play_file("Wild_Eep.wav")