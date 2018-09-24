#osciloscopio
import visa as v
from userData import instrumentsData
from userData import measurementsData
from instruments import osciloscope
from instruments import generator

class meterTechnician:
    def _init_(self):
        self.rm = v.ResourceManager()
        self.instruments = rm.list_resources()
        self.f = 0
        self.v1 = 0
        self.v2 = 0
        self.fase = np.array[]
        self.MyInstrumentsData = instrumentsData()
        self.MyMeasurementsData = measurementsData()
        self.canalString = "CHANnel 1"
    def prepareInstruments(self, instrumentData):
        self.MyInstrumentsData = instrumentData
        self.osc = osciloscope(MyinstrumentsData.oscIndez)
        self.gen = generator(MyinstrumentsData.genIndex)

    def prepareMeasurement(self, measurementData):
        self.MyMeasurementsData = measurementData
        
    

    #METODOS PARA LA CLASE GENERADOR

    def 

    