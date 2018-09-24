#bodeUserInterface
from userData import instrumentsData
from userData import measurementsData
from TKinter import *

class graphicalInterface:
    def __ini__(self):
        #userData
        self.instData = instrumentsData()
        self.measData = measurementsData()
        #graphicalResources
        self.raiz = Tk()
        self.raiz.geometry('300x200')

        self.raiz.resizable(width=True,height=True)
        self.raiz.title('Auto Bode Software')

        #variables vinculadas a los graphical resources
        self.isMinScaleHz = True
        self.isMinScaleKHz = False
        self.fMin = 0

        self.isMaxScaleHz = True
        self.isMaxScaleKHz = False
        self.fMax = 0

        self.isVinScaleVolt = True
        self.isVinScaleMiliVolt = False

        self.isExcelWanted = True
        self.nombreExcel = "FrequencyResponse" 
        self.isMagGraphWanted = False
        self.isFaseGraphWanged = False

        

    def show(self): #se muestra la interfaz grafica con el usuario para que elija la userData


