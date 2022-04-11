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
#Werte in mbar

t_1 = np.arrange(0,600,10)

### Drehschieber p_t MEssung alle 10s 

dreh_p_1 = np.array([995.1, 644, 479, 358, 265, 201, 147, 103, 75, 55, 40.2, 29.9, 21.5, 15.1, 10.8, 7.9, 5.9, 4.5, 3.5, 2.8, 2.2, 1.9, 1.6, 1.4, 1.2, 1, 0.93, 0.83, 0.76, 0.68, 0.63, 
                    0.59, 0.54, 0.5, 0.47, 0.44, 0.41, 0.39, 0.37, 0.35, 0.33, 0.31, 0.30, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.21, 0.21, 0.2, 0.19, 0.18, 0.17, 0.17, 0.16, 0.16, 0.15, 0.15, 0.14 ])

dreh_p_2 = np.array([995.4, 640, 439, 327, 236, 177, 131, 95, 69.8, 51, 36.7, 26.4, 19.1, 14, 10, 7.3, 5.5, 4.2, 3.2, 2.6, 2.1, 1.6, 1.5, 1.3, 1.2, 0.99, 0.91, 0.82, 0.74, 0.67, 0.62,
                    0.57, 0.53, 0.5, 0.46, 0.43, 0.41, 0.39, 0.36, 0.35, 0.33, 0.31, 0.3, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22, 0.21, 0.20, 0.2, 0.19, 0.18, 0.18, 0.17, 0.16, 0.16, 0.15, 0.15 ])

dreh_p_3 = np.array([989.7, 640, 477, 357, 266, 196, 144, 108, 76.9, 56.2, 41.1, 30.3, 21.4, 15.5, 11.3, 8.5, 6.1, 4.6, 3.6, 2.9, 2.3, 1.9, 1.6, 1.4, 1.2, 1.1, 0.94, 0.86, 0.77, 0.70, 0.64, 0.6, 0.55,
                    0.51, 0.47, 0.44, 0.42, 0.4, 0.38, 0.35, 0.33, 0.32, 0.3, 0.29, 0.28, 0.27, 0.25, 0.24, 0.23, 0.23, 0.21, 0.21, 0.2, 0.19, 0.18, 0.18, 0.17, 0.16, 0.16, 0.15, 0.15])


### Drehschieber Leckrate alle 10s bis 200s (Arrayelement )

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

dreh_leck_2_2 = np.array([10, 19.3, ])
#####RECHNUNGEN#######

########Grafiken########


plt.figure()
plt.plot(f,U/(10),"x",label="Messwerte")
plt.plot(x,func(x,omega0) )
plt.xscale('log')
plt.xlabel(r"$\Omega=\frac{\nu}{\nu_0}$")
plt.ylabel(r"$\frac{U_Br}{U_0}$")
#plt.xticks([5*10**3,10**4,2*10**4,4*10**4],[r"$5*10^3$", r"$10^4$", r"$2*10^4$", r"$4*10^4$"])
#plt.yticks([0,np.pi/8,np.pi/4,3*np.pi/8,np.pi/2],[r"$0$",r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
plt.tight_layout()
plt.legend()
plt.savefig("build/plots/plot1.pdf")