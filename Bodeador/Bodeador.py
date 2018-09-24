#main bodeador

from dataManager import dataManager
from meterTechnician import meterTechnician
#import bodeUserInterface import graphicalInterface
from userData import instrumentsData
from userData import measurementsData
#inicializacion de clases
#gui = graphicalInterface()
idata = instrumentsData()
mdata = 
ingeniero = meterTechnician()
dm = dataManager()

#gui.show() #interfaz con el usuario
#ingeniero.prepareInstruments(gui.getInstrumentsData())

while gui.userWantContinue():
    ingeniero.prepareMeasurement(gui.getMeasurementData())
    ingeniero.meas()
    dm.calculateMag(ingeniero.getV1(), ingeniero.getV2())
    dm.setFase(ingeniero.getFase())
    dm.setFreq(ingeniero.getFreq())
    if (gui.doUserWantExcel()):
        dm.setRutaExcel(gui.getRutaExcel() + ".xlsx")
        dm.writeExcel()
    if (gui.doUserWantGraphMag()):
        dm.graphBodeMag()
    if (gui.doUserWantGraphFase()):
        dm.graphBodeFase()
    gui.askToMeasAgain()
    


