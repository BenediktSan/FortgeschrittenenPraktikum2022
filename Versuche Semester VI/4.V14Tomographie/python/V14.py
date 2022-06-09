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

#Alluminium Hülle (Block 1):
#al_cnts = np.array([6801, 6541, 6610])
#al_FWHM = np.array([5.83, 5.93, 5.89])

#N_al = unp.uarray([37402, 36357,37957],[274,285,268])
N_al_1 = 37402
N_al_2 = 36357
N_al_3 = 37957

#Block 2:
#b2_cnts = np.array([5660, 5438])
#b2_FWHM = np.array([5.82, 5.85])
N_b2_1 = 30323
N_b2_2 = 29521
#Block 3:
#b3_cnts = np.array([233, 257, 248, 120, 123, 388])
#b3_FWHM = np.array([5.87, 5.74, 6.64, 6.03, 5.80, 5.64])
N_b3_1 = 1330
N_b3_2 = 1375
N_b3_3 = 1366
N_b3_4 = 614
N_b3_5 = 568
N_b3_6 = 2258
#Block 4:
#b4_cnts = np.array([1740, 1777, 1893, 5376, 268, 5349, 1110, 1003, 1286, 1358, 1299, 1642])
#b4_FWHM = np.array([6.20, 5.99, 5.61, 5.87, 5.90, 5.79, 5.71,  5.51, 5.69, 5.79, 5.64, 5.75])
N_b4_1 = 10972
N_b4_2 = 11123
N_b4_3 = 10915
N_b4_4 = 29942
N_b4_5 = 1475
N_b4_6 = 29503
N_b4_7 = 6745
N_b4_8 = 5814
N_b4_9 = 7040
N_b4_10 = 7959
N_b4_11 = 7281
N_b4_12 = 9338
### Funktionen

def dufloat(cnts, FWHM):
	Amp = cnts * FWHM
	return ufloat(Amp, np.sqrt(Amp))

def dufloat2(N):
	return ufloat(N, np.sqrt(N))

t_0 = 240
I_0 = dufloat(I_0_cnts , I_0_FWHM)

### Amplitude mit Aluminium Hülle, mit Unsicherheiten in Ufloat:  (Erst mit der dem Produkt aus Peakhöhe und FWHM, dann mit NetArea)
#I_al_1 = dufloat(al_cnts[0] , al_FWHM[0]) # Gerade
#I_al_2 = dufloat(al_cnts[1] , al_FWHM[1]) # Diagonale
#I_al_3 = dufloat(al_cnts[2] , al_FWHM[2]) # Nebendiagonale
I_al_1 = dufloat2(N_al_1) # Gerade
print("I_al Gerade:", I_al_1)
I_al_2 = dufloat2(N_al_2) # Diagonale
print("I_al Diagonale:", I_al_2)
I_al_3 = dufloat2(N_al_3) # Nebendiagonale
print("I_al Nebendiagonale: ",I_al_3)

### Amplitude mit Block 2, mit Unsicherheiten in Ufloat:
#I_b2_1 = dufloat(b2_cnts[0] , b2_FWHM[0]) # Gerade
#I_b2_2 = dufloat(b2_cnts[1] , b2_FWHM[1]) # Diagonale
I_b2_1 = dufloat2(N_b2_1) # Gerade
I_b2_2 = dufloat2(N_b2_2) # Diagonale
I_b2 = (I_b2_1 + I_b2_2)/2
#print("Mittelwert I_b2: ", I_b2)

### Amplitude mit Block 3, mit Unsicherheiten in Ufloat:
#I_b3_1 = dufloat(b3_cnts[0] , b3_FWHM[0]) # Gerade
#I_b3_2 = dufloat(b3_cnts[1] , b3_FWHM[1]) # Gerade
#I_b3_3 = dufloat(b3_cnts[2] , b3_FWHM[2]) # Gerade
#I_b3_4 = dufloat(b3_cnts[3] , b3_FWHM[3]) # Diagonale
#I_b3_5 = dufloat(b3_cnts[4] , b3_FWHM[4]) # Diagonale
#I_b3_6 = dufloat(b3_cnts[5] , b3_FWHM[5]) # Nebendiagonale

