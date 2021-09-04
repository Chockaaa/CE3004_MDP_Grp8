port='/dev/ttyS0'
Baudrate=115200
import serial
y="20"
ser=serial.Serial('COM4', baudrate=Baudrate,timeout=1)
i=0
while 1:
    i=i+1
    
    data=ser.readline().decode('ascii')
    ser.write(bytes(y, 'UTF-8'))
    print(data)
    
    




