# Included for posterity
#
# The tests below have been used for determining
# optimum delay times at 9600baud
#
# Certain commands will cause a serial buffer overflow
# if they are not allowed time to complete

import time
from time import localtime, strftime
from random import randint
from serialtft import SerialTFT

tft = SerialTFT("/dev/ttyAMA0", 9600)

BAR_WIDTH = 4
BAR_MARGIN = 1

# Clear Screen
tft.screen_rotation(SerialTFT.Rotation.landscape)
tft.bg_color(SerialTFT.Color.black)
tft.clear_screen()

bar_left = BAR_MARGIN

colors = [
	SerialTFT.Color.red,
	SerialTFT.Color.blue,
	SerialTFT.Color.green,
	SerialTFT.Color.cyan,
	SerialTFT.Color.magenta,
	SerialTFT.Color.yellow,
	SerialTFT.Color.white
]

'''
while 1:
	for color in colors:
		tft.fg_color(color)
		tft.draw_circle(SerialTFT.Screen.width_half,SerialTFT.Screen.height_half,50-color)
'''

'''
while 1:
	for color in colors:
		tft.fg_color(color)
		tft.draw_circle(SerialTFT.Screen.width_half+randint(-50,50),SerialTFT.Screen.height_half+randint(-40,40),randint(1,20))
'''

'''
for color in colors:
	tft.bg_color(color)
	tft.clear_screen()
	time.sleep(0.5)


tft.bg_color(SerialTFT.Color.black)
tft.clear_screen()

color_idx = 0;


while (bar_left + BAR_MARGIN < SerialTFT.Screen.width):

	tft.fg_color(colors[color_idx])

	tft.draw_filled_rect(bar_left,1,BAR_WIDTH,randint(1,119))

	bar_left += BAR_MARGIN + BAR_WIDTH

	color_idx += 1

	if( color_idx > 6 ):
		color_idx = 0
'''

square_left = 0
square_top = 0
square_width = 4
square_height = 8
square_margin = 1

square_top = square_margin
square_left = square_margin

tft.clear_screen()

color_idx = 0;

while (square_top + square_margin < SerialTFT.Screen.height):
	while (square_left + square_margin < SerialTFT.Screen.width):

		tft.fg_color(colors[color_idx])
		tft.draw_filled_rect(square_left,square_top,square_width,square_height)

		square_left += square_width + square_margin

		color_idx += 1

		if( color_idx > 6 ):
			color_idx = 0

	square_top += square_height + square_margin
	square_left = square_margin