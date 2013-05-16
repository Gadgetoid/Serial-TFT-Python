# coding=ASCII
import math

CMD_BEGIN	= chr(27)
CMD_END		= chr(255)
RETURN		= chr(13)

# Colour values
COL_BLACK	= 0
COL_BLUE		= 1
COL_RED		= 2
COL_GREEN	= 3
COL_CYAN		= 4
COL_MAGENTA	= 5
COL_YELLOW	= 6
COL_WHITE	= 7

# Built-in Solarized Colour values
COL_SOLARIZED_BLACK	= 8
COL_SOLARIZED_BLUE	= 9
COL_SOLARIZED_RED	= 10
COL_SOLARIZED_GREEN	= 11
COL_SOLARIZED_CYAN	= 12
COL_SOLARIZED_MAGENTA	= 13
COL_SOLARIZED_YELLOW	= 14
COL_SOLARIZED_WHITE	= 15

# Redundant shorthand for BG/FG colour commands
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

def fg_color(color):
	return CMD_BEGIN + chr(1) + chr(color) + CMD_END

def bg_color(color):
	return CMD_BEGIN + chr(2) + chr(color) + CMD_END

def hex_to_rgb(value):
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

def set_color_hex(col,hex):
	colour = hex_to_rgb(hex)
	return set_color_rgb(col,colour[0],colour[1],colour[2])

def set_color_packed(col,colour):
	low,high = divmod(colour,256)
	return CMD_BEGIN + chr(15) + chr(col) + chr(low) + chr(high) + CMD_END

def set_color_rgb(col,r,g,b):
	value = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
	low,high = divmod(value,256)
	return CMD_BEGIN + chr(15) + chr(col) + chr(low) + chr(high) + CMD_END

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
	return CMD_BEGIN + chr(10) + chr(x1) + chr(y1) + chr(x2) + chr(y2) + CMD_END

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


# Colour Themes


# If you're using the firmware with colour palette support
# you can write one of the below themes to set it up
# Tip; to use dark and light at the same time, 
# move dark to indexes 8-15

# The TFT uses 16 bit packed colour, hex is 24 bit,
# so expect some loss of accuracy

# Solarized
COL_THEME_SOLARIZED = set_color_packed(0,0x1AB)   # black 
COL_THEME_SOLARIZED += set_color_packed(1,0x245A) # blue
COL_THEME_SOLARIZED += set_color_packed(2,0xD985) # red
COL_THEME_SOLARIZED += set_color_packed(3,0x84C0) # green
COL_THEME_SOLARIZED += set_color_packed(4,0x2D13) # cyan
COL_THEME_SOLARIZED += set_color_packed(5,0xD1B0) # magenta
COL_THEME_SOLARIZED += set_color_packed(6,0xB440) # yellow
COL_THEME_SOLARIZED += set_color_packed(7,0xEF5A) # white

# Flat UI
COL_THEME_FLAT_UI = set_color_rgb(0,0x34,0x49,0x5E)  # black 
COL_THEME_FLAT_UI += set_color_rgb(1,0x34,0x98,0xDB) # blue
COL_THEME_FLAT_UI += set_color_rgb(2,0xE7,0x4C,0x3C) # red
COL_THEME_FLAT_UI += set_color_rgb(3,0x2E,0xCC,0x71) # green
COL_THEME_FLAT_UI += set_color_rgb(4,0x1A,0xBC,0x9C) # cyan
COL_THEME_FLAT_UI += set_color_rgb(5,0x9B,0x59,0xB6) # magenta
COL_THEME_FLAT_UI += set_color_rgb(6,0xF1,0xC4,0x0F) # yellow
COL_THEME_FLAT_UI += set_color_rgb(7,0xEC,0xF9,0xF1) # white

# Dark

COL_THEME_DARK = set_color_hex(0,'#000000') # black 
COL_THEME_DARK += set_color_hex(1,'#003366') # blue
COL_THEME_DARK += set_color_hex(2,'#660000') # red
COL_THEME_DARK += set_color_hex(3,'#006633') # green
COL_THEME_DARK += set_color_hex(4,'#336666') # cyan
COL_THEME_DARK += set_color_hex(5,'#660066') # magenta
COL_THEME_DARK += set_color_hex(6,'#996600') # yellow
COL_THEME_DARK += set_color_hex(7,'#DDDDDD') # white

# Light

COL_THEME_LIGHT = set_color_hex(0,'#222222') # black 
COL_THEME_LIGHT += set_color_hex(1,'#0099FF') # blue
COL_THEME_LIGHT += set_color_hex(2,'#FF3333') # red
COL_THEME_LIGHT += set_color_hex(3,'#99FF33') # green
COL_THEME_LIGHT += set_color_hex(4,'#33FFFF') # cyan
COL_THEME_LIGHT += set_color_hex(5,'#FF3399') # magenta
COL_THEME_LIGHT += set_color_hex(6,'#FFFF33') # yellow
COL_THEME_LIGHT += set_color_hex(7,'#FFFFFF') # white

# If you don't want to reset your serial TFT
# use this theme to return the colours to defaults

COL_THEME_DEFAULT = set_color_packed(0,0x0000) # black 
COL_THEME_DEFAULT += set_color_packed(1,0x001F) # blue
COL_THEME_DEFAULT += set_color_packed(2,0xF800) # red
COL_THEME_DEFAULT += set_color_packed(3,0x07E0) # green
COL_THEME_DEFAULT += set_color_packed(4,0x07FF) # cyan
COL_THEME_DEFAULT += set_color_packed(5,0xF81F) # magenta
COL_THEME_DEFAULT += set_color_packed(6,0xFFE0) # yellow
COL_THEME_DEFAULT += set_color_packed(7,0xFFFF) # white

COL_THEME_MATRIX = set_color_hex(0,'#002100') # black 
COL_THEME_MATRIX += set_color_hex(1,'#005200') # blue
COL_THEME_MATRIX += set_color_hex(2,'#006300') # red
COL_THEME_MATRIX += set_color_hex(3,'#007400') # green
COL_THEME_MATRIX += set_color_hex(4,'#008500') # cyan
COL_THEME_MATRIX += set_color_hex(5,'#009600') # magenta
COL_THEME_MATRIX += set_color_hex(6,'#00A700') # yellow
COL_THEME_MATRIX += set_color_hex(7,'#00FF00') # white

COL_THEME_RED = set_color_hex(0,'#210000') # black 
COL_THEME_RED += set_color_hex(1,'#520000') # blue
COL_THEME_RED += set_color_hex(2,'#630000') # red
COL_THEME_RED += set_color_hex(3,'#740000') # green
COL_THEME_RED += set_color_hex(4,'#850000') # cyan
COL_THEME_RED += set_color_hex(5,'#960000') # magenta
COL_THEME_RED += set_color_hex(6,'#A70000') # yellow
COL_THEME_RED += set_color_hex(7,'#FF0000') # white
