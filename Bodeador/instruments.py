#instruments
import visa as v
import copy

class osciloscope:
<<<<<<< HEAD
    def __init__(self, direccion):
        self.rm.open_resource(direccion)
=======
    def __init__(self, osc_res):
        self.osc= osc_res
        self.osc.write(":TRIG:SWE AUTO")
        self.osc.write("TRIG:EDGE:COUP AC")
        self.canalString= "CHAN1"
>>>>>>> d988de27a0aa91909d12148c0c6a1f4ea29aa955

    #METODOS DE COMANDOS OSCILOSCOPIO

    #CHANNELS

    def changeChannel(self, numberOfChannel):
        self.canalString = "CHANnel " + numberOfChannel

    def setBWL(self):
        self.osc.write(":" + canalString + ":BWL")

    def setDCcoupling(self):
        self.osc.write(":" + canalString + ":COUP DC")

    def setACcoupling(self):
        self.osc.write(":" + canalString + ":COUP AC")

    def setProbeX1(self):
        self.osc.write(":" + canalString + ":PROB 1.0E1")
    def setProbeX10(self):
        self.osc.write(":" + canalString + ":PROB 1.0E2")
    
    def setScale(self, scale):
        self.osc.write(":" + canalString + ":SCAL " + scale)

    def getScale(self):
        return self.osc.query_ascii_values(":" + canalString + ":SCAL?")

    def setVoltUnit(self):
        self.osc.write(":" + canalString + ":UNITs VOLT")
    def setAmpereUnit(self):
        self.osc.write(":" + canalString + ":UNITs AMP")

    def setOffset(self, offset):
        self.osc.write(":" + canalString + ":OFFSet " + offset + " V")
    def readOffset(self):
        self.osc.query_ascii_values(":" + canalString + "OFFS?")

    #QUICK MEAS

    def measFase(self, numberOfChannelReference):
        return self.osc.query_ascii_values("MEAS:PHA? " + "CHANnel " + numberOfChannelReference + self.canalString)

    def measPk2Pk(self):
        return self.osc.query_ascii_values(":MEAS:VPP? " + self.canalString)

    #ACQUIRE

    def setNaverages(self, n):
        self.osc.write(":ACQ:COUN " + n)

    def setHighResolution(self):
        self.osc.write("ACQ:TYPE:HRES")
    def setNormal(self):
        self.osc.write("ACQ:TYPE:NORM")
    def setAverage(self):
        self.osc.write("ACQ:TYPE:AVER")
    def setPeakDetect(self):
        self.osc.write("ACQ:TYPE:PEAK")
        
    #TIMEBASE

    def setRollMode(self):
        self.osc.write(":TIM:ROLL:MODE ROLL")

    def setTimeBasePosCero(self):
        self.osc.write(":TIM:POS 0")

    def setTimeScale(self, t):
        self.osc.write(":TIM:SCAL " + t)

    #TRIGGER

    def setTriggerCero(self):
        self.osc.write(":TRIG[:EDGE]:LEVel 0")



class generator:
<<<<<<< HEAD
    def __init__(self):
        self.rm.open_resource(direccion)
=======
    def __init__(self,gen_res):
        self.gen= gen_res
        self.gen.write("OUTP:LOAD INF")
        self.gen.write("FUNC SIN")

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
>>>>>>> d988de27a0aa91909d12148c0c6a1f4ea29aa955

