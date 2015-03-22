#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight
from flask import Flask
from flask.ext.restful import Api, Resource


app = Flask(__name__)
api = Api(app)
grid = []
for i in range(0,8):
  grid.append(EightByEight(address=0x70+i))

class 8X8Matrix(Resource):
    def get(self):
      pass

    def put(self, id):
      for x in range(0, 8):
      for y in range(0, 8):
        grid[id].setPixel(x, y)
        time.sleep(0.01)

    def delete(self, id):
      pass

api.add_resource(8X8Matrix, /8x8/<int:id>, endpoint = '8x8')



