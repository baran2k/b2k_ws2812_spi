Python b2k_ws2812_spi
=============

This is lib for control ws2812 strip led with spi on raspbery pi or orange pi

Install:
-----
```
git clone https://github.com/baran2k/b2k_ws2812_spi.git
cd b2k_ws2812_spi/
sudo python setup.py install

* also you need install (if not) spidev lib
* for Raspbery Pi you must enable spi via raspi-config first!
```

Connections to the WS2812:
-----
```
GND   --   GND one of pin 6, 9, 14, 20, 25 (30, 34, 39)
DIN   --   MOSI (Pin 19)
VCC   --   5V DON'T CONNECT POWER TO RPi (OPi)!! USE POWER SUPPLY!!!
```
Usage
-----
```
* b2k_ws2812_spi.setNumPixels(number of pixels) - sets number of pixels in ws2812
  * b2k_ws2812_spi.setNumPixels() - without parameters returns the number of sets pixels

* b2k_ws2812_spi.setPixel(number pixel, RED, GREEN, BLUE) - set pixel to color in rgb
  * RED, GREEN, BLUE - must be in range of 0-255
    where:
        0 - no light
        255 - max light brightness
        
* b2k_ws2812_spi.setAll(RED,GREEN,BLUE) - same as before, but sets ALL pixel to color rgb

* b2k_ws2812_spi.show() - light the ws2812 strip
                                
```

Example program
--------

```
#!/usr/bin/python
import b2k_ws2812_spi
import time

b2k_ws2812_spi.setNumPixels(6)

#set 1st pixel color to red
b2k_ws2812_spi.setPixel(0,50,0,0)
#set 2nd pixel color to green
b2k_ws2812_spi.setPixel(1,0,50,0)
#set 3rd pixel color to blue
b2k_ws2812_spi.setPixel(2,0,0,50)
#set 4th pixel color to orange
b2k_ws2812_spi.setPixel(3,50,30,0)
#set 5th pixel color to white
b2k_ws2812_spi.setPixel(4,50,50,50)
#set 6th pixel color to yellow
b2k_ws2812_spi.setPixel(5,50,50,0)
#light strip
b2k_ws2812_spi.show()
time.sleep(2)
#set all pixel color to red
b2k_ws2812_spi.setAll(50,0,0)
#ligth strip
b2k_ws2812_spi.show()
time.sleep(2)
#turn of all pixels
b2k_ws2812_spi.setAll(0,0,0)
#ligth strip
b2k_ws2812_spi.show()
```

* NOTE: `this module use the GRB model! not the RGB`
