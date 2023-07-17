import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd7in3g
import logging
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)                           #Enable log-information for debbuging

try:
    epd = epd7in3g.EPD()
    epd.init()
    epd.Clear()

    font48 = ImageFont.truetype("Font.ttc", 48)

    #Draw something on the e-ink screen
    Himage = Image.new('1', (epd.width, epd.height), 255)           #Clear the frame (255 = white)
    draw = ImageDraw.Draw(Himage)                                   #Create new image buffer
    draw.text((40, 40), 'Hello world', font = font48, fill = 0)     #Write text on position 40,40 (x,y) in black
    epd.display(epd.getbuffer(Himage))                              #Display the buffer on the screen
    time.sleep(4)

    epd.init()
    epd.Clear()
    epd.sleep()

except IOError as e:
    logging.info(e)