#bodeUserInterface
from userData import instrumentsData
from userData import measurementsData
import tkinter as tk 

Hz = 1
KHz = 2
AC = 1
DC = 2
HRES = 1
NORM = 2
PEAK = 3
AVER = 4
LOG = 1
LINEAR = 2

class graphicalInterface:
    def __ini__(self):
        #userData
        self.instData = instrumentsData()
        self.measData = measurementsData()
        #graphicalResources
        self.raiz = Tk()
        self.raiz.geometry('800x680')

        self.raiz.resizable(width=True,height=True)
        self.raiz.title('Auto Bode Software')
        self.placeRadioButtons()
        self.placeButtons()
        self.placeCheckButtons()
        self.placeEntryText()
        self.placeSliders()
        

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
        self.raiz.mainloop()

    def placeRadioButtons(self):
        self.TKvarStartF = tk.StringVar()
        self.rButton_startF_Hz = tk.Radiobutton(text="Unit - Hz", 
                                variable = self.TKvarStarF, value = Hz, command = self.refreshSliderStartF)
        self.rButton_startF_KHz = tk.Radiobutton(text="Unit - KHz", 
                                variable = self.TKvarStarF, value = KHz, command = self.refreshSliderStartF)

        self.TKvarStopF = tk.StringVar()
        self.rButton_stopF_Hz = tk.Radiobutton(text="Unit - Hz", 
                                variable = self.TKvarStopF, value = Hz, command = self.refreshSliderStopF)
        self.rButton_stopF_KHz = tk.Radiobutton(text="Unit - KHz", 
                                variable = self.TKvarStopF, value = KHz, command = self.refreshSliderStopF)

        self.TKvarCoupling = tk.StringVar()
        self.rButton_couplingAC = tk.Radiobutton(text="couple AC", 
                                variable = self.TKvarCoupling, value = AC, command = self.refreshCouplingMode)
        self.rButton_couplingDC = tk.Radiobutton(text="couple DC", 
                                variable = self.TKvarCoupling, value = DC, command = self.refreshCouplingMode)

        self.TKvarAcq = tk.StringVar()
        self.rButton_acqHRES = tk.Radiobutton(text="High Resolution", 
                                variable = self.TKvarAcq, value = HRES, command = self.refreshAcqMode)
        self.rButton_acqNORM = tk.Radiobutton(text="Normal Resolution", 
                                variable = self.TKvarAcq, value = NORM, command = self.refreshAcqMode)

        self.rButton_acqPEAK = tk.Radiobutton(text="Peak Detect", 
                                variable = self.TKvarAcq, value = PEAK, command = self.refreshAcqMode)

        self.rButton_acqAVER = tk.Radiobutton(text="Average", 
                                variable = self.TKvarAcq, value = AVER, command = self.refreshAcqMode)

        self.TKvarSweepType
        self.rButton_sweepLog = tk.Radiobutton(text="Logarithmic sweep", 
                                variable = self.TKvarSweepType, value = LOG, command = self.refreshSweepType)
        self.rButton_sweepLinear = tk.Radiobutton(text="Linear sweep", 
                                variable = self.TKvarSweepType, value = LINEAR, command = self.refreshSweepType)
        



    def refreshSliderStartF(self):


    def refreshSliderStopF(self):

    def refreshCouplingMode(self):

    def refreshAcqMode(self):

    def refreshSweepType(self):

    def placeButtons(self):
        self.botonGoBode = tk.Button(raiz, text="Go Bode", command=self.goBode_button)
        self.botonQuitProgram = tk.Button(self.raiz, text = "Quit", command=self.quitProgram_button)

    def goBode_button(self):

    def quitProgram_button(self):
    
    def placeCheckButtons(self):
        self.bool_excel = tk.BooleanVar()
        self.excel_checkButton = tk.Checkbutton(root, text="Create Excel with measures", 
                                                                    variable=self.bool_excel)
        self.bool_graphMag = tk.BooleanVar()
        self.graphMag_checkButton = tk.Checkbutton(root, text="Graph magnitude diagram", 
                                                                variable=self.bool_grahpMag)
        self.bool_graphFase = tk.BooleanVar()
        self.graphFase_checkButton = tk.Checkbutton(root, text="Graph phase diagram", 
                                                                        variable=self.bool_grahpFase)

    def placeEntryText(self):
        self.nombreExcel_tk = tk.Entry(self.raiz)

    def placeSliders(self):
        self.startF_slider = Scale(self.raiz, from_=0, to=5000, tickinterval=100, orient=HORIZONTAL, 
                                                        command=self.refreshStartF_slider)
        self.stopF_slider = Scale(self.raiz, from_=0, to=5000, tickinterval=100, orient=HORIZONTAL, 
                                                        command=self.refreshStartF_slider)

    def refreshStartF_slider(self):
        
    









        



