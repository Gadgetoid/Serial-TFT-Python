# coding=ASCII#
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
import time
import socket
import math
from time import localtime, strftime
from serialtft import *


CLOCK_ORIGIN_X = SCREEN_WIDTH_HALF
CLOCK_ORIGIN_Y = SCREEN_HEIGHT_HALF-1
CLOCK_RADIUS	  = SCREEN_HEIGHT_HALF-20

DEBUG = True

serialport = serial.Serial("/dev/tty.usbserial-A4013DP7", 9600, timeout=0.5)

serialport.write(set_color(0,255,0,0))
serialport.write(set_color(1,0,0,0))
serialport.write(set_color(2,255,255,255))
serialport.write(set_color(3,255,255,255))
serialport.write(set_color(4,255,255,255))
serialport.write(set_color(5,255,255,255))
#serialport.write(set_color(6,255,255,255))
#serialport.write(set_color(7,255,255,255))

# Clear Screen
serialport.write(SCREEN_LANDSCAPE)
serialport.write(BG_COL_BLACK)
serialport.write(CLEAR_SCREEN)

# Draw clock outline
serialport.write(FG_COL_MAGENTA)
serialport.write(draw_filled_circle(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS))
time.sleep(0.1)

# Fill clock with black
serialport.write(FG_COL_BLACK)
serialport.write(draw_filled_circle(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-2))
time.sleep(0.1)

# Draw numbers 12, 6, 3 and 9
serialport.write(FG_COL_WHITE)
serialport.write(draw_filled_circle(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,3))
time.sleep(0.1)

serialport.write(FONT_SIZE_SMALL)

serialport.write(FG_COL_GREEN)

serialport.write(goto_pixel(SCREEN_WIDTH_HALF-5,5))
serialport.write('12')

serialport.write(goto_pixel(SCREEN_WIDTH_HALF-3,SCREEN_HEIGHT - 13))
serialport.write('6')

serialport.write(goto_pixel(SCREEN_WIDTH_HALF+50,SCREEN_HEIGHT_HALF-3))
serialport.write('3')

serialport.write(goto_pixel(SCREEN_WIDTH_HALF-54,SCREEN_HEIGHT_HALF-3))
serialport.write('9')

lasthour = -1
lastmin = -1
lastsec = -1

while 1:
	currentmin = time.localtime().tm_min
	currentsec = time.localtime().tm_sec
	currenthour = time.localtime().tm_hour

	if(currenthour > 12):
		currenthour = currenthour - 12 # Adjust from 24-hour time
	
	currenthour = (currenthour * 5) + (currentmin/10) # Adjust hour to range 0-60

	# Erase any old hands

	serialport.write(FG_COL_BLACK)

	if( lasthour != currenthour ):
		serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-25,lasthour))

	if( lastmin != currentmin ):
		serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-10,lastmin))

	if( lastsec != currentsec ):
		serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-15,lastsec))


	# Redraw new hands and ones we may have erased above
	# Because the lines intersect closer to the origin they need to be redrawn when intersection ends

	serialport.write(FG_COL_BLUE)
	serialport.write(goto_char(1,14))
	serialport.write(strftime("%H:%M:%S", localtime())+chr(13))
	serialport.write(goto_char(26 - len(strftime("%a", localtime())),14))
	serialport.write(strftime("%a", localtime())+chr(13))

	serialport.write(FG_COL_WHITE)

	serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-25,currenthour))

	serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-10,currentmin))
		
	serialport.write(FG_COL_RED)
	serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-15,currentsec))
	
	lasthour = currenthour
	lastmin = currentmin
	lastsec = currentsec
	
	time.sleep(1)

