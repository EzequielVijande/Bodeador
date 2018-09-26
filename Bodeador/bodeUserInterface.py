#bodeUserInterface
from userData import instrumentsData
from userData import measurementsData
from userData import preferenceData
import tkinter as tk 
from tkinter import ttk
from tkinter import *

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
X1 = 1
X10 = 2

class graphicalInterface:
    def __init__(self):
        #userData a completar
        self.measData = measurementsData()
        self.pData = preferenceData()

        #variables auxiliares vinculadas a los resources gráficos
        self.isMinScaleHz = True
        self.isMinScaleKHz = False
        self.fMin = 0

        self.isMaxScaleHz = True
        self.isMaxScaleKHz = False
        self.fMax = 0
        #graphicalResources
        self.raiz = Tk()
        self.raiz.geometry('960x580')

        self.raiz.resizable(width=True,height=True)
        self.raiz.title('Auto Bode Software')
        self.placeRadioButtons()
        self.placeButtons()
        self.placeCheckButtons()
        self.placeEntryText()
        self.placeSliders()
        self.placeComboBoxes()

        self.raiz.mainloop()
        

    def placeRadioButtons(self):
        self.scaleStartF = tk.IntVar()
        self.rButton_startF_Hz = tk.Radiobutton(self.raiz, text="Hz", 
            variable = self.scaleStartF, value = Hz, command = self.refreshFminScale).grid(row = 2, column = 3)
    
        self.rButton_startF_KHz = tk.Radiobutton(self.raiz, text="KHz", 
                            variable = self.scaleStartF, value = KHz, command = self.refreshFminScale).grid(row = 3, column = 3)

        self.scaleStopF = tk.IntVar()
        self.rButton_stopF_Hz = tk.Radiobutton(self.raiz, text="Hz", 
                                variable = self.scaleStopF, value = Hz, command = self.refreshFmaxScale).grid(row = 4, column = 3)
        self.rButton_stopF_KHz = tk.Radiobutton(self.raiz, text="KHz", 
                                variable = self.scaleStopF, value = KHz, command = self.refreshFmaxScale).grid(row = 5, column = 3)

        self.labelCoupling = tk.Label(self.raiz, text = "Coupling").grid(row = 3, column = 4)
        self.coupling = tk.IntVar()
        self.rButton_couplingAC = tk.Radiobutton(self.raiz, text="couple AC", 
                                variable = self.coupling, value = AC, command = self.refreshCoupling).grid(row =3, column = 5)
        self.rButton_couplingDC = tk.Radiobutton(self.raiz, text="couple DC", 
                                variable = self.coupling, value = DC, command = self.refreshCoupling).grid(row =4, column = 5)
        
        self.labelAcq = tk.Label(self.raiz, text = "Acquire").grid(row = 5, column = 4)
        self.acq = tk.IntVar()
        self.rButton_acqHRES = tk.Radiobutton(self.raiz, text="High Resolution", variable = self.acq, 
                                value = HRES, command = self.refreshAcqMode).grid(row =5, column = 5)
        self.rButton_acqNORM = tk.Radiobutton(self.raiz, text="Normal Resolution", variable = self.acq, 
                                value = NORM, command = self.refreshAcqMode).grid(row =6, column = 5)

        self.rButton_acqPEAK = tk.Radiobutton(self.raiz, text="Peak Detect", variable = self.acq, 
                            value = PEAK, command = self.refreshAcqMode).grid(row =7, column = 5)

        self.rButton_acqAVER = tk.Radiobutton(self.raiz, text="Average", variable = self.acq, 
                            value = AVER, command = self.refreshAcqMode).grid(row =8, column = 5)

        self.labelSweepMode = tk.Label(self.raiz, text = "Sweep Mode").grid(row = 1, column = 4)
        self.sweepType = tk.IntVar()
        self.rButton_sweepLog = tk.Radiobutton(self.raiz, text="Logarithmic sweep", 
                                variable = self.sweepType, value = LOG, command = self.refreshSweepType).grid(row =1, column = 5)
        self.rButton_sweepLinear = tk.Radiobutton(self.raiz, text="Linear sweep", 
                                variable = self.sweepType, value = LINEAR, command = self.refreshSweepType).grid(row =2, column = 5)

        self.labelProbe = tk.Label(self.raiz, text = "Probe").grid(row = 3, column = 6)
        self.probe = tk.IntVar()
        self.rButton_probeX1 = tk.Radiobutton(self.raiz, text = "X1", variable = self.probe, 
                                    value = X1, command = self.refreshProbe).grid(row = 4, column = 6)
        self.rButton_probeX10 = tk.Radiobutton(self.raiz, text = "X10", variable = self.probe, 
                                    value = X10, command = self.refreshProbe).grid(row = 5, column = 6)
        

    def refreshFminScale(self):
        aux = self.scaleStartF.get()
        if aux == Hz:
            self.isMinScaleHz = True
            self.isMinScaleKHz = False
        elif aux == KHz:
            self.isMinScaleHz = False
            self.isMinScaleKHz = True
        self.setFinalfMin

    def setFinalfMin(self):
        if self.isMinScaleHz:
            self.measData.fMin = self.fMin

        elif self.isMinScaleKHz:
            self.measData.fMin = (self.fMin * 1000)

    def refreshFmaxScale(self):
        aux = self.scaleStopF.get()
        if aux == Hz:
            self.isMaxScaleHz = True
            self.isMaxScaleKHz = False
        elif aux == KHz:
            self.isMaxScaleHz = False
            self.isMaxScaleKHz = True
            
        self.setFinalfMax

    def setFinalfMax(self):
        if self.isMaxScaleHz:
            self.measData.fMax = self.fMax
        elif self.isMaxScaleKHz:
            self.measData.fMax = (self.fMax * 1000)

    def refreshCoupling(self):
        aux = self.coupling.get()
        if aux == AC:
            self.measData.ACcouple = True
            self.measData.DCcouple = False

        elif aux == DC:
            self.measData.ACcouple = False
            self.measData.DCcouple = True


    def refreshAcqMode(self):
        aux = self.acq.get()
        if aux == HRES:
            self.measData.acqHRES = True
            self.measData.acqAVER = False
            self.measData.acqNORM = False
            self.measData.acqPEAK = False

        elif aux == AVER:
            self.measData.acqHRES = False
            self.measData.acqAVER = True
            self.measData.acqNORM = False
            self.measData.acqPEAK = False

        elif aux == NORM:
            self.measData.acqHRES = False
            self.measData.acqAVER = False
            self.measData.acqNORM = True
            self.measData.acqPEAK = False

        elif aux == PEAK:
            self.measData.acqHRES = False
            self.measData.acqAVER = False
            self.measData.acqNORM = False
            self.measData.acqPEAK = True


    def refreshSweepType(self):
        aux = self.sweepType.get()
        if aux == LOG:
            self.measData.isRangeLog = True
            self.measData.isRangeLinear = False
        elif aux == LINEAR:
            self.measData.isRangeLog = False
            self.measData.isRangeLinear = True

    def refreshProbe(self):
        aux = self.probe.get()
        if aux == X1:
            self.measData.probeX1 = True
            self.measData.probeX10 = False

        elif aux == X10:
            self.measData.probeX1 = False
            self.measData.probeX10 = True


    def placeButtons(self):
        self.botonGoBode = tk.Button(self.raiz, text="Go Bode", command=self.goBode_button).grid(row = 14, column = 4)
        self.botonQuitProgram = tk.Button(self.raiz, text = "Quit", command=self.quitProgram_button).grid(row = 14, column = 5)

    def goBode_button(self):
        
        self.refreshTime2Establish() #se obtiene el valor de un combobox ya que dicho combobox no puede
                                    #obtener su valor por si solo
        self.setExcelName()  #se lee un textmessage
        self.pData.userWantContinue = True
        self.raiz.destroy()

    def quitProgram_button(self):
        self.pData.userWantContinue = False
        self.raiz.destroy()
    
    def placeCheckButtons(self):
        self.labelPreferences = tk.Label(self.raiz, text = "Other Preferences").grid(row = 9, column = 4)
        self.bool_excel = tk.BooleanVar()
        self.excel_checkButton = tk.Checkbutton(self.raiz, text="Create Excel with measures", 
                                                                    variable=self.bool_excel, command = self.refreshExcelPreference).grid(row = 10, column = 5)
        self.bool_graphMag = tk.BooleanVar()
        self.graphMag_checkButton = tk.Checkbutton(self.raiz, text="Graph magnitude diagram", 
                                                                variable=self.bool_graphMag, command = self.refreshGraphMagPreference).grid(row = 9, column = 5)
        self.bool_graphFase = tk.BooleanVar()
        self.graphFase_checkButton = tk.Checkbutton(self.raiz, text="Graph phase diagram", 
                                                                        variable=self.bool_graphFase, command = self.refreshGraphFasePreference).grid(row = 9, column = 6)

    def refreshExcelPreference(self):
        self.pData.userWantExcel = self.bool_excel.get()

    def refreshGraphMagPreference(self):
        self.pData.userWantGraphMag = self.bool_graphMag.get()

    def refreshGraphFasePreference(self):
        self.pData.userWantGraphFase = self.bool_graphFase.get()

    def placeEntryText(self):
        self.excelName = tk.StringVar()
        self.nombreExcel_tk = tk.Entry(self.raiz, textvariable = self.excelName).grid(row = 10, column = 6)

    def setExcelName(self):
        self.pData.excelName = self.excelName.get()

    def placeSliders(self):

        self.label_freqTitle = tk.Label(self.raiz, text = "Frequency").grid(row = 1, column = 1)
        self.label_startF = tk.Label(self.raiz, text = "Start Frequency").grid(row = 2, column = 1)
        self.slide_fmin = tk.IntVar()
        self.startF_slider = tk.Scale(self.raiz, from_=0, to=5000, length = 200, orient=HORIZONTAL, 
                    variable = self.slide_fmin, command=self.refreshStartF_slider).grid(row = 2, column = 2)
    
        
        self.label_stopF = tk.Label(self.raiz, text = "Stop Frequency").grid(row = 4, column = 1)
        self.slide_fmax = tk.IntVar()
        self.stopF_slider = tk.Scale(self.raiz, from_=0, to=5000, length =200, orient=HORIZONTAL, 
                    variable = self.slide_fmax, command=self.refreshStopF_slider).grid(row = 4, column = 2)
        
        self.label_inputTitle = tk.Label(self.raiz, text = "Input Signal").grid(row = 6, column = 1)
        self.slide_vin = tk.IntVar()
        self.slide_mvin = tk.IntVar()
        self.label_Vin = tk.Label(self.raiz, text = "High Input(Vpp)").grid(row = 7, column = 1)
        self.Vin_slider = tk.Scale(self.raiz, from_=0.0, to=20.0, length = 100, orient=HORIZONTAL, 
                        variable = self.slide_vin, command=self.refreshVin_slider).grid(row = 7, column = 2)
        self.label_mVin = tk.Label(self.raiz, text = "Low Input Signal (mVpp)").grid(row = 8, column = 1)
        self.mVin_slider = tk.Scale(self.raiz, from_=0.0, to=1000.0, length = 100, orient=HORIZONTAL, 
                                variable = self.slide_mvin, command=self.refreshVin_slider).grid(row = 8, column = 2)
        self.slide_mvoffset = tk.IntVar()
        self.slide_voffset = tk.IntVar()
        self.label_Voffset = tk.Label(self.raiz, text = "High Offset Signal (Vpp)").grid(row = 9, column = 1)
        self.Voffset_slider = tk.Scale(self.raiz, from_=-10, to=10, length = 100, orient=HORIZONTAL, 
                            variable = self.slide_voffset, command=self.refreshVoffset_slider).grid(row = 9, column = 2)

        self.label_mVoffset = tk.Label(self.raiz, text = "Low Offset Signal (mVpp)").grid(row = 10, column = 1)
        self.mVin_slider = tk.Scale(self.raiz, from_=-1000, to=1000, length = 100, orient=HORIZONTAL, 
                                variable = self.slide_mvoffset, command=self.refreshVoffset_slider).grid(row = 10, column = 2)
        
        self.slide_npoints = tk.IntVar()
        self.label_Npoints = tk.Label(self.raiz, text = "Number of Points to Meas").grid(row = 13, column = 1)
        self.nPoints_slider = tk.Scale(self.raiz, from_=0, to=400, length = 100, orient=HORIZONTAL, 
                                        variable = self.slide_npoints, command=self.refreshNpoints_slider).grid(row = 13, column = 2)

    def refreshStartF_slider(self, event):
        self.fMin = self.slide_fmin.get()
        self.setFinalfMin()

    def refreshStopF_slider(self, event):
        self.fMax = self.slide_fmax.get()
        self.setFinalfMax()

    def refreshVin_slider(self, event):
        self.measData.Vin = self.slide_vin.get() + (self.slide_mvin.get() / 1000)

    def refreshVoffset_slider(self, event):
        self.measData.Voffset = self.slide_voffset.get() + (self.slide_mvoffset.get() / 1000)

    def refreshNpoints_slider(self, event):
        self.measData.numberOfPoints = self.slide_npoints.get()

    
        
    def placeComboBoxes(self):
        self.labelTime2Establish = tk.Label(self.raiz, text = "Time to Establishment (seg)").grid(row = 11, column = 1)
        self.comboTime2Establish = ttk.Combobox(self.raiz)
        self.comboTime2Establish["values"] = ['auto', '0.5', '1', '1.5', '2', '2.5', '3', '4', '5', '10', '15', '20'] #tiempo en segundos
        self.comboTime2Establish.current(2)
        self.comboTime2Establish.grid(row = 11, column = 2)

    def refreshTime2Establish(self):
        if self.comboTime2Establish.get() == 'auto':
            self.measData.autoEstablish = True
        else:
            self.measData.establish = float(self.comboTime2Establish.get())
            self.measData.autoEstablish = False
        
        
    









        



