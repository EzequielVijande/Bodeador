#instruments
import visa as v
import copy

class osciloscope:
    def __init__(self, osc_res):
        self.osc= osc_res
        self.osc.write(":TRIG:SWE AUTO")
        self.osc.write("TRIG:EDGE:COUP AC")
        self.canalString= "CHAN1"
    #METODOS DE COMANDOS OSCILOSCOPIO

    #CHANNELS

    def changeChannel(self, numberOfChannel):
        self.canalString = "CHAN" + str(numberOfChannel)

    def setBWL(self):
        self.osc.write(":" + self.canalString + ":BWL")

    def setDCcoupling(self):
        self.osc.write(":" + self.canalString + ":COUP DC")

    def setACcoupling(self):
        self.osc.write(":" + self.canalString + ":COUP AC")

    def setProbeX1(self):
        self.osc.write(":" + self.canalString + ":PROB 1.0E0")
    def setProbeX10(self):
        self.osc.write(":" + self.canalString + ":PROB 1.0E1")
    
    def setScale(self, scale):
        self.osc.write(":" + self.canalString + ":SCAL " + str(scale))

    def getScale(self):
        return self.osc.query_ascii_values(":" + self.canalString + ":SCAL?")

    def setVoltUnit(self):
        self.osc.write(":" + self.canalString + ":UNITs VOLT")
    def setAmpereUnit(self):
        self.osc.write(":" + self.canalString + ":UNITs AMP")

    def setOffset(self, offset):
        self.osc.write(":" + self.canalString + ":OFFSet " + offset + " V")
    def readOffset(self):
        retrurn (self.osc.query_ascii_values(":" + self.canalString + "OFFS?"))[0]

    def setNOISErejectOn(self):
        print("Sorry, noise reject cannot be seted on")

    #QUICK MEAS

    def measFase(self, numberOfChannelReference):
        return (self.osc.query_ascii_values(":MEAS:PHAS? " + "CHAN" + str(numberOfChannelReference)+"," + self.canalString))[0]

    def measPk2Pk(self):
        return (self.osc.query_ascii_values(":MEAS:VPP? " + self.canalString))[0]

    def obtainActualScaleY(self):
        print("Sorry, obtainScaleY cannot be implemented")

    #ACQUIRE

    def setNaverages(self, n):
        self.osc.write(":ACQ:COUN " + str(n))

    def setHighResolution(self):
        self.osc.write("ACQ:TYPE HRES")
    def setNormal(self):
        self.osc.write("ACQ:TYPE NORM")
    def setAverage(self):
        self.osc.write("ACQ:TYPE AVER")
    def setPeakDetect(self):
        self.osc.write("ACQ:TYPE PEAK")
        
    #TIMEBASE

    def setRollMode(self):
        self.osc.write(":TIM:ROLL:MODE ROLL")

    def setTimeBasePosCero(self):
        self.osc.write(":TIM:POS 0")

    def setTimeScale(self, t):
        self.osc.write(":TIM:SCAL " + str(t))

    #TRIGGER

    def setTriggerCero(self):
        self.osc.write(":TRIG:LEVel 0")
    def setHFrejectOn(self):
        self.osc.write(":TRIG:HFReject 1")
    def setHFrejectOff(self):
        self.osc.write(":TRIG:HFReject 0")
    def setLFrejectOn(self):
        self.osc.write("TRIG:COUP LFReject")




class generator:
    def __init__(self,gen_res):
        self.gen= gen_res
        self.gen.write("OUTP:LOAD INF")
        self.gen.write("FUNC SIN")
        self.setOutputOff()

    def setVoltage(self,vol):
        self.gen.write("VOLT "+str(vol))
    def setOffset(self, value):
        self.gen.write("VOLT:OFFS "+str(value))
    def setFrequency(self, f):
        self.gen.write("FREQ "+str(f))
    def setOutputOff(self):
         self.gen.write("OUTP OFF")
    def setOutputOn(self):
         self.gen.write("OUTP ON")

