#osciloscopio
import visa as v
import time
import numpy as np
from userData import instrumentsData
from userData import measurementsData
from instruments import osciloscope
from instruments import generator

Ncuadrados = 10 #numero de cuadrados del osciloscopio 
ajusteEscalaY = (Ncuadrados - 4)
ajusteEscalaX = 1.5/Ncuadrados
maxNpoints = 300
periods2Establish = 10
LOOP_LIMITER = 500

class meterTechnician:
    def __init__(self,m_Data):
        self.rm = v.ResourceManager()
        self.instruments = self.rm.list_resources()
        self.MyInstrumentsData = self.UpdateInstruments()
        self.prepareInstruments()
        self.MyMeasurementsData = measurementsData()
        self.MyMeasurementsData = m_Data
        self.v1= []
        self.v2= []
        self.fase=[]

    def UpdateInstruments(self):
        first_instrument_name = self.instruments[0]     #Obtengo las direcciones de
        second_instrument_name = self.instruments[1]    #ambos instrumentos
        self.first_instrument= self.rm.open_resource(first_instrument_name) #Establezco la conexion a ambos instrumentos
        self.second_instrument= self.rm.open_resource(second_instrument_name)

        Id1= str(self.first_instrument.query('*IDN?'))
        strings1= Id1.split(',')
        model1 = strings1[1]
        if model1[0] =='3': #si el modelo empieza con 3 es un generadaor
            gen_index=0
            osc_index=1
        else:               #caso contrario asumo que es un osciloscopio
            gen_index=1
            osc_index=0
        return instrumentsData(osc_index, gen_index)


    def prepareInstruments(self):
        if (self.MyInstrumentsData.oscIndex)==0:
            self.osc = osciloscope(self.first_instrument)
            self.gen = generator(self.second_instrument)
        else:
            self.osc = osciloscope(self.second_instrument)
            self.gen = generator(self.first_instrument)
        

    def prepareMeasurement(self):

        self.prepareGenerator()  #configuracion del generador

        self.osc.changeChannel(2) 
        self.initializeChannel()  #configuracion de canal 2
        self.osc.changeChannel(1) 
        self.initializeChannel()  #configuracion de canal 1

        self.debugNumberOfPoints()

        self.prepareFrequences()  #configuraciones generales del osciloscopio
        self.prepareTrigger()
        self.prepareAcquire()
        self.initializeTimeBase()
    
    def meas(self):
        self.gen.setOutputOn()
        for i in self.f:
            self.gen.setFrequency(int(i))
            self.waitEstablishment(int(i))
            self.osc.setTimeScale((1/int(i))*ajusteEscalaX)
            self.osc.changeChannel(1)
            self.prepareScaleY()
            
            self.v1.append(self.osc.measPk2Pk())
            self.osc.changeChannel(2)
            self.osc.setScale(self.osc.measPk2Pk()/ajusteEscalaY)
            self.v2.append(self.osc.measPk2Pk())
            self.fase.append(self.osc.measFase(1))
        
    def prepareTrigger(self):
        self.osc.setTriggerCero()
    
    def prepareAcquire(self):
        if self.MyMeasurementsData.acqAVER:
            self.osc.setAverage()
            self.osc.setNaverages(self.MyMeasurementsData.nAverages)
        if self.MyMeasurementsData.acqHRES:
            self.osc.setHighResolution()
        if self.MyMeasurementsData.acqNORM:
            self.osc.setNormal()
        if self.MyMeasurementsData.acqPEAK:
            self.osc.setPeakDetect()
        

        
    def initializeTimeBase(self):
        self.osc.setRollMode()
        self.osc.setTimeBasePosCero()
        self.osc.setTimeScale((1/self.MyMeasurementsData.fMin)*ajusteEscalaX)
        self.setFilter()

    def setFilter(self):
        if self.MyMeasurementsData.HFrejectOn:
            self.osc.setHFrejectOn()
        if self.MyMeasurementsData.NOISEreject:
            self.osc.setNOISErejectOn()



    def setProbe(self):
        if self.MyMeasurementsData.probeX10:
            self.osc.setProbeX10()
        if self.MyMeasurementsData.probeX1:
            self.osc.setProbeX1()

    def setCoupling(self):
        if self.MyMeasurementsData.DCcouple:
            self.osc.setDCcoupling()

        elif self.MyMeasurementsData.ACcouple:
            self.osc.setACcoupling()
        elif self.MyMeasurementsData.LFrejectOn:
            self.osc.setLFrejectOn()
        
        
    def initializeChannel(self):
        self.osc.setScale(self.MyMeasurementsData.Vin/ajusteEscalaY)
        self.setProbe() #X1 o X10
        self.osc.setBWL()
        self.setCoupling()

    def prepareGenerator(self):
        self.gen.setOffset(self.MyMeasurementsData.Voffset)
        self.gen.setVoltage(self.MyMeasurementsData.Vin)
        self.gen.setFrequency(self.MyMeasurementsData.fMin)

    def prepareFrequences(self):
        if (self.MyMeasurementsData.isRangeLinear):
            self.f = np.linspace(self.MyMeasurementsData.fMin, self.MyMeasurementsData.fMax, 
                                                        num = self.MyMeasurementsData.numberOfPoints)
        if (self.MyMeasurementsData.isRangeLog):
            self.f = np.geomspace(self.MyMeasurementsData.fMin, self.MyMeasurementsData.fMax, 
                                            self.MyMeasurementsData.numberOfPoints)
    def debugNumberOfPoints(self):
        if self.MyMeasurementsData.numberOfPoints > maxNpoints:
            self.MyMeasurementsData.numberOfPoints = maxNpoints
    def waitEstablishment(self, fActual):
        if self.MyMeasurementsData.autoEstablish:
            time.sleep(periods2Establish/fActual)
        else:
            time.sleep(self.MyMeasurementsData.establish) #tiempo de establecimiento

    def prepareScaleY(self):
        pk2pk = self.osc.measPk2Pk()
        counter = 0
        while (pk2pk != 1e37) or (counter < LOOP_LIMITER):
            auxScaleY = self.osc.obtainActualScaleY()
            self.osc.setScale(auxScaleY*2)
            counter = counter +1
            pk2pk = self.osc.measPk2Pk()
            self.osc.setScale(int(pk2pk/int(auxScaleY)))
        

        


        


    