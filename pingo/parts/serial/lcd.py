import serial
import time


class LCD16x2(object):
    
    def __init__(self, port, baudrate=9600):
        self.serial = serial.Serial(port, baudrate)
        
    def clear(self):
        self.set_cursor(0, 0)
        self.serial.write(b' ' * 32)
    
    def set_cursor(self, line=0, column=0):
        first_pos = (128, 192)
        code = first_pos[line] + column
        self.serial.write(chr(254) + chr(code))
        
    def write(self, octets):
        self.serial.write(octets)
        
