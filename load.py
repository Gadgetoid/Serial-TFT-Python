# This file is full of tests, experiments and tinkering
# used to verify changes to serialtft.py and prototype
# new examples. Don't expect it to do anything predictable.
#
# It has been included for posterity and is subject to change.
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

from functools import reduce

tft = SerialTFT("/dev/ttyAMA0", 9600, True, False)

BAR_WIDTH = 4
BAR_MARGIN = 1

# Clear Screen
tft.screen_rotation(SerialTFT.Rotation.landscape)
tft.bg_color(SerialTFT.Color.black)
tft.clear_screen()

colors = [
	SerialTFT.Color.blue,
	SerialTFT.Color.red,
	SerialTFT.Color.green,
	SerialTFT.Color.cyan,
	SerialTFT.Color.magenta,
	SerialTFT.Color.yellow,
	SerialTFT.Color.white
]

tft.font_size(SerialTFT.Font.small)
tft.fg_color(SerialTFT.Color.white)
print('Drawing text')
tft.write_line('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eu turpis enim, at luctus quam. Mauris augue augue, blandit quis dictum in, accumsan eget odio. In id laoreet massa.')
tft.font_size(SerialTFT.Font.medium)
tft.write_line('Starting load tests')
tft.font_size(SerialTFT.Font.large)
tft.write_line('Soooon')
time.sleep(5)

print('Testing pixel draw rate')
result = []
circle_count = 0
last_sec = time.localtime().tm_sec
total_count = 0
while len(result) < 10:
	for color in colors:
		#tft.fg_color(color)
		tft.draw_pixel(randint(0,tft.Screen.width),randint(0,tft.Screen.height),color)
		circle_count += 1
		total_count += 1
		if time.localtime().tm_sec !=last_sec:
			last_sec = time.localtime().tm_sec
			print('Drawn ' + str(circle_count))
			result.append(circle_count)
			circle_count = 0

# First result is unreliable
result.pop(0)
print('Average rate: ' + str(reduce(lambda x, y: x + y, result) / len(result)))

'''
print('Testing fast box draw rate')
result = []
circle_count = 0
last_sec = time.localtime().tm_sec
for x in range(0,200):
	for color in colors:
		#tft.fg_color(color)
		tft.draw_box_fast(randint(0,tft.Screen.width),randint(0,tft.Screen.height),randint(0,tft.Screen.width),randint(0,tft.Screen.height),color)
		circle_count += 1
		if time.localtime().tm_sec !=last_sec:
			last_sec = time.localtime().tm_sec
			print('Drawn ' + str(circle_count))
			result.append(circle_count)
			circle_count = 0

# First result is unreliable
result.pop(0)
print('Average rate: ' + str(reduce(lambda x, y: x + y, result) / len(result)))
'''

print('Testing box draw rate')
result = []
circle_count = 0
last_sec = time.localtime().tm_sec
total_count = 0
while len(result) < 10:
	for color in colors:
		#tft.fg_color(color)
		tft.draw_box(randint(0,tft.Screen.width),randint(0,tft.Screen.height),randint(0,tft.Screen.width),randint(0,tft.Screen.height),color)
		circle_count += 1
		total_count += 1
		if time.localtime().tm_sec !=last_sec:
			last_sec = time.localtime().tm_sec
			print('Drawn ' + str(circle_count))
			result.append(circle_count)
			circle_count = 0

# First result is unreliable
result.pop(0)
print('Average rate: ' + str(reduce(lambda x, y: x + y, result) / len(result)))


print('Testing filled box draw rate')
result = []
circle_count = 0
last_sec = time.localtime().tm_sec
total_count = 0
while len(result) < 10:
	for color in colors:
		#tft.fg_color(color)
		tft.draw_filled_box(randint(0,tft.Screen.width),randint(0,tft.Screen.height),randint(0,tft.Screen.width),randint(0,tft.Screen.height),color)
		circle_count += 1
		total_count += 1
		if time.localtime().tm_sec !=last_sec:
			last_sec = time.localtime().tm_sec
			print('Drawn ' + str(circle_count))
			result.append(circle_count)
			circle_count = 0

# First result is unreliable
result.pop(0)
print('Average rate: ' + str(reduce(lambda x, y: x + y, result) / len(result)))

print('--------------------------------------')

print('Testing line draw rate')
result = []
circle_count = 0
last_sec = time.localtime().tm_sec
total_count = 0
while len(result) < 10:
	for color in colors:
		#tft.fg_color(color)
		tft.draw_line(randint(0,tft.Screen.width),randint(0,tft.Screen.height),randint(0,tft.Screen.width),randint(0,tft.Screen.height),color)
		circle_count += 1
		total_count += 1
		if time.localtime().tm_sec !=last_sec:
			last_sec = time.localtime().tm_sec
			print('Drawn ' + str(circle_count))
			result.append(circle_count)
			circle_count = 0

