#
# Hobbytronics TFT - example code (serial_tft.py)
# Displays Raspberry Pi Logo (create as bitmap 160x128)
# and the current Day and time at the bottom of the screen.
# Run in background using command..
# sudo python serial_tft.py &
#
# See product page at http://www.hobbytronics.co.uk/tft-serial-display-18
# for full command details
#

import serial

from serialtft import *

CLOCK_ORIGIN_X = SCREEN_WIDTH_HALF
CLOCK_ORIGIN_Y = SCREEN_HEIGHT_HALF-1
CLOCK_RADIUS	  = SCREEN_HEIGHT_HALF-20

DEBUG = True

serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

# Clear Screen
serialport.write(SCREEN_LANDSCAPE)
serialport.write(BG_COL_BLACK)
serialport.write(CLEAR_SCREEN)

serialport.write(draw_bitmap("ckn.bmp",0,0))

