from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from bisect import bisect
import random
import os
import sys

scale = [
		" ",
		" ",
		".,-",
		"_ivc=!/|\\~",
		"gjez2]/(YL)t[+T7Vf",
		"mdK4ZGbNDXY5P*Q",
		"W8KMA",
		"#%$"
		]
 
bounds = [36, 72, 108, 144, 180, 216, 252]
img_rescale = 1
font = "font/Anonymous.ttf"
font_char_size = 5, 5
font_color = (0, 0, 0)
font_size = 11
font_spacing = 1
img_color = True

path = sys.argv[1]

image = Image.open(path, "r")
size = image.size[0], image.size[1]
file_name = (path.split("/"))
file_name = file_name[len(file_name)-1][:-4]

font = ImageFont.truetype(font, font_size)

image = image.resize((image.size[0]/img_rescale, image.size[1]/img_rescale), Image.BILINEAR)
b_image = image.convert("P")

size = [image.size[0] * (font_char_size[0] + font_spacing),
		image.size[1] * (font_char_size[1] + font_spacing)] 

img_new = Image.new('RGB', size, "white")
draw = ImageDraw.Draw(img_new)

ascii_image = ""
pos_y = 0
for y in range(image.size[1]):
	pos_x = 0
	for x in range(image.size[0]):
		dif = 255 - b_image.getpixel((x, y))
		scale_line = scale[bisect(bounds, dif)]

		if img_color:
			font_color = image.getpixel((x, y))

		draw.text((pos_x, pos_y), scale_line[random.randint(0, len(scale_line)-1)], font_color, font=font)
		pos_x += font_char_size[0] + font_spacing

		ascii_image += scale_line[random.randint(0, len(scale_line)-1)]
	pos_y += font_char_size[1] + font_spacing
	ascii_image += "\n"	

img_new.save(file_name + "_ascii.png")
img_new.close()