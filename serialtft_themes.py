# Hobbytronics TFT - driver library color themes
# Author: Philip Howard <phil@gadgetoid.com>
# Version: 1.0

from serialtft_constants import *

# Helper functions, these let you specify a colour
# using a variety of methods, rgb, hex and packed 16 bit

def hex_to_rgb(value):
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:int(i+lv/3)], 16) for i in range(0, lv, int(lv/3)))

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

# If you're using the firmware with colour palette support
# you can write one of the below themes to set it up
# Tip; to use dark and light at the same time, 
# move dark to indexes 8-15

# The TFT uses 16 bit packed colour, hex is 24 bit,
# so expect some loss of accuracy

# Solarized

COL_THEME_SOLARIZED = set_color_packed(8,0x1AB)   # black 
COL_THEME_SOLARIZED += set_color_packed(9,0x245A) # blue
COL_THEME_SOLARIZED += set_color_packed(10,0xD985) # red
COL_THEME_SOLARIZED += set_color_packed(11,0x84C0) # green
COL_THEME_SOLARIZED += set_color_packed(12,0x2D13) # cyan
COL_THEME_SOLARIZED += set_color_packed(13,0xD1B0) # magenta
COL_THEME_SOLARIZED += set_color_packed(14,0xB440) # yellow
COL_THEME_SOLARIZED += set_color_packed(15,0xEF5A) # white

# Flat UI

COL_THEME_FLAT_UI = set_color_rgb(8,0x34,0x49,0x5E)  # black 
COL_THEME_FLAT_UI += set_color_rgb(9,0x34,0x98,0xDB) # blue
COL_THEME_FLAT_UI += set_color_rgb(10,0xE7,0x4C,0x3C) # red
COL_THEME_FLAT_UI += set_color_rgb(11,0x2E,0xCC,0x71) # green
COL_THEME_FLAT_UI += set_color_rgb(12,0x1A,0xBC,0x9C) # cyan
COL_THEME_FLAT_UI += set_color_rgb(13,0x9B,0x59,0xB6) # magenta
COL_THEME_FLAT_UI += set_color_rgb(14,0xF1,0xC4,0x0F) # yellow
COL_THEME_FLAT_UI += set_color_rgb(15,0xEC,0xF9,0xF1) # white

# Dark

COL_THEME_DARK = set_color_hex(8,'#000000') # black 
COL_THEME_DARK += set_color_hex(9,'#003366') # blue
COL_THEME_DARK += set_color_hex(10,'#660000') # red
COL_THEME_DARK += set_color_hex(11,'#006633') # green
COL_THEME_DARK += set_color_hex(12,'#336666') # cyan
COL_THEME_DARK += set_color_hex(13,'#660066') # magenta
COL_THEME_DARK += set_color_hex(14,'#996600') # yellow
COL_THEME_DARK += set_color_hex(15,'#DDDDDD') # white

# Light

COL_THEME_LIGHT = set_color_hex(8,'#222222') # black 
COL_THEME_LIGHT += set_color_hex(9,'#0099FF') # blue
COL_THEME_LIGHT += set_color_hex(10,'#FF3333') # red
COL_THEME_LIGHT += set_color_hex(11,'#99FF33') # green
COL_THEME_LIGHT += set_color_hex(12,'#33FFFF') # cyan
COL_THEME_LIGHT += set_color_hex(13,'#FF3399') # magenta
COL_THEME_LIGHT += set_color_hex(14,'#FFFF33') # yellow
COL_THEME_LIGHT += set_color_hex(15,'#FFFFFF') # white

# Green

COL_THEME_MATRIX = set_color_hex(8,'#002100') # black 
COL_THEME_MATRIX += set_color_hex(9,'#005200') # blue
COL_THEME_MATRIX += set_color_hex(10,'#006300') # red
COL_THEME_MATRIX += set_color_hex(11,'#007400') # green
COL_THEME_MATRIX += set_color_hex(12,'#008500') # cyan
COL_THEME_MATRIX += set_color_hex(13,'#009600') # magenta
COL_THEME_MATRIX += set_color_hex(14,'#00A700') # yellow
COL_THEME_MATRIX += set_color_hex(15,'#00FF00') # white

# Red

COL_THEME_RED = set_color_hex(8,'#210000') # black 
COL_THEME_RED += set_color_hex(9,'#520000') # blue
COL_THEME_RED += set_color_hex(10,'#630000') # red
COL_THEME_RED += set_color_hex(11,'#740000') # green
COL_THEME_RED += set_color_hex(12,'#850000') # cyan
COL_THEME_RED += set_color_hex(13,'#960000') # magenta
COL_THEME_RED += set_color_hex(14,'#A70000') # yellow
COL_THEME_RED += set_color_hex(15,'#FF0000') # white

# If you don't want to reset your serial TFT
# use this theme to return the colours to defaults

COL_THEME_DEFAULT = set_color_packed(8,0x0000) # black 
COL_THEME_DEFAULT += set_color_packed(9,0x001F) # blue
COL_THEME_DEFAULT += set_color_packed(10,0xF800) # red
COL_THEME_DEFAULT += set_color_packed(11,0x07E0) # green
COL_THEME_DEFAULT += set_color_packed(12,0x07FF) # cyan
COL_THEME_DEFAULT += set_color_packed(13,0xF81F) # magenta
COL_THEME_DEFAULT += set_color_packed(14,0xFFE0) # yellow
COL_THEME_DEFAULT += set_color_packed(15,0xFFFF) # white
