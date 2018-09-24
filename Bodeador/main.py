import visa
from instruments import osciloscope


direccion = "USB0::0x0957::0x1724::MY45002351::0::INSTR"
rm= visa.ResourceManager()
inst= osciloscope(direccion,rm)

inst.setTriggerCero()

