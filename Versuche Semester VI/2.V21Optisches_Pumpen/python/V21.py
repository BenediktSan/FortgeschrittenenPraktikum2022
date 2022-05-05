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

##Dimensionen der Spulen
#Sweep-Spule:
r_sweep = 16.39 * 0.01 
n_sweep = 11

#horizontal-Spule
r_hor = 15.79 * 0.01
n_hor = 154	

#vertikal-Spule
r_ver = 11.735 * 0.01
n_ver = 20

##Konstanten einlesen
mu = const.mu_0
h  = const.h
mu_b, ___ , ___ = const.physical_constants["Bohr magneton"]  

##Isotopenverhältnis:
P_1 = 9
P_2 = 19
P_ges = P_1 + P_2
print('Das Gemisch besteht zu :' ,P_1 / P_ges * 100 ,'% aus Isotop 1')
print('Das Gemisch besteht zu :' ,P_2 / P_ges * 100 ,'% aus Isotop 2')

##Funktionen definieren:

def Helm( I , R , N):
	B = mu * ( 8 * I * N) / (np.sqrt(125) * R)
	return B

def gyro(m):
	gF = h / (m * mu_b)
	return gF

def spin(gF):
	I = 1/2 * (2.002/gF -1)
	return I

###Funktionen aufrufen:

B_1 = Helm(i_sweep_1 , r_sweep, n_sweep) + Helm(i_hor_1, r_hor, n_hor)
B_2 = Helm(i_sweep_2 , r_sweep, n_sweep) + Helm(i_hor_2, r_hor, n_hor)
print('Die Magnetfeldstärken von Isotop 1: ', B_1)
print('Die Magnetfeldstärken von Isotop 2: ', B_2)
print('Die Magnetfeldstärke in Vertikalrichtung beträgt: ' , Helm( 0.23 , r_ver , n_ver))

##Fitten:

p_arr_1 , cov_1 = np.polyfit(freq, B_1, deg=1, cov=True)
#print(p_arr_1)
error_1 = np.sqrt(np.diag(cov_1))
m_1 = ufloat(p_arr_1[0],error_1[0])
b_1 = ufloat(p_arr_1[1],error_1[1])
print("Steigung des Megnetfeldes von Isotop 1:",m_1)
print("Achsenabschnit des Megnetfeldes von Isotop 1:",b_1)
#print(error_1)
p_arr_2 , cov_2 = np.polyfit(freq, B_2, deg=1, cov=True)
error_2 = np.sqrt(np.diag(cov_2))
m_2 = ufloat(p_arr_2[0], error_2[0])
b_2 = ufloat(p_arr_2[1], error_2[1])
print("Steigung des Magnetfeldes von Isotop 2:", m_2)
print("Achsenabschnit des Magnetfeldes von Isotop 2:", b_2)

print('###')
##gyromagnetischer Faktor:

gF_1 = gyro(m_1)
print('Der gyromagnetische Faktor von Isotop 1: ', gF_1)
gF_2 = gyro(m_2)
print('Der gyromagnetische Faktor von Isotop 2: ', gF_2)

##Kernspin:

ki_1 = spin(gF_1)
print('Der Kernspin von Isotop 1: ', ki_1)
ki_2 = spin(gF_2)
print('Der Kernspin von Isotop 2: ', ki_2)


##Plotten:
#Linspace:
x_freq = np.linspace(0, 1, 1000)
#Peak magnetfleder
plt.figure()
plt.plot(freq*1e-6, B_1*1e6, 'r+', label='Isotop 1')
plt.plot(x_freq, (x_freq * 1e6 * p_arr_1[0] + p_arr_1[1])*1e6,'r-' , label='Fit zu Isotop 1')
plt.plot(freq*1e-6, B_2*1e6, 'g+', label='Isotop 2')
plt.plot(x_freq, (x_freq * 1e6 * p_arr_2[0] + p_arr_2[1])*1e6, 'g-' , label='Fit zu Isotop 2')
plt.xlabel('Frequenz der RF-Spule /  MHz')
plt.ylabel(r"Horizontalkomponente von B / $\mu T$")
plt.legend()
plt.savefig('build/Magnetfeld.png')

 
