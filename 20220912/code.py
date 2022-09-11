# This project expresses how the emotion of love progresses from being chill to passionate.
# The LED light blinks "love you" in morse code.
# Each alphabet is blinked in different color to express the deepened emotion of love.
# The LED light begins from green which represents the early stages of love.
# The color slowly changes to red, representing the deepened love.


import time
import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3


while True:
    led[0] = (0, 0, 0)
    time.sleep(1)

    #"L" in morse code, color green
    led[0] = (0, 153, 76)
    time.sleep(0.5)
    led[0] = (0, 0, 0)
    time.sleep(0.1)

    led[0] = (0, 153, 76)
    time.sleep(1.5)
    led[0] = (0, 0, 0)
    time.sleep(0.1)

    led[0] = (0, 153, 76)
    time.sleep(0.5)
    led[0] = (0, 0, 0)
    time.sleep(0.1)

    led[0] = (0, 153, 76)
    time.sleep(0.5)
    led[0] = (0, 0, 0)
    time.sleep(1)


    #"O" in morse code, color green blue
    led[0] = (0,153,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (0,153,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (0,153,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(1)

    #"V" in morse code, color blue green
    led[0] = (0,76,153)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (0,76,153)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (0,76,153)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (0,76,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(1)

    #"E" in morse code, color blue
    led[0] = (0,0,153)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(1)

    #"Y" in morse code, color blue red
    led[0] = (76,0,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (76,0,153)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (76,0,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (76,0,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(1)

    #"O" in morse code, color red blue
    led[0] = (153,0,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (153,0,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (153,0,153)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(1)

    #"E" in morse code, color red
    led[0] = (153,0,76)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (153,0,76)
    time.sleep(0.5)
    led[0] = (0,0,0)
    time.sleep(0.1)

    led[0] = (153,0,76)
    time.sleep(1)
    led[0] = (0,0,0)
    time.sleep(5)
