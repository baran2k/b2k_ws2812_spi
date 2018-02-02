#!/usr/bin/python
def write(spi, color):
    tx=[0x00]
    for rgb in color:
        for byte in rgb:            
            for bit in range(4):
                tx.append(((byte>>(2*bit+1))&1)*0x60 + ((byte>>(2*bit+0))&1)*0x06 + 0x88)
    spi.xfer(tx, int(4/1.05e-6))