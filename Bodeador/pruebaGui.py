#programa de prueba de interfaz grafica

from bodeUserInterface import graphicalInterface
from userData import measurementsData
from userData import preferenceData

gui = graphicalInterface()
print("frecuencia inicial: " + str(gui.measData.fMin) + " Hz")
print("frecuencia final: " + str(gui.measData.fMax) + " Hz")
print("Vin: " + str(gui.measData.Vin) + " Volts")
print("Voffset " + str(gui.measData.Voffset) + " Volts")
print("Number of points to meas: " + str(gui.measData.numberOfPoints))
if gui.measData.ACcouple:
    print("coupling: AC")
if gui.measData.DCcouple:
    print("coupling: DC")
if gui.measData.acqAVER:
    print("acquire : AVERAGE")
if gui.measData.acqHRES:
    print("acquire: HIGH RESOLUTION")
if gui.measData.acqNORM:
    print("acquire: NORMAL")
if gui.measData.acqPEAK:
    print("acquire: PEAK DETECT")
if gui.measData.isRangeLinear:
    print("Sweep mode: LINEAR ")
if gui.measData.isRangeLog:
    print("Sweep mode: LOGARITHMIC")
if gui.measData.probeX1:
    print("Probe: X1")
if gui.measData.probeX10:
    print("Probe: X10")
if gui.measData.autoEstablish:
    print("Time to Establishment measure in automathic mode")
else:
    print("Time to Establishment measure seted manually in " + str(gui.measData.establish) + " seg")
if gui.pData.userWantExcel:
    print("User wants to create EXCEl FILE named as " + gui.pData.excelName)

if gui.pData.userWantGraphFase:
    print("User wants to graph phase diagram")
if gui.pData.userWantGraphMag:
    print("User wants to graph magnitude diagram")
if gui.pData.userWantContinue:
    print("User wants to go bode")
else:
    print("User wants to quit")


