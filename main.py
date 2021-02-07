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
    
    def __init__(self, x, y):
        self.x     =  x;
        self.y     =  y;
        self.color =  "@";
        self.discrete =  False;
    def draw(self, g):
        if(self.discrete is True):
            half_height  =  int(g.height *0.5)+3
            length  = (self.y - half_height);
            if length > 0:
                for y in range(length):
                    g.draw_pixel(self.x, self.y - y, self.color);
            else:
               for y in range(abs(length)):
                    g.draw_pixel(self.x, self.y + y, self.color);
           
        else:
            g.draw_pixel(self.x, self.y, self.color);

        self.x+=1
                
def generate_grid(width,height, default="-"):
    grid  =  list();
    for h in range(height):
        grid.append(list());
        for w in range(width):
            grid[h].append(default);

    return grid;
    


class Graphics(object):

    def __init__(self, width, height):
        self.height    =  height;
        self.width     =  width;
        
        self.clear();
        
    def clear(self):
        self.grid = generate_grid(self.width,self.height);
        
    def draw_pixel(self, x, y, character):
        if(x >= 0) and (x < self.width):
            if((y >= 0) and (y <self.height)):
                self.grid[y][x]  = character;
    @property
    def data(self):
        return self.__data;
    
        
class Console(object):

    def __init__(self, width , height):
        self.graphics  =  Graphics(width, height)
        self.pixels    =  list();
        self.x_value    = 0;
        self.x = 5;
        self.y = 5;
        self.discrete  = True;
   
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
      self.display = "";
      #draw middle line
      yPos  =  int(self.height * 0.5)+3
      for xPos in range(self.width):
          self.graphics.grid[yPos][xPos] = "*"
        
    def draw(self):
        self.clear();
        for pixel in self.pixels:
            pixel.discrete =  self.discrete;
            pixel.draw(self.graphics);
        
        for h in range(self.graphics.height):
            if(h >= self.y):
                for w in range(self.graphics.width):
                    if(w >= self.y):
                         self.display += self.graphics.grid[h][w];
                    else:
                        self.display+=" ";
            self.display+="\n";
        print(self.display);
       
        
if __name__ == "__main__":
     screen  =  Console(16*8,16*2);
    
     screen.x+=5;
     direction = 0;
     xPos      = 0;
     period    = 4*10;
     k         = 2;
     freq      = k *( 2 * math.pi) / period;
     
     while(True):
         xPos -=1;
         c = 0;
         c     += complex(math.cos(freq * xPos),math.sin(freq * xPos));
         c  =  c / abs(c);
         yPos  =  ((c.imag * 0.5)+ 0.5) * screen.height * 0.8
         screen.add_pixel(Pixel(int(screen.x+ xPos),int(screen.y + yPos)+1));
         screen.draw();
         time.sleep(0.15);
         
       
             
     
