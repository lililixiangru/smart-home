################################################################################
#                           叁议电子
#                        www.ppptalk.com
# 版本：      pyboard改进版(V1.0)
# 文件名：    main.py
# 说明：      8位数码管实验(TM1638驱动)
# 淘宝店地址： https://shop115025335.taobao.com
# 免责声明：  该程序仅用于学习与交流
# (c) PPPTalk  All Rights Reserved
################################################################################

from seg8 import SEG8
import time

SEG8 = SEG8('Y9','Y10','Y11') #DIO->Y9, SCK->Y10, STB-> Y11

segnum = [0xF6,0xCF,0xFD,0xB6,0xA2,0xB8,0xBE,0x00]

SEG8.init()

SEG8.show_num(segnum)








