#main bodeador

from dataManager import dataManager
from meterTechnician import meterTechnician
from bodeUserInterface import graphicalInterface
<<<<<<< HEAD
import matplotlib.pyplot as plt
=======
>>>>>>> parent of 61d96cc... se termina la gui layout, falta debbuggearla nuevamente.
#inicializacion de clases
gui = graphicalInterface()
ingeniero = meterTechnician(gui.measData)
dm = dataManager()
<<<<<<< HEAD
=======

>>>>>>> parent of 61d96cc... se termina la gui layout, falta debbuggearla nuevamente.

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
    


