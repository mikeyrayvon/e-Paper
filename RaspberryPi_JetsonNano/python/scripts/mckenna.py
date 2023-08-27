#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
framesdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'frames2')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd1in54_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("McKenna")
    
    epd = epd1in54_V2.EPD()
    
    logging.info("init and Clear")
    epd.init(0)
    epd.Clear(0xFF)
    time.sleep(1)
    
    # read bmp file 
    logging.info("Drawing terrance...")
    image = Image.open(os.path.join(picdir, 'mckenna.bmp'))
    epd.display(epd.getbuffer(image))
    time.sleep(5)

    epd.init(1)
    num = 1
    while (True):
        logging.info("Drawing lamb video frame..." + str(num))
        image = Image.open(os.path.join(framesdir, str(num) + '.bmp'))
        epd.displayPart(epd.getbuffer(image))
        num = num + 1
        if(num == 1895):
            break
    
    logging.info("Clear...")
    epd.init(0)
    epd.Clear(0xFF)
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd1in54_V2.epdconfig.module_exit()
    exit()
