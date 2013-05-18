# Hobbytronics TFT - driver library
# Author: Philip Howard <phil@gadgetoid.com>
# Version: 1.0

import math
import time
import serial
import serialtft_themes
from serialtft_constants import *

class SerialTFT:
	class Screen:
		width 		= SCREEN_WIDTH
		height 		= SCREEN_HEIGHT
		width_half 	= SCREEN_WIDTH_HALF
		height_half = SCREEN_HEIGHT_HALF
	class Font:
		small 		= 1
		medium 		= 2
		large 		= 3
	class Rotation:
		portrait_left 			= 0
		portrait_right 			= 2
		landscape_upsidedown 	= 1
		landscape 				= 3
	class Color:
		black = 0
		blue = 1
		red = 2
		green = 3
		cyan = 4
		magenta = 5
		yellow = 6
		white = 7
		user_1 = 8
		user_2 = 9
		user_3 = 10
		user_4 = 11
		user_5 = 12
		user_6 = 13
		user_7 = 14
		user_8 = 15
	class Theme:
		default 	= serialtft_themes.COL_THEME_DEFAULT
		red 		= serialtft_themes.COL_THEME_RED
		matrix 		= serialtft_themes.COL_THEME_MATRIX
		light 		= serialtft_themes.COL_THEME_LIGHT
		dark 		= serialtft_themes.COL_THEME_DARK
		flat_ui 	= serialtft_themes.COL_THEME_FLAT_UI
		solarized 	= serialtft_themes.COL_THEME_SOLARIZED

	def __init__(self,device='/dev/ttyAMA0',baud_rate=9600):
		'''
			Set up SerialTFT with device and baud_rate
		'''
		self.port = serial.Serial(device, baud_rate, timeout=0.5)

	def clear_screen(self):
		self.port.write(CLEAR_SCREEN)
		# Drawing too quickly after clearning the screen
		# seems to lead to dropped commands
		time.sleep(0.2)

	def set_theme(self,theme):
		'''
			Change user colours to a specific theme

			Use one of SerialTFT.Theme.
		'''
		self.port.write(theme)

	def write(self,text):
		'''
			Write a text string
		'''
		self.port.write(text)

	def write_line(self,text):
		'''
			Write a text string followed by a carriage return
		'''
		self.port.write(text + chr(13))

	def font_size(self,font_size):
		'''
			Set up font size

			1 = small
			2 = medium 
			3 = large
		'''
		self.port.write(CMD_BEGIN + CMD_FONT_SIZE + chr(font_size) + CMD_END)

	def screen_rotation(self,int_rotation):
		'''
			Set up screen Rotation

			Use one of SerialTFT.Rotation.
		'''
		self.port.write(CMD_BEGIN + CMD_SCREEN_ROTATION + chr(int_rotation) + CMD_END)

	def fg_color(self,color):
		'''
			Set the active foreground colour
		'''
		self.port.write(CMD_BEGIN + CMD_FG_COLOR + chr(color) + CMD_END)

	def bg_color(self,color):
		'''
			Set the active background color
		'''
		self.port.write(CMD_BEGIN + CMD_BG_COLOR + chr(color) + CMD_END)

	def draw_bitmap(self,file,x,y):
		'''
			Draw a bitmap from the SD card
		'''
		self.port.write(CMD_BEGIN + CMD_DISPLAY_BITMAP + chr(x) + chr(y) + file + CMD_END)

	def goto_pixel(self,pixel_x,pixel_y):
		'''
			Go to pixel location
		'''
		self.port.write(CMD_BEGIN + CMD_POS_PIXEL + chr(pixel_x) + chr(pixel_y) + CMD_END)

	def goto_char(self,char_x,char_y):
		'''
			Go to character position, depends on font size
		'''
		self.port.write(CMD_BEGIN + CMD_POS_TEXT + chr(char_x) + chr(char_y) + CMD_END)

	def draw_line(self,x1,y1,x2,y2):
		'''
			Draw a line in foreground color
		'''
		self.port.write(CMD_BEGIN + CMD_DRAW_LINE + chr(x1) + chr(y1) + chr(x2) + chr(y2) + CMD_END)

	def draw_box(self,x1,y1,x2,y2):
		'''
			Draw a rectangle outline in foreground color
		'''
		self.port.write(CMD_BEGIN + CMD_DRAW_BOX + chr(x1) + chr(y1) + chr(x2) + chr(y2) + CMD_END)

	def draw_rect(self,x1,y1,width,height):
		self.draw_box(x1,y1,x1+width,y1+height)

	def draw_filled_box(self,x1,y1,x2,y2):
		'''
			Draw a rectangle filled with foreground color
		'''
		self.port.write(CMD_BEGIN + CMD_DRAW_FILLED_BOX + chr(x1) + chr(y1) + chr(x2) + chr(y2) + CMD_END)

	def draw_filled_rect(self,x1,y1,width,height):
		'''
			Draw a filled rectangle at x,y of size width,height
		'''
		self.draw_filled_box(x1,y1,x1+width,y1+height)

	def draw_circle(self,x,y,radius):
		'''
			Draw a circle outline in foreground color
		'''
		self.port.write(CMD_BEGIN + CMD_DRAW_CIRCLE + chr(x) + chr(y) + chr(radius) + CMD_END)

		if( radius > 30 ):
			time.sleep(0.1)

	def draw_filled_circle(self,x,y,radius):
		'''
			Draw a circle filled with foreground color
		'''
		self.port.write(CMD_BEGIN + CMD_DRAW_FILLED_CIRCLE + chr(x) + chr(y) + chr(radius) + CMD_END)

		# Give circle time to complete drawing
		# These values have been obtained from
		# basic brute-force circle drawing tests
		if( radius > 30 ):
			time.sleep(0.1)
		elif( radius > 15 ):
			time.sleep(0.05)
		else:
			time.sleep(0.02)

	def analog_hand(self,origin_x,origin_y,radius,minutes):
		'''
			Draw a line from origin x,y of length radius at degrees minutes

			Useful for drawing clock hands or partitioning pie-charts
		'''
		angle = (minutes / 60.0) * (2*math.pi)
		x = origin_x + radius*math.sin(angle)
		y = origin_y - radius*math.cos(angle)

		x_a = origin_x + 6*math.sin(angle)
		y_a = origin_y - 6*math.cos(angle)
		
		self.draw_line(int(round(x_a)),int(round(y_a)),int(round(x)),int(round(y)))

	def hex_to_rgb(self,value):
		value = value.lstrip('#')
		lv = len(value)
		return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

	def set_color_hex(self,col,hex):
		colour = self.hex_to_rgb(hex)
		self.set_color_rgb(col,colour[0],colour[1],colour[2])

	def set_color_packed(self,col,colour):
		low,high = divmod(colour,256)
		self.port.write(CMD_BEGIN + CMD_SET_COLOR + chr(col) + chr(low) + chr(high) + CMD_END)

	def set_color_rgb(self,col,r,g,b):
		value = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
		low,high = divmod(value,256)
		self.port.write(CMD_BEGIN + CMD_SET_COLOR + chr(col) + chr(low) + chr(high) + CMD_END)
