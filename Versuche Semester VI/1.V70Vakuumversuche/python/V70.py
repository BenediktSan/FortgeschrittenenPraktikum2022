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

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")




########MESSWERTE#######


####### WERTE IN mbar

t_1 = np.arange(0,610,10)
t_1 = np.append(t_1,1000)
### Drehschieber p_t MEssung alle 10s 
#als endwert 2.1e-2 einfügen

dreh_p_1 = np.array([995.1, 644, 479, 358, 265, 201, 147, 103, 75, 55, 40.2, 29.9, 21.5, 15.1, 10.8, 7.9, 5.9, 4.5, 3.5, 2.8, 2.2, 1.9, 1.6, 1.4, 1.2, 1, 0.93, 0.83, 0.76, 0.68, 0.63, 
                    0.59, 0.54, 0.5, 0.47, 0.44, 0.41, 0.39, 0.37, 0.35, 0.33, 0.31, 0.30, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.21, 0.21, 0.2, 0.19, 0.18, 0.17, 0.17, 0.16, 0.16, 0.15, 0.15, 0.14,0.021 ])

dreh_p_2 = np.array([995.4, 640, 439, 327, 236, 177, 131, 95, 69.8, 51, 36.7, 26.4, 19.1, 14, 10, 7.3, 5.5, 4.2, 3.2, 2.6, 2.1, 1.6, 1.5, 1.3, 1.2, 0.99, 0.91, 0.82, 0.74, 0.67, 0.62,
                    0.57, 0.53, 0.5, 0.46, 0.43, 0.41, 0.39, 0.36, 0.35, 0.33, 0.31, 0.3, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22, 0.21, 0.20, 0.2, 0.19, 0.18, 0.18, 0.17, 0.16, 0.16, 0.15, 0.15,0.021 ])

dreh_p_3 = np.array([989.7, 640, 477, 357, 266, 196, 144, 108, 76.9, 56.2, 41.1, 30.3, 21.4, 15.5, 11.3, 8.5, 6.1, 4.6, 3.6, 2.9, 2.3, 1.9, 1.6, 1.4, 1.2, 1.1, 0.94, 0.86, 0.77, 0.70, 0.64, 0.6, 0.55,
                    0.51, 0.47, 0.44, 0.42, 0.4, 0.38, 0.35, 0.33, 0.32, 0.3, 0.29, 0.28, 0.27, 0.25, 0.24, 0.23, 0.23, 0.21, 0.21, 0.2, 0.19, 0.18, 0.18, 0.17, 0.16, 0.16, 0.15, 0.15,0.021])


### Drehschieber Leckrate alle 10s bis 200s (Arrayelement 20 ; :21)

## 0.4 mbar gleichgewicht

dreh_leck_1_1 = np.array([0.39, 1.3, 1.4, 1.5, 1.6, 1.6, 1.7, 1.8, 1.9, 1.9, 2, 
                        2.1, 2.1, 2.2, 2.3, 2.3, 2.4, 2.5, 2.6, 2.7, 2.7 ])
    
dreh_leck_1_2 = np.array([0.39, 1.4, 1.5, 1.6, 1.6, 1.7, 1.8, 1.9, 1.9, 2, 
                        2.1, 2.2, 2.2, 2.3, 2.4, 2.5, 2.5, 2.6, 2.7, 2.8])

dreh_leck_1_3 = np.array([0.39, 1.3, 1.4, 1.5, 1.6, 1.6, 1.7, 1.8, 1.9, 1.9, 2,
                        2.1, 2.1, 2.2, 2.2, 2.3, 2.4, 2.5, 2.6, 2.6, 2.7])

## 10 mbar gleichgewicht

dreh_leck_2_1 = np.array([10, 19.3, 23.1, 26.8, 30.3, 34.2, 38, 41.5, 45.5, 48.9, 53, 
                        56, 60.5, 63.8, 67.5, 71.5, 75, 78.8, 82.8, 86.8, 90.2])

dreh_leck_2_2 = np.array([10, 19.3, 23.1, 26.8, 30.3, 34.2, 38, 41.5, 45.5, 48.9, 53, 
                        56, 60.5, 63.8, 67.5, 71.5, 75, 78.8, 82.8, 86.6, 90.2 ])

dreh_leck_2_3 = np.array([10, 19.2, 22.9, 26.8, 30.4, 34.1, 37.8, 41.6, 45.3, 49.1, 
                        52.8, 56.6, 60.3, 64, 68.1, 71.1, 75.2, 79.2, 82.6, 90.1])

## 40mbar Gleichgewicht

