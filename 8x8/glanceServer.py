#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight
from flask import Flask
from flask.ext.restful import Api, Resource
import os
from PIL import Image


app = Flask(__name__)
api = Api(app)
grid = []
icons = {}

for d, r, files in os.walk("icons/"):
	for filename in files:
		#print filename
		im = Image.open("icons/"+filename, 'r')
		pixels = im.load() # this is not a list, nor is it list()'able
		width, height = im.size
		all_pixels = []
		for x in range(width):      
			for y in range(height):
				cpixel = pixels[x, y]
				all_pixels.append(cpixel)
		#print all_pixels
        icons[filename]=all_pixels

print icons
for i in range(0,8):
  grid.append(EightByEight(address=0x70+i))

class Matrix8X8(Resource):
  def get(self):
    print "GET"
    pass

  def put(self, id):
    print"PUT"
    for x in range(0, 8):
      for y in range(0, 8):
        grid[id].setPixel(x, y)
        time.sleep(0.01)

  def delete(self, id):
    print "DELETE"
    pass

  def post(self, id):
    print "POST"
    pass

api.add_resource(Matrix8X8, '/8x8/<int:id>', endpoint = '8x8')



if __name__ == '__main__':
    app.run(host='0.0.0.0')


