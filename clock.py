# Hobbytronics TFT - analogue clock example code (clock.py)
#
# This example demonstrates the serialtft library included
#
# Modified from original clock example by Philip Howard
# Displays an analogue clock face with hour/min/sec hands
# and the current Day and time at the bottom of the screen.
# Run in background using command..
# sudo python clock.py &
#
# See product page at http://www.hobbytronics.co.uk/tft-serial-display-18
# for full command details
#

import time
from time import localtime, strftime
from serialtft import SerialTFT

CLOCK_ORIGIN_X 		= SerialTFT.Screen.width_half
CLOCK_ORIGIN_Y 		= SerialTFT.Screen.height_half-1
CLOCK_RADIUS		= SerialTFT.Screen.height_half-20
CLOCK_BACKGROUND 	= SerialTFT.Color.black
CLOCK_OUTLINE		= SerialTFT.Color.magenta
CLOCK_CENTER		= SerialTFT.Color.blue
CLOCK_NUMBERS		= SerialTFT.Color.green
CLOCK_DIGITAL		= SerialTFT.Color.blue
CLOCK_HOUR_HAND 	= SerialTFT.Color.cyan
CLOCK_MINUTE_HAND 	= SerialTFT.Color.cyan
CLOCK_SECOND_HAND 	= SerialTFT.Color.red

# Setup the SerialTFT library, we want to clean up the LCD on exit
# so specify true for clear_on_exit
# We're driving the SerialTFT within sane limits,
# so we can turn off flush safely.
# SerialTFT( device, baud_rate, clear_on_exit, flush )
tft = SerialTFT("/dev/ttyAMA0", 9600, True, False)


# Uncomment the colour setup if you have firmware support
# for user-colours. Modified firmware can be found here:
# https://github.com/Gadgetoid/serial_tft_18/

# -- COLOR SETUP --
#tft.set_theme(SerialTFT.Theme.matrix)
#CLOCK_BACKGROUND 	= SerialTFT.Color.user_black
#CLOCK_OUTLINE		= SerialTFT.Color.user_magenta
#CLOCK_CENTER		= SerialTFT.Color.user_blue
#CLOCK_NUMBERS		= SerialTFT.Color.user_green
#CLOCK_DIGITAL		= SerialTFT.Color.user_blue
#CLOCK_HOUR_HAND	= SerialTFT.Color.user_cyan
#CLOCK_MINUTE_HAND 	= SerialTFT.Color.user_cyan
#CLOCK_SECOND_HAND 	= SerialTFT.Color.user_red
# -- END COLOR SETUP --

# Clear Screen
tft.screen_rotation(SerialTFT.Rotation.landscape)
tft.bg_color(CLOCK_BACKGROUND)
tft.clear_screen()

# Draw clock outline
tft.fg_color(CLOCK_OUTLINE)
tft.draw_filled_circle(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS)

# Fill clock with background
tft.fg_color(CLOCK_BACKGROUND)
tft.draw_filled_circle(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-2)

# Draw the hub at the clock center
tft.fg_color(CLOCK_CENTER)
tft.draw_filled_circle(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,3)

# Draw the numbers 12, 6, 3 and 9 around the clock in green
tft.font_size(SerialTFT.Font.small)
tft.fg_color(CLOCK_NUMBERS)

tft.goto_pixel(SerialTFT.Screen.width_half-5,5)
tft.write('12')

tft.goto_pixel(SerialTFT.Screen.width_half-3,SerialTFT.Screen.height-13)
tft.write('6')

tft.goto_pixel(SerialTFT.Screen.width_half+50,SerialTFT.Screen.height_half-3)
tft.write('3')

tft.goto_pixel(SerialTFT.Screen.width_half-54,SerialTFT.Screen.height_half-3)
tft.write('9')

lasthour	= -1
lastmin		= -1
lastsec		= -1

while 1:
	currentmin	= time.localtime().tm_min
	currentsec	= time.localtime().tm_sec
	currenthour = time.localtime().tm_hour

	if(currenthour > 12):
		currenthour = currenthour - 12 # Adjust from 24-hour time
	
	currenthour = (currenthour * 5) + (currentmin/10) # Adjust hour to range 0-60

	# Erase any old hands

	tft.fg_color(CLOCK_BACKGROUND)

	if( lasthour != currenthour ):
		tft.analog_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-25,lasthour)

	if( lastmin != currentmin ):
		tft.analog_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-10,lastmin)

	if( lastsec != currentsec ):
		tft.analog_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-15,lastsec)

	# Draw the time/day at the bottom of the screen
	tft.fg_color(CLOCK_DIGITAL)
	tft.goto_char(1,14)
	tft.write_line(strftime("%H:%M:%S", localtime()))
	tft.goto_char(26 - len(strftime("%a", localtime())),14)
	tft.write_line(strftime("%a", localtime()))

	# Redraw hands

	tft.fg_color(CLOCK_HOUR_HAND)
	tft.analog_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-25,currenthour)

	tft.fg_color(CLOCK_MINUTE_HAND)
	tft.analog_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-10,currentmin)
		
	tft.fg_color(CLOCK_SECOND_HAND)
	tft.analog_hand(CLOCK_ORIGIN_X,CLOCK_ORIGIN_Y,CLOCK_RADIUS-15,currentsec)
	
	lasthour = currenthour
	lastmin = currentmin
	lastsec = currentsec
	
	time.sleep(1)

