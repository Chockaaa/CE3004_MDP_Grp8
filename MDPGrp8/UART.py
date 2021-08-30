port='/dev/ttyS0'
Baudrate=115200
import serial
x=100020003000
y='a'
ser=serial.Serial('COM4', baudrate=Baudrate,timeout=1)
while 1:
    
    data=ser.readline().decode('ascii')
    
    y=str(x)
    ser.write(bytes(y, 'UTF-8'))
    print(data)
    x=x+1




