port='/dev/ttyS0'
Baudrate=115200
import serial
import time

ser=serial.Serial('COM5', baudrate=Baudrate,timeout=1)
i=0
data=""
while 1:
   
    
    
    ser.write(bytes(input("Input:"), 'UTF-8'))
    time.sleep(0.5)
    ser.write(bytes('00000', 'UTF-8'))
    print("Output:")
    while(data!="READY"):
        data=ser.readline().decode('UTF-8')
        print(data)
    data=""    
    
    




