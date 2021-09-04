port='/dev/ttyS0'
Baudrate=115200
import serial
y="22"
ser=serial.Serial('COM4', baudrate=Baudrate,timeout=1)
while 1:
    
    
    data=ser.readline().decode('ascii')
    ser.write(bytes(y, 'UTF-8'))
    print(data)
    




