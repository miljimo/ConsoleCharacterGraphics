import sys;
import subprocess;
import os;
import math;
import time
import queue;
from threading import Thread;


def arange(start , end , step =1):
    result  =  list()
    result.append(start);
    while(start != end):
        start += step
        result.append(start);
        
    return  result;



class Pixel(object):
    
    def __init__(self, x, y, period=65 ):
        self.x =  x;
        self.y =  y;
        freq  =  (math.pi * 2) / period;
        self.xvalues        =  arange(0, period);
        self.yvalues        =  list();
        
        for x in self.xvalues:
            c      = complex(math.cos(x * freq), math.sin(x * freq));
            length =  abs(c);
            self.yvalues.append( ((c.imag / length) * 0.5)+ 0.5);

        self.length =  len(self.xvalues);
      
    def draw(self, graphics):
        length =  len(self.xvalues);
        for x  in range(length):
            value   =  self.yvalues[x];
            yPos    =  int(value *  (graphics.height * 0.9)) + self.y
            graphics.draw_pixel(self.x + (x - length), yPos, "*");
        


def generate_grid(width,height, default="."):
    grid  =  list();

    for h in range(height):
        grid.append(list());
        for w in range(width):
            grid[h].append(default);

    return grid;
    


class Graphics(object):

    def __init__(self, width, height):
        self.grid    =  generate_grid(width,height);
        self.height  =  height;
        self.width   =  width;
        
        
    def clear(self):
        self.grid    =  generate_grid(self.width,self.height);
        
    def draw_pixel(self, x, y, character):
        if(x >= 0) and (x < self.width):
            if((y >= 0) and (y <self.height)):
                self.grid[y][x]  = character;
        
class Console(object):

    def __init__(self, width , height):
        self.graphics  =  Graphics(width, height)
        self.pixels =  list();
        self.__Thread  = Thread(target=self.ProcessPixel)
        self.__Thread.daemon= True
        self.__Thread.start();
        self.buffer    =  self.graphics.grid;


    def ProcessPixel(self):
        while(True):
            pass;
        
    @property    
    def width(self):
        return self.graphics.width;
    
    @property
    def height(self):
        return self.graphics.height;

    def add_pixel(self , pixel):
        self.pixels.append(pixel);
        
    def clear(self):
      self.graphics.clear();
      os.system('cls')
        
        
    def draw(self):
        self.clear();
        for pixel in self.pixels:
            pixel.draw(self.graphics);
            pixel.x+=1;
        pixel =  self.pixels[len(self.pixels)-1];
        nPixel = Pixel(-(pixel.x + pixel.length),0);
      
        display = "";
        for h in range(self.graphics.height):
            for w in range(self.graphics.width):
                display += self.graphics.grid[h][w];
            display+="\n";
        print(display);
       
        

        
        
        
        
        
 
if __name__ == "__main__":
     screen  =  Console(120,30);
     pixel = Pixel(0,0)
     screen.add_pixel(pixel)
     direction = 0;
     while(True):
         screen.draw();
       
             
     
