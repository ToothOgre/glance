#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight

# ===========================================================================
# 8x8 Pixel Example
# ===========================================================================
grid = []
for i in range(0,8):
  grid.append(EightByEight(address=0x70+i))

print "Press CTRL+Z to exit"

# Continually update the 8x8 display one pixel at a time
while(True):
  for i in range(0,8):
    grid[i].clear()
    for x in range(0, 8):
      for y in range(0, 8):
        grid[i].setPixel(x, y)
        time.sleep(0.01)
    #time.sleep(0.1)
    #grid[i].clear()
    #time.sleep(0.1)
#for gridSingle in grid:
  #gridSingle.clear()
