# main.py -- put your code here!
from pyb import UART
import time
from pyb import Pin
import pyb

uart = UART(6,115200)
uart.write('AT\r\n')
time.sleep_ms(5)
uart.write('AT+CWMODE_CUR=1\r\n')
time.sleep_ms(5)
uart.write('AT+CWLAP\r\n')
time.sleep_ms(5000)
uart.write('AT+CWJAP_CUR="HUAWEI P20 Pro","12345678901"\r\n')
time.sleep_ms(5000)
time.sleep_ms(5000)
uart.write('AT+CIFSR\r\n')
time.sleep_ms(10)
uart.write('AT+CIPMUX=1\r\n')
time.sleep_ms(10)
uart.write('AT+CIPSERVER=1,8888\r\n')
time.sleep_ms(10)

pyb.LED(1).off()
pyb.LED(2).off()
pyb.LED(3).off()
pyb.LED(4).off()
motor = Pin('Y5',Pin.OUT_PP)
motor.low()

while True:
  if uart.any()>0:
    str = uart.read(30)
    if str[11:17]==b'led1on':
      pyb.LED(1).on()
    if str[11:18]==b'led1off':
      pyb.LED(1).off()
    if str[11:17]==b'led2on':
      pyb.LED(2).on()
    if str[11:18]==b'led2off':
      pyb.LED(2).off()    
    if str[11:17]==b'led3on':
      pyb.LED(3).on()
    if str[11:18]==b'led3off':
      pyb.LED(3).off()   
    if str[11:17]==b'led4on':
      pyb.LED(4).on()
    if str[11:18]==b'led4off':
      pyb.LED(4).off() 
    if str[11:17]==b'motoro':
      motor.high()
      time.sleep_ms(5000)
      time.sleep_ms(2000)
    if str[11:18]==b'motorof':
      motor.low()
      time.sleep_ms(5000)

