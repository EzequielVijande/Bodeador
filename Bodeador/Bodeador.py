#main bodeador

from dataManager import dataManager
from meterTechnician import meterTechnician
from bodeUserInterface import graphicalInterface

gui = graphicalInterface()

if gui.pData.userWantContinue:
    ingeniero = meterTechnician(gui.measData)
    dm = dataManager()
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
    if (gui.pData.userWantGraphFase or gui.pData.userWantGraphMag):
        dm.show()
    


