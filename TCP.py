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

# to debug the communication
#c.debug(True)
inputRegD = c.read_discrete_inputs(0, 16)
coil = c.read_coils(0, 16)
read_holding = c.read_holding_registers(0, 2)
inputReg = c.read_input_registers(0, 2)

while True:
    if inputRegD:
        #print(regs)
        #print(type(regs))
        #print(type(coil))
        x=inputRegD[5]
        print("Read Input: " + str(inputRegD))
        print("Read Coils: " + str(coil))
        print("Holding Register: "+ str(read_holding))
        print("Read Input Register: " + str(inputReg))

    else:
        print("read error")
    time.sleep(5)


