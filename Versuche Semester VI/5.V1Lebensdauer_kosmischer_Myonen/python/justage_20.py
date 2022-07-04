import numpy as np 
import os
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")


def gerade(x, m, b):
    return m*x+b

dt,T, N = np.genfromtxt('python/data/justage_20.dat', unpack=True)

N = N/T

#fit 
N_cut=N[5:16]
dt_cut = dt[5:16]

print(dt_cut[0])
print(dt_cut[-1])

params, covariance_matrix = np.polyfit(dt_cut, N_cut, deg=0, cov=True)
uncertainties = np.sqrt(np.diag(covariance_matrix))

#Ausgeben der Parameter
print("\nRegressionsparameter für Platau für justage 20ns in ns")
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.8f} ± {error:.8f}')

halfmax = params[0]/2

x = np.linspace(np.min(dt_cut), np.max(dt_cut))
y = np.ones(len(x))
plt.plot(x, params[0]*y,  linewidth=1, label="Plateau")
plt.errorbar(dt, N, xerr=0, yerr=np.sqrt(N), fmt='.', label="Daten")
#plt.hlines(np.mean(N_cut)/2, np.min(dt_cut)-5, np.max(dt_cut)+6, color='green', linestyles='dashed', label='Plataumittelwert/2')
plt.xlabel(r"$\Delta t_{Delay}$ / $ ns$")
plt.ylabel(r"$N$ / $ \frac{1}{s}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plots/justage_20.pdf')

print(f"Mittelwert=({np.mean(N_cut):.4}+/-{np.std(N_cut):.3})")
print(f"Halbwertsbreite=({np.mean(N_cut/2):.3}+/-{np.std(N_cut/2):.3})")