import serial.tools.list_ports
print("printing")
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device)
    

    