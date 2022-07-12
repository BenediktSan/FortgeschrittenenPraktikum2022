import numpy as np 
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.optimize import curve_fit
import os

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")



def efunk(x, N0, l):
    return N0*np.exp(-l*x)+0.761           #eventuell noch ändern


#N = np.genfromtxt('data/ronja.dat', unpack=True)
N = np.genfromtxt('python/data/v01-messwerte.Spe', skip_header =5, unpack=True)
K = np.linspace(1,len(N),len(N))

#Kanäle in Zeit umrechnen
a = ufloat(0.02231226, 0.00001810)
b = ufloat(-0.0170105, 0.00293725)
t = a * K + b




#Regression
#params, cov = curve_fit(efunk,  noms(t_cut),  N_cut)
params, cov = curve_fit(efunk,  noms(t[3:-62]),  N[3:-62])

print(f"\nStoppsignale: {N.sum()}")


print("\nRegressionsparameter für die Lebensdauer sind")
errors = np.sqrt(np.diag(cov))
for name, value, error in zip('Nl', params, errors):
    print(f'{name} = {value:.8f} ± {error:.8f}')

#Plot
x=noms(np.linspace(np.min(t[2:-47]), np.max(t[2:-47])))
plt.errorbar(noms(t),     N,     xerr=stds(t),     yerr=np.sqrt(N),color = "lime",  markersize=2.5, elinewidth=0.4, fmt='.', label="abgeschnittene Messdaten")
plt.errorbar(noms(t[3:-62]), N[3:-62], xerr=stds(t[3:-62]), yerr=np.sqrt(N[3:-62]),color = "teal",   markersize=3.5, elinewidth=0.4, fmt='.', label="Messdaten")
plt.plot(x, efunk(x, params[0], params[1]),color = "purple",  label="Fit")
plt.xlabel(r"$t $ / $\mu s$")
plt.ylabel(r"$N $ / $\frac{1}{s}$")
plt.legend(loc='best')
plt.tight_layout()
plt.grid()
plt.savefig('build/plots/lebensdauer.pdf')

#Berechnung der mittleren Lebensdauer
lam=ufloat(params[1], errors[1])
tau=1/lam
print(f"\nLambda beträgt {lam} 1/us")
print(f"\ndie mittlere Lebensdauer beträgt tau=({tau:.4})us")

tau_pdg=ufloat(2.1969811,0.0000022)         #in us
p=(tau-tau_pdg)/tau_pdg *100
print(f"relative Abweichung von tau {p} % vom Theoriewert tau = {tau_pdg} us")