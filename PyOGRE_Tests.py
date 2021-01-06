import serial
from time import sleep
import sys
import time
import math

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor



COM  = 'COM4'
BAUD = 115200
    
#COML  = 'COM9'
#BAUDL = 115200

ser = serial.Serial(COM, BAUD, timeout = .1)
#serL = serial.Serial(COML, BAUDL, timeout = .1)


v_angle = 0
dist = 0
h_angle = 0
class MyApp(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)
         
        
        self.scene = self.loader.loadModel("models/zup-axis")
   
        self.scene.reparentTo(self.render)
        
        self.scene.setScale(4, 4,4)
        self.scene.setPos(0,0,0)
        
        dancer = Actor("models/panda-model")
        dancer.setPos(0,0,0)
        dancer.setScale(0.004,0.004,0.004)
        
        t_end = time.time()+10   
        while time.time() < t_end:
            placeholder = render.attachNewNode("Dancer-Placeholder")
            remain = t_end - time.time()
            print(remain)
            global v_angle
            global dist
            global h_angle
            msg = ser.readline().strip().decode()     
            data = msg.split()
            print(msg)
           # msgL = serL.readline().strip().decode()                   
            if msg:            
                v_angle = float(data[1])              
            
                dist = float(data[0])
                dist = dist/2
            
            
                 
            if dist != 65535:
                
                placeholder.setPos((-1)*dist*math.cos(math.radians(0))*math.cos(math.radians(v_angle)), dist*math.cos(math.radians(0))*math.sin(math.radians(v_angle)),0)
                dancer.instanceTo(placeholder)
                
        #    time.sleep(0.002)    
          
            #placeholder.setPos(dist*math.cos(math.radians(h_angle)),dist*math.sin(math.radians(h_angle)),0)
            #print("x:",dist*math.cos(math.radians(v_angle))*math.cos(math.radians(h_angle)),"y:",dist*math.cos(math.radians(v_angle))*math.sin(math.radians(h_angle)),"z:",dist*math.sin(math.radians(v_angle)),"v_angle:",v_angle,"h_angle:",h_angle,"distance:",dist)
            #dancer.instanceTo(placeholder)
            
        

    

            
            
              
                

app = MyApp()
app.run()