# First result is unreliable
result.pop(0)
print('Average rate: ' + str(reduce(lambda x, y: x + y, result) / len(result)))

print('--------------------------------------')

print('Testing circle draw rate')
result = []
circle_count = 0
last_sec = time.localtime().tm_sec
total_count = 0
while len(result) < 10:
	for color in colors:
		#tft.fg_color(color)
		tft.draw_circle(SerialTFT.Screen.width_half+randint(-50,50),SerialTFT.Screen.height_half+randint(-40,40),randint(1,40),color)
		circle_count += 1
		total_count += 1
		if time.localtime().tm_sec !=last_sec:
			last_sec = time.localtime().tm_sec
			print('Drawn ' + str(circle_count))
			result.append(circle_count)
			circle_count = 0

# First result is unreliable
result.pop(0)
print('Average rate: ' + str(reduce(lambda x, y: x + y, result) / len(result)))

print('--------------------------------------')

print('Testing filled circle draw rate')
result = []
circle_count = 0
last_sec = time.localtime().tm_sec
total_count = 0
while len(result) < 10:
	for color in colors:
		#tft.fg_color(color)
		tft.draw_filled_circle(SerialTFT.Screen.width_half+randint(-50,50),SerialTFT.Screen.height_half+randint(-40,40),randint(1,40),color)
		circle_count += 1
		total_count += 1
		if time.localtime().tm_sec !=last_sec:
			last_sec = time.localtime().tm_sec
			print('Drawn ' + str(circle_count))
			result.append(circle_count)
			circle_count = 0

# First result is unreliable
result.pop(0)
print('Average rate: ' + str(reduce(lambda x, y: x + y, result) / len(result)))

print('--------------------------------------')


tft.flush = True

print('Testing circle draw rate, flush enabled')
result = []
circle_count = 0
last_sec = time.localtime().tm_sec
total_count = 0
while len(result) < 10:
	for color in colors:
		tft.fg_color(color)
		tft.draw_circle(SerialTFT.Screen.width_half+randint(-50,50),SerialTFT.Screen.height_half+randint(-40,40),randint(1,40))
		circle_count += 1
		total_count += 1
		if time.localtime().tm_sec !=last_sec:
			last_sec = time.localtime().tm_sec
			print('Drawn ' + str(circle_count))
			result.append(circle_count)
			circle_count = 0

# First result is unreliable
result.pop(0)
print('Average rate: ' + str(reduce(lambda x, y: x + y, result) / len(result)))

print('--------------------------------------')
print('Testing filled circle draw rate, flush enabled')
result = []
circle_count = 0
last_sec = time.localtime().tm_sec
total_count = 0
while len(result) < 10:
	for color in colors:
		tft.fg_color(color)
		tft.draw_filled_circle(SerialTFT.Screen.width_half+randint(-50,50),SerialTFT.Screen.height_half+randint(-40,40),randint(1,40))
		circle_count += 1
		total_count += 1
		if time.localtime().tm_sec !=last_sec:
			last_sec = time.localtime().tm_sec
			print('Drawn ' + str(circle_count))
			result.append(circle_count)
			circle_count = 0

# First result is unreliable
result.pop(0)
print('Average rate: ' + str(reduce(lambda x, y: x + y, result) / len(result)))

print('--------------------------------------')
exit(0)


while 1:
	for color in colors:
		#tft.fg_color(color)
		tft.draw_filled_circle(SerialTFT.Screen.width_half,SerialTFT.Screen.height_half,50-randint(0,49),color)



PIX_PER_COL = 17

tft.set_theme(SerialTFT.Theme.matrix)

bar_left = BAR_MARGIN

letters = []

left = 0
for letter in range(0,32):
	letters.append([letter,randint(0,150),randint(0,110),randint(0,60),randint(0,1),randint(3,6)])
	left += 10

left = 0
while 1:

	for letter in letters:
		letter[2] += randint(3,6)
		letter[3] += randint(3,6)
		if( letter[2] > 120 ):
			letter[2] = 0
			letter[1] = randint(0,150)
			letter[3] = randint(0,60)
			letter[4] = randint(0,1)
			letter[5] = randint(3,6)

		left = letter[1]
		top = letter[2]

		col_idx = int(round(letter[3] / PIX_PER_COL,0))
		if( col_idx > 6 ):
			col_idx = 6
		col = colors[ col_idx ]

		if(letter[4]==1):
			col = 0

		#tft.fg_color(col)

		tft.draw_circle(left,top,letter[5],col)
		#tft.goto_pixel(left,top)

		#tft.write(letter[0])


	time.sleep(0.1)

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

'''
square_left = 0
square_top = 0
square_width = 2
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
'''
