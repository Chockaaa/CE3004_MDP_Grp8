port='/dev/ttyS0'
Baudrate=115200
import serial
listt=["10","20","11","21","12","22"]
y="20"
ser=serial.Serial('COM4', baudrate=Baudrate,timeout=1)
i=0
while 1:
    i=i+1
    
    data=ser.readline().decode('ascii')
    ser.write(bytes(listt[i%6], 'UTF-8'))
    print(data)
    
    




