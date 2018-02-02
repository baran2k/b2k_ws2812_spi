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
VCC   --   5V DON'T CONNECT POWER TO RPi!! USE POWER SUPPLY!!!
```
Usage
-----
```
b2k_ws2812_spi.write(spi, [[GREEN,RED,BLUE], [GREEN,RED,BLUE], [GREEN,RED,BLUE]])
                                   ^                ^                   ^
                                first led       second led          third led
                                
RED, GREEN, BLUE - must be in range of 0x00 - 0xFF 
	where 	0x00 - no light
		0xFF - max light brightness

NOTE: this module use the GRB model! not the RGB
```

Example program
--------

```
#!/usr/bin/python
import spidev
import b2k_ws2812_spi
import time
import random
spi = spidev.SpiDev()
spi.open(0,0)

#number led of pixel strip
numPixels = 10
#init range for pixel count
pixel = []
for i in range(numPixels):
    pixel.append([0x00,0x00,0x00])	
		
for i in range(3):
    for i in range(numPixels):
        #set pixel color to red
        pixel[i]=[0x00,0x15,0x00]
        #light strip
        b2k_ws2812_spi.write(spi, pixel)
        time.sleep(0.08)
    for i in range(numPixels):
        #set pixel color to green
        pixel[i]=[0x15,0x00,0x00]
        #light strip
        b2k_ws2812_spi.write(spi, pixel)
        time.sleep(0.08)	
    for i in range(numPixels):
        #set pixel color to blue
        pixel[i]=[0x00,0x00,0x15]
        #light strip
        b2k_ws2812_spi.write(spi, pixel)
        time.sleep(0.08)
    for i in range(numPixels):
        #set pixel color to orange
        pixel[i]=[0x14,0x15,0x00]
        #light strip
        b2k_ws2812_spi.write(spi, pixel)
        time.sleep(0.08)
    for i in range(numPixels):
        #set pixel color to yellow
        pixel[i]=[0x15,0x15,0x00]
        #light strip
        b2k_ws2812_spi.write(spi, pixel)
        time.sleep(0.08) 
        
for i in range(numPixels):
    pixel[i] = [0x00,0x00,0x00]
    b2k_ws2812_spi.write(spi, pixel)
```

* NOTE: `this module use the GRB model! not the RGB`