dreh_leck_3_1 = np.array([40.1, 61.7, 75.8, 90, 104, 118.2, 133.2, 146.4, 160.5, 174.5, 188.7, 
                        202.1, 216.1, 230.2, 244.3, 258.6, 274.1, 286.7, 300.8, 315, 329.1])

dreh_leck_3_2 = np.array([40.2, 61.4, 75.5, 89.5, 103.7, 117.8, 131.9, 145.9, 160.1, 174.1, 188.2, 
                        201.5, 215.6, 229.8, 245.3, 258.2, 272.2, 285.3, 303.2, 314.4, 328.5 ])

dreh_leck_3_3 = np.array([40.1, 61.4, 75.5, 89.6, 103.7, 117.8, 131.8, 145.9, 159.9, 174.0, 188.1, 
                        201.4, 215.5, 229.5, 243.7, 257.8, 271.9, 285.9, 300.1, 314.2, 328.3])

## 80mbar_Gleichgewicht
dreh_leck_4_1 = np.array([80, 116.9, 143.9, 171, 198, 224, 251.1, 178.2, 305.2, 332.3, 359.4, 
                        386.2, 413, 439, 466.3, 492.8, 518.8, 544.8, 570.4, 595, 620.8 ])

dreh_leck_4_2 = np.array([80, 116, 143.1, 170.3, 197.3, 223.4, 252.1, 280, 307.1, 334.2, 361.3, 
                        388.1, 415.1, 441.3, 468.3, 494.7, 520.7, 546.6, 572.3, 596.4, 620])

dreh_leck_4_3 = np.array([80, 115.9, 143.1, 170, 196.8, 225.9, 253, 280, 307.2, 334.2, 361.2, 
                        488.1, 417.1, 441.7, 468.2, 494.2, 520.8, 546.7, 572.2, 597.3, 622.5])

### Turbomolekular p(t)  kurve  200s alle 10s 

# als endwert 1 e-5 einfügen

turbo_pump_p_1 = np.array([166, 7.8, 3.3, 2.72, 2.54, 2.42, 2.33, 2.25, 2.2, 2.16, 2.12,
                            2.09, 2.06, 2.03, 2.01, 1.98, 1.96, 1.94, 1.92, 1.91, 1.9, 1]) * 10**(-5)

turbo_vent_p_1 = np.array([496, 14.2, 5.12, 4.22, 3.96, 3.83, 3.73, 3.66, 3.6, 3.52, 3.49, 
                            3.46, 3.44, 3.42, 3.4, 3.36, 3.34, 3.31, 3.28, 3.25, 1]) * 10**(-5)

turbo_pump_p_2 = np.array([169, 8.73,2.98, 2.4, 2.22, 2.13, 2.05, 1.99, 1.94, 1.9, 1.87, 
                        1.84, 1.81, 1.79, 1.77, 1.75, 1.73, 1.71, 1.7, 1.68, 1.67, 1  ]) * 10**(-5)

turbo_vent_p_2 = np.array([504, 13.2, 4.72, 3.81, 3.61, 3.49, 3.4, 3.33, 3.26, 3.2, 3.16,
                        3.12, 3.08, 3.05, 3.02, 3, 2.98, 2.95, 2.93, 2.91, 2.89, 1]) * 10**(-5)

turbo_pump_p_3 = np.array([167, 79.8, 2.7, 2.2, 2.04, 1.95, 1.88, 1.82, 1.78, 1.74, 1.71, 
                        1.68, 1.66, 1.63, 1.62, 1.6, 1.58, 1.57, 1.55, 1.54, 1.53, 1]) * 10**(-5)

turbo_vent_p_3 = np.array([495, 12.8, 4.36, 3.58, 3.4, 3.26, 3.16, 3.09, 3.02, 2.97, 2.93, 
                            2.89, 2.85, 2.82, 2.79, 2.76, 2.74, 2.72, 2.7, 2.68, 2.66, 1]) * 10**(-5)


## LEckrate Turbopumpe Messwerte am Ventil

##Gleichgewicht 1 e-4 mbar

turbo_leck_1_1 = np.array([1.01, 2.51, 3.78, 4.99, 6.15, 7.44, 9.16, 11, 13, 14.7, 16.3, 18.2, 20.2]) * 10**(-4)

turbo_leck_1_2 = np.array([1.03, 2.58, 3.86, 5.04, 6.18, 7.54, 9.28, 11, 13.1, 14.7, 16.4, 18.3, 20.2]) * 10**(-4)

