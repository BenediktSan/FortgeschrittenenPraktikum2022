import numpy as np 
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
import os
from tabulate import tabulate


def printer(a,b,c,d,name):
    print(f"### {name} ###")
    table1 ={'Messreihe 1': a, 'Messreihe 2': b,  'Messreihe 3': c, 'Messreihe 4': d }
    print("\n", tabulate(table1, tablefmt = "latex_raw"))    

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")


def gerade(x, m, b):
    return m*x+b

dt,T, N = np.genfromtxt('python/data/justage_10.dat', unpack=True)

N_print =N
N=N/T

#fit 
N_cut=N[3:10]
dt_cut = dt[3:10]

print(dt_cut[0])
print(dt_cut[-1])

params, covariance_matrix = np.polyfit(dt_cut, N_cut, deg=1, cov=True)
uncertainties = np.sqrt(np.diag(covariance_matrix))

#Ausgeben der Parameter
print("\nRegressionsparameter für Platau für justage 10ns in ns")
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.8f} ± {error:.8f}')

halfmax = params[0]/2

x = np.linspace(np.min(dt_cut), np.max(dt_cut))
y = np.ones(len(x))
plt.plot(x, gerade(x, *params),  linewidth=1, label="Plateaufit")
plt.errorbar(dt, N, xerr=0, yerr=np.sqrt(N),  fmt='.', label="Messdaten")
#plt.hlines(np.mean(N_cut)/2, np.min(dt_cut)-5, np.max(dt_cut)+6, color='green', linestyles='dashed', label='Plataumittelwert/2')
plt.xlabel(r"$\Delta t_{Delay}$ / $ ns$")
plt.ylabel(r"$\frac{N}{T}$ / $ \frac{1}{s}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plots/justage_10.pdf')

print(f"Mittelwert=({np.mean(N_cut):.4}+/-{np.std(N_cut):.3})")
print(f"Halbwertsbreite=({np.mean(N_cut/2):.3}+/-{np.std(N_cut/2):.3})")

#printer(dt, T, N_print, N,"justage_10")