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




########MESSWERTE#######
#I_0 Messung:
I_0_cnts = 7041
I_0_FWHM = 5.83

#Alluminium Block:
al_cnts = np.array([6801, 6541, 6610])
al_FWHM = np.array([5.83, 5.93, 5.89])

#Block 2:
b2_cnts = np.array([5660, 5438])
b2_FWHM = np.array([5.82, 5.85])

#Block 3:
b3_cnts = np.array([233, 257, 248, 120, 123, 388])
b3_FWHM = np.array([5.87, 5.74, 6.64, 6.03, 5.80, 5.64])

#Block 4:
b4_cnts = np.array([1740, 1777, 1893, 5376, 268, 5349, 1110, 1003, 1286, 1358, 1299, 1642])
b4_FWHM = np.array([6.20, 5.99, 5.61, 5.87, 5.90, 5.79, 5.71,  5.51, 5.69, 5.79, 5.64, 5.75])

### Funktionen

def dufloat(cnts, FWHM):
	Amp = cnts * FWHM
	return ufloat(Amp, np.sqrt(Amp))

t_0 = 240
I_0 = dufloat(I_0_cnts , I_0_FWHM)

I_al_1 = dufloat(al_cnts[0] , al_FWHM[0]) # Gerade
I_al_2 = dufloat(al_cnts[1] , al_FWHM[1]) # Diagonale
I_al_3 = dufloat(al_cnts[2] , al_FWHM[2]) # Nebendiagonale

I_b2_1 = dufloat(b2_cnts[0] , b2_FWHM[0]) # Gerade
I_b2_2 = dufloat(b2_cnts[1] , b2_FWHM[1]) # Diagonale

I_b3_1 = dufloat(b3_cnts[0] , b3_FWHM[0]) # Gerade
I_b3_2 = dufloat(b3_cnts[1] , b3_FWHM[1]) # Gerade
I_b3_3 = dufloat(b3_cnts[2] , b3_FWHM[2]) # Gerade
I_b3_4 = dufloat(b3_cnts[3] , b3_FWHM[3]) # Diagonale
I_b3_5 = dufloat(b3_cnts[4] , b3_FWHM[4]) # Diagonale
I_b3_6 = dufloat(b3_cnts[5] , b3_FWHM[5]) # Nebendiagonale

I_b4_1  = dufloat(b4_cnts[0]  , b4_FWHM[0]) # Gerade
I_b4_2  = dufloat(b4_cnts[1]  , b4_FWHM[1]) # Gerade
I_b4_3  = dufloat(b4_cnts[2]  , b4_FWHM[2]) # Gerade
I_b4_4  = dufloat(b4_cnts[3]  , b4_FWHM[3]) # Gerade
I_b4_5  = dufloat(b4_cnts[4]  , b4_FWHM[4]) # Gerade
I_b4_6  = dufloat(b4_cnts[5]  , b4_FWHM[5]) # Gerade
I_b4_7  = dufloat(b4_cnts[6]  , b4_FWHM[6]) # Diagonale
I_b4_8  = dufloat(b4_cnts[7]  , b4_FWHM[7]) # Diagonale
I_b4_9  = dufloat(b4_cnts[8]  , b4_FWHM[8]) # Nebendiagonale
I_b4_10 = dufloat(b4_cnts[9]  , b4_FWHM[9]) # Nebendiagonale
I_b4_11 = dufloat(b4_cnts[10] , b4_FWHM[10]) # Nebendiagonale
I_b4_12 = dufloat(b4_cnts[11] , b4_FWHM[11]) # Nebendiagonale


w = np.sqrt(2)
a1 = np.array([(1,1,1,0,0,0,0,0,0),(0,0,0,1,1,1,0,0,0),(0,0,0,0,0,0,1,1,1)])
a2 = np.array([(1,0,0,1,0,0,1,0,0),(0,1,0,0,1,0,0,1,0),(0,0,1,0,0,1,0,0,1)])
a3 = np.array([(w,0,0,0,w,0,0,0,w),(0,0,w,0,w,0,w,0,0),(0,w,0,0,0,w,0,0,0)])
a4 = np.array([(0,0,0,w,0,0,0,w,0),(0,w,0,w,0,0,0,0,0),(0,0,0,0,0,w,0,w,0)])
A = np.vstack((a1,a2,a3,a4))

def mu(I_0,I,d):
	return unp.log(I_0/I) / d

mu_b2_1 = mu(I_al_1, I_b2_1 , 3)
print(mu_b2_1)

mu_b2_2 = mu(I_al_2, I_b2_2 , 3 * w)
print(mu_b2_2)





def rel_abw(theo,a):
    c = (theo - a)/theo
    print(f"Relative Abweichung in Prozent: {noms(c) * 100 :.4f} \pm {stds(c) * 100 :.5f}\n")


# ---------------------------------Nullmessung/Spektrum----------------------------------------------------------------------------------
pulses = np.genfromtxt('data/spektrum.txt', unpack=True)
x_axis = np.arange(len(pulses))

r_0 = np.sum(pulses)/t_0 #/per/sec
sig_0 = np.sqrt(np.sum(pulses))/t_0

R_0 = unp.uarray([r_0], [sig_0])

plt.figure()
plt.bar(x_axis, pulses)
plt.xlim(8,220)
plt.xlabel("Channel")
plt.ylabel("Anzahl der Ereignisse")
plt.grid()
plt.tight_layout()
plt.savefig('build/spektrum.pdf')





def mittel(a,b,c):
    if (np.size(a) != np.size(b) or np.size(b) != np.size(c)):
        print("NICHT ALLE WERTE EINGETRAGEN")
        if(np.size(a)>np.size(b)):
            print("FEHLER IN ARRAY  b)")
        else:
            if(np.size(b)>np.size(c)):
                print("FEHLER IN ARRAY  c)")
            else:
                print("FEHLER IN ARRAY  a)")
    arr = unp.uarray(np.zeros(np.size(a)),np.zeros(np.size(a)))
    for i in range(0,np.size(a)):
        arr[i] = unc.ufloat(np.mean([a[i], b[i], c[i]]), np.std([a[i], b[i], c[i]])/ np.sqrt(3))
    return arr



def printer(a,b,c,name):
    if(name == "leck"):
        table1 ={'Messreihe 1': a, 'Messreihe 2': b,  'Messreihe 3': c, 'gemittelte Messwerte': mittel(a, b, c)}
        print("\n", tabulate(table1, tablefmt = "latex_raw"))    
    else:
        table1 ={'Messreihe 1': a, 'Messreihe 2': b,  'Messreihe 3': c, 'gemittelte Messwerte': mittel(a, b, c), 'log': logstuff(err_mess(mittel(a, b, c)),0,np.size(a)-1)}
        print("\n", tabulate(table1, tablefmt = "latex_raw"))    











#############################Auswertung#####################################


print("########## AUSWERTUNG ###############\n\n")


###Tabellen

print("####### TABELLEN #########")

########Grafiken########

