#programa de prueba para las clases meterTechnician y los instrumentos

from dataManager import dataManager
from meterTechnician import meterTechnician
from userData import measurementsData
from userData import instrumentsData  #en principio esta data (instrumentsData
                                    #seria ingresada por el usuario,
                                    #sin embargo, se podria mejorar esto deduciendo los datos de los 
                                    #instrumentos mediante pyVisa.

mData = measurementsData()
iData = instrumentsData()
ingeniero = meterTechnician()
dm = dataManager()

#se setean algunos parametros de medicion (los demas se determinan en el constructor)
mData.numberOfPoints = 100 
mData.DCcouple = False
mData.ACcouple = True
mData.fMin = 1000 #1KHz
mData.fMax = 100000 #100KHz
mData.Vin = 2 #2 VPP


#se setean los datos miembros de iData
iData.oscIndex = 1
iData.genIndex = 2


#se pasan los parametros al ingeniero
ingeniero.prepareInstruments(iData)
ingeniero.prepareMeasurement(mData)
ingeniero.meas()
dm.calculateMag(ingeniero.getV1(), ingeniero.getV2())
dm.setFase(ingeniero.getFase())
dm.setFreq(ingeniero.getFreq())
if 1: #para estas condiciones de los bloques 'if' faltaria hacer una clase que contenga las preferencias 
                #del usuario, por ejemplo, si desea o no desea una archivo de excel con los datos
    dm.setRutaExcel(gui.getRutaExcel() + ".xlsx")
    dm.writeExcel()
if 1:
     dm.graphBodeMag()
if 1:
    dm.graphBodeFase()

    

