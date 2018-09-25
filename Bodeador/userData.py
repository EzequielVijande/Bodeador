#userData
class instrumentsData:
    def __init__(self,o_index,g_index):
        self.oscIndex = o_index
        self.genIndex = g_index

class measurementsData:
    def __init__(self):
        self.isRangeLinear = False
        self.isRangeLog = True

        self.numberOfPoints = 20
        self.fMin = 0 #Hz
        self.fMax = 0 #Hz

        self.Vin = 1 #Volts
        self.Voffset = 0 #Volts

        self.HFrejectOn = False
        self.LFrejectOn = False

        self.establish = 1 #segundos

        self.acqHRES = True
        self.acqNORM = False
        self.acqPEAK = False
        self.acqAVER = False
        self.nAverages = 2

        self.probeX10 = False
        self.probeX1 = True

        self.ACcouple = False
        self.DCcouple = True

