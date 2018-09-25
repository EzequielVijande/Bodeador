#programa de prueba de interfaz grafica

from bodeUserInterface import graphicalInterface
from userData import measurementsData
from userData import preferenceData

gui = graphicalInterface()
print("frecuencia inicial: " + str(gui.measData.fMin) + " Hz")
print("frecuencia final: " + str(gui.measData.fMax) + " Hz")
print("Vin: " + str(gui.measData.Vin) + " Volts")
print("Voffset " + str(gui.measData.Voffset) + " Volts")
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
if gui.pData.userWantExcel:
    print("User want to create EXCEl FILE named as " + gui.pData.excelName)

if gui.pData.userWantGraphFase:
    print("User want to graph phase diagram")
if gui.pData.userWantGraphMag:
    print("User want to graph magnitude diagram")
if gui.pData.userWantContinue:
    print("User want to continue with the program")


