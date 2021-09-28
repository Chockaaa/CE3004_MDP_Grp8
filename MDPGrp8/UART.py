port='/dev/ttyS0'
Baudrate=115200
import serial
import time
listt=["10","20","11","21","12","22"]
y="20"
ser=serial.Serial('COM5', baudrate=Baudrate,timeout=1)
i=0
while 1:
    i=i+1
    
    
    ser.write(bytes(input(), 'UTF-8'))
    time.sleep(1)
    data=ser.readline().decode('UTF-8')
    print(data)
    ser.write(bytes('00000', 'UTF-8'))
    
    
    




