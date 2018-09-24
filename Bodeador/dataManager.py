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
        self.mag = 20*np.log10(vout/vin)

    def setFase(self, fase):
        self.fase = fase

    def setFreq(self, freq):
        self.frecuencias = freq

    def graphBodeMag(self):
        plt.semilogx(self.f, self.mag)
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Magnitud (dB)")
        plt.title("Diagrama de Bode - Magnitud")
        datacursos(display = 'multiple', draggable = True)

    def graphBodeFase(self):
        plt.semilogx(self.f, self.fase)
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Fase (grados)")
        plt.title("Diagrama de Bode - Fase")
        datacursos(display = 'multiple', draggable = True)

    def setRutaExcel(self, ruta):
        self.rutaExcel = ruta

