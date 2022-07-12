import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
import uncertainties.unumpy as unp
import os
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

if os.path.exists("build") == False:
    os.mkdir("build")

if os.path.exists("build/plots") == False:
    os.mkdir("build/plots")



def gerade(x, m, b):
    return m * x + b


t, K = np.genfromtxt("python/data/kalibration.dat", unpack=True)

params, covariance_matrix = np.polyfit(K, t, deg=1, cov=True)
uncertainties = np.sqrt(np.diag(covariance_matrix))

# Ausgeben der Parameter
print("\nRegressionsparameter für Kalibration")
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip("ab", params, errors):
    print(f"{name} = ({value*10**3:.8f} ± {error*10**3:.8f})ns")

uparams = unp.uarray(params, uncertainties)

t_such = 10 #in mu s

channel = (t_such - uparams[1] )/( uparams[0])

print(f"\n Der Kanal {noms(channel)} \pm {stds(channel)} entspricht der Suchzeit.\n")
print(params[0],"\t", params[1])
print(gerade(450, *params))
x = np.linspace(np.min(K), np.max(K))
plt.plot(x, gerade(x, *params),  label="Fit")
plt.plot(K, t, "x", markersize=10, label="Messdaten")
plt.xlabel(r"MCA-Kanal")
plt.ylabel(r"$\Delta t$ / $ \mu s$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plots/kalibration.pdf")