I_b3_1 = dufloat2(N_b3_1) # Gerade
I_b3_2 = dufloat2(N_b3_2) # Gerade
I_b3_3 = dufloat2(N_b3_3) # Gerade
I_b3_4 = dufloat2(N_b3_4) # Gerade
I_b3_5 = dufloat2(N_b3_5) # Diagonale
I_b3_6 = dufloat2(N_b3_6) # Nebendiagonale

### Amplitude mit Block 4, mit Unsicherheiten in Ufloat: 

#I_b4_1  = dufloat(b4_cnts[0]  , b4_FWHM[0]) # Gerade
#I_b4_2  = dufloat(b4_cnts[1]  , b4_FWHM[1]) # Gerade
#I_b4_3  = dufloat(b4_cnts[2]  , b4_FWHM[2]) # Gerade
#I_b4_4  = dufloat(b4_cnts[3]  , b4_FWHM[3]) # Gerade
#I_b4_5  = dufloat(b4_cnts[4]  , b4_FWHM[4]) # Gerade
#I_b4_6  = dufloat(b4_cnts[5]  , b4_FWHM[5]) # Gerade
#I_b4_7  = dufloat(b4_cnts[6]  , b4_FWHM[6]) # Diagonale
#I_b4_8  = dufloat(b4_cnts[7]  , b4_FWHM[7]) # Diagonale
#I_b4_9  = dufloat(b4_cnts[8]  , b4_FWHM[8]) # Nebendiagonale
#I_b4_10 = dufloat(b4_cnts[9]  , b4_FWHM[9]) # Nebendiagonale
#I_b4_11 = dufloat(b4_cnts[10] , b4_FWHM[10]) # Nebendiagonale
#I_b4_12 = dufloat(b4_cnts[11] , b4_FWHM[11]) # Nebendiagonale

I_b4_1  = dufloat2(N_b4_1) # Gerade
I_b4_2  = dufloat2(N_b4_2) # Gerade
I_b4_3  = dufloat2(N_b4_3) # Gerade
I_b4_4  = dufloat2(N_b4_4) # Gerade
I_b4_5  = dufloat2(N_b4_5) # Gerade
I_b4_6  = dufloat2(N_b4_6) # Gerade
I_b4_7  = dufloat2(N_b4_7) # Diagonale
I_b4_8  = dufloat2(N_b4_8) # Diagonale
I_b4_9  = dufloat2(N_b4_9) # Nebendiagonale
I_b4_10 = dufloat2(N_b4_10) # Nebendiagonale
I_b4_11 = dufloat2(N_b4_11) # Nebendiagonale
I_b4_12 = dufloat2(N_b4_12) # Nebendiagonale

#Daten von Würfel 4 mit Unsicherheiten an Vekot übergeben:
I_b4 = np.array([I_b4_1, I_b4_2, I_b4_3, I_b4_4, I_b4_5, I_b4_6, I_b4_7, I_b4_8, I_b4_9, I_b4_10, I_b4_11, I_b4_12])

#Daten von Würfel 4 ohne Unsicherheiten an Vektor übergeben:
#I_b4 = np.array([I_b4_1.n, I_b4_2.n, I_b4_3.n, I_b4_4.n, I_b4_5.n, I_b4_6.n, I_b4_7.n, I_b4_8.n, I_b4_9.n, I_b4_10.n, I_b4_11.n, I_b4_12.n])

#Skaliten des Intensitäten Vektors mit Unsicherheiten: 
for i in range(0,6):
	I_b4[i] = unp.log(I_al_1/ I_b4[i] )
for i in range(5,8):
	I_b4[i] = unp.log(I_al_1/ I_b4[i] )
for i in range(8,12):
	I_b4[i] = unp.log(I_al_1/ I_b4[i] )

#Skalieren des Intensitäten Vektors ohne Unsicherheiten:
#for i in range(0,6):
#	I_b4[i] = np.log(I_al_1.n / I_b4[i] )
#for i in range(5,8):
#	I_b4[i] = np.log(I_al_2.n / I_b4[i] )
#for i in range(8,12):
#	I_b4[i] = np.log(I_al_3.n / I_b4[i] )
print(I_b4)

