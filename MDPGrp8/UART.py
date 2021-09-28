port='/dev/ttyS0'
Baudrate=115200
import serial
import time
import math
ser=serial.Serial('COM5', baudrate=Baudrate,timeout=1)
i=0
data=""
while 1:
   
    while(1):
        val=input("Input:")
        if(len(val)==5):
            break
    
    ser.write(bytes(val, 'UTF-8'))
    time.sleep(0.5)
    ser.write(bytes('00000', 'UTF-8'))
    print("Output:")
    starttime=time.time()
    while(len(data)!=5):
        data=ser.readline().decode('UTF-8')
        print(data)
        endtime=time.time()        
        if((endtime-starttime)>=17):
            print("NO Reply")
            break

    data=""    
    
    




