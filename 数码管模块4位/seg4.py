


import pyb
from pyb import Pin
import time


class SEG4():
    global seg_list
    seg_list = [0x03,0x9F,0x25,0x0D,0x99,0x49,0x41,0x1F,0x01,0x09]

    def __init__(self, qs_pin, stc_pin, shc_pin):
        self.qs  = qs_pin
        self.stc = stc_pin
        self.shc = shc_pin

        self.qs  = Pin(qs_pin,  Pin.OUT_PP)
        self.stc = Pin(stc_pin, Pin.OUT_PP)
        self.shc = Pin(shc_pin, Pin.OUT_PP)

    def seg_74hc595_write_16bit(self, seg, dig):
        for i in range(8):
            if (seg & 0x01) == 0x01:
                self.qs(1)
            else:
                self.qs(0)
            self.shc(0)
            self.shc(1)
            seg = (seg >> 1)

        for i in range(8):
            if (dig & 0x01) == 0x01:
                self.qs(1)
            else:
                self.qs(0)
            dig = (dig >> 1)
            self.shc(0)
            self.shc(1)

        self.stc(0)
        self.stc(1)

    def seg_show_num(self,seg_num):
        if len(seg_num)==4:
            self.seg_74hc595_write_16bit(seg_list[int(seg_num[0])],0x80)
            self.seg_74hc595_write_16bit(seg_list[int(seg_num[1])],0x40)
            self.seg_74hc595_write_16bit(seg_list[int(seg_num[2])],0x20)
            self.seg_74hc595_write_16bit(seg_list[int(seg_num[3])],0x10)
        if len(seg_num)==5:
            if seg_num[1]=='.':
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[0])]&0xfe,0x80)
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[2])],0x40)
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[3])],0x20)
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[4])],0x10)    

            if seg_num[2]=='.':
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[0])],0x80)
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[1])]&0xfe,0x40)
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[3])],0x20)
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[4])],0x10)  
            
            if seg_num[3]=='.':
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[0])],0x80)
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[1])],0x40)
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[2])]&0xfe,0x20)
                self.seg_74hc595_write_16bit(seg_list[int(seg_num[4])],0x10)                                                                             

