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
    
    logging.info("Drawing terrance")
    terrance = Image.open(os.path.join(picdir, 'mckenna.bmp'))
    epd.display(epd.getbuffer(terrance))

    max_frames = 500
    num = 1
    while (True):
        logging.info(time.strftime('%H:%M:%S'))
        if num % 10 == 0:
            logging.info("Terrance on iteration " + str(num))
            epd.init(0)
            epd.display(epd.getbuffer(terrance))
            time.sleep(1)
        epd.init(1)
        logging.info("Opening frame " + str(num))
        image_path = os.path.join(framesdir, str(num) + '.bmp')
        image = Image.open(image_path)
        logging.info("Displaying frame " + str(num))
        epd.displayPart(epd.getbuffer(image))
        num = num + 1
        if(num == max_frames):
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
    epd.init(0)
    epd.Clear(0xFF)
    epd1in54_V2.epdconfig.module_exit()
    exit()
