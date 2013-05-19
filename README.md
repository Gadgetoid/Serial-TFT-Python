Serial-TFT-Python
=================

Python library for the HobbyTronics Serial-TFT board: http://www.hobbytronics.co.uk/tft-serial-display-18

Requires python-pyserial.

Version 1.1:
Updated to work in Python3.x in addition to Python2.x

Version 1.2:
Added deconstructor and enter/exit handlers for use using 'with' syntax
Constructor is now: SerialTFT( device, baud_rate, clean_on_exit )

If you want to leave your last sent commands on the LCD, specify False for clean_on_exit
This is useful for bringing up a script, writing a notification to the LCD and exiting

Example:

with SerialTFT('/dev/ttyAMA0',9600,False) as tft
	tft.write('Hello world')

clock.py
========

The included clock.py example can be run on a Raspberry Pi to display an analog clock

stars.py
========

This over-the-top demo renders a 3d starfield onto the TFT... slowly!

Themes
======

To use thmes and user colours, you must use my modified firmware.

You can find it here: https://github.com/Gadgetoid/serial_tft_18

You will need an FTDI USB to Serial adaptor board to program the ATMega328
on the HobbyTronics Serial-TFT board. 

You can find it here: http://www.hobbytronics.co.uk/ftdi-basic

