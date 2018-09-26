#main bodeador

from dataManager import dataManager
from meterTechnician import meterTechnician
from bodeUserInterface import graphicalInterface
import matplotlib.pyplot as plt
#inicializacion de clases
gui = graphicalInterface()
ingeniero = meterTechnician(gui.measData)
dm = dataManager()

if gui.pData.userWantContinue:
    ingeniero.prepareMeasurement()
    ingeniero.meas()
    dm.calculateMag(ingeniero.v1, ingeniero.v2)
    dm.setFase(ingeniero.fase)
    dm.setFreq(ingeniero.f)
    if (gui.pData.userWantExcel):
        dm.setRutaExcel(gui.pData.excelName+ ".xlsx")
        dm.writeExcel()
    if (gui.pData.userWantGraphMag):
        dm.graphBodeMag()
    if (gui.pData.userWantGraphFase):
        dm.graphBodeFase()
    plt.show()
    


