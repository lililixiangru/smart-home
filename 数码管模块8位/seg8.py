


import pyb
from pyb import Pin
import time

class SEG8():
    def __init__(self,dio_pin,sck_pin,stb_pin):
        self.dio = Pin(dio_pin,Pin.OUT_PP)
        self.sck = Pin(sck_pin,Pin.OUT_PP)
        self.stb = Pin(stb_pin,Pin.OUT_PP)

    def tm1638_write_cmd(self,cmdwrite):
        self.sck(1)
        self.stb(1)
        self.stb(0)

        for i in range(8):
            self.dio(cmdwrite&0x01)
            self.sck(0)
            time.sleep_us(1)
            self.sck(1)
            time.sleep_us(1)
            cmdwrite >>= 1

        self.sck(1)
        time.sleep_us(1)
        self.stb(1)
        time.sleep_us(1)

    def tm1638_write_data(self,addrwrite,datawrite):
        self.sck(1)
        self.stb(1)
        self.stb(0)

        for i in range(8):
            self.dio(addrwrite&0x01)
            self.sck(0)
            time.sleep_us(1)
            self.sck(1)
            time.sleep_us(1)
            addrwrite >>= 1

        for i in range(8):
            self.dio(datawrite&0x01)
            self.sck(0)
            time.sleep_us(1)
            self.sck(1)
            time.sleep_us(1)
            datawrite >>= 1

        self.sck(1)
        time.sleep_us(1)
        self.stb(1)
        time.sleep_us(1)

    def tm1638_send_data(self,cmdwrite,addrwrite,datawrite):
        self.tm1638_write_cmd(cmdwrite)
        self.tm1638_write_data(addrwrite,datawrite)

    def tm1638_clear(self):
        for i in range(16):
            self.tm1638_send_data(0x40,0xc0+i,0x00)

    def init(self):
        self.tm1638_write_cmd(0x88)
        self.tm1638_write_cmd(0x44)
        self.tm1638_clear()

    def show_num(self,numshow):
        for i in range(8):
            self.tm1638_send_data(0x40,0xc0+i*2,numshow[i])

