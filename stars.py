# Hobbytronics TFT - 3d star field demo (stars.py)
#
# This example demonstrates the serialtft library included
#
# Based on code found here:
# http://codentronix.com/2011/05/28/3d-starfield-made-using-python-and-pygame/
#
# This is example will run slowly and REQUIES modified firmware for best effect
#
# Run in background using command..
# sudo python stars.py &
#
# See product page at http://www.hobbytronics.co.uk/tft-serial-display-18
# for full command details
#

import time
import random
from random import randrange
from serialtft import SerialTFT

# Set this to True if you're using modified firmware from:
# https://github.com/Gadgetoid/serial_tft_18/
# You'll get a faster, monochrome starfield

MY_FIRMWARE_IS_MODIFIED = False

# Play with these values to change the star field
# higher values look better, but will run much, much slower

NUM_STARS = 20
MAX_DEPTH = 20

class Simulation:
    def __init__(self, num_stars, max_depth):
 
        self.tft = SerialTFT("/dev/ttyAMA0", 9600, True, False)

        self.start_col = 0
        self.max_col = 7
        self.max_size = 2

        # This colour setup is best if you have firmware support

        # -- COLOR SETUP --
        if(MY_FIRMWARE_IS_MODIFIED):
            self.tft.set_color_hex(8,"#000000")
            self.tft.set_color_hex(9,"#333333")
            self.tft.set_color_hex(10,"#555555")
            self.tft.set_color_hex(11,"#777777")
            self.tft.set_color_hex(12,"#999999")
            self.tft.set_color_hex(13,"#BBBBBB")
            self.tft.set_color_hex(14,"#DDDDDD")
            self.tft.set_color_hex(15,"#FFFFFF")
            self.start_col = 8
            self.max_col = 15
            self.max_size = 2
        # -- END COLOR SETUP ---

        # Clear Screen
        self.tft.screen_rotation(SerialTFT.Rotation.landscape)
        self.tft.bg_color(SerialTFT.Color.black)
        self.tft.fg_color(SerialTFT.Color.white)
        self.tft.clear_screen()

        self.num_stars = num_stars
        self.max_depth = max_depth
 
        self.init_stars()
 
    def init_stars(self):
        """ Create the starfield """
        self.stars = []
        for i in range(self.num_stars):
            # A star is represented as a list with this format: [X,Y,Z]
            star = [randrange(-15,15), randrange(-15,15), randrange(1, self.max_depth)]
            self.stars.append(star)
 
    def move_and_draw_stars(self):
        """ Move and draw the stars """
        origin_x = self.tft.Screen.width / 2
        origin_y = self.tft.Screen.height / 2
 
        for star in self.stars:


            # Erase old position of star
            
            k = 128.0 / star[2]
            x = int(star[0] * k + origin_x)
            y = int(star[1] * k + origin_y)

            if 0 <= x < self.tft.Screen.width and 0 <= y < self.tft.Screen.height:
                size = int((1 - float(star[2]) / self.max_depth) * self.max_size) + 1
                if(MY_FIRMWARE_IS_MODIFIED):
                    self.tft.draw_pixel(x,y,0)
                    #self.tft.draw_box(x,y,size,size,0)
                else:
                    self.tft.fg_color(0)
                    self.tft.draw_rect(x,y,size,size)
            


            # The Z component is decreased on each frame.
            # Decease this number for a smoother, slower starfield
            star[2] -= 0.40
 
            # If the star has past the screen (I mean Z<=0) then we
            # reposition it far away from the screen (Z=max_depth)
            # with random X and Y coordinates.
            if star[2] <= 0:
                star[0] = randrange(-15,15)
                star[1] = randrange(-15,15)
                star[2] = self.max_depth
 
            # Convert the 3D coordinates to 2D using perspective projection.
            k = 128.0 / star[2]
            x = int(star[0] * k + origin_x)
            y = int(star[1] * k + origin_y)
 
            # Draw the star (if it is visible in the screen).
            # We calculate the size such that distant stars are smaller than
            # closer stars. Similarly, we make sure that distant stars are
            # darker than closer stars. This is done using Linear Interpolation.
            if 0 <= x < self.tft.Screen.width and 0 <= y < self.tft.Screen.height:
                size = int((1 - float(star[2]) / self.max_depth) * self.max_size) + 1
                shade = self.start_col + int((1 - float(star[2]) / self.max_depth) * 7) + 3

                if(shade > self.max_col):
                    shade = self.start_col

                if(MY_FIRMWARE_IS_MODIFIED):
                    self.tft.draw_pixel(x,y,shade)
                    #self.tft.draw_box(x,y,size,size,shade)
                else:
                    self.tft.fg_color(shade)
                    self.tft.draw_rect(x,y,size,size)

 
    def run(self):
        while 1:
            self.move_and_draw_stars()


Simulation(NUM_STARS,MAX_DEPTH).run()

