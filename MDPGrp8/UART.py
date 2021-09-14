port='/dev/ttyS0'
Baudrate=115200
import serial
listt=["10","20","11","21","12","22"]
y="20"
ser=serial.Serial('COM5', baudrate=Baudrate,timeout=1)
i=0
while 1:
    i=i+1
    
    data=ser.readline().decode('ascii')
    ser.write(bytes(input(), 'UTF-8'))
    print(data)
    
    




