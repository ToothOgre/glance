#!/usr/bin/python

import time
import datetime
from Adafruit_8x8 import EightByEight
from flask import Flask, request
from flask.ext.restful import Api, Resource
import os
from PIL import Image
import serial
from font import fonts


app = Flask(__name__)
api = Api(app)
grid = []
icons = {}
ser=serial.Serial("/dev/ttyUSB0", 115200)

try:
  ser.close()
except:
  pass
ser.open()

def drawChar(chr, x, y,r,g,b): 
    chr=ord(chr)
    a=chr*5
    for i in range(a,a+5):
        tmp=""
        for j in range(7-len(bin(int(hex(fonts[i]),16))[2:])): 
            #print '0',
            tmp+='0'
        tmp+=str(bin(int(hex(fonts[i]),16))[2:])
        #print "\n"
        #print tmp
        tmp2=y
        for k in range(6,-1,-1):
            
            if tmp[k]=='1':
                ser.write(str(x)+","+str(tmp2)+","+str(r/32)+","+str(g/32)+","+str(b/32)+"*")
                time.sleep(0.002)
            tmp2+=1
        #print "y = ",tmp2    
            #pass
        x+=1    
def clearPanel():
  for y in range(16):
    for x in range(32):
      #r, g, b = rgb_im.getpixel((x, y))
      ser.write(str(x)+","+str(y)+","+str(0)+","+str(0)+","+str(0)+"*")
      time.sleep(0.002)
       
def printText(text, x,y, r,g,b):
    if len(text)>5:
        for i in range(len(text)):
            tmp=x
            for chr in text[i:i+5]:
                drawChar(chr,tmp,y,r,g,b)
                tmp+=6
            time.sleep(0.1)
            tmp=x
            for chr in text[i:i+5]:
                drawChar(chr,tmp,y,0,0,0)
                tmp+=6
            #time.sleep(0.1)
    else:
        for chr in text:
            drawChar(chr,x,y,r,g,b)
            x+=6
            
            
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
                if cpixel[0]>127 and cpixel[1]>127 and cpixel[2]>127:
                    cpixel=1
                else:
                    cpixel=0
                all_pixels.append(cpixel)
        #print all_pixels
        icons[filename]=all_pixels

#print icons
for i in range(0,8):
    grid.append(EightByEight(address=0x70+i))

def writeIconToMatrix(gridNumber, IconFileName):
    icon = icons[IconFileName]
    #print icon
    grid[gridNumber].clear()
    for x in range(0, 8):
        for y in range(0, 8):
            #print (x*8)+y
            if icon[(x*8)+y] == 1:
                grid[gridNumber].setPixel(y, (7-x))
                #time.sleep(0.01)
            
            
class Matrix8X8(Resource):
    def get(self):
        print "GET"
        pass

    def put(self):
        print"PUT"
        for file in request.form['iconFile'].split(","):
            if file=="clear":
                grid[int(request.form['gridNumber'])].clear()
            else:
                writeIconToMatrix(int(request.form['gridNumber']), file.strip())
                try:
                    time.sleep(float(request.form['interval'])/1000)
                except:
                    pass

    def delete(self, id):
        print "DELETE"
        pass

    def post(self, id):
        print "POST"
        pass

        
class PlaySound(Resource):
    def get(self):
        print "GET"
        pass

    def put(self):
        print"PUT"
        for file in request.form['soundFile'].split(","):
            os.system("omxplayer "+file)
            try:
                time.sleep(float(request.form['interval'])/1000)
            except:
                pass

    def delete(self, id):
        print "DELETE"
        pass

    def post(self, id):
        print "POST"
        pass
        
        
        
class RGBPanel(Resource):
    def get(self):
        print "GET"
        pass

    def put(self):
        print"PUT"
        printText(request.form['text'],int(request.form['x']),int(request.form['y']),int(request.form['red']),int(request.form['green']),int(request.form['blue']))
            

    def delete(self, id):
        print "DELETE"
        pass

    def post(self, id):
        print "POST"
        pass



class RGBPanelClear(Resource):
    def get(self):
        print "GET"
        clearPanel()
        pass
        
api.add_resource(Matrix8X8, '/8x8/icon')
api.add_resource(PlaySound, '/8x8/sound')
api.add_resource(RGBPanel, '/8x8/panel')
api.add_resource(RGBPanelClear, '/8x8/panel/clear')


if __name__ == '__main__':
    #writeIconToMatrix(0, 'icon_water1.bmp')
    os.system("omxplayer sound/glanceready.mp3")
    printText("Hello", 0, 0, 255, 255, 255)
    app.run(host='0.0.0.0')
    