### Unsere Projektionsmatrix:
w = np.sqrt(2)
a1 = np.array([(1,1,1,0,0,0,0,0,0),(0,0,0,1,1,1,0,0,0),(0,0,0,0,0,0,1,1,1)])
a2 = np.array([(1,0,0,1,0,0,1,0,0),(0,1,0,0,1,0,0,1,0),(0,0,1,0,0,1,0,0,1)])
a3 = np.array([(w,0,0,0,w,0,0,0,w),(0,0,w,0,w,0,w,0,0),(0,w,0,0,0,w,0,0,0)])
a4 = np.array([(0,0,0,w,0,0,0,w,0),(0,w,0,w,0,0,0,0,0),(0,0,0,0,0,w,0,w,0)])
A1 = np.vstack((a1,a2,a3,a4))

### Projektionsmatrix von Jana:
a1 = np.array([(0,w,0,w,0,0,0,0,0),(0,0,w,0,w,0,w,0,0),(0,0,0,0,0,w,0,w,0)])
a2 = np.array([(1,1,1,0,0,0,0,0,0),(0,0,0,1,1,1,0,0,0),(0,0,0,0,0,0,1,1,1)])
a3 = np.array([(0,w,0,0,0,w,0,0,0),(w,0,0,0,w,0,0,0,w),(0,0,0,w,0,0,0,w,0)])
a4 = np.array([(0,0,1,0,0,1,0,0,1),(0,1,0,0,1,0,0,1,0),(1,0,0,1,0,0,1,0,0)])
A2 = np.vstack((a1,a2,a3,a4))
I = I_b4
I_ja = np.array((I[3], I[4], I[5], I[11], I[10], I[9], I[7], I[1], I[6], I[8], I[0], I[2])) 
def mu(I_0,I,d):
	return unp.log(I_0/I) / d
print("----------Block 2------------")
mu_b2_1 = mu(I_al_1, I_b2_1 , 3)
print("Gerade: mu_b2_1", mu_b2_1)

mu_b2_2 = mu(I_al_2, I_b2_2 , 3 * w)
print("Diagonale: mu_b2_2", mu_b2_2)

print("Mittelwert mu_b2: ", (mu_b2_1 + mu_b2_2)/2)

print("---------Block 3------------")
mu_b3_1 = mu(I_al_1, I_b3_1 , 3)
mu_b3_2 = mu(I_al_1, I_b3_2 , 3)
mu_b3_3 = mu(I_al_1, I_b3_3 , 3)
print("Gerade: mu_b3_1: ", mu_b3_1, " mu_b3_2: ", mu_b3_2 , " mu_b3_3: ", mu_b3_3)
mu_b3_4 = mu(I_al_2, I_b3_4 , w*3)
mu_b3_5 = mu(I_al_2, I_b3_5 , w*3)
print("Diagonale: mu_b3_4: ", mu_b3_4 , " mu_b3_5: ", mu_b3_5)
mu_b3_6 = mu(I_al_3, I_b3_6 , w*2)
print("Nebendiagonale: mu_b3_6: ", mu_b3_6)
print("Mittelwert mu_b3: ", (mu_b3_1 + mu_b3_2 + mu_b3_3 + mu_b3_4 + mu_b3_5 + mu_b3_6)/6)

print("--------Block 4------------")
mu_b4_1 = np.linalg.inv(A1.T @ A1) @ A1.T @ I_b4
mu_b4_2 = np.linalg.inv(A2.T @ A2) @ A2.T @ I_ja
print("mu_b4_1: \n",mu_b4_1)
print("mu_b4_2: \n",mu_b4_2)
#print("--------------------------------")
#print(np.linalg.inv(A.T @ A) @ A.T )
#print("--------------------------------")
#print(np.linalg.inv(A.T @ A) )
#print("--------------------------------")
#print(A.T @ A )
#print("--------------------------------")
print("A1: \n", A1.round(2))
print("A2: \n", A2.round(2))
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
plt.xlim(15,100)
plt.xlabel("Channel")
plt.ylabel("Anzahl der Ereignisse")
plt.grid()
plt.tight_layout()
plt.savefig('python/build/spektrum.pdf')





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


#print("########## AUSWERTUNG ###############\n\n")


###Tabellen

#print("####### TABELLEN #########")

########Grafiken########

