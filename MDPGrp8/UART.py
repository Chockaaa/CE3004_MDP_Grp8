port='/dev/ttyS0'
Baudrate=115200
import serial

ser=serial.Serial('COM4', baudrate=Baudrate,timeout=1)
while 1:
    
    data=ser.readline().decode('ascii')
    ser.write(b'0101')
    print(data)




