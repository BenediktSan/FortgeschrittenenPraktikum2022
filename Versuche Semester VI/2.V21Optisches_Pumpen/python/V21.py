import numpy as np
import matplotlib.pyplot as plt
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy
import os
from tabulate import tabulate
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)


if os.path.exists("build") == False:
    os.mkdir("build")
if os.path.exists("build/plots") == False:
       os.mkdir("build/plots")

## Read in the measurements

#Fequenzen der RF Spule in Hz:
freq = np.array([1,2,3,4,5,6,7,8,9,10]) * 1e5

#Stromstärken der Sweep-Spule in A:
i_sweep_1 = np.array([6.82,4.75,7.1,2.37,2.1,2.65,2.4,4.05,2.45,3.85]) * 0.1
i_sweep_2 = np.array([7.95,7.1,10.6,7.15,8.05,9.7,10.65,8.87,6.87,7.5]) * 0.1

#Stromstärke der Horizontal-Spule in A:
i_hor_1 = np.array([0,0.02,0.02,0.07,0.09,0.1,0.12,0.13,0.15,0.16])
i_hor_2 = np.array([0,0.02,0.02,0.07,0.09,0.1,0.12,0.16,0.2,0.22])

#Peak tiefen:
p_1 = np.array([9,10.5,9.5,9,10])
p_2 = np.array([19,21.5,19,19,20])

#Ver


##Dimensionen der Spulen:

#Sweep-Spule:
r_sweep = 16.39 * 0.01
n_sweep= 11

#Horizontalspule:
r_hor = 15.70 * 0.01
n_hor = 154

##Konstanten einlesen
mu = const.mu_0




##Funktionen definieren:

def Helm( I , R , N):
	B = mu * ( 8 * I * N) / (np.sqrt(125) * R)
	return B

##Funktionen aufrufen:

B_1 = Helm(i_sweep_1, r_sweep, n_sweep) +  Helm(i_hor_1, r_hor, n_hor)
B_2 = Helm(i_sweep_2, r_sweep, n_sweep) +  Helm(i_hor_2, r_hor, n_hor)


#Plotten:
plt.figure()
plt.plot(freq, B_1, 'o', label = 'Isotop 1')
plt.plot(freq, B_2, '+', label = 'Isotop 2')
plt.legend()
plt.xlabel('Frequenzen der RF Spule')
plt.ylabel('Magnetfeldstärke in den Peaks')
plt.savefig('Magnetfeld.png')


