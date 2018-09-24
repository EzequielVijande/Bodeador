import visa
from instruments import osciloscope
from instruments import generator


direccion = "USB0::0x0957::0x0407::MY44013183::0::INSTR"
rm= visa.ResourceManager()
inst= generator(direccion,rm)
inst.setVoltage(1)
inst.setOffset(0)
