import os
from PIL import Image

for d, r, files in os.walk("icons/"):
	for filename in files:
		print filename
		im = Image.open("icons/"+filename, 'r')
		pixels = im.load() # this is not a list, nor is it list()'able
		width, height = im.size
		all_pixels = [][]
		for x in range(width):
			for y in range(height):
				cpixel = pixels[x, y]
				all_pixels[x][y] = cpixel
		print all_pixels
