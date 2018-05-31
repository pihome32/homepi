
from PIL import Image, ImageDraw, ImageFont
import sys
import argparse
import json
#import matplotlib

#matplotlib.use('Agg')
#from pylab import *
#import matplotlib.pyplot as plt

def build_image(data):
	
	data= json.loads(data)
	print(data)
	base_image = Image.open('template.png')
	area = (0, 0, 384, 640)
	im = Image.new('L', (384, 640), 255) # Create a blank image
    #font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 74)
	font = ImageFont.truetype("DejaVuSans.ttf", 74)
	im.paste(base_image, area)
	draw = ImageDraw.Draw(im) # Create a draw object
	draw.text((90, 10), str(data['temperature']), font = font, fill = 127)
	draw.text((90, 120), str(data['out_temp']), font=font, fill=127)
	draw.text((90, 220), str(data['humidity']), font=font, fill=127)

	im.save("img1.png")