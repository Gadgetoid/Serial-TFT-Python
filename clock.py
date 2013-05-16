# Hobbytronics TFT - analogue clock example code (clock.py)
# Modified from original clock example by Philip Howard
# Displays an analogue clock face with hour/min/sec hands
# and the current Day and time at the bottom of the screen.
# Run in background using command..
# sudo python clock.py &
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
CLOCK_BACKGROUND = COL_BLACK
CLOCK_OUTLINE	= COL_MAGENTA
CLOCK_CENTER		= COL_BLUE
CLOCK_NUMBERS	= COL_GREEN
CLOCK_DIGITAL	= COL_CYAN
CLOCK_HOUR_HAND	= COL_BLUE
CLOCK_MINUTE_HAND= COL_BLUE
CLOCK_SECOND_HAND= COL_RED

serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

# Change this to set the theme if you're using firmware that supports it
# serialport.write(COL_THEME_RED)

# Clear Screen
serialport.write(SCREEN_LANDSCAPE)
serialport.write(bg_color(CLOCK_BACKGROUND))
serialport.write(CLEAR_SCREEN)

# Draw clock outline
serialport.write(fg_color(CLOCK_OUTLINE))
serialport.write(draw_filled_circle(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS))
time.sleep(0.1)

# Fill clock with background
serialport.write(fg_color(CLOCK_BACKGROUND))
serialport.write(draw_filled_circle(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-2))
time.sleep(0.1)

# Draw the hub at the clock center
serialport.write(fg_color(CLOCK_CENTER))
serialport.write(draw_filled_circle(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,3))
time.sleep(0.1)

# Draw the numbers 12, 6, 3 and 9 around the clock in green

serialport.write(FONT_SIZE_SMALL)

serialport.write(fg_color(CLOCK_NUMBERS))

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

	serialport.write(fg_color(CLOCK_BACKGROUND))

	if( lasthour != currenthour ):
		serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-25,lasthour))

	if( lastmin != currentmin ):
		serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-10,lastmin))

	if( lastsec != currentsec ):
		serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-15,lastsec))

	# Draw the time/day at the bottom of the screen

	serialport.write(fg_color(CLOCK_DIGITAL))
	serialport.write(goto_char(1,14))
	serialport.write(strftime("%H:%M:%S", localtime())+chr(13))
	serialport.write(goto_char(26 - len(strftime("%a", localtime())),14))
	serialport.write(strftime("%a", localtime())+chr(13))

	# Redraw hands

	serialport.write(fg_color(CLOCK_HOUR_HAND))

	serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-25,currenthour))

	serialport.write(fg_color(CLOCK_MINUTE_HAND))

	serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-10,currentmin))
		
	serialport.write(fg_color(CLOCK_SECOND_HAND))
	serialport.write(analogue_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-15,currentsec))
	
	lasthour = currenthour
	lastmin = currentmin
	lastsec = currentsec
	
	time.sleep(1)

