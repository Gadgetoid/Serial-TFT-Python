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

def set_color(col,r,g,b):
	value = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
	print value
	#high = (value >> 8) & 0xff
	#low = value & 0xff
	high,low = divmod(value,256)
	print low
	print high
	return CMD_BEGIN + chr(15) + chr(col) + chr(high) + chr(low) + CMD_END

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
