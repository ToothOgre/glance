import os
from PIL import Image

for d, r, files in os.walk("icons/"):
	for filename in files:
		print filename
		im = Image.open(filename, 'r')
		pixels = i.load() # this is not a list, nor is it list()'able
		width, height = i.size
		all_pixels = []
		for x in range(width):
			for y in range(height):
				cpixel = pixels[x, y]
				all_pixels.append(cpixel)
		print all_pixels