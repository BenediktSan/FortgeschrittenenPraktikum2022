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



dt,T, N = np.genfromtxt('python/data/justage_20.dat', unpack=True)

N_print =N
N=N/T

#fit 
N_cut=N[5:17]
dt_cut = dt[5:17]

print(dt_cut[0])
print(dt_cut[-1])

params1, covariance_matrix1 = np.polyfit(dt_cut, N_cut, deg=0, cov=True)
uncertainties1 = np.sqrt(np.diag(covariance_matrix1))

#Ausgeben der Parameter
print("\nRegressionsparameter für Platau für justage 10ns in ns")
errors1 = np.sqrt(np.diag(covariance_matrix1))
for name, value, error in zip('ab', params1, errors1):
    print(f'{name} = {value:.8f} ± {error:.8f}')

halfmax = params1[0]/2

x_halbw = np.linspace(dt[0] - 3, dt[-1] + 1)



#i hate my life

N_cut_before=N[:6]
dt_cut_before = dt[:6]

N_cut_after=N[17:]
dt_cut_after = dt[17:]


params2, covariance_matrix2 = np.polyfit(dt_cut_before, N_cut_before, deg=1, cov=True)
uncertainties2 = np.sqrt(np.diag(covariance_matrix2))

#Ausgeben der Parameter
print("\nRegressionsparameter für Platau für justage 10ns in ns")
errors2 = np.sqrt(np.diag(covariance_matrix2))
for name, value, error in zip('ab', params2, errors2):
    print(f'{name} = {value:.8f} ± {error:.8f}')



params3, covariance_matrix3 = np.polyfit(dt_cut_after, N_cut_after, deg=1, cov=True)
uncertainties3 = np.sqrt(np.diag(covariance_matrix3))

#Ausgeben der Parameter
print("\nRegressionsparameter für Platau für justage 20ns in ns")
errors3 = np.sqrt(np.diag(covariance_matrix3))
for name, value, error in zip('ab', params3, errors3):
    print(f'{name} = {value:.8f} ± {error:.8f}')


x = np.linspace(np.min(dt_cut), np.max(dt_cut))
y = np.ones(len(x))

x_auf = np.linspace(dt[0] - 3, dt[6] + 1)
x_ab = np.linspace(dt[17] - 1, dt[-1] +1)



halbw = params1[0]/2

uparams2 = unp.uarray(params2, errors2)
print(f"\nSchnittpunkt links = {(halbw - uparams2[1])/uparams2[0]}")

uparams3 = unp.uarray(params3, errors3)
print(f"Schnittpunkt rechts = {(halbw - uparams3[1])/uparams3[0]}")
print(f"Differenz = {(halbw - uparams3[1])/uparams3[0] - (halbw - uparams2[1])/uparams2[0]} ")
print(f"komische Formel = {2*20 - ((halbw - uparams3[1])/uparams3[0] - (halbw - uparams2[1])/uparams2[0])}\n")

plt.plot(x, gerade(x,0, *params1), "b",  linewidth=1, label="Plateaufit")
plt.plot(x_halbw, gerade(x_halbw, 0,params1[0]/2),"b--", linewidth=1, label="Halbwertsbreite")
plt.plot(x_auf, gerade(x_auf, *params2), "g",  linewidth=1, label="Fit aufsteigende Flanke")
plt.plot(x_ab, gerade(x_ab, *params3), "g",  linewidth=1, label="Fit abfallende Flanke")
plt.errorbar(dt, N, xerr=0, yerr=np.sqrt(N),color = "orange",  fmt='.', label="Messdaten")
#plt.hlines(np.mean(N_cut)/2, np.min(dt_cut)-5, np.max(dt_cut)+6, color='green', linestyles='dashed', label='Plataumittelwert/2')
plt.xlabel(r"$\Delta t_{Delay}$ / $ ns$")
plt.ylabel(r"$\frac{N}{T}$ / $ \frac{1}{s}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plots/justage_20.pdf')

print(f"Mittelwert=({np.mean(N_cut):.4}+/-{np.std(N_cut):.3})")
print(f"Halbwertsbreite=({np.mean(N_cut/2):.3}+/-{np.std(N_cut/2):.3})")

#printer(dt, T, N_print, N,"justage_10")