#main bodeador

from dataManager import dataManager
from meterTechnician import meterTechnician
from bodeUserInterface import graphicalInterface

#inicializacion de clases
gui = graphicalInterface()
ingeniero = meterTechnician(gui.measData)
dm = dataManager()

if gui.pData.userWantContinue:
    ingeniero.prepareMeasurement()
    ingeniero.meas()
    dm.calculateMag(ingeniero.v1, ingeniero.v2)
    dm.setFase(ingeniero.getFase())
    dm.setFreq(ingeniero.getFreq())
    if (gui.pData.userWantExcel):
        dm.setRutaExcel(gui.pData.excelName+ ".xlsx")
        dm.writeExcel()
    if (gui.pData.userWantGraphMag):
        dm.graphBodeMag()
    if (gui.pData.userWantGraphFase):
        dm.graphBodeFase()
    gui.askToMeasAgain()
    


