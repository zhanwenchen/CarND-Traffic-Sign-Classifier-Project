from PIL import Image
from math import floor
import os

def pad_to_square_longer_side(fname):
	old_im = Image.open(fname)
	old_size = old_im.size

	if old_size[0] == old_size[1]: return

	longer_side = max(old_size[0], old_size[1])

	print("longer_side is ", longer_side)

	new_size = [longer_side, longer_side]
	new_im = Image.new("RGB", new_size)   ## luckily, this is already black!
	new_im.paste(old_im, (int(floor(new_size[0]-old_size[0])/2),
	                      int(floor(new_size[0]-old_size[0])/2)))

	new_im.show()
	new_im.save(fname)

def resize(width, height, fname):
	old_im = Image.open(fname)
	old_im.thumbnail([width, height], Image.ANTIALIAS)
	old_im.show()
	old_im.save(fname)

# for file_name in os.listdir('internet_images'):
for file_name in os.listdir('.'):
	if '.jpg' in file_name:
		pad_to_square_longer_side(file_name)
		resize(32, 32, file_name)
