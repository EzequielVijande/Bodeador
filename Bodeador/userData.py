#userData
class instrumentsData:
    def __init__(self):
        self.oscIndex = 0
        self.genIndex = 0

class measurementsData:
    def __init__(self):
        self.numberOfPoints = 0
        self.freqRange = []
        self.HFrejectOn = False
        self.LFrejectOn = False
        self.establish = 0
        self.acqHRES = False
        self.acqNORM = False
        self.acqPEAK = False
        self.acqAVER = False
        self.nAverages = 0

