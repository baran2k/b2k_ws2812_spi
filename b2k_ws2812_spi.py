#!/usr/bin/python
import spidev
spi = spidev.SpiDev()
spi.open(0,0)
numPixs = 0
pixel = []

def setNumPixels(num = 0):
    global numPixs, pixel
    if num > 0:
        numPixs = num
        for i in range(numPixs):
            pixel.append([0x00, 0x00, 0x00])
    return numPixs

def setPixel(i, r, g, b):
    global pixel
    pixel[i] = [g, r, b]

def setAll(r, g, b):
    global pixel, numPixs
    for i in range(numPixs):
        pixel[i]=[g, r, b]

def show():
    tx=[0x00]
    for rgb in pixel:
        for byte in rgb:            
            for bit in range(3,-1,-1):
                tx.append(((byte>>(2*bit+1))&1)*0x60 + ((byte>>(2*bit+0))&1)*0x06 + 0x88)
    spi.xfer(tx, int(4/1.05e-6))
