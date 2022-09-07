print('Hello Desert Media Art!')
print("Let's blink!")

import board
import digitalio  # loading python library
import time

print("It is time" + str(time.monotonic()))

# This variable gives us access to the hardware pin, board.LED = use this, it can be pin13
led = digitalio.DigitalInOut(board.LED)

# Set the LED pin as an output so we can turn it on/off
led.direction = digitalio.Direction.OUTPUT

# Record the starting time
startTime = time.monotonic()

# Limit how long the LED is going to blink
secondsToBlink = 5

print('Starting to blink')
while (time.monotonic() - startTime)< secondsToBlink : # defalut is true
    led.value = True
    time.sleep(0.25)
    led.value = False
    time.sleep(0.25)

    print("  runtime - %.1f" % time.monotonic())
    if led.value == True:
        print("1")
    else:
        print("0")

print('All done')
