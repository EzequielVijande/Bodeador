import visa 
from visa import instrument 
my_instrument = instrument("GPIB0::7::INSTR") 
my_instrument.write("*IDN?") 
print (my_instrument.read() )
