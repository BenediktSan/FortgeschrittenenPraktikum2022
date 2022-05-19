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

##Dimensionen der Spulen:

#Sweep-Spule:
r_sweep = 16.39 * 0.01
n_sweep= 11

#Horizontalspule:
r_hor = 15.70 * 0.01
n_hor = 154

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

<<<<<<< HEAD
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


||||||| e3a7749
##Funktionen aufrufen:

B_1 = Helm(i_sweep_1) + 
=======
def gyro(m):
	gF = h / (m * mu_b)
	return gF

def spin(gF):
	I = 1/2 * (2.002/gF -1)
	return I

def Zeequad(gF , B , M , E):
	Z = (gF ** 2) * ( mu_b ** 2) * (B ** 2) * (1 - 2 * M) / E
	return Z

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

##Quadratischer Zeemaneffekt:

M_F_1 = -1
B_max_1 = 163e-6
Delta_E_1 = 4.54e-24
M_F_2 = -2
B_max_2 = 238e-6
Delta_E_2 = 2.01e-24

print('Für Isotop 1 ergibt der quadratische Zeemaneffekt: ', Zeequad( gF_1 , B_max_1 , M_F_1 , Delta_E_1))
print('Für Isotop 1 ergibt der lineare Zeemanneffekt: ', gF_1 * mu_b * B_max_1)
print('Für Isotop 2 ergibt der quadratische Zeemaneffekt: ', Zeequad( gF_2 , B_max_2 , M_F_2 , Delta_E_2))
print('Für Isotop 2 ergibt der lineare Zeemaneffekt: ', gF_2 * mu_b * B_max_2)


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

###Dikussion

B_Erd_v_Theo = 44e-6
I_1_Theo = 1.5
I_2_Theo = 2.5

print('Abweichung des Bestimmten Magnetfeldes: ', 1 - ( Helm( 0.23 , r_ver , n_ver)/ B_Erd_v_Theo))
print('Abweichung des Kernspins von Isotop 1: ', 1 - ki_1 / I_1_Theo)
print('Abweichung des Kernspins von Isotop 2: ', 1 - ki_2 / I_2_Theo)	
print('Abweichung des Anteils von Isotop 1: ', 1- 32.143/27.835)
print('Abweichung des Anteils von Isotop 2: ', 1- 67.857/72.835)
>>>>>>> 6991b1f9aa8a74b1c9f80a5155c7babe056fa33e
