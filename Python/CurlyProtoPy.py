import serial
import time
from serial.tools.list_ports import comports

class Curly:
    def __init__(self, Board="Arduino", baudRate=9600):
        self.baudRate = baudRate
        connected = False
        Found = False
        
        for port in comports():
            if Board.lower() in port.description.lower():
                print(f"A device is found at {port}")
                print(f"{port.description}")
                if input(f"Connect to {port} (y) / Keep searching (n) :").lower() == "y":
                    Found = True
                    try:
                        self.CurlyObj = serial.Serial(port.device)
                        self.CurlyObj.baudrate = baudRate
                        self.CurlyObj = serial.Serial(self.portNumber, self.baudRate)
                        connected = True
                        print(f'{Board} at {port} is Connected')
                    except:
                        print(f"Unable to connect to {Board}")

        if Found and not connected:
            print(f"Unable to connect to {Board}")
        if not Found:
            print(f"{Board} not found")


    def sendData(self, data):
        sendingString = "{"      # start character (start sending)
        for d in data:
            sendingString += str(int(d))
        sendingString += "}"     # end character (end sending)
