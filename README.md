# arduino-lidar-python-scanner
Python Arduino Laser Scanner

In this project I had to use two Arduino Uno because of my computer's USB 3.0 could not recognize Arduino Mega 2560 but Main Python code had setted up for Mega so my 2 Arduino Uno acting like Mega.
So you won't be has to use two Uno.

In main.py we connect Arduino to Python but other Arduino directly connected to the other arduino so it's unnecessary to connect both of them in to pc.

```py
COM  = 'COM4'
BAUD = 115200
    
ser = serial.Serial(COM, BAUD, timeout = .1)
```


Then we build a 3D scene for scan render this time I'll use Panda 3D but you can use whatever you want to use.
```py
self.scene = self.loader.loadModel("models/zup-axis") #x-y-z axis
   
        self.scene.reparentTo(self.render)
        
        self.scene.setScale(4, 4,4)
        self.scene.setPos(0,0,0)
        
        dancer = Actor("models/panda-model") # our instanced object
        dancer.setPos(0,0,0)
        dancer.setScale(0.004,0.004,0.004)
```        

This scanner could not work until forever so we have to add an time limit (in here its 10 seconds).

```py
t_end = time.time()+10   
        while time.time() < t_end:
``` 
In this block we get the message from Arduino but we has to encrypt and turn into a array by .split() because Arduino sends two value which is degree and the other is measurement


```py
 msg = ser.readline().strip().decode()     
            data = msg.split()
``` 
Firstly we have to make sure message is exist then we turned them into float.
```py
if msg:            
                v_angle = float(data[1])              
            
                dist = float(data[0])
                
```                

and the last thing instancing objects by coordinates.But I need to make sure measurement is not equal to 65535 because lidar sometimes give that value without reason (65535 cm equals to 655 meter which is impossiable for that device.).
```py 
 if dist != 65535:
                
                placeholder.setPos((-1)*dist*math.cos(math.radians(0))*math.cos(math.radians(v_angle)), dist*math.cos(math.radians(0))*math.sin(math.radians(v_angle)),0)
                dancer.instanceTo(placeholder)
```                  
Arduino Scheme
![Arduino_Scheme](https://i.imgur.com/2II52DF.jpg)


Results:
![Result_1](https://i.imgur.com/2II52DF.jpg)
![Result_2](https://i.imgur.com/tHwkaIq.jpg)
