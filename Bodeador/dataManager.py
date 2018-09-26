#datosManager

import pandas as pd
from pandas import ExcelWriter
import numpy as np
import matplotlib.pyplot as plt
from mpldatacursor import datacursor


class dataManager:

    def __init__ (self):
        self.rutaExcel = 'rtaFrecuencia.xlsx'
        self.frecuencias = 0
        self.mag = 0
        self.fase = 0

    def writeExcel(self):
        df = pd.DataFrame({'f': self.frecuencias,
                   'mag': self.mag,
                   'fase': self.fase})
        df = df[['f', 'mag', 'fase']]
        writer = ExcelWriter(self.rutaExcel)
        df.to_excel(writer, 'Hoja de datos', index=False)
        writer.save()

    def setMag(self, mag):
        self.mag = mag

    def calculateMag(self, vin, vout):
        self.mag = 20*np.log10(np.asarray(vout)/np.asarray(vin))

    def setFase(self, fase):
        self.fase = np.asarray(fase)

    def setFreq(self, freq):
        self.frecuencias = freq

    def graphBodeMag(self):
        plt.figure(1)
        plt.semilogx(self.frecuencias, self.mag)
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Magnitud (dB)")
        plt.title("Diagrama de Bode - Magnitud")
        datacursor(display = 'multiple', draggable = True)
       
    def graphBodeFase(self):
        plt.figure(2)
        plt.semilogx(self.frecuencias, self.fase)
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Fase (grados)")
        plt.title("Diagrama de Bode - Fase")
        datacursor(display = 'multiple', draggable = True)
        

    def setRutaExcel(self, ruta):
        self.rutaExcel = ruta

    def show(self):
        plt.show()

