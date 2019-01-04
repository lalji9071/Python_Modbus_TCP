from pyModbusTCP.client import ModbusClient
import time
import os

def cls():
    os.system("cls")
# TCP auto connect on first modbus request
#c = ModbusClient(host="localhost", port=502, auto_open=True)

# TCP auto connect on modbus request, close after it
#c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=True)


c = ModbusClient()
c.host("192.168.58.10")
c.port(502)
# managing TCP sessions with call to c.open()/c.close()
c.open()
while True:
    regs = c.read_discrete_inputs(0, 16)
    coil= c.read_coils(0,16)
    if regs:
        #print(regs)
        #print(type(regs))
        #print(coil)
        #print(type(coil))
        x=regs[5]
        print(x)
    else:
        print("read error")
    time.sleep(5)


