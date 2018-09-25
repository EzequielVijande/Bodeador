#codigo de prueba
from userData import measurementsData
from dataManager import dataManager
class prueba:
    def __init__(self):
        self.MyInstrumentsData = measurementsData()
        self.datoDePrueba = 10

inst = prueba()
inst.MyInstrumentsData.numberOfPoints = inst.datoDePrueba
print(inst.MyInstrumentsData.numberOfPoints)

asd = dataManager()
f = [1, 2, 3]
asd.setFreq(f)
asd.setMag(f)
asd.setFase(f)
asd.writeExcel()