turbo_leck_1_3 = np.array([1, 2.52, 3.75, 4.97, 6.03, 7.25, 8.88, 10.7, 12.4, 14.1, 15.7, 17.5, 19.3]) * 10**(-4)


##Gleichgewicht 2 e-4 mbar

turbo_leck_2_1 = np.array([2.02, 4.86, 8, 12.1, 16.2, 20.6, 15.6, 31.5, 37.6, 43.2, 49.5, 56.3, 62.4]) * 10**(-4)

turbo_leck_2_2 = np.array([2.04, 4.86, 7.96, 12.2, 16.3, 20.6, 16, 31.8, 37.4, 4.32, 49.4, 56.4, 62.2]) * 10**(-4)

turbo_leck_2_3 = np.array([2.03, 4.84, 7.82, 12, 16, 20.5, 25.6, 31.4, 36.9, 42.8, 49.2, 56.2, 62]) * 10**(-4)


##Gleichgewicht 7 e-5 mbar

turbo_leck_3_1 = np.array([0.7, 1.84, 2.75, 3.62, 4.46, 5.18, 6.01, 6.79, 7.8, 8.9, 10.1, 11.2, 12.5]) * 10**(-4)

turbo_leck_3_2 = np.array([0.702, 1.83, 2.79, 3.72, 4.53, 5.32, 6.16, 6.94, 7.93, 9.14, 10.3, 11.5, 12.8]) * 10**(-4)

turbo_leck_3_3 = np.array([0.698, 1.82, 2.76, 3.62, 4.46, 5.30, 6.1, 6.86, 9.0, 10.2, 11.3, 12.6]) * 10**(-4)

    

##Gleichgewicht 5 e-5 mbar

turbo_leck_4_1 = np.array([0.5, 1.34, 2.15, 2.76, 3.37, 4.06, 4.63, 5.24, 5.82, 6.41, 7, 7.69, 8.45]) * 10**(-4)

turbo_leck_4_2 = np.array([0.499, 1.41, 2.20, 2.84, 3.5, 4.17, 4.76, 5.36, 5.92, 6.5, 7.16, 7.86, 8.72]) * 10**(-4)

turbo_leck_4_3 = np.array([0.504, 1.36, 2.14, 2.86, 3.52, 4.14, 4.76, 5.37, 5.98, 6.4, 7.19, 7.96, 8.7]) * 10**(-4)


#####RECHNUNGEN#######

### Werte mitteln


def mittel(a,b,c):
    arr = unp.uarray(np.zeros(np.size(a)),np.zeros(np.size(a)))
    for i in range(0,np.size(a)):
        arr[i] = unc.ufloat(np.mean([a[i], b[i], c[i]]), np.std([a[i], b[i], c[i]])/ np.sqrt(np.size(3)))
    return arr

dreh_p = mittel(dreh_p_1, dreh_p_2, dreh_p_2)
print(dreh_p[1])

table = (turbo_leck_1_1.T, turbo_leck_1_2.T, turbo_leck_1_3.T)
np.transpose(table)
headers = ("A", "B", "C")
print(dreh_leck_1_1.T)
print(table)
#print(tabulate(table, headers, tablefmt="latex"))

table ={'alpha1': turbo_leck_1_1, 'alphag': turbo_leck_1_2,  'delg':turbo_leck_1_3, 'delr':mittel(turbo_leck_1_1, turbo_leck_1_2, turbo_leck_1_3)}
#print("\n ",tabulate (table, tablefmt="latex"))


def printer(a):
    n = 2
    title = "Messreihe "
    table = {title.join("1") : a[0]}
    for i in range(1,n):
        table ={table[0] ,{title.join("1" ) : a[i]}}
    print("\n", tabulate(table, tablefmt = "latex_raw"))


########Grafiken########


plt.figure()
plt.plot(t_1,(dreh_p_1),"x",label="Messwerte")
#plt.errorbar(x, unp.nominal_values(y), yerr=unp.std_devs(y), fmt='rx')
#plt.plot(x,func(x,omega0) )
plt.yscale('log')
plt.xlabel(r"$t [s]$")
plt.ylabel(r"$p$")
#plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
#plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot1.pdf")

plt.figure()
plt.plot(t_1[:21],dreh_leck_1_1,"x",label="Messwerte")
#plt.errorbar(x, unp.nominal_values(y), yerr=unp.std_devs(y), fmt='rx')
#plt.plot(x,func(x,omega0) )
#plt.yscale('log')
plt.xlabel(r"$t [s]$")
plt.ylabel(r"$p$")
#plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
#plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot2.pdf")