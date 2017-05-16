import os
import pandas as pd
import numpy as np
from Fourier.Fourier import fourierExtrapolation
import pylab as pl

print('\n***********************************\n')
print('Predictive Analysis: Standard Linear Regression\n')
def LR():
    os.chdir('LinearRegression')
    exec(open("LR.py").read())
LR()
print('\n***********************************\n')

print('Predictive Analysis: Fourier Extrapolation\n')
def Fourier():
    os.chdir('../Fourier')
    exec(open("Fourier.py").read())
Fourier()
print('\n***********************************\n')

# print('Predictive Analysis: Wavelet Extrapolation\n')
# def Wavelet():
#     os.chdir('../Wavelet')
#     exec(open("Wavelet.py").read())
# Wavelet()
# print('\n***********************************\n')

# print('Predictive Analysis: Chaotic System\n')
# def Chaotic():
#     os.chdir('../Chaotic')
#     exec(open("Chaotic.py").read())
# Chaotic()
# print('\n***********************************\n')

print('Predictive Analysis: Deep Learning: Linear Regression\n')
def NeuralNetLR():
    os.chdir('../NeuralNetRegression')
    exec(open("LR.py").read())
NeuralNetLR()
print('\n***********************************\n')

# print('Predictive Analysis: Deep Learning: TBD\n')
# def DeeperNN():
#     os.chdir('../DeeperNN')
#     exec(open("NN.py").read())
# DeeperNN()
# print('\n***********************************\n')

