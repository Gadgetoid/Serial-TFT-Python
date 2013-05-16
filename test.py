# coding=ASCII
import math

CMD_BEGIN	= chr(27)
CMD_END		= chr(255)
RETURN		= chr(13)

BG_COL_BLACK		= CMD_BEGIN + chr(2) + chr(0) + CMD_END
BG_COL_BLUE		= CMD_BEGIN + chr(2) + chr(1) + CMD_END
BG_COL_RED		= CMD_BEGIN + chr(2) + chr(2) + CMD_END
BG_COL_GREEN		= CMD_BEGIN + chr(2) + chr(3) + CMD_END
BG_COL_CYAN		= CMD_BEGIN + chr(2) + chr(4) + CMD_END
BG_COL_MAGENTA	= CMD_BEGIN + chr(2) + chr(5) + CMD_END
BG_COL_YELLOW	= CMD_BEGIN + chr(2) + chr(6) + CMD_END
BG_COL_WHITE		= CMD_BEGIN + chr(2) + chr(7) + CMD_END

FG_COL_BLACK		= CMD_BEGIN + chr(1) + chr(0) + CMD_END
FG_COL_BLUE		= CMD_BEGIN + chr(1) + chr(1) + CMD_END
FG_COL_RED		= CMD_BEGIN + chr(1) + chr(2) + CMD_END
FG_COL_GREEN		= CMD_BEGIN + chr(1) + chr(3) + CMD_END
FG_COL_CYAN		= CMD_BEGIN + chr(1) + chr(4) + CMD_END
FG_COL_MAGENTA	= CMD_BEGIN + chr(1) + chr(5) + CMD_END
FG_COL_YELLOW	= CMD_BEGIN + chr(1) + chr(6) + CMD_END
FG_COL_WHITE		= CMD_BEGIN + chr(1) + chr(7) + CMD_END

LINE_BEGINNING	= CMD_BEGIN + chr(5) + CMD_END
TEXT_BEGINNING 	= CMD_BEGIN + chr(6) + chr(0) + chr(0) + CMD_END

SCREEN_PORTRAIT_LEFT 			= CMD_BEGIN + chr(3) + chr(0) + CMD_END
SCREEN_LANDSCAPE_UPSIDEDOWN  	= CMD_BEGIN + chr(3) + chr(1) + CMD_END
SCREEN_PORTRAIT_RIGHT 		= CMD_BEGIN + chr(3) + chr(2) + CMD_END
SCREEN_LANDSCAPE 			= CMD_BEGIN + chr(3) + chr(3) + CMD_END

FONT_SIZE_SMALL 	= CMD_BEGIN + chr(4) + chr(1) + CMD_END
FONT_SIZE_MEDIUM = CMD_BEGIN + chr(4) + chr(2) + CMD_END
FONT_SIZE_LARGE 	= CMD_BEGIN + chr(4) + chr(3) + CMD_END

CLEAR_SCREEN		= CMD_BEGIN + chr(0) + CMD_END

SCREEN_WIDTH		= 160
SCREEN_HEIGHT	= 128

SCREEN_WIDTH_HALF	= SCREEN_WIDTH/2
SCREEN_HEIGHT_HALF	= SCREEN_HEIGHT/2

# Command helper functions

def draw_bitmap(file,x,y):
	return CMD_BEGIN + chr(13) + chr(x) + chr(y) + file + CMD_END

def goto_pixel(pixel_x,pixel_y):
	return CMD_BEGIN + chr(7) + chr(pixel_x) + chr(pixel_y) + CMD_END

def goto_char(char_x,char_y):
	return CMD_BEGIN + chr(6) + chr(char_x) + chr(char_y) + CMD_END

def draw_line(x1,y1,x2,y2):
	return CMD_BEGIN + chr(8) + chr(x1) + chr(y1) + chr(x2) + chr(y2) + CMD_END

def draw_box(x1,y1,x2,y2):
	return CMD_BEGIN + chr(9) + chr(x1) + chr(y1) + chr(x2) + chr(y2) + CMD_END

def draw_filled_box(x1,y1,x2,y2):
	return CMD_BEGIN + chr(9) + chr(x1) + chr(y1) + chr(x2) + chr(y2) + CMD_END

def draw_circle(x,y,radius):
	return CMD_BEGIN + chr(11) + chr(x) + chr(y) + chr(radius) + CMD_END

def draw_filled_circle(x,y,radius):
	return CMD_BEGIN + chr(12) + chr(x) + chr(y) + chr(radius) + CMD_END

def analogue_hand(origin_x,origin_y,radius,minutes):
	angle = (minutes / 60.0) * (2*math.pi)
	x = origin_x + radius*math.sin(angle)
	y = origin_y - radius*math.cos(angle)

	x_a = origin_x + 6*math.sin(angle)
	y_a = origin_y - 6*math.cos(angle)
	
	return draw_line(int(round(x_a)),int(round(y_a)),int(round(x)),int(round(y)))
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
from time import localtime, strftime


CLOCK_ORIGIN_X = SCREEN_WIDTH_HALF
CLOCK_ORIGIN_Y = SCREEN_HEIGHT_HALF-1
CLOCK_RADIUS	  = SCREEN_HEIGHT_HALF-20

DEBUG = True

serialport = serial.Serial("/dev/tty.usbserial-A4013DP7", 9600, timeout=0.5)

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